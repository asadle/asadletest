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
    if message.content.startswith("경고누적"):
    await client.send_message(message.channel, "고유번호를 입력해 주세요")

    if message.content.startswith("76561198969579722"):
    await client.send_message(message.channel, "샌박기존경고 "3" 회 "누적" "8" "시간벤처리됨")
    if message.content.startswith("76561199028947184 "):
    await client.send_message(message.channel, "샌박기존지속적인 룰위반" "8" "벤처리됨")
    if message.content.startswith("76561199060808072"):
    await client.send_message(message.channel, "서바이벌 룰위반 경고" "1" "입니다")
    if message.content.startswith("76561199028524034"):
    await client.send_message(message.channel, "초식 전투 룰 위반 경고" "1" "회")
    
       
    
access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
