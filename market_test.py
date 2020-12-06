from datetime import datetime
import matplotlib.pyplot as plt;
import pandas as pd
from pandas.plotting import register_matplotlib_converters 
register_matplotlib_converters() 
import MetaTrader5 as mt5
from MetaTrader5 import AccountInfo;
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import json
import requests

# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

symbol = "USDJPY"

account = 64232831
# 4941427
account_password = "xmcnMm135642"
account_server1= "XMGlobal-MT5"
account_server2= "XMGlobal-MT5 2"

server_url = "http://192.168.1.117:8081/"

mt5.login(account, server=account_server2, password=account_password)

symbol_info = mt5.symbol_info("USDJPY")
print("symbol_info  - ",symbol_info)
