import psutil
from notifications import notify
BATTERY_REMINDER_PERCENT="19"
while True:
    battery=psutil.sensors_battery()
    if str(battery.percent) == BATTERY_REMINDER_PERCENT and battery.power_plugged == False:
        notify(BATTERY_REMINDER_PERCENT,secs_left=battery.secsleft,event="battery-low")
        break
    if battery.power_plugged:
        notify(battery.percent,"plugged-in")
        break
    if str(battery.percent) == "100":
        notify(battery.percent,event="fully-charged")
        break