import discord
from discord.ext import commands
import requests
import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ping(ctx, *args):
    respuesta = ' '.join(args)
    await ctx.send(respuesta)

@bot.event
async def on_ready():
    print(f'Activos! {bot.user}')

bot.run(config.TOKEN)