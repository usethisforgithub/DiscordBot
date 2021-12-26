# bot.py
import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

import os

import discord
from dotenv import load_dotenv

from uniswap import Uniswap

address = ""          # or None if you're not going to make transactions
private_key = ""  # or None if you're not going to make transactions
version = 2                       # specify which version of Uniswap to use
provider = "https://mainnet.infura.io/v3/0d03a3c1be184734b0c2c27fc9a52a07"    # can also be set through the environment variable `PROVIDER`
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

# Some token addresses we'll be using later in this guide
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
wool = "0x8355DBE8B0e275ABAd27eB843F3eaF3FC855e525"
usdc = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



bot = commands.Bot(command_prefix='/')


@bot.command(name='price')
async def testCommand(ctx):
    woolPrice = uniswap.get_price_input(wool, usdc, 10**18)/1000000
    await ctx.send("WOOL: $" + str(woolPrice))

print("Bot is running")
bot.run(TOKEN)
