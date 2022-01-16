from sqlalchemy import create_engine
import cx_Oracle 
from . import config_public

cx_Oracle.init_oracle_client(lib_dir=config_public.cx_Oracle_client_path)

username = config_public.db_username
password = config_public.db_password
host = config_public.db_host_ip
port = config_public.db_port
sid = cx_Oracle.makedsn(host,port,sid=config_public.db_sid)
cstr = 'oracle://{user}:{password}@{sid}'.format(
  user=username,
  password=password,
  sid=sid
)

engine = create_engine(cstr)
db = engine.connect()
