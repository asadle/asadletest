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
        await client.send_message(message.channel, "안녕하세요 카프라입니다")
    if message.content.startswith("아사들"):
        await client.send_message(message.channel, "왜불러 응 아니야")
    if message.content.startswith("심심해"):
        await client.send_message(message.channel, "심심하면 일을하든가 공부를 하세요")
    if message.content.startswith("공부하기싫어"):
        await client.send_message(message.channel, "공부안하면 나중에 거지가 될수있습니다")   
    if message.content.startswith("응아니야"):
        await client.send_message(message.channel, "응 나두안이야 메롱")
    if message.content.startswith("hi"):
        await client.send_message(message.channel, "하이 방갑다는의미로 안녕이란듯이죠 방갑습니다")
    if message.content.startswith("안니야"):
        await client.send_message(message.channel, "응 나두안이야 메롱")    
    if message.content.startswith("안녕"):
        await client.send_message(message.channel, "방가워요")
        
        
access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
