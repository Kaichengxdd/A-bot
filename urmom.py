import typing
import discord, random
import dotenv
dotenv.load_dotenv()
import os # default module
from discord import option
bot = discord.Bot(
    activity = discord.Game(
        name = "E"
    ),
    status = discord.Status.idle
)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "coinflip", description = "so u lose")
@option("choice", description="Enter what do you think aadi will think when u ask him what's the answer of 1+1", choices=[2, 3])
async def coinflip(ctx, choice : int):
    result = random.randint(2, 3)
    if (result == choice):
        await ctx.respond("you did it❤️")
    else:
        await ctx.respond("you failed it, you got a 92 :/")

@bot.slash_command()
async def names(ctx):
    arr: typing.List[str] = []
    arr.append(ctx.author.name)
    await ctx.respond(arr)

@bot.slash_command()
async def ping(ctx):
    await ctx.respond(f"Pong! {bot.latency * 1000}ms")

@bot.slash_command()
async def embedtest(ctx):
    embed = discord.Embed(
        title = "Hello",
        description = "This is a test embed",
        color = discord.Color(0xFF00FF),
    )
    await ctx.respond(embed = embed, content = "HI", ephemeral = False)
token=os.getenv("TOKEN")
bot.run(token) # run the bot with the token
