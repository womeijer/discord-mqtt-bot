# discord-mqtt-bot
a bot that can act as a discord - mqtt bridge

The current functionality is limited to sending a message

## how to use it as a bot?
currently my bot is just running [here](https://repl.it/@womei/discord-mqtt-bot?v=1), so you have to make sure to press the green button.

Add it to your server [here.](https://discord.com/api/oauth2/authorize?client_id=782542970506444820&permissions=0&scope=bot)

### sending a message

Send a PM to the bot with the command prefix "mqtt: " and then the topic of the mqtt message, followed by the message.

For example:
```mqtt: publish "test/womeijer" "hello there"```

sends the message "hello there" to ```mqtt.eclipseprojects.io/test/womeijer```

## how do I run this myself?

- clone this repo
- [set up a discord bot](https://discordapp.com/developers/)
- add a .env file with:
  - ```DISCORD_BOT_SECRET= "YOUR_KEY_HERE"```
  - ```DEFAULT_MQTT_SERVER="your.server.address"```
- run the main.py file
- it should run?

## Notes:
__this is late at night for me and I am tired__


I am working on:
- subscribing to messages and adding callbacks for it
- multiple users/server per context
- user authentication
- a server that's always running
- premium features
