from discord_webhooks import DiscordWebhooks
WEBHOOK_URL=""
def notify(battery_percentage,event=None,secs_left=0):
    webhook=DiscordWebhooks(WEBHOOK_URL)
    if event == "battery-low":
        webhook.set_footer(text="--Abhimanyu Sharma")
        webhook.set_content(title="Battery Reminder!",description="Charge Your Battery Now!")
        webhook.add_field(name="Battery Percent",value=str(battery_percentage))
        webhook.add_field(name="Seconds Left",value=str(secs_left))
    if event == "plugged-in":
        webhook.set_content(title="Your Laptop Is Charging!",description=f"Battery Percentage : {battery_percentage}")
    if event == "fully-charged":
        webhook.set_content(title="Fully Charged!",description=f"Battery Percentage : {battery_percentage}")
        webhook.add_field(name="Seconds Left",value=str(secs_left))        
    if event == "critically-low":
        webhook.set_content(title="Critically Low ... Charge Now!",description=f"Battery Percentage : {battery_percentage}")
        webhook.add_field(name="Seconds Left",value=str(secs_left))
    webhook.send()