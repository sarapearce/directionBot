import discord
import os
# import pandas as pd

client = discord.Client()

# message: what the user typed in to the input
# reply: what the chatbot replies to the message with

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        # dict looking for keywords
        # need to loop through the dict (do I have to loop??)
      # if message contains a phrase from the index
      {
        ('Hello', 'Hi', 'Hey', 'Ok'): 'Gobble, Gobble, Gobble',
        ('Who', 'What', 'Where', 'When', 'Why', 'How'): 'Please do not eat me!',
        ('Thanks', 'Turkey', 'Stuffing', 'Pie', 'Pumpkin', 'Potatoes', 'Pilgrim', 'Gobble'): 'I love Thanksgiving Too!'
      }.get(message, 'Happy Thanksgiving you Turkey!')

        # Greeting words [Hello, Hi, Hey, Ok]
            # Reply: Gobble, gobble, gobble
        # Question words [Who, What, Where, When, Why, How]
            # Reply: Please don't eat me!
        # Thanksgiving words [Thanks, Turkey, Stuffing, Pie, Pumpkin, Potatoes, Gobble]
            # Reply: I love Thanksgiving too!
        # Default
            # Reply: Happy Thanksgiving you Turkey!

        reply = 'This is the test reply'
        # send our reply
        await client.send_message(message.channel, reply)

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
