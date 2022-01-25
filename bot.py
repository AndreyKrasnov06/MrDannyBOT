import discord
import asyncio
import botCommands
import json
import random
from discord.utils import get
from discord.ext.commands import Bot, has_permissions
from discord.ext import commands
from discord import Embed, Emoji
with open("config.json") as config:
    config = json.load(config)


# УПРАВЛЕНИЕ ПРЕФИКСАМИ
def get_prefix(client, message):  # first we define get_prefix
    with open('prefixes.json', 'r') as f:  # we open and read the prefixes.json, assuming it's in the same file
        prefixes = json.load(f)  # load the json as prefixes
    return prefixes[str(message.guild.id)]  # recieve the prefix for the guild id given


bot = commands.Bot(command_prefix=get_prefix)


@bot.event
async def on_guild_join(guild):  # when the bot joins the guild
    with open('prefixes.json', 'r') as f:  # read the prefix.json file
        prefixes = json.load(f)  # load the json file

    prefixes[str(guild.id)] = 'bl!'  # default prefix

    with open('prefixes.json', 'w') as f:  # write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4)  # the indent is to make everything look a bit neater


@bot.event
async def on_guild_remove(guild):  # when the bot is removed from the guild
    with open('prefixes.json', 'r') as f:  # read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))  # find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f:  # deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)


@bot.command(pass_context=True)
@has_permissions(administrator=True)  # ensure that only administrators can use this command
async def префикс(ctx, prefix):  # command: bl!changeprefix ...
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:  # writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')  # confirms the prefix it's been changed to
    # next step completely optional: changes bot nickname to also have prefix in the nickname
    name = f'{prefix}BotBot'


@bot.event
async def on_ready():
    print("second part of Bot is logged in")
    # channel = bot.get_channel(929398422505668678)
    # emoji = bot.get_emoji(929398978380976198)
    # embed = Embed(title=f'Приветсвую', description=f'Нажмите на реакцию {emoji} ниже чтобы получить роль Участник',
    #              color=0xFF00FF)
    # await channel.send(embed=embed)


# @bot.event
# async def on_message(message):
# pass
# emoji = bot.get_emoji(929398978380976198)
# if message.author != bot.user:
#     return

# if message.channel.category.id == 929400040542322708:
#     members = message.channel.overwrites

#     await message.add_reaction(emoji)
#     for m in members:
#         try:
#             m.nick
#         except AttributeError:
#             pass
#         else:
#             await message.channel.set_permissions(m, overwrite=None)
# if message.channel.id == 929398422505668678:
#     await message.add_reaction(emoji)


@bot.event
async def on_raw_reaction_add(reaction):
    channel = bot.get_channel(reaction.channel_id)
    emoji = bot.get_emoji(929398978380976198)
    if channel.category.id == 929400040542322708:
        if not reaction.member.bot:
            if reaction.emoji == emoji:
                role = reaction.member.guild.get_role(929397694127013889)
                await reaction.member.add_roles(role)


@bot.command()
async def о_сервере(ctx):
    await ctx.send(botCommands.about())


@bot.command()
async def инфо(ctx):
    embed = Embed(
        title=f"Пользователь запросил помощь",
        description="Команды информации:",
        color=0xFF00FF)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"`{get_prefix}о_сервере`",
                    value=f"выведет общую информацию сервера",
                    inline=False)
    embed.add_field(name=f"`{get_prefix}роли`",
                    value=f"выведет информацию о ролях",
                    inline=False)
    embed.add_field(name=f"`{get_prefix}правила`",
                    value=f"выведет основные правила",
                    inline=False)
    embed.add_field(name=f"`{get_prefix}правила_модераторов`",
                    value="выведет основные правила для модераторов",
                    inline=False)
    embed.set_footer(text="всю эту информацию вы можете найти в чатах с соответственным названием")
    await ctx.send(embed=embed)


@bot.command()
async def роли(ctx):
    print("пытаюсь")
    await ctx.send(botCommands.roles())


@bot.command()
async def эмодзи(ctx):
    funny_face = bot.get_emoji(929435758660567050)
    await ctx.send(funny_face)


@bot.command()
async def помощь(ctx):
    embed = Embed(
        title=f"Пользователь запросил помощь",
        description="Команды бота:",
        color=0xFF00FF)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name='''`п!модераторство`''',
                    value='''выведет команды для модераторства
                        ''',
                    inline=False)
    embed.add_field(name='''`п!инфо`''',
                    value='''выведет команды для информации сервера
                        ''',
                    inline=False)
    embed.add_field(name='''`п!прочее`''',
                    value='''выведет прочую информаци по серверу и не только''',
                    inline=False)
    embed.set_footer(text='''по всем остальным вопросам обращаться в поддержку''')
    await ctx.send(embed=embed)


