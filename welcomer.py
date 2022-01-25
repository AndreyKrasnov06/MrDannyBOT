import discord

import json
import random
import os

from discord.utils import get
from discord import client
from discord.ext.commands import Bot
from discord.ext import commands
from config import settings
from discord import Embed, Emoji
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix=settings['prefix'])
сlient = bot
channel = bot.get_channel(931904264895352872)


@сlient.event
async def on_member_join(member):
    embed = Embed(description=f'Приветствую, {member.author.mention} на нашем сервере', color=0xFF00FF)
    channel = bot.get_channel(931906445362995252)
    print('joined')
    await channel.send(embed=embed)


@сlient.event
async def on_member_leave(member):
    embed = Embed(description=f'{member.author.mention} покинул сервер', color=0xFF00FF)
    channel = bot.get_channel(931906445362995252)
    await channel.send(embed=embed)





@bot.command()
async def join(ctx):
    embed = Embed(description=f'Приветствую, {ctx.author.mention} на нашем сервере', color=0xFF00FF)
    channel = bot.get_channel(931906445362995252)
    await channel.send(embed=embed)

@bot.command()
async def left(ctx):
    embed = Embed(description=f'{ctx.author.mention} покинул сервер', color=0xFF00FF)
    channel = bot.get_channel(931906445362995252)
    await channel.send(embed=embed)



bot.run(settings['token'])
