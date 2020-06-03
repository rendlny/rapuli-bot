import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv
from functions import *

# load in discord token from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

# set bots command prefix
bot = commands.Bot(command_prefix='~')

@bot.command(name='turnip')
async def turnip_price(ctx, arg1):
    await ctx.message.delete()

    pins = await ctx.channel.pins()
    last_pin = pins[-1]
    pin_content = last_pin.content
    #new_pin_content = addUsersTurnipPriceToMsg(ctx.message.author.mention, pin_content, arg1)

    #check if user posting their price is already mentioned in the pinned msg
    if ctx.message.author.mention in pin_content:
        new_pin_content = ""
        for msg_part in pin_content.split("|"):
            if "TURNIP STONKS" in msg_part:
                new_pin_content = msg_part

            elif ctx.message.author.mention in msg_part:
                user, turnip_link = msg_part.split(" => ")
                new_turnip_link = "| {} => {}{}.".format(user, turnip_link, arg1)
                new_pin_content = new_pin_content+new_turnip_link

            else:
                new_pin_content = new_pin_content+'| '+msg_part
    else:
        new_pin_content = pin_content+"\n\n| {} => https://turnipprophet.io/?prices={}.".format(ctx.message.author.mention, arg1)


    #if ctx.message.author.mention in pin_content:
        #new_pin_content = pin_content+"{}.".format(arg1)
#    else:
    #    new_pin_content = pin_content+"""\n\n{} => https://turnipprophet.io/?prices={}.""".format(ctx.message.author.mention, arg1)
    await last_pin.edit(content=new_pin_content)

@bot.command(name="pattern")
async def turnip_last_pattern(ctx, arg1):
    await ctx.message.delete()
    pattern = turnipPatternToInt(arg1)

    pins = await ctx.channel.pins()
    last_pin = pins[-1]
    pin_content = last_pin.content

    if ctx.message.author.mention in pin_content:
        new_pin_content = pin_content+"&pattern={}".format(pattern)
    else:
        new_pin_content = pin_content+"""\n\n| {} => https://turnipprophet.io/?prices=.&pattern={}""".format(ctx.message.author.mention, pattern)
    await last_pin.edit(content=new_pin_content)

@bot.command(name='start')
async def bot_setup(ctx):
    if ctx.author.id == 207867044140417025:
        await ctx.channel.purge(limit=None)
        message = await ctx.channel.send("STARTING")
        msg_format = """__TURNIP STONKS__\n| {} => https://turnipprophet.io/?prices=""".format(ctx.message.author.mention)
        await message.edit(content=msg_format)
        await message.pin()
        await ctx.message.delete()

@bot.command(name='purge')
async def clear_channel(ctx):
    if ctx.author.id == 207867044140417025:
        await ctx.channel.purge(limit=None, check=lambda msg: not msg.pinned)

@bot.command(name='exit')
async def kill_bot_process(ctx):
    if ctx.author.id == 207867044140417025:
        await ctx.message.delete()
        await bot.logout()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