@bot.command()
async def канал(ctx):  # Создаём функцию и передаём аргумент ctx.
    await ctx.send(botCommands.channel)


@bot.command()
async def модерирование(ctx):
    embed = Embed(
        title=f"Команды модераторства:",
        color=0xFF00FF)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="```п!бан```",
                    value="банит пользователя",
                    inline=False)
    embed.add_field(name="```п!мут```",
                    value="мутит пользователя",
                    inline=False)
    embed.add_field(name="```п!анмут```",
                    value="размучивает пользователя",
                    inline=False)
    embed.add_field(name="```п!очистить <число сообщений>```",
                    value="очищает указанное число сообщений",
                    inline=False)
    embed.add_field(name="```п!очистить <число сообщений> <ник человека>```",
                    value="очищает указанное число сообщений определенного человека",
                    inline=False)
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def debug(ctx, emoji: Emoji):
    embed = Embed(description=f"emoji: {emoji}", title=f"emoji: {emoji}")
    embed.add_field(name="id", value=repr(emoji.id))
    embed.add_field(name="name", value=repr(emoji.name))
    await ctx.send(embed=embed)


# @Client.command(pass_context=True)
# async def очистить(ctx, number, user: discord.User = ""):
#    number = int(number)
#    if user == "":
#        await ctx.channel.purge(limit=number + 1)
#    else:
#        await ctx.channel.purge(limit=number + 1, check=lambda m: m.author == user)
#    embed = Embed(title=f"Было очищено {number} соощений", description="это сообщение будет удалено через 5 секунд",
#                  color=0xFF00FF)
#    await ctx.send(embed=embed)
#    await asyncio.sleep(5)
#    await ctx.channel.purge(limit=1)


@bot.command(pass_context=True)
async def чек(ctx, user: discord.Member):
    member = ctx.message.author
    role = member.guild.get_role(929015140601430026)
    if role in user.roles:
        await ctx.send("у вас есть роль")
    else:
        await ctx.send("у вас нету роли")


@bot.command()
async def бан(ctx, user: discord.User, *reason):
    tick = bot.get_emoji(929304182765269012)
    nope = bot.get_emoji(929304208941940736)
    member = ctx.message.author
    role_1 = member.guild.get_role(923277518885228562)
    reason = " ".join(reason)
    if role_1 in ctx.author.roles:
        if user.id != ctx.author.id:
            # ===============================================================
            await ctx.guild.ban(user)
            # ===============================================================
            embed = Embed(title=f"{tick} {user} был успешно забанен",
                          description=f"    причина: {reason}",
                          color=0x9DFAB7)
            embed.set_author(name=user.display_name, icon_url=user.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = Embed(title=f"{nope} {user} не может быть забанен",
                      description=f"    причина: недостаточно прав",
                      color=0xFF6666)
        embed.set_author(name=user.display_name, icon_url=user.avatar_url)
        await ctx.send(embed=embed)


@bot.command()
async def mute(ctx, user: discord.Member, time: int, reason):
    role = user.guild.get_role(1234567890)  # айди роли которую будет получать юзер
    await ctx.send(f"{user} получил мут на {time} минут по причине: {reason}")
    await user.add_roles(role)
    await user.move_to(None)
    await asyncio.sleep(time * 60)
    await user.remove_roles(role)


@bot.command()
async def мут(ctx, user: discord.Member, time: float, *reason):
    tick = bot.get_emoji(929304182765269012)
    nope = bot.get_emoji(929304208941940736)
    member = ctx.message.author
    role_1 = member.guild.get_role(929396705806409758)
    muted = member.guild.get_role(929426920666464357)
    reason = " ".join(reason)
    if role_1 in ctx.author.roles:
        embed1 = Embed(title=f"{tick} {user} был успешно замучен на {time} минут",
                       description=f"    причина: {reason}",
                       color=0x9DFAB7)
        embed1.set_author(name=user.display_name, icon_url=user.avatar_url)
        await user.add_roles(muted)
        await user.move_to(None)
        await ctx.send(embed=embed1)
        await asyncio.sleep(time * 60)
        await user.remove_roles(muted)
        await ctx.send("размучен")
    else:
        embed = Embed(title=f"{nope} {user} не может быть замучен",
                      description=f"    причина: недостаточно прав",
                      color=0xFF6666)
        embed.set_author(name=user.display_name, icon_url=user.avatar_url)
        await ctx.send(embed=embed)


@bot.command()
async def анбан(ctx, user: discord.User):
    await ctx.guild.unban(user)


@bot.event
async def on_member_join(member):
    pass


@bot.event
async def on_member_leave(member):
    pass


@bot.command()
async def join(ctx):
    pass


@bot.command()
async def left(ctx):
    pass


bot.run(config['token'])
