# Dependency imports
# from dotenv import load_dotenv
import discord
import playsound
# import winsound
# import bs4

# from discord.ext import commands
from discord.ext.commands import Bot
from gtts import gTTS
from pathlib import Path
from selenium import webdriver

# Python standard imports
from time import sleep
from datetime import datetime
# import requests
import math
import os
import random

# Get Environment variables - replit enforces public repos, 
# 	But you can define access private environment variables with os.getenv("VARNAME")
# NEW
if Path('.env').exists() is True:
	from environs import Env
	env = Env()
	env.read_env('.environment')
	TOKEN = env('DISCORD_TOKEN')
	USER = env('USER')
	CODE_CHANNEL = env("CODE_CHANNEL")
	INSTAGRAM_USERNAME = env("INSTAGRAM_USERNAME")
	INSTAGRAM_PASSWORD = env("INSTAGRAM_PASSWORD")
else:
	from os import getenv
	TOKEN = getenv('DISCORD_TOKEN')
	USER = getenv('USER')
	CODE_CHANNEL = getenv("CODE_CHANNEL")
	INSTAGRAM_USERNAME = getenv("INSTAGRAM_USERNAME")
	INSTAGRAM_PASSWORD = getenv("INSTAGRAM_PASSWORD")
# DEPRECATED bc I prefer environs
# load_dotenv("text.txt")

BASE_DIR = Path(__file__).resolve()
CLOUD_DIR = BASE_DIR / "cloud"
POLLS_DIR = BASE_DIR / "polls"
SLEEP_DIR = BASE_DIR / "sleep"

# Selenium setup
# DEPRECATED
# useChrome = False
# if useChrome is True:
#     chromedriver_path = 'chromedriver'
	# webdriver = webdriver.Chrome(executable_path=chromedriver_path)

# Discord setup
bot = Bot("!")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def read_boolfile(filename):
	with open(filename, "r") as bool_file:
		value = bool_file.read().strip()
	
	if value == "True":
		return True
	elif value == "False":
		return False
	else:
		raise ValueError(".bool has been corrupted")


@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

# CODESTYLE: Use with blocks rather than file.open, file.do, file.close
	# file = open("cloud.txt", "r")
	# cloud = file.read().splitlines()
	# file.close()
	with open("cloud.txt", "r") as file:
		cloud_data = file.read().splitlines()

	# file = open("cloud id.txt", "r")
	# cloudID = file.read().splitlines()
	# file.close()
	with open("cloud_id.txt", "r") as file:
		cloud_id_data = file.read().splitlines()

# TODO: Not quite sure what this does, could do the same with Path().iterdir()?
# Depends whether cloud dir contains dirs?
	files = next(os.walk("cloud"))[2]
	channel = client.get_channel(857310481261133864)

	# count = 0
	# loop=bool(True)    # CODESTYLE: this is the same as loop = True
	# while loop ==True: # CODESTYLE: no need to define loop, you can just say "while True:"
# CODESTYLE: Use for-loop rather than while-loop with counter variable
	cloud_list = []
	cloud_id_list = []
	for file in files:
		# if count < len(files):
		# if files[count] not in cloud:
		if file not in cloud_data:
			# sent = f'cloud/{file}'
			# item = await channel.send(file=discord.File(sent))
			item = await channel.send(file=discord.File(CLOUD_DIR / file))
			item = str(item.id)

# CODESTYLE: rather than opening and closing the file n times over the loop,
#              it would be more efficient to append the new data to a list 
#              and write from the list after the loop.
			# file = open("cloud id.txt", "a")
			# file.write(item)
			# file.write("\n")
			# file.close()
			# with open("cloud_id.txt", "a") as f:
			# 	f.write(item)
			# 	f.write("\n")
			cloud_id_list.append(item)

			# file = open("cloud.txt", "a")
			# file.write(files[count])
			# file.write("\n")
			# file.close()
			# with open("cloud.txt", "a") as f:
			# 	f.write(file)
			# 	f.write("\n")
				# count = count + 1
			cloud_list.append(file)
			# else:
			#     count = count + 1

		# else:
		#     break
	with open("cloud.txt", "a") as file:
		file.write("\n".join(cloud_list))

	with open("cloud_id.txt", "a") as file:
		file.write("\n".join(cloud_id_list))

	# count = 0
	# loop = bool(True)
	# while loop is True:
