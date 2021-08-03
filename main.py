# Imports
import discord
from discord.ext import commands
import json

# Initialize bot and set command prefix
QBot = commands.Bot(command_prefix="$")

# Cooking variables
QBot.is_cooking = False
QBot.cooking_step = 0
QBot.recipe

# Bot startup status event
@QBot.event
async def on_ready():
    print("QuesadillaBot up and ready to cook!")
    # Load recipe data
    # TODO: Do something with the data
    with open("recipe.json", "r") as recipe_data:
        QBot.recipe = recipe_data

# On_Message Commands
# startcooking: begins the process of displaying the steps to cooking a quesadilla
@QBot.command(aliases=['start'])
async def startcooking(ctx):
    QBot.is_cooking = True
    QBot.cooking_step = 0
    await ctx.send("First step here")

# stopcooking: stops the process of displaying the steps to cooking a quesadilla
@QBot.command(aliases=["stop"])
async def stopcooking(ctx):
    QBot.is_cooking = False
    QBot.cooking_step = 0
    await ctx.send("Stopped cooking a quesadilla.")

# nextstep: displays the next step in cooking a quesadilla
@QBot.command(aliases=['next'])
async def nextstep(ctx):
    if (QBot.is_cooking):
        QBot.cooking_step += 1
        await ctx.send("Next step here")
    else:
        await ctx.send("No quesadilla is being made right now.") 

# Obtain discord bot key
with open("key.txt", "r") as key_data:
    key = key_data.readline()

# Run QuesadillaBot
QBot.run(key)