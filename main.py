# Dependency imports
# from dotenv import load_dotenv)
import discord
import playsound
# import winsound
import bs4
from environs import Env
# from discord.ext import commands
from discord.ext.commands import Bot
from gtts import gTTS
from selenium import webdriver

# Python standard imports
from time import sleep
from datetime import datetime
import requests
import math
import os
import random

# Get Environment variables
# NEW
env = Env()
env.read_env('env.txt')
TOKEN = env('DISCORD_TOKEN')
USER = env('USER')
CODE_CHANNEL = env("CODE_CHANNEL")
INSTAGRAM_USERNAME = env("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = env("INSTAGRAM_PASSWORD")
# DEPRECATED
# load_dotenv("text.txt")
# TOKEN = os.getenv('DISCORD_TOKEN')
# USER = os.getenv('USER')
# CODE_CHANNEL = os.getenv("CODE_CHANNEL")

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


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

    file = open("cloud.txt", "r")
    cloud = file.read().splitlines()
    file.close()

    file = open("cloud id.txt", "r")
    cloudID = file.read().splitlines()
    file.close()

    count = 0
    files = next(os.walk("cloud"))[2]
    channel = client.get_channel(857310481261133864)

    loop = bool(True)
    while loop is True:
        if count < len(files):
            if files[count] not in cloud:
                sent = f'cloud/{files[count]}'
                item = await channel.send(file=discord.File(sent))
                item = str(item.id)

                file = open("cloud id.txt", "a")
                file.write(item)
                file.write("\n")
                file.close()

                file = open("cloud.txt", "a")
                file.write(files[count])
                file.write("\n")
                file.close()
                count = count + 1

            else:
                count = count + 1

        else:
            break
    count = 0
    loop = bool(True)
    while loop is True:
        if count < len(cloud):
            if cloud[count] not in files:
                remove = await channel.fetch_message(cloudID[count])
                await remove.delete()

                gone = cloud.pop(count)
                goneID = cloudID.pop(count)

                file = open("cloud.txt", "w")
                for line in cloud:
                    if line != gone:
                        file.write(line)
                        file.write("\n")
                file.close()

                file = open("cloud id.txt", "w")
                for line in cloudID:
                    if line != goneID:
                        file.write(line)
                        file.write("\n")
                file.close()

        else:
            break


@client.event
async def on_member_join(member):

    sys_channel = member.guild.system_channel
    if sys_channel:
        try:
            await sys_channel.send(
                'Hey ' + member.mention + ' welcome to ' + member.guild.name +
                '! To see all my functions, type "bot functions"!')
        except Exception as error:
            print(error)


@client.event
async def on_message(message):

    TorF = open("torf.txt", "r")
    on = TorF.read()
    TorF.close()

    europe = ['EU', 'europe', 'Europe', 'eu']
    america = [
        'NA', 'na', 'america', 'America', 'north america', 'North america',
        'north America', 'North America'
    ]

    if message.author == client.user:
        return

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

    if message.content in europe:
        file = open("lastRegion.txt", "w")
        file.write("EU")
        file.close()

    elif message.content in america:
        file = open("lastRegion.txt", "w")
        file.write("NA")
        file.close()

    message.content = message.content.lower()

    guild = message.guild

    if "goodnight" in message.content:
        author = str(message.author)
        author = author.split("#")[0]
        await message.channel.send(
            f'Hey {author} dont forget to record your sleeping times!')

    if "bot functions" in message.content and on is True:
        response = (
            'i am capable of:\nbot functions by typing: "BOT functions"random number generator by typing: "BOT rng"\ngetting the time for people in other time zones by typing "BOT current times"\ncreating polls by typing "bot create poll"+a list of the options\nvoting in a poll by typing "bot poll vote"+the number of the option you want to choose\nclosing a poll by typing "bot close poll"\ngetting your average sleep schedule by typing "bot sleep"\nsay something mean by typing "bot offend"\nautomatically send suspected among us codes to codes chat\nrecords last suspected among us region\n\ndeveloper only features:\nturning me on and off'
        )
        await message.channel.send(response)

    elif "bot rng" in message.content and on is True:
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

    elif "bot current times" in message.content and on is True:
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
        if on is True:
            if message.author.id == 484893096761622554:
                TorF = open("torf.txt", "w+")
                TorF.write("False")
                TorF.close()

                await message.channel.send("goodbye!")
            else:
                await message.channel.send(
                    "you dont have permission to turn me off >:(")
        else:
            await message.channel.send("im already off")

    elif "bot turn on" in message.content:
        if on is False:
            if message.author.id == 484893096761622554:
                TorF = open("torf.txt", "w+")
                TorF.write("True")
                TorF.close()

                await message.channel.send("hello!")
            else:
                await message.channel.send(
                    "you dont have permission to turn me on >:(")
        else:
            await message.channel.send("im already on")

    elif "bot create poll" in message.content and on is True:
        currentPole = open("poll files/current_pole.txt", "r")
        torf = currentPole.read()
        currentPole.close()
        if torf is True:
            await message.channel.send("there is already an active poll!")
        elif torf is False:
            currentPole = open("poll files/current_pole.txt", "w+")
            currentPole.write("True")
            currentPole.close()
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
                    file = open("poll files/poll.txt", "a")
                    file.write(add2list)
                    file.write("\n")
                    file.close()

                    pollList[count] = pollList[count].replace(
                        ",", "type " + num + " for ")
                    await message.channel.send(pollList[count])
                    count = count + 1
                else:
                    break

    elif "bot poll vote" in message.content and on is True:
        currentPole = open("poll files/current_pole.txt", "r")
        torf = currentPole.read()
        currentPole.close()

        if torf is False:
            await message.channel.send("there is no poll currently open!")
        elif torf is True:

            alreadyVoted = open("poll files/already voted.txt")
            voter = alreadyVoted.read().splitlines()
            alreadyVoted.close()

            message.author = str(message.author)
            author = message.author.split("#")[0]
            if author in voter:
                await message.channel.send(f'{author} has already voted!')
            else:

                message.content = message.content.replace("bot poll vote ", "")
                message.content = int(message.content)

                options = open("poll files/poll.txt", "r")
                get = options.read().splitlines()
                options.close()

                if message.content > len(get) + 1:
                    await message.channel.send(
                        f'ERROR: not a valid vote. There isnt this many options!'
                    )
                elif message.content < 1:
                    await message.channel.send(
                        f'ERROR: not a valid vote. Please choose a number greater than 0!'
                    )
                else:
                    await message.channel.send(
                        f'{author} voted for {get[message.content-1]}!')
                    file = open("poll files/already voted.txt", "a")
                    file.write(author)
                    file.write("\n")
                    file.close()

                    file = open("poll files/votes.txt", "a")
                    file.write(str(message.content))
                    file.write("\n")
                    file.close()

    elif "bot close poll" in message.content:
        file = open("poll files/current_pole.txt", "r")
        openPole = file.read()
        file.close()

        if openPole == "False":
            await message.channel.send(
                "ERROR: there is no poll currently open!")
        else:

            collect = open("poll files/votes.txt")
            vote = collect.read().splitlines()
            collect.close()

            if len(vote) == 0:
                await message.channel.send("No votes yet, nothing has won")

            else:
                options = open("poll files/poll.txt", "r")
                choice = options.read().splitlines()
                length = len(choice)
                options.close()

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

            file = open("poll files/current_pole.txt", "w")
            file.write("False")
            file.close()

            file = open("poll files/poll.txt", "w")
            file.write("")
            file.close()

            file = open("poll files/already voted.txt", "w")
            file.write("")
            file.close()

            file = open("poll files/votes.txt", "w")
            file.write("")
            file.close()

    elif "bot offend" in message.content:
        file = open("offend.txt", "r")
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

        file = open("sleep list/" + author, "a+")
        file.write(hour + ":" + minute)
        file.write("\n")
        file.close()

        file = open("sleep list/" + author, "r")
        schedule = file.read().splitlines()
        file.close()
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
