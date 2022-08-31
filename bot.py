from nturl2path import url2pathname
import os
import discord
import random
import requests
from dotenv import load_dotenv
from information import facts
from bs4 import BeautifulSoup

# replace the token variable with your own bot token to test the bot out
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if user_message.lower() == '!nerd':
        await message.channel.send('Commands:\n!fact\n!math\n!wiki')
        return
    elif user_message.lower() == '!fact':
        await message.channel.send('Fun fact, ' + facts[random.randint(0, 99)])
        return
    elif user_message.lower() == '!math':
        equation = ''
        amount_of_nums = random.randint(2, 5)

        for i in range(amount_of_nums):
            equation += str(random.randint(1, 100))
            operator_choice = random.randint(0,3)
            if i + 1 != amount_of_nums:
                if operator_choice == 0:
                    equation += ' + '
                elif operator_choice == 1:
                    equation += ' - '
                elif operator_choice == 2:
                    equation += ' × '
                elif operator_choice == 3:
                    equation += ' ÷ '

        await message.channel.send('What is ' + equation + '?')
        return
    elif user_message.lower() == '!wiki':
        wiki_url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(wiki_url.content, "html.parser")
        title = soup.find(class_="firstHeading").text
        await message.channel.send('Here is a wiki article about ' + title + ': https://en.wikipedia.org/wiki/' + title.replace(' ', '_'))
        return


client.run(TOKEN)