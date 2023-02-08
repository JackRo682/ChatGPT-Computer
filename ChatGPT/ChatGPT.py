import discord
import openai

openai.api_key = "      "

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"{message.content}",
        max_tokens=5000,
        n=5,
        stop=None,
        temperature=0.5,
    )

    response_text = response["choices"][0]["text"]
    response_text_all = response_text

    while len(response["choices"][0]["text"].split(" ")) == 1024:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"{message.content} {response_text_all}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response_text = response["choices"][0]["text"]
        response_text_all += response_text
    
    await message.channel.send(response_text_all)


client.run("        ")