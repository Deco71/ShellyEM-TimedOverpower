import os
from datetime import datetime
from time import sleep
from time import time
from dotenv import load_dotenv
import requests
import json

load_dotenv()
timer_threshold = float(os.getenv("TIMER"))
power_threshold  = float(os.getenv("POWER"))
ip = os.getenv("IP")
check = int(os.getenv("CHECK"))
api = os.getenv("API")

if (not timer_threshold) or (not power_threshold) or (not ip) or (not check) or (not api):
    print("Error: one or more env variables are missing. Check .env file using the variables defined in the example.env file")
    exit(1)

print("Timer: " + str(timer_threshold))
print("Power: " + str(power_threshold))
print("IP: " + ip)
print("Check: " + str(check))
print("API: " + api)
print("------------------")


timer = 0

while True:
    sleep(check)
    try:
        res = requests.get('http://' + ip + '/status')
    except:
        print("[ERROR] -" + str(datetime.now()) + "- Error: Could not connect to the device")
        continue
    actual_usage = json.loads(res.text)['emeters'][1]["power"]
    print("[INFO] -" + str(datetime.now()) + "- Actual usage: " + str(actual_usage))
    if actual_usage > power_threshold:
        if timer == 0:
            timer = time()
        else: 
          if time() - timer > timer_threshold:
            print("[INFO] -" + str(datetime.now()) + "- Power usage is too high. Hitting URL:")
            try:
                res = requests.get(api)
            except:
                print("[ERROR] -" + str(datetime.now()) + "- Error: Could not connect to the API endpoint")
                continue
            timer = 0  
    else:
        timer = 0
