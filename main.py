import discord
from discord.ext import commands
from Fusionbrain import *

intents = discord. Intents.default ()
intents.message_content = True
bot = commands.Bot (command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak online durumdayım yardım için /help')

@bot.command()
async def start(ctx):
    await ctx.send(f'Merhaba. Ben {bot.user}, bir Discord sohbet botuyum.')

@bot.command()
async def AiImage(ctx, *, metin):
    asd = await ctx.send("Görsel oluşturuluyor pls bekleyin")
    imager(file_generate(metin), "AI_img.jpeg")
    await asd.edit(content="Görüntü Oluşturuldu")
    with open("AI_img.jpeg",'rb') as fotograf:
        qwerty = discord.File(fotograf)
        await ctx.send(file = qwerty)


bot.run("")