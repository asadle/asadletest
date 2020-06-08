import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='', type=1))

@client.event
async def on_message(message):
    if message.content.startswith("카프라"):
        await client.send_message(message.channel, "안녕하세요.카프라입니다.")
    if message.content.startswith("아사들"):
        await client.send_message(message.channel, "왜불러")
    
       
    
access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
