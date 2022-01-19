import requests
from stock.database.dataworker import Base, insert_stock, select_all
from stock import engine
import pandas as pd
import matplotlib.pyplot as plt
import sys
from scipy.signal import find_peaks
from stock import config

def initDB():
    Base.metadata.create_all(engine)

def data_stock_api():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED\
    &symbol={0}&slice={1}&interval={2}&apikey={3}'.format(
        config.api_stock, config.api_slice, config.api_interval, config.apikey)
    r = requests.get(url)
    data = r.json()
    price = []
    # This will broke after change interval 
    for key in data['Time Series (5min)']:
        date = key
        price.append({"datetime":key, "close":data['Time Series (5min)'][date]['4. close']})
    return price

def report_to_csv():
    data = pd.DataFrame.from_dict(select_all())
    data.to_csv('gathered_data.csv',index=False)

def draw_chart():
    data = pd.DataFrame.from_dict(select_all())
    data['datetime'] = pd.to_datetime(data['datetime'])
    data['close'] = data['close'].astype(float)
    data.set_index('datetime').plot()
    plt.show()

def run():
    initDB()
    insert_stock(data_stock_api())

if __name__ == '__main__':
    run()
    if sys.argv[1] == "csv":
        report_to_csv()
    elif sys.argv[1] == "chart":
        draw_chart()
    else:
        print("Wrong arg name, alowed csv or chart")
