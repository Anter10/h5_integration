from datetime import datetime
import matplotlib.pyplot as plt;
import pandas as pd
from pandas.plotting import register_matplotlib_converters 
register_matplotlib_converters() 
import MetaTrader5 as mt5
from MetaTrader5 import AccountInfo;


# # 连接到MetaTrader 5 
# if not mt5.initialize(): 
#     print("initialize() failed") 
#     mt5.shutdown()


# terminal_info = mt5.terminal_info()

# print("客户端信息  = ",terminal_info)
# print("MQL 版本信息  = ",mt5.version())

# account = 4941427
# account_password = "xmcnMm135642"
# account_server= "XMGlobal-MT5"

# authorized = mt5.login(account,  account_password)
# if(authorized):
#     print(mt5.account_info())
#     account_info = AccountInfo(mt5.account_info())

   
# else:
#     print("failed to connect at account error code {}".format(account, mt5.last_error()))
 
from HS_Mt5 import HS_Mt5


account = 64232831
# 4941427
account_password = "xmcnMm135642"
account_server1= "XMGlobal-MT5"
account_server2= "XMGlobal-MT5 2"

hs_mt5 = HS_Mt5()
hs_mt5.login(account, account_server2,account_password)
print(hs_mt5.account_info())


symbol = "USDJPY"

lot = 0.1
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask + 1
deviation = 20
print("当前的做多价格=  ",price)
sl =  price - 500 * point
tp = price + 500 * point
print("sl = ",sl)
print("tp = ",tp)

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "magic": 234000,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl":sl,
    "tp": tp,
    "stoplimit":price + 200 * point,
    "deviation": deviation,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_FOK,
}

# 发送交易请求
result = mt5.order_send(request)
# # 检查执行结果
print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send failed, retcode={}".format(result.retcode))


order_total = mt5.orders_total()
print("当前的下单总量 = ",order_total)

 
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# check the presence of active orders
orders=mt5.positions_total()
t_orders = mt5.orders_get()

position = mt5.orders_get(symbol = "USDJPY")
print("position ",position)

print("t_orders ",t_orders)
if orders>0:
    print("Total orders=",orders)
else:
    print("Orders not found")
 



# shut down connection to the MetaTrader 5 terminal
# mt5.shutdown()

print("mt5 orders version ",mt5.orders_total())