# CODESTYLE: Use for-loop with enumerate instead of while-loop + manual counter
	cloud_list = []
	cloud_id_list = []
	for count, line in enumerate(cloud_data):
		# if count < len(cloud):
		# if cloud[count] not in files:
		if line not in files: 
			remove = await channel.fetch_message(cloud_id_data[count])
			await remove.delete()

			gone = cloud_data.pop(count)
			gone_id = cloud_id_data.pop(count)

			# file = open("cloud.txt", "w")
			# with open("cloud.txt", "w") as f:
				# for line in cloud_data:
			if line != gone:
						# file.write(line)
						# file.write("\n")
						# f.write(line)
						# f.write("\n")
				cloud_list.append(line)
			# file.close()

			# file = open("cloud id.txt", "w")
			# with open("cloud id.txt", "w") as f:
			for line in cloud_id_data:
				if line != gone_id:
						# file.write(line)
						# file.write("\n")
						# f.write(line)
						# f.write("\n")
					cloud_id_list.append(line)
			# file.close()
		# else:
		#     break
	with open("cloud.txt", "a") as file:
		file.write("\n".join(cloud_list))

	with open("cloud_id.txt", "a") as file:
		file.write("\n".join(cloud_id_list))


@client.event
async def on_member_join(member):
	sys_channel = member.guild.system_channel
	if sys_channel is not None:
		try:
			await sys_channel.send(
				f'Hey {member.mention} welcome to {member.guild.name}!'
				'To see all my functions, type "bot functions"!')
		except Exception as error:
			print(error)


