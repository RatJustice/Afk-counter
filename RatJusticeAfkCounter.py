import discord, random, os
from discord.ext import commands
 
input("PRESS ENTER CONTINUE:")
os.system('cls')
token = input("ENTER TOKEN: ")
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))
os.system('cls')
os.system(f'title [AFK COUNTER]')
os.system(f'mode 60,20')
 


 
@client.event
async def on_ready():
  print(f""" \u001b[31m
 ███  █████ █  █   ████  ███  █   █ █   █ █████ █████ ████  
█   █ █     █ █   █     █   █ █   █ ██  █   █   █     █   █ 
█████ ████  ██ █  █     █   █ █   █ █ █ █   █   ████  ████  
█   █ █     █  █  █     █   █ █   █ █  ██   █   █     █   █ 
█   █ █     █   █  ████  ███  █████ █   █   █   █████ █   █ 
 Made By RATJX$TICE. Afk Counter Is Ready, Say "afk check" to type.
------------------------------
""")
 
@client.event
async def on_message(message):
    channel = message.channel
    if message.content.endswith('afk check'):
      for i in range(1, 1000):
        await message.channel.send(i)

 
client.run(token, bot=False)
