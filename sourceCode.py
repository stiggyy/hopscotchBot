#imports
import discord
import os
import time
import discord.ext
import random
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
from discord.ext import commands
import keep_alive


#fun setup stuff
client = discord.Client()

#the default prefix is ".". I removed the default help command. To bring it back delete "help_command=None".
client = commands.Bot(command_prefix='.', help_command=None)

#on connect/disconnect
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(".help - music commands in the works 👀"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_disconnect():
  print("Bot disconnected.")

#commands
@client.command()
#basic ping command(this is really just to test if the bot works)
async def ping(ctx):
    await ctx.send("pong!") 
    print("Command executed.")

@client.command()
#hugs whoever the commander mentions.
async def hug(ctx, member: discord.Member):
  await ctx.send("Hugged " + member.mention + "!")
  print("Command executed.") 

@client.command()
#kills whoever the commander mentions.
async def kill(ctx, member: discord.Member):
  await ctx.send("killed " + member.mention + "!")
  print("Command executed.") 

@client.command()
#shares pronouns
async def pronouns(ctx):
  await ctx.send("My pronouns are they/them!")
  print("Command executed.")

@client.command()
#sends invite link
async def invite(ctx):
  await ctx.send("Invite me to your server! http://bit.ly/hopscotch-invite")
  print("Command executed.")

@client.command()
#sends back message
async def realwomen(ctx):
    await ctx.send("real women.... SHIT on their husbands!!!!!!!!!!!!")
    print("Command executed.")

@client.command(aliases = ['8ball', '8b', 'ask'])
#randomly chooses an answer in response to any question asked by the commander
async def eightball(ctx, *, queston):
    responses = ["yes", "absolutely", "affirmative" , "no", "maybe", "of course not, what'd you expect?", "I Do Not Know.", "no <3", "ribbit ribbit", "The answer is unclear."]
    await ctx.send(random.choice(responses))
    print("Command executed.")

@client.command(aliases = ['cf'])
#either returns heads or tails
async def coinflip(ctx):
    cf = ["heads", "tails"]
    await ctx.send(random.choice(cf))
    print("Command executed.")

@client.command(aliases = ['np'])
#returns a random number 1-10
async def numberpick(ctx):
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    await ctx.send(random.choice(x))
    print("Command executed.")

@client.command(aliases = ['r'])
#reacts to a message with the frog emoji
async def react(ctx,*, question):
  await ctx.message.add_reaction('🐸')
  print("Command executed.")

@client.command()
#sends link to source code
async def source(ctx):
  await ctx.send("Here is my source code! https://github.com/stiggyy/hopscotchBot")
  print("Command executed.")

@client.command()
#sends link to list of commands
async def help(ctx):
  await ctx.send("https://github.com/stiggyy/hopscotchBot/blob/main/about/help-commands.md")
  print("Command executed.")

  
@client.command()
#dms command
async def dm(ctx):
  await ctx.author.send("👋 Howdy! Im hopscotch.")
  print("Command executed.")




client.run('token') 
