#please create a file in replit called "keep_alive.py" by going to "files" and pressing the forder like icon..aftet that,
#go to the code i made named "keep_alive.py"thats where you will find the code to put into the "keep_alive.py"file you created on replit :) 
import discord
from keep_alive import keep_alive
from discord.ext import commands
import os

#creates the prefix of the bot
bot = commands.Bot(command_prefix="!")


#also please go to commands in replit and press secrets and then write the key as "TOKEN" and then write the value as "your bot token" you can find your token in the site where you made the bot just go back to discord developer portal and then find the application you made and go to bot and find the reset token button after finding press reset token and copy paste the token and paste it into the value in replit 
#prints this on the console if the bot is running and the code is correct
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')


#the bot says hi when someone says hello in the server your bot is in
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if "hello" in msg.content:
        await msg.channel.send("hiii")
#the msg.author == bot.user:return checks if the bot is the one who said hello and doesent run the code when the bot says it because the bot might endlessly keep spamming hi
#this is just a simple code you can learn more by searching for tutorials and reading the "discord.py documentation" i suggest learning python first before engaging in the discord.py documentation

#runs the bot and makes the bot online
keep_alive()
bot.run(os.getenv('TOKEN'))
