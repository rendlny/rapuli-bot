import discord

from dotenv import load_dotenv
load_dotenv()
import os

TOKEN = os.getenv("TOKEN")

client = discord.Client()

print('STARTING')

@client.event
async def on_message(message):
    # prevent bot to replying to itself
    if message.author == client.user:
        return

    if message.content.startswith('~turnip'):
        sent = message.content

        try:
            sentparts = sent.split(' ')
            price = sentparts[1]
            msg = price+'Hello {0.author.mention}'.format(message)
        except IndexError:
            msg = 'Please provide your current turnip price'
        else:
            msg = 'Please provide your current turnip price'
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
