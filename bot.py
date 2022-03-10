import os

import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
downvoted = ""
approved_users = []

def perform_setup():
    global downvoted
    global approved_users
    with open("downvoted.txt") as f:
        downvoted_array = f.read()

    for s in downvoted_array:
        downvoted += s

    with open("approved_users.txt") as f:
        approved_users = f.read().splitlines()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='downvote')
async def downvote(ctx):
    if ctx.author == bot.user:
        return

    if str(ctx.author) in approved_users and ctx.message.reference is not None:
        #await ctx.reply('le downboats')
        await ctx.message.delete()
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await message.reply(downvoted)
        await message.add_reaction('👎')
    else:
        print('Something went wrong or someone other than me tried using it')

perform_setup()
bot.run(TOKEN)
