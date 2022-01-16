import requests
from stock.database.dataworker import Base, insert_stock, select_all
from stock import engine
import pandas as pd
import matplotlib.pyplot as plt

def initDB():
    Base.metadata.create_all(engine)

def data_stock_api():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=HESR2JI98B14OIXH'
    r = requests.get(url)
    data = r.json()
    price = []
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
    print("Init DB")
    initDB()
    print("Get data form ")
    insert_stock(data_stock_api())
    print("Prepare csv ")
    report_to_csv()
    print("Draw chart ")
    draw_chart()

if __name__ == '__main__':
    run()