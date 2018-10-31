import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time
import random
import youtube_dl
if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

Client = discord.Client()
client = commands.Bot(command_prefix = "$")
bot = commands.Bot("$")
startup_extensions = ("Music")

chat_filter = ["cancer", "stfu", "faggot", "hoe", "kanker", "teef", "hoer", "arse", "bastard", "bellend", "berk", "CUNT", "cock-up", "Dickhead", "git", "Knob", "Pish"]
bypass_filter = []

@client.event
async def on_ready():
    print(client.user.name)
    print("Bot is online and connected to Discord")


#Commands

@client.event
async def on_message(message):
    if message.content.upper().startswith('$PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('$NSFW'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> away you naughty boi!!" % (userID))
    if message.content.upper().startswith('$SAY'): 
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

#roles
    if message.content.upper().startswith('$AMILOLIGE'):
        if "457546929719738379" in [role.id for role in message.author.roles]: 
            await client.send_message(message.channel, "You are the LOLIGE")
        else:
            await client.send_message(message.channel, "You are not the LOLIGE")
    if message.content.upper().startswith('$AMICHADMIN'):
        if "457547175962869761" in [role.id for role in message.author.roles]: 
            await client.send_message(message.channel, "You are a ChAdmin")
        else:
            await client.send_message(message.channel, "You are not a ChAdmin")
    if message.content.upper().startswith('$AMIASTAFF'):
        if "457547965205053443" in [role.id for role in message.author.roles]: 
            await client.send_message(message.channel, "You are a staff memeber")
        else:
            await client.send_message(message.channel, "You are not a staff member")
    if message.content.upper().startswith('$AMIMOD'):
        if "457547596286787622" in [role.id for role in message.author.roles]: 
            await client.send_message(message.channel, "You are a moderator")
        else:
            await client.send_message(message.channel, "You are not A moderator")
#memes
    if message.content.upper().startswith('$NICEMEME'):
        await client.send_message(message.channel, "http://niceme.me")
#country
    if message.content.upper().startswith('$IAMBRITISH'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='British')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role British")
    if message.content.upper().startswith('$IAMSWEDISH'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='Swedish')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role Swedish")
    if message.content.upper().startswith('$IAMDUTCH'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='Dutch')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role Dutch")
    if message.content.upper().startswith('$IAMPOLISH'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='Polish')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role Polish")
    if message.content.upper().startswith('$IAMFRENCH'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='French')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role French")
    if message.content.upper().startswith('$IAMNORWEGIAN'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='Norwegian')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role Norwegian")
    if message.content.upper().startswith('$IAMGERMAN'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='German')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role German")
    if message.content.upper().startswith('$IAMRUSSIAN'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='Russian')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role Russian")
    if message.content.upper().startswith('$IAMTURKISH'):
        member = message.author
        userID = message.author.id
        role = discord.utils.get(member.server.roles, name='Turkish')
        await client.add_roles(member, role)
        await client.send_message(message.channel, "Assigned role Turkish")
#Trippie
    if message.content.upper().startswith('$PLAYTRIPPIE'):
        author = message.author
        channel = author.voice_channel
        voice = await client.join_voice_channel(channel)
        player = voice.create_ffmpeg_player('trippie.mp3')
        await client.send_message(message.channel, "Playing, Trippie Redd Taking A Walk (Prod. by Scott Storch) (WSHH Exclusive - Official Audio)")
        player.start()
    if message.content.upper().startswith('$STOPPIE'):
        server = message.server
        voice_client = client.voice_client_in(server)
        leave = await voice_client.disconnect()
        await client.send_message(message.channel, "Stopped the music!")
#cyka
    if message.content.upper().startswith('$CYKA'):
        author = message.author
        channel = author.voice_channel
        voice = await client.join_voice_channel(channel)
        player = voice.create_ffmpeg_player('cyka.mp3')
        await client.send_message(message.channel, "Cyka blyat")
        player.start()
#flipacoin
    if message.content.upper().startswith('$FLIPACOIN'):
        coins = ['heads', 'tails','heads', 'tails','heads', 'tails','heads', 'tails','heads', 'tails','heads', 'tails',]
        await client.send_message(message.channel, random.choice(coins))
#help
    if message.content.upper().startswith('$HELP'):       
        await client.send_message(message.channel, " $ping makes me say !pong \n $nsfw shows something thats not ment for work \n $say makes me say whatever you want \n \n $amilolige Makes me tell you if you are the lolige \n $amichadmin makes me tell you if you are the chadmin \n $amistaff makes me tell you if you are a staff member \n $amimod makes me show you if you are a mod \n \n $play url makes me play a song from youtube pls fill in a url \n $stop makes me stop playing the song \n $cyka makes me play a good file \n $meme makes me show you a meme \n$flipacoin makes me flip a coin \n $help makes me show this \n \n $iamdutch makes me assign the role Dutch \n $iamswedish makes me assign the role swedish \n $iambritish makes me assign the role british \n $iamgerman makes me assign the role german \n $iamrussian makes me assign the role russian \n $iampolish makes me assign the role Polish \n $iamnorwegian makes me assign the role Norwegian \n $iamfrench makes me assign the role french \n $iamturkish makes me assign the role turkish")

#IF statement
        
    if message.content.upper().startswith('CANCER'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('KANKER'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('STFU'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('HOER'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('TEEF'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('FAGGOT'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('NAZI'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('WOOSH'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('CUNT'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('PRAT'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('TWAT'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('PLONKER'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('GIT'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('FECK'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)
    if message.content.upper().startswith('DICKHEAD'):
        userID = message.author.id
        await client.send_message(message.channel, "Watch your tongue <@%s>!" % (userID))
        await client.delete_message(message)



#new music bot


    
        


client.run("NTA2MjA0MTczOTUyNjE0NDAw.DrevMQ.tmYeTCzVUYmiWeDjIKWhCuy4Dwc")
