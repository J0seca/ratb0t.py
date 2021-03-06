# -*- coding: utf-8 -*-

#pip install discord.py asyncio googlesearch youtube-dl

#ratb0t Discord
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from googlesearch import search
import youtube_dl

client = Bot(command_prefix="!")

#token_bot = input("Bienvenido a ratb0t, pegue token del bot: \n")

@client.event
async def on_ready():
    print('Bot conectado a discord como:  {0.user}'.format(client))
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('ctm'):
        await message.channel.send(':x')

    if message.content.startswith(str(client.user).split("#")[0]):
        await message.channel.send('No pesco wnes ')

        
    await client.process_commands(message)

@client.command()
async def google(ctx, *args):
    await ctx.send("Buscando en google: " + " ".join(args))
    resultado = search(" ".join(args), pause=2, start=0, stop=1)
    for r in resultado:
        await ctx.send(r)

@client.command()
async def youtube(ctx, *args):
    resultado = search("youtube " + " ".join(args), pause=2, start=0, stop=5)
    for r in resultado:
        await ctx.send(r)

@client.command()
async def wiki(ctx, *args):
    resultado = search("wikipedia " + " ".join(args), pause=2, start=0, stop=1)
    for r in resultado:
        await ctx.send(r)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

client.run('OSJFMaf8u08uf0addjKFKHSJnk1meZ5ReYjF666') # Put bot token here
#client.run(token_bot)

