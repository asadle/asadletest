import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")



@client.event
async def on_message(message):
    if message.content.startswith("123456789102345678"):
        await message.channel.send("5")

    if message.content.startswith("안녕"):
        await message.channel.send("응 아니야.시팔")


client.run("NzE4NDMxMTUyNTY1NjQ5NDU4.XtoxOg.SApGkeavJhnijQIaRFXoAzBji78")