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
# 检查是否存在活动订单

point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask + 1
deviation = 20

print("account info ",mt5.account_info())


# deal order
# request_deal = {
#     "action": mt5.TRADE_ACTION_DEAL,
#     "symbol": symbol,
#     "volume": 0.01,
#     "type": mt5.ORDER_TYPE_BUY,
#     "price": mt5.symbol_info_tick(symbol).ask,
#     "sl": mt5.symbol_info_tick(symbol).ask-100*point,
#     "tp": mt5.symbol_info_tick(symbol).ask+100*point,
#     "deviation": 10,
#     "magic": 234000,
#     "comment": "python script",
#     "type_time": mt5.ORDER_TIME_GTC,
#     "type_filling": mt5.ORDER_FILLING_IOC,
# }

# order_deal_result = mt5.order_send(request_deal)
# print("order_deal_result ",order_deal_result)

# pending order
# request_pending = {
#     "action":mt5.TRADE_ACTION_PENDING,
#     "symbol":symbol,
#     "volume":0.01,
#     "stoplimit": mt5.symbol_info_tick(symbol).ask-100*point,
#     "deviation": 10,
#     "type": mt5.ORDER_TYPE_BUY_STOP_LIMIT,
#     "type_filling":mt5.ORDER_FILLING_IOC,
#     "comment": "python script",
#     "type_time": mt5.ORDER_TIME_GTC,
#     "price": mt5.symbol_info_tick(symbol).ask+100*point,
#     "magic":100012
# }

# pending_result = mt5.order_send(request_pending)
# print("pending_result ",pending_result)


# print("当前的用户订单数量 =  ",mt5.orders_total())

# print("当前的正在进行的订单数量 = ",mt5.positions_total())

# position_get_no_param = mt5.positions_get()
# print("position_get_no_param ",position_get_no_param)

# for trade_position in position_get_no_param:
#     print("trade_position = ",trade_position.ticket)


# position_get_param_symbol = mt5.positions_get(symbol=symbol)
# print("position_get_param_symbol ",position_get_param_symbol)

# position_get_param_ticket = mt5.positions_get(ticket=206387229)
# print("position_get_param_ticket  = ",position_get_param_ticket)

# from_date = datetime(2020,11,30)
 

# history_orders_total = mt5.history_orders_total(from_date, datetime.now())
# print("history_orders_total = ",history_orders_total)

# history_orders_get =  mt5.history_orders_get(from_date, datetime.now())
# print("history_orders_get = ",history_orders_get)

# history_deals_total = mt5.history_deals_total(from_date, datetime.now()) 
# print("history_deals_total ",history_deals_total)

# symbols_total = mt5.symbols_total()
# print("symbols_total ",symbols_total)



symbols = ["USDJPY", "USDCHF","EURUSD"]


def job():
    # 更新市场信息
    for symbol_name in symbols:
        symbol_info_tick = mt5.symbol_info_tick(symbol_name)
        market = {}
        market["own_server"] = account_server2
        market["market_name"] = symbol_name
        market["time"] = symbol_info_tick.time
        market["bid"] = symbol_info_tick.bid
        market["ask"] = symbol_info_tick.ask
        market["last"] = symbol_info_tick.last
        market["volume"] = symbol_info_tick.volume
        market["time"] = symbol_info_tick.time
        market["time_msc"] = symbol_info_tick.time_msc
        market["flags"] = symbol_info_tick.flags
        market["volume_real"] = symbol_info_tick.volume_real
        response = requests.post(server_url + "update_market/",json=market)
        json_response = response.json()
        print("json_response ",json_response )

    position_get_no_param = mt5.positions_get()
    # 更新position order   
    for trade_position in position_get_no_param:
        position = {}
        position["ticket"] = trade_position.ticket
        position["time"] = trade_position.time
        position["time_msc"] = trade_position.time_msc
        position["time_update"] = trade_position.time_update
        position["time_update_msc"] = trade_position.time_update_msc
        position["type"] = trade_position.type
        position["magic"] = trade_position.magic
        position["identifier"] = trade_position.identifier
        position["reason"] = trade_position.reason
        position["volume"] = trade_position.volume
        position["price_open"] = trade_position.price_open
        position["sl"] = trade_position.sl
        position["tp"] = trade_position.tp
        position["price_current"] = trade_position.price_current
        position["swap"] = trade_position.swap
        position["profit"] = trade_position.profit
        position["symbol"] = trade_position.symbol
        position["comment"] = trade_position.comment
        position["external_id"] = trade_position.external_id
        response = requests.post(server_url + "update_position_order/",json=position)
        json_response = response.json()
        print("position_response ",json_response )
        
    # 更新 pending order
    pending_orders = mt5.orders_get()
    for pending_order in pending_orders:
        pending = {}
        pending["ticket"] = pending_order.ticket
        pending["time_setup"] = pending_order.time_setup
        pending["type"] = pending_order.type
        pending["state"] = pending_order.state
        pending["time_expiration"] = pending_order.time_expiration
        pending["time_done"] = pending_order.time_done
        pending["time_setup_msc"] = pending_order.time_setup_msc
        pending["time_done_msc"] = pending_order.time_done_msc
        pending["type_filling"] = pending_order.type_filling
        pending["type_time"] = pending_order.type_time
        pending["magic"] = pending_order.magic
        pending["reason"] = pending_order.reason
        pending["position_id"] = pending_order.position_id
        pending["position_by_id"] = pending_order.position_by_id
        pending["volume_initial"] = pending_order.volume_initial
        pending["volume_current"] = pending_order.volume_current
        pending["price_open"] = pending_order.price_open
        pending["sl"] = pending_order.sl
        pending["tp"] = pending_order.tp
        pending["price_current"] = pending_order.price_current
        pending["price_stoplimit"] = pending_order.price_stoplimit
        pending["symbol"] = pending_order.symbol
        pending["comment"] = pending_order.comment
        pending["external_id"] = pending_order.external_id

        response = requests.post(server_url + "update_pending_order/",json=pending)
        json_response = response.json()
    

    # 更新 deal order
    from_date = datetime(2020,11,30)
    deal_orders = mt5.history_deals_get(from_date, datetime.now())
    for deal in deal_orders:
        deal_data = {}
        deal_data["ticket"] = deal.ticket
        deal_data["order"] = deal.order
        deal_data["time"] = deal.time
        deal_data["time_msc"] = deal.time_msc
        deal_data["type"] = deal.type
        deal_data["entry"] = deal.entry
        deal_data["magic"] = deal.magic
        deal_data["reason"] = deal.reason
        deal_data["position_id"] = deal.position_id
        deal_data["volume"] = deal.volume
        deal_data["price"] = deal.price
        deal_data["commission"] = deal.commission
        deal_data["swap"] = deal.swap
        deal_data["profit"] = deal.profit
        deal_data["fee"] = deal.fee
        deal_data["symbol"] = deal.symbol
        deal_data["comment"] = deal.comment
        deal_data["external_id"] = deal.external_id


        response = requests.post(server_url + "update_deal_order/",json=deal_data)
        json_response = response.json()

# job()
# 定义BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=1)
sched.start()
