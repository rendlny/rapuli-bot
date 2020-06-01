import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv

# load in discord token from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

# set bots command prefix
bot = commands.Bot(command_prefix='~')

@bot.command(name='turnip')
async def turnip_price(ctx, arg1):
    await ctx.message.delete()

    pins = await ctx.channel.pins()  # or await channel.pins()
    last_pin = pins[-1]
    pin_content = last_pin.content
    await last_pin.edit(content=pin_content+"{}.".format(arg1))

    await client.send_message(message.channel, ' : %s is the best ' % myid)

@bot.command(name='start')
async def bot_setup(ctx):
    if ctx.author.id == 207867044140417025:
        await ctx.channel.purge(limit=None)
        message = await ctx.channel.send("STARTING")
        msg_format = """__TURNIP STONKS__
        {} => https://turnipprophet.io/?prices=""".format(ctx.message.author.mention)
        await message.edit(content=msg_format)
        await message.pin()
        await ctx.message.delete()

@bot.command(name='purge')
async def clear_channel(ctx):
    if ctx.author.id == 207867044140417025:
        await ctx.channel.purge(limit=None, check=lambda msg: not msg.pinned)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
