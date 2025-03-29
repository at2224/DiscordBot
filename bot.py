import discord
import requests 
import json 
import os
from dotenv import load_dotenv
"""
Go to this link to create discord bot, enable permissions, get token, and make invite link:
https://discord.com/developers/applications

"""
load_dotenv()
TOKEN = os.getenv('TOKEN')

# getting memees from public api link in json format and returns reddit meme link
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

# class extends discord.py class which we installed
# responds to discord messages starting with $
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return 
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
    

# set settings basically. set message_content to true to post messages
intents = discord.Intents.default()
intents.message_content = True
# assigns settings to client and uses discord API token to run client
client = MyClient(intents=intents)
client.run(TOKEN)