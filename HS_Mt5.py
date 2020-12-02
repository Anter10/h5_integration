
import MetaTrader5 as mt5;
from MetaTrader5 import AccountInfo;


class HS_Mt5:
  
   # 初始化
   def __init__(self):
       print("HS mt5 init")
       mt5.initialize()
       self._account_info = None

    # 登录账号
   def login(self, account,server, password):
       print("当前登录的账号 = ",account)
       account = mt5.login(account,server = server,  password = password)
       self._account_info = mt5.account_info()
       print("当前登录的账号信息  = ",self._account_info)
   
   # 账号信息
   def account_info(self):
       return self.account_info

