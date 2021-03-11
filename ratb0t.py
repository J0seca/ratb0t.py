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
        await message.channel.send('????')

        
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


####### noticias DF

import urllib
from urllib import request
from bs4 import BeautifulSoup
import time

@client.command()
async def noticiasdf(ctx):
    source = urllib.request.urlopen("http://df.cl")
    soup = BeautifulSoup(source)
    for link in soup.find_all("h2"):
        await ctx.send(25*"-" + "\n" + link.get_text() + "\n")
        enlace = str(link.a).split('"')[1:2]
        await ctx.send("http://df.cl" + "".join(enlace) + "\n" + "\n")
        time.sleep(5)

@client.command()
async def indices(ctx):
    source = urllib.request.urlopen("https://si3.bcentral.cl/Indicadoressiete/secure/Indicadoresdiarios.aspx")
    soup = BeautifulSoup(source)

    await ctx.send("Indicadores del banco central:\n"+25*"-")

    await ctx.send("Unidad de fomento (UF): " + soup.find(id="lblValor1_1").get_text() + " CLP")
    await ctx.send("Dólar Observado: " + soup.find(id="lblValor1_3").get_text() + " CLP")
    await ctx.send("Onza de Oro: " + soup.find(id="lblValor2_3").get_text() + " USD")
    await ctx.send("Onza de Plata: " + soup.find(id="lblValor2_4").get_text() + " USD")
    await ctx.send("Libra de Cobre: " + soup.find(id="lblValor2_5").get_text() + " USD")
    await ctx.send(25*"-")

client.run('ODE2OTIfe3wtwy4wtwtw2rwr232dewf2DwDndYdUzx8')
#client.run(token_bot)
