from stock import db
from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer(),Sequence('id_seq'), primary_key=True)
    create_date = Column(String(length=100))
    close_data = Column(String(length=100))

def insert_stock(data):
    insert = Table('stock', Base.metadata, autoreload=True)
    db.execute(insert.insert().values(create_date=bindparam("datetime"),close_data=bindparam("close")), data)

def amount_stock_data():
    stock_table = table('stock', column('id'))
    rows_count = db.execute(select(func.count()).select_from(stock_table)).scalar_one()
    return rows_count

def select_all():
    stock_table = table('stock')
    rows = db.execute(select(column('create_date'), column('close_data')).select_from(stock_table))
    prep = []
    for row in rows:
        prep.append({"datetime":row['create_date'], "close":row['close_data']})
    return prep

def worst_stock_day():
    print("data")

def best_stock_day():
    print("data")


