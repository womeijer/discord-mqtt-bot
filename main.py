# connects to a server and lets you send messages
import os
import discord
from discord.ext import commands
import paho.mqtt.client as mqtt


description = '''A great little bot that lets you bridge MQTT and discord!'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='mqtt: ', description=description, intents=intents)

server_message = "no connection"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def connected(ctx):
    """Returns the latest result of the MQTT client connecting."""
    await ctx.send(server_message)

@bot.command()
async def publish(ctx, topic:str, message: str):
    """sends a message to the server"""
    try:
        #send the message on the MQTT server
      result = client.publish(topic, payload=message, qos=0, retain=False)
    except Exception:
        await ctx.send('something when wrong!')
        return
    #result = "success"

    await ctx.send("The publish attempt was {}".format(result.is_published()))


### MQTT setup and call back functions
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global server_message
    print("Connected with result code "+str(rc))
    server_message = "Connected to {} with code {}".format(server, str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
server = os.environ.get("DEFAULT_MQTT_SERVER")
client.connect(server, 1883, 100)

#start non blocking MQTT
client.loop_start()


### connect Discord robot
token = os.environ.get("DISCORD_BOT_SECRET") 

#bot.run is blocking code
bot.run(token)

#stop the MQTT loop
client.loop_stop(force=True)