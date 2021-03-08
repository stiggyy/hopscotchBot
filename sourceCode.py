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

#client def
client = discord.Client()
#command call
client = commands.Bot(command_prefix='.')

#events when/if bot connects/disconnects
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(".help"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_disconnect():
  print("Bot disconnected.")

#commands
@client.command()
async def ping(ctx):
    await ctx.send("pong!") 

@client.command()
async def hug(ctx, member: discord.Member):
  await ctx.send("Hugged " + member.mention + "!") 

@client.command()
async def pronouns(ctx):
  await ctx.send("My pronouns are they/them!")

@client.command()
async def invite(ctx):
  await ctx.send("Invite me to your server! http://bit.ly/hopscotch-invite")

@client.command()
async def realwomen(ctx):
    await ctx.send("real women.... SHIT on their husbands!!!!!!!!!!!!")

@client.command(aliases = ['8ball', '8b', 'ask'])
async def eightball(ctx, *, queston):
    responses = ["yes", "no", "maybe", "of course not, what'd you expect?", "I Do Not Know.", "no <3", "ribbit ribbit", "The answer is unclear."]
    await ctx.send(random.choice(responses))

@client.command(aliases = ['cf'])
async def coinflip(ctx):
    cf = ["heads", "tails"]
    await ctx.send(random.choice(cf))

@client.command(aliases = ['np'])
async def numberpick(ctx):
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    await ctx.send(random.choice(x))

@client.command()
async def react(ctx,*, question):
  emojis = ['❤️', '👍', '🐸']
  await ctx.send(random.choice(emojis))



client.run('token') 
