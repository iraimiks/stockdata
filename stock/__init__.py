from sqlalchemy import create_engine
import cx_Oracle 
from . import config

cx_Oracle.init_oracle_client(lib_dir=config.cx_Oracle_client_path)

username = config.db_username
password = config.db_password
host = config.db_host_ip
port = config.db_port
sid = cx_Oracle.makedsn(host,port,sid=config.db_sid)
cstr = 'oracle://{user}:{password}@{sid}'.format(
  user=username,
  password=password,
  sid=sid
)

engine = create_engine(cstr)
db = engine.connect()
