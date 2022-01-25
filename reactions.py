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
Client = bot

@bot.event
async def on_ready():
    print("some reactions add")
    channel = bot.get_channel(930139626662932510)
    user = bot.get_user(716958894223654914)
    #role = user.guild.get_role(930465630816182354)
    await channel.purge(limit=1)
    brawl = bot.get_emoji(930153275326599279)
    mine = bot.get_emoji(930153275381133342)
    gensh = bot.get_emoji(930153274953306214)
    soulk = bot.get_emoji(930153275184009257)
    YouTube = bot.get_emoji(930509769075224616)
    embed = Embed(title=f'Ниже вы можете получить роли, нажав на определенные реакции', description="роли должны быть выданы автоматически. При проблемах пишите в поддержку", color=0xFF00FF)
    embed.add_field(name=f'''Нажмите {YouTube}, чтобы получить роль @подписчик''', value='''при наличии этой роли вы будете получать оповещения о выходе новых роликов''', inline=False)
    embed.add_field(name=f'''Нажмите {brawl}, чтобы получить доступ''', value='''позже вам будет открыт доступ к каналу по тематике игры: brawl stars''', inline=False)
    embed.add_field(name=f'''Нажмите {mine}, чтобы получить доступ''', value='''позже вам будет открыт доступ к каналу по тематике игры: minecraft''', inline=False)
    embed.add_field(name=f'''Нажмите {gensh}, чтобы получить доступ''', value='''позже вам будет открыт доступ к каналу по тематике игры: genshin impact''', inline=False)
    embed.add_field(name=f'''Нажмите {soulk}, чтобы получить доступ''', value='''позже вам будет открыт доступ к каналу по тематике игры: soul knight''', inline=False)
    await channel.send(embed=embed)

@bot.event
async def on_message(message):
    channel = bot.get_channel(930139626662932510)
    brawl = bot.get_emoji(930153275326599279)
    mine = bot.get_emoji(930153275381133342)
    gensh = bot.get_emoji(930153274953306214)
    soulk = bot.get_emoji(930153275184009257)
    YouTube = bot.get_emoji(930509769075224616)
    if message.author != bot.user:
        return
    if message.channel.id == 930139626662932510:
        await message.add_reaction(brawl)
        await message.add_reaction(mine)
        await message.add_reaction(gensh)
        await message.add_reaction(soulk)
        await message.add_reaction(YouTube)


@bot.event
async def on_raw_reaction_add(reaction):
    channel = bot.get_channel(reaction.channel_id)
    role_b = reaction.member.guild.get_role(930139317404315712)
    role_m = reaction.member.guild.get_role(930149851373666355)
    role_g = reaction.member.guild.get_role(930149513031729192)
    role_s = reaction.member.guild.get_role(930149647723405412)
    role_sub = reaction.member.guild.get_role(930465630816182354)
    brawl = bot.get_emoji(930153275326599279)
    mine = bot.get_emoji(930153275381133342)
    gensh = bot.get_emoji(930153274953306214)
    soulk = bot.get_emoji(930153275184009257)
    YouTube = bot.get_emoji(930509769075224616)
    if not reaction.member.bot:
        if reaction.emoji == brawl:
            await reaction.member.add_roles(role_b)
        if reaction.emoji == mine:
            await reaction.member.add_roles(role_m)
        if reaction.emoji == gensh:
            await reaction.member.add_roles(role_g)
        if reaction.emoji == soulk:
            await reaction.member.add_roles(role_s)
        if reaction.emoji == YouTube:
            await reaction.member.add_roles(role_sub)

@bot.event
async def on_raw_reaction_remove(reaction):
    channel = bot.get_channel(reaction.channel_id)
    role_b = reaction.member.get_guild().get_role(930139317404315712)
    role_m = reaction.member.guild.get_role(930149851373666355)
    role_g = reaction.member.guild.get_role(930149513031729192)
    role_s = reaction.member.guild.get_role(930149647723405412)
    role_sub = reaction.member.guild.get_role(930465630816182354)
    brawl = bot.get_emoji(930153275326599279)
    mine = bot.get_emoji(930153275381133342)
    gensh = bot.get_emoji(930153274953306214)
    soulk = bot.get_emoji(930153275184009257)
    YouTube = bot.get_emoji(930509769075224616)
    if not reaction.member.bot:
        if reaction.emoji == brawl:
            await reaction.member.remove_roles(role_b)
        if reaction.emoji == mine:
            await reaction.member.remove_roles(role_m)
        if reaction.emoji == gensh:
            await reaction.member.remove_roles(role_g)
        if reaction.emoji == soulk:
            await reaction.member.remove_roles(role_s)
        if reaction.emoji == YouTube:
            await reaction.member.remove_roles(role_sub)


bot.run(settings['token'])
