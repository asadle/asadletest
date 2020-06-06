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
    if message.content.startswith("코인"):
        await client.send_message(message.channel, "고유번호를 입력해 주세요")
    
    if message.content.startswith("12345678901234567"):
        await client.send_message(message.channel, "현재보유코인은" "3" "입니다")
    if message.content.startswith("76561198846670769"):
        await client.send_message(message.channel, "현재보유코인은" "4" "입니다")
    if message.content.startswith("76561198840612651"):
        await client.send_message(message.channel, "현재보유코인은" "2" "입니다")
    if message.content.startswith("76543210987456321"):
        await client.send_message(message.channel, "현재보유코인은" "3" "입니다")
    
       
    
access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
