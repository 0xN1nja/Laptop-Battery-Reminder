import psutil
import time
from notifications import notify
BATTERY_REMINDER_PERCENT="19"
while True:
    battery=psutil.sensors_battery()
    if int(battery.percent) <= int(BATTERY_REMINDER_PERCENT) and battery.power_plugged == False:
        notify(battery.percent,secs_left=battery.secsleft,event="battery-low")
        time.sleep(60)
    if battery.power_plugged:
        notify(battery.percent,"plugged-in",secs_left=battery.secsleft)
        time.sleep(60)
    if int(battery.percent) == 100:
        notify(battery.percent,event="fully-charged",secs_left=battery.secsleft)
        time.sleep(60)
    if int(battery.percent) <= 9:
        notify(battery.percent,event="critically-low",secs_left=battery.secsleft)
        time.sleep(60)