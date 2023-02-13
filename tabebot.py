import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from random import randint


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

#This is if "Server Members Intent is turned on"
#intents.members = True

#with recent discord.py update, intents need to be applied
client = discord.Client(intents = intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('Hello / ')
    if message.content.startswith('help'):
        await message.channel.send('Need help deciding on what to eat? Type in "recommend" for a randomized suggestion on the genre of food in Tokyo. Alternatively, you could type in "options" to see all supported food suggestions.')
    if message.content.startswith('options'):
        await message.channel.send('Type in "Ramen", "Soba", "Sushi", "Udon", "Katsu", "Curry", "Western", "Italian", "Chinese", "Korean"')
    if message.content.startswith('What should I eat?'):
        await message.channel.send('Type recommend for suggestions')
    if message.content.startswith('recommend'):

        list = [ramen, soba, udon, katsu, curry, western, italian, chinese, korean]
        await message.channel.send(list[randint(0,8)])
        
    if message.content.startswith('Ramen'):
        await message.channel.send('Check these Ramen places out: https://tabelog.com/tokyo/rstLst/ramen/?Srt=D&SrtT=rt&sort_mode=1')
    if message.content.startswith('Soba'):
        await message.channel.send('List for Soba: https://tabelog.com/tokyo/rstLst/soba/?Srt=D&SrtT=rt&sort_mode=1')    
    if message.content.startswith('Sushi'): 
        await message.channel.send('Here are the top sushi places: https://tabelog.com/tokyo/rstLst/sushi/?Srt=D&SrtT=rt&sort_mode=1')
    if message.content.startswith('Udon'):
        await message.channel.send('Check out these Udon locations: https://tabelog.com/tokyo/rstLst/udon/?Srt=D&SrtT=rt&sort_mode=1')
    if message.content.startswith('Katsu'):
        await message.channel.send('Tonkatsu: https://tabelog.com/tokyo/rstLst/tonkatsu/?Srt=D&SrtT=rt&sort_mode=1')
    if message.content.startswith('Curry'):
        await message.channel.send('Top curry locations: https://tabelog.com/tokyo/rstLst/curry/?Srt=D&SrtT=rt&sort_mode=1&select_sort_flg=1')
    if message.content.startswith('Western'):
        await message.channel.send('Tired of Japanese food? Here are some Western suggestions: https://tabelog.com/tokyo/rstLst/yoshoku/?Srt=D&SrtT=rt&sort_mode=1')
    if message.content.startswith('Italian'):
        await message.channel.send('Best italian dishes in Tokyo: https://tabelog.com/tokyo/rstLst/italian/?Srt=D&SrtT=rt&sort_mode=1')
    if message.content.startswith('Chinese'):
        await message.channel.send('Top Chinese dishes around: https://tabelog.com/tokyo/rstLst/chinese/?Srt=D&SrtT=rt&sort_mode=1')
    if message.content.startswith('Korean'):
        await message.channel.send('Best Korean places in Tokyo: https://tabelog.com/tokyo/rstLst/korea/?Srt=D&SrtT=rt&sort_mode=1')                

ramen = 'Check these places out: https://tabelog.com/tokyo/rstLst/ramen/?Srt=D&SrtT=rt&sort_mode=1'
soba = 'List for Soba: https://tabelog.com/tokyo/rstLst/soba/?Srt=D&SrtT=rt&sort_mode=1'
sushi = 'Here are the top sushi places: https://tabelog.com/tokyo/rstLst/sushi/?Srt=D&SrtT=rt&sort_mode=1'
udon = 'Check out these locations: https://tabelog.com/tokyo/rstLst/udon/?Srt=D&SrtT=rt&sort_mode=1'
katsu = 'Tonkatsu: https://tabelog.com/tokyo/rstLst/tonkatsu/?Srt=D&SrtT=rt&sort_mode=1'
curry = 'Top curry locations: https://tabelog.com/tokyo/rstLst/curry/?Srt=D&SrtT=rt&sort_mode=1&select_sort_flg=1'
western = 'Tired of Japanese food? Here are some Western suggestions: https://tabelog.com/tokyo/rstLst/yoshoku/?Srt=D&SrtT=rt&sort_mode=1'
italian = 'Best italian dishes in Tokyo: https://tabelog.com/tokyo/rstLst/italian/?Srt=D&SrtT=rt&sort_mode=1'
chinese = 'Top Chinese dishes around: https://tabelog.com/tokyo/rstLst/chinese/?Srt=D&SrtT=rt&sort_mode=1'
korean = 'Best Korean places in Tokyo: https://tabelog.com/tokyo/rstLst/korea/?Srt=D&SrtT=rt&sort_mode=1'

TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
