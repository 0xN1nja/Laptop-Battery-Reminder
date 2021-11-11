import psutil
from notifications import notify
BATTERY_REMINDER_PERCENT="19"
while True:
    battery=psutil.sensors_battery()
    if str(battery.percent) == BATTERY_REMINDER_PERCENT and battery.power_plugged == False:
        notify(BATTERY_REMINDER_PERCENT,secs_left=battery.secsleft)
        break
    if battery.power_plugged:
        notify(battery.percent,"plugged-in")
        break