import os
import discord
import cryptocompare
from keep_alive import keep_alive
import random

cryptocompare.cryptocompare._set_api_key_parameter("api_key")

prayers = ["Our Father, Satoshi Nakamoto, Bitcoin be thy coin, thy crypto come, trades will be done, on exchanges and in digital wallets.\n\nGive us this day our daily pump. And forgive us our dumps, as we forgive those who hard fork against us.\n\nAnd lead us not into overhyped ICO's, but deliver us from FUD.\n\nFor thine is the crypto, and the hodl, and the glory, for ever and ever. Amen.", "Oh Crypto, who art in blockchains, hallowed be thy wallet, the kingdom come, thy will be done in fiat as it is on blockchains, give us our daily satoshis, and forgive us our weak hands as we forgive those who dump on us, lead us not into fomo, and deliver us from FUD, Amen"]

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$help"):
    await message.channel.send("$btc - Display Bitcoin price in USD\n$eth - Display Ethereum price in USD\n$doge - Display Doge price in USD\n$prayer - Repent")

  if message.content.startswith("$hello"):
    await message.channel.send("Hello, Keep Hodling!")
  
  if message.content.startswith("$prayer"):
    await message.channel.send(random.choice(prayers))

  if message.content.startswith("$btc"):
    await message.channel.send(cryptocompare.get_price('BTC', currency='USD'))

  if message.content.startswith("$eth"):
    await message.channel.send(cryptocompare.get_price('ETH', currency='USD'))

  if message.content.startswith("$doge"):
    await message.channel.send(cryptocompare.get_price('DOGE', currency='USD'))

keep_alive()
client.run(os.getenv("TOKEN"))
