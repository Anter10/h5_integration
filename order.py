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



symbols = ["USDJPY", "USDCHF","EURUSD","GBPUSD","GER30Cash","HK50Cash"]


def job():
    # 更新市场信息
    for symbol_name in symbols:
        symbol_info_tick = mt5.symbol_info(symbol_name)
        market = {}
        print("symbol_info_tick ",symbol_info_tick);
        market["time"]                        = symbol_info_tick.time
        market["bid"]                         = symbol_info_tick.bid
        market["ask"]                         = symbol_info_tick.ask
        market["last"]                        = symbol_info_tick.last
        market["volume"]                      = symbol_info_tick.volume
        market["volume_real"]                 = symbol_info_tick.volume_real
        market["custome"]                     = symbol_info_tick.volume_real
        market["chart_mode"]                  = symbol_info_tick.chart_mode
        market["select"]                      = symbol_info_tick.select
        market["visible"]                     = symbol_info_tick.visible
        market["session_deals"]               = symbol_info_tick.session_deals
        market["session_sell_orders"]         = symbol_info_tick.session_sell_orders
        market["volumehigh"]                  = symbol_info_tick.volumehigh
        market["volumelow"]                   = symbol_info_tick.volumelow
        market["digits"]                      = symbol_info_tick.digits
        market["spread"]                      = symbol_info_tick.spread
        market["spread_float"]                = symbol_info_tick.spread_float
        market["ticks_bookdepth"]             = symbol_info_tick.ticks_bookdepth
        market["trade_calc_mode"]             = symbol_info_tick.trade_calc_mode
        market["trade_mode"]                  = symbol_info_tick.trade_mode
        market["start_time"]                  = symbol_info_tick.start_time
        market["expiration_time"]             = symbol_info_tick.expiration_time
        market["trade_stops_level"]           = symbol_info_tick.trade_stops_level
        market["trade_freeze_level"]          = symbol_info_tick.trade_freeze_level
        market["trade_exemode"]               = symbol_info_tick.trade_exemode
        market["swap_mode"]                   = symbol_info_tick.swap_mode
        market["swap_rollover3days"]          = symbol_info_tick.swap_rollover3days
        market["margin_hedged_use_leg"]       = symbol_info_tick.margin_hedged_use_leg
        market["expiration_mode"]             = symbol_info_tick.expiration_mode
        market["filling_mode"]                = symbol_info_tick.filling_mode
        market["order_mode"]                  = symbol_info_tick.order_mode
        market["order_gtc_mode"]              = symbol_info_tick.order_gtc_mode
        market["option_mode"]                 = symbol_info_tick.option_mode
        market["option_right"]                = symbol_info_tick.option_right
        market["bid"]                         = symbol_info_tick.bid
        market["bidhigh"]                     = symbol_info_tick.bidhigh
        market["bidlow"]                      = symbol_info_tick.bidlow
        market["ask"]                         = symbol_info_tick.ask
        market["askhigh"]                     = symbol_info_tick.askhigh
        market["asklow"]                      = symbol_info_tick.asklow
        market["last"]                        = symbol_info_tick.last
        market["lasthigh"]                    = symbol_info_tick.lasthigh
        market["lastlow"]                     = symbol_info_tick.lastlow
        market["volume_real"]                 = symbol_info_tick.volume_real
        market["volumehigh_real"]             = symbol_info_tick.volumehigh_real
        market["option_strike"]               = symbol_info_tick.option_strike
        market["point"]                       = symbol_info_tick.point
        market["trade_tick_value"]            = symbol_info_tick.trade_tick_value
        market["trade_tick_value_profit"]     = symbol_info_tick.trade_tick_value_profit
        market["trade_tick_value_loss"]       = symbol_info_tick.trade_tick_value_loss
        market["trade_tick_size"]             = symbol_info_tick.trade_tick_size
        market["trade_contract_size"]         = symbol_info_tick.trade_contract_size
        market["trade_accrued_interest"]      = symbol_info_tick.trade_accrued_interest
        market["trade_face_value"]            = symbol_info_tick.trade_face_value
        market["trade_liquidity_rate"]        = symbol_info_tick.trade_liquidity_rate
        market["volume_min"]                  = symbol_info_tick.volume_min
        market["volume_max"]                  = symbol_info_tick.volume_max
        market["volume_step"]                 = symbol_info_tick.volume_step
        market["volume_limit"]                = symbol_info_tick.volume_limit
        market["swap_long"]                   = symbol_info_tick.swap_long
        market["swap_short"]                  = symbol_info_tick.swap_short
        market["margin_initial"]              = symbol_info_tick.margin_initial
        market["margin_maintenance"]          = symbol_info_tick.margin_maintenance
        market["session_volume"]              = symbol_info_tick.session_volume
        market["session_turnover"]            = symbol_info_tick.session_turnover
        market["session_interest"]            = symbol_info_tick.session_interest
        market["session_buy_orders_volume"]   = symbol_info_tick.session_buy_orders_volume
        market["session_sell_orders_volume"]  = symbol_info_tick.session_sell_orders_volume
        market["session_open"]                = symbol_info_tick.session_open
        market["session_close"]               = symbol_info_tick.session_close
        market["session_aw"]                  = symbol_info_tick.session_aw
        market["session_price_settlement"]    = symbol_info_tick.session_price_settlement
        market["session_price_limit_min"]     = symbol_info_tick.session_price_limit_min
        market["session_price_limit_max"]     = symbol_info_tick.session_price_limit_max
        market["margin_hedged"]               = symbol_info_tick.margin_hedged
        market["price_change"]                = symbol_info_tick.price_change
        market["price_volatility"]            = symbol_info_tick.price_volatility
        market["price_theoretical"]           = symbol_info_tick.price_theoretical
        market["price_greeks_delta"]          = symbol_info_tick.price_greeks_delta
        market["price_greeks_theta"]          = symbol_info_tick.price_greeks_theta
        market["price_greeks_gamma"]          = symbol_info_tick.price_greeks_gamma
        market["price_greeks_vega"]           = symbol_info_tick.price_greeks_vega
        market["price_greeks_rho"]            = symbol_info_tick.price_greeks_rho
        market["price_greeks_omega"]          = symbol_info_tick.price_greeks_omega
        market["price_sensitivity"]           = symbol_info_tick.price_sensitivity
        market["basis"]                       = symbol_info_tick.basis
        market["category"]                    = symbol_info_tick.category
        market["currency_base"]               = symbol_info_tick.currency_base
        market["currency_profit"]             = symbol_info_tick.currency_profit
        market["currency_margin"]             = symbol_info_tick.currency_margin
        market["bank"]                        = symbol_info_tick.bank
        market["description"]                 = symbol_info_tick.description
        market["exchange"]                    = symbol_info_tick.exchange
        market["formula"]                     = symbol_info_tick.formula
        market["isin"]                        = symbol_info_tick.isin
        market["name"]                        = symbol_info_tick.name
        market["page"]                        = symbol_info_tick.page
        market["path"]                        = symbol_info_tick.path
        
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
    
 
job()
# 定义BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=1)
# sched.start()