@client.event
async def on_message(message):
	# TorF = open("torf.txt", "r")
	# file = open(".bool", "r")
	# on = bool_file.read()
	# TorF.close()
	BOT_ENABLED = read_boolfile('.bool')

	europe = ['eu', 'europe']
	america = ['na', 'america', 'north america']

	if message.author == client.user:
		return
	# if message.content.startswith("bot"):
	# 	await message.channel.send('')

	if len(message.content) == 6:
		if message.content == message.content.upper():

			bet = message.content.isalpha()
			if bet is True:

				channel = client.get_channel(
					833891322029015060)  #CODE_CHANNEL)
				sent = client.get_channel(message.channel.id)
				if sent != channel:
					guild = (message.guild.name)
					print(guild, GUILD)
					if guild == GUILD:
						print(5)
						file = open("lastRegion.txt", "r")
						region = file.read()
						file.close()
						await channel.send(
							f'suspected among us code: {message.content}')
						await channel.send(f'last recorded region: {region}')

	if message.content.lower() in europe:
		# file = open("lastRegion.txt", "w")
		with open("lastRegion.txt", "w") as file:
			file.write("EU")
		# file.close()

	elif message.content in america:
		# file = open("lastRegion.txt", "w")
		with open("lastRegion.txt", "w") as file:
			file.write("NA")
		# file.close()

	message.content = message.content.lower()

	guild = message.guild

	if "goodnight" in message.content:
		author = str(message.author)
		author = author.split("#")[0]
		await message.channel.send(
			f'Hey {author} dont forget to record your sleeping times!')

	# if "bot functions" in message.content and on is True:
	if "bot functions" in message.content and BOT_ENABLED is True:
		response = (
			'i am capable of:\nbot functions by typing: "BOT functions"random number generator by typing: "BOT rng"\ngetting the time for people in other time zones by typing "BOT current times"\ncreating polls by typing "bot create poll"+a list of the options\nvoting in a poll by typing "bot poll vote"+the number of the option you want to choose\nclosing a poll by typing "bot close poll"\ngetting your average sleep schedule by typing "bot sleep"\nsay something mean by typing "bot offend"\nautomatically send suspected among us codes to codes chat\nrecords last suspected among us region\n\ndeveloper only features:\nturning me on and off'
		)
		await message.channel.send(response)

	# elif "bot rng" in message.content and on is True:
	elif "bot rng" in message.content and BOT_ENABLED is True:
		message.content = message.content.replace("bot rng", "")
		if len(message.content) == 0 or message.content[0] == " " and len(
				message.content) < 2:
			response = "ERROR: please add perimeters for the random number"
			await message.channel.send(response)

		else:
			try:
				message.content = message.content[1:len(message.content)]
				paramOne = message.content.split(",")[0]
				paramTwo = message.content.split(",")[-1]
				print(paramOne, paramTwo)

				paramOne = int(paramOne)
				paramTwo = int(paramTwo)
				rng = random.randint(paramOne, paramTwo)
			except:
				rng = 'ERROR: incorrect formatting. example: "bot rng 25,75"'
			await message.channel.send(rng)

	# elif "bot current times" in message.content and on is True:
	elif "bot current times" in message.content and BOT_ENABLED is True:
		now = datetime.now()
		minute = now.strftime("%M")
		england = now.strftime("%H")
		england = int(england)
		a = england + 9
		if a > 23:
			a = a - 24
		israel = england + 2
		if israel > 23:
			israel = israel - 24
		GandN = england + 1
		if GandN == 24:
			GandN = 0
		c = england - 5
		if c < 0:
			c = c + 24
		england = str(england)
		israel = str(israel)
		GandN = str(GandN)
		c = str(c)
		a = str(a)
		response = str("Englands time is " + england + ":" + minute +
					   "\nNetherlands and Germanys time is " + GandN + ":" +
					   minute + "\nIsrael and Russias time is " + israel +
					   ":" + minute + "\nCanadas time is " + c + ":" + minute +
					   "\nAustralias time is " + a + ":" + minute)

		response = response.replace("'", "")
		await message.channel.send(response)

	elif "bot turn off" in message.content:
		# if on is True:
		if BOT_ENABLED is True:
			if message.author.id == 484893096761622554:
				# TorF = open("torf.txt", "w+")
				with open("torf.txt", "w+") as TorF:
					TorF.write("False")
				# TorF.close()

				await message.channel.send("goodbye!")
			else:
				await message.channel.send(
					"you dont have permission to turn me off >:(")
		else:
			await message.channel.send("im already off")

	elif "bot turn on" in message.content:
		# if on is False:
		if BOT_ENABLED is False:
			if message.author.id == 484893096761622554:
				# TorF = open("torf.txt", "w+")
				with open("torf.txt", "w+") as TorF:
					TorF.write("True")
				# TorF.close()

				await message.channel.send("hello!")
			else:
				await message.channel.send(
					"you dont have permission to turn me on >:(")
		else:
			await message.channel.send("im already on")

	# elif "bot create poll" in message.content and on is True:
	elif "bot create poll" in message.content and BOT_ENABLED is True:
		# currentPole = open("poll files/current_pole.txt", "r")
		with open(POLLS_DIR / "current_poll.txt", "r") as current_poll:
			torf = current_poll.read()
		# currentPole.close()
		if torf is True:
			await message.channel.send("there is already an active poll!")
		elif torf is False:
			# currentPole = open("poll files/current_pole.txt", "w+")
			with open(POLLS_DIR / "current_poll.txt", "w+") as current_poll:
				current_poll.write("True")
			# currentPole.close()
			pollList = []
			message.content = message.content.replace("bot create poll ", "")
			count = 0
			lastCount = 0
			loop = bool(True)
			while loop is True:
				if count == len(message.content):
					pollList.append(message.content[lastCount:count])
					break
				else:
					if message.content[count] == ",":
						pollList.append(message.content[lastCount:count])
						lastCount = count
						count = count + 2
					else:
						count = count + 1
			count = 0
			pollList[0] = "," + pollList[0]
			loop = bool(True)
			while loop is True:
				if count < len(pollList):
					num = str(count + 1)
					add2list = pollList[count].replace(",", "")
					# file = open("poll files/poll.txt", "a")
					with open(POLLS_DIR / "poll.txt", "a") as file:
						file.write(add2list)
						file.write("\n")
					# file.close()

					pollList[count] = pollList[count].replace(
						",", "type " + num + " for ")
					await message.channel.send(pollList[count])
					count = count + 1
				else:
					break

	# elif "bot poll vote" in message.content and on is True:
	elif "bot poll vote" in message.content and BOT_ENABLED is True:
		# currentPole = open("poll files/current_pole.txt", "r")
		with open(POLLS_DIR / "current_poll.txt", "r") as current_poll:
			torf = current_poll.read()
		# currentPole.close()

		if torf is False:
			await message.channel.send("there is no poll currently open!")
		elif torf is True:

			# alreadyVoted = open("poll files/already voted.txt")
			with open(POLLS_DIR/ "voted.txt") as already_voted:
				voter = already_voted.read().splitlines()
			# alreadyVoted.close()

			message.author = str(message.author)
			author = message.author.split("#")[0]
			if author in voter:
				await message.channel.send(f'{author} has already voted!')
			else:

				message.content = message.content.replace("bot poll vote ", "")
				message.content = int(message.content)

				# options = open("poll files/poll.txt", "r")
				with open(POLLS_DIR / "poll.txt", "r") as options:
					get = options.read().splitlines()
				# options.close()

				if message.content > len(get) + 1:
					await message.channel.send(
						f"ERROR: Not a valid vote. There aren't this many options!"
					)
				elif message.content < 1:
					await message.channel.send(
						f'ERROR: Not a valid vote. Please choose a number greater than 0!'
					)
				else:
					await message.channel.send(
						f'{author} voted for {get[message.content-1]}!')
					# file = open("poll files/already voted.txt", "a")
					with open(POLLS_DIR / "voted.txt", "a") as file:
						file.write(author)
						file.write("\n")
					# file.close()

					# file = open("poll files/votes.txt", "a")
					with open(POLLS_DIR / "votes.txt", "a") as file:
						file.write(str(message.content))
						file.write("\n")
					# file.close()

	elif "bot close poll" in message.content:
		# file = open("poll files/current_pole.txt", "r")
		with open(POLLS_DIR / "current_poll.txt", "r") as file:
			open_poll = bool(file.read())
		# file.close()

		if open_poll is False:
			await message.channel.send(
				"ERROR: there is no poll currently open!")
		else:

			# collect = open("poll files/votes.txt")
			with open(POLLS_DIR / "votes.txt") as collect:
				votes = collect.read().splitlines()
			# collect.close()

			# if len(votes) == 0:
			#     await message.channel.send("No votes yet, nothing has won")

			# else:
			if len(votes) >= 1:
				# options = open("poll files/poll.txt", "r")
				with open(POLLS_DIR / "poll.txt", "r") as options:
					choice = options.read().splitlines()
					length = len(choice)
				# options.close()

				def most_frequent(vote):
					return max(set(vote), key=vote.count)

				winner = int(most_frequent(vote))
				howmany = 0

				num = 0
				loop = bool(True)
				while loop is True:
					if num == len(vote):
						break
					else:
						if vote[num] == winner:
							print("fuck")
							howmany = howmany + 1
						num = num + 1

				await message.channel.send(
					f'{choice[winner-1]} won the poll with {howmany} votes!')

			# file = open("poll files/current_pole.txt", "w")
			# with open(POLLS_DIR / "current_poll.txt", "w") as file:
			# 	file.write("False")
			# # file.close()

			# # file = open("poll files/poll.txt", "w")
			# with open(POLLS_DIR / "poll.txt", "w") as file:
			# 	file.write("")
			# # file.close()

			# with open(POLLS_DIR / "voted.txt", "w") as file:
			# 	file.write("")
			# # file.close()

			# with open(POLLS_DIR / "votes.txt", "w") as file:
			# 	file.write("")
			# file.close()
			for file in POLLS_DIR.iterdir():
				with open(file, "w") as f:
					f.write("")

			with open(POLLS_DIR / "current_poll.txt", "w") as file:
				file.write("False")

	elif "bot offend" in message.content:
		# file = open("offend.txt", "r")
		with open ("offend.txt", "r") as file:
			mean = file.read().splitlines()
		offend = random.choice(mean)
		await message.channel.send(offend)

	elif "@thedepresseddonkey" in message.content:
		user = client.get_user(484893096761622554)
		message.author = str(message.author)
		author = message.author.split("#")[0]
		await user.send(
			f'"{author}" {message.content} in {message.guild.name}!')

	elif "484893096761622554" in message.content:
		message.author = str(message.author)
		author = message.author.split("#")[0]
		message.content = str(message.content)
		message.content = message.content.replace("<@!484893096761622554>",
												  "@thedepresseddonkey")
		message = (f'{author} said {message.content}')

		tts = gTTS(message)
		tts.save("tts.mp3")
		playsound.playsound("tts.mp3")

	elif "bot sleep" in message.content:
		message.author = str(message.author)
		author = message.author.split("#")[0]
		now = datetime.now()
		minute = now.strftime("%M")
		hour = now.strftime("%H")

		# file = open("sleep list/" + author, "a+")
		with open(SLEEP_DIR / author, "a+") as file:
			file.write(hour + ":" + minute)
			file.write("\n")
		# file.close()

		# file = open("sleep list/" + author, "r")
		with open(SLEEP_DIR / author, "r") as file:
			schedule = file.read().splitlines()
		# file.close()
		count = 0
		hour = 0
		minute = 0
		loop = bool(True)
		while loop is True:
			if count == len(schedule):
				break
			else:
				current = schedule[count]
				currentH = current.split(":")[0]
				currentM = current.split(":")[-1]

				currentH = int(currentH)
				currentM = int(currentM)

				hour = hour + currentH
				minute = minute + currentM
				count = count + 1

		minute = minute + (hour * 60)
		divide = minute / len(schedule)
		averageH = math.floor(divide / 60)
		averageM = math.floor(divide % 60)

		await message.channel.send(
			f'Good night {author}!\nyour average time to go to bed is {averageH}:{averageM}'
		)

	if not guild:
		if message.author.name == USER:
			if "special functions" in message.content:
				await channel.send(
					"My special functions include:\nsending instagram DMs\nsending files through discord"
				)

				try:
					agree = webdriver.find_element_by_xpath(
						'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button'
					)
					agree.click()
					sleep(3)
				except Exception as error:
					print(error)

				elems = webdriver.find_elements_by_xpath(
					'//*[@id="thumbnail"]')
				torf = True
				for elem in elems:
					if torf is True:
						link = elem.get_attribute("href")
						webdriver.get(link)
						torf = False

			elif "send message " in message.content:
				if message.author.id == 484893096761622554:
					message.content = message.content.replace(
						"bot send message to ", "")
					count = 0
					count2 = 0
					loop = bool(True)
					while loop is True:

						if message.content[count] == ",":
							break
						else:
							count = count + 1
					name = message.content[:count]
					text = message.content.split(",")[-1]

					webdriver.get(
						'https://www.instagram.com/accounts/login/?source=auth_switcher'
					)
					sleep(3)

					try:
						cookies = webdriver.find_element_by_xpath(
							'/html/body/div[2]/div/div/button[1]')
						cookies.click()
						sleep(3)

						username = webdriver.find_element_by_xpath(
							'//*[@id="loginForm"]/div/div[1]/div/label/input')
						username.send_keys(INSTAGRAM_USERNAME)
						password = webdriver.find_element_by_xpath(
							'//*[@id="loginForm"]/div/div[2]/div/label/input')
						password.send_keys(INSTAGRAM_PASSWORD)
						sleep(1)

						button_login = webdriver.find_element_by_xpath(
							'//*[@id="loginForm"]/div/div[3]/button')
						button_login.click()
						sleep(3)
					except:
						print("already logged in")

					webdriver.get('https://www.instagram.com/direct/inbox/')
					sleep(3)

					try:
						no = webdriver.find_element_by_xpath(
							'/html/body/div[3]/div/div/div/div[3]/button[2]')
						no.click()
						sleep(5)
					except:
						pass

					choose = webdriver.find_element_by_xpath(
						'//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'
					)
					choose.click()
					sleep(3)

					writeName = webdriver.find_element_by_xpath(
						'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input'
					)
					writeName.send_keys(name)
					sleep(5)

					who = webdriver.find_element_by_xpath(
						'/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button'
					)
					who.click()
					sleep(3)

					Next = webdriver.find_element_by_xpath(
						'/html/body/div[5]/div/div/div[1]/div/div[2]/div/button'
					)
					Next.click()
					sleep(3)

					writeMessage = webdriver.find_element_by_xpath(
						'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'
					)
					writeMessage.send_keys(text)

					send = webdriver.find_element_by_xpath(
						'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button'
					)
					send.click()

					await message.channel.send('message "' + text +
											   '" sent successfully to "' +
											   name + '"!')

			else:
				await message.channel.send(
					"This was not a command, try typing 'bot functions' for my normal functions or type 'special functions' for more personal features!"
				)


client.run(TOKEN)
