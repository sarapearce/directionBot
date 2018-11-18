import discord
import os
import pandas as pd

client = discord.Client()

# message: what the user typed in to the input
# reply: what the chatbot replies to the message     with

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        # API call to GoogleSheet

        # convert Googlesheet object to pandas df, with header row

        # grab listening switch values from df and compare against input

        # grab reply switch values from df and compare against input

        # build our reply

        # send our reply
        # await client.send_message(message.channel, message.content[::-1])
        await client.send_message(message.channel, message.content["waddup homie"])

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
