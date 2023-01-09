import discord
import os
import dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

dotenv.load_dotenv()
token = os.environ["TOKEN"]
client.run(token)
