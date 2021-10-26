import random

import discord
from discord.ext import commands
from .settings import env


bot = commands.Bot('bro ')


@bot.event
async def on_ready():
	print(f"Meming on behalf of {bot.user.name}.")


@bot.command()
async def ping(ctx):
	await ctx.send(f'pong {bot.latency * 1000}ms')


@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question):
	responses = [
		"It is certain.",
		"It is decidedly so.",
		"Without a doubt.",
		"Yes definitely.",
		"You may rely on it.",
		"As I see it, yes.",
		"Most likely.",
		"Outlook good.",
		"Yes.",
		"Signs point to yes.",
		"Reply hazy, try again.",
		"Ask again later.",
		"Better not tell you now.",
		"Cannot predict now.",
		"Concentrate and ask again.",
		"Don't count on it.",
		"My reply is no.",
		"My sources say no.",
		"Outlook not so good.",
		"Very doubtful.",
	]
	await ctx.send(f'In answer to your question: {question},\n\n{random.choice(responses)}')

bot.run(env('BOT_TOKEN'))
