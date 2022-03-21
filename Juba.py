import time, discord, os, httpx
from colored import fg
from datetime import date
from discord.ext import commands
from JubaLib import Juba

d = date.today()
os.system('cls')
os.system('title ')

green = fg("#0abf1f")
white = fg("#ffffff")
red = fg("#ba1c11")

Juba = Juba("config.json")
Token = Juba.Parse("token")
ParsedColor = Juba.Parse("color")
Color = fg(str(ParsedColor))

user = commands.Bot(command_prefix=".")

@user.event
async def on_ready():
    Juba.OnConnect(color=Color)
    time.sleep(1)
    print(f"{green}{d}{white} | Connected to Discord!")
    print(f"{green}{d}{white} | Listening with {round(user.latency * 1000)}ms ")

@user.event
async def on_message(message):
    if "https://discord.gift" in message.content:
        try:
            code = message.content.split('https://discord.gift/')[1].split(' ')[0]
            result = httpx.post(
            'https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
            json={'channel_id': str(message.channel.id)},
            headers={'authorization': Token, 'user-agent': 'Mozilla/5.0'})
            
            if result.status_code == 200:
                print(f"{green}{d}{white} | Successfully redeemed code {white}| {green}{code} {white}| {green}{round(user.latency * 1000)}ms")
            else:
                print(f"{green}{d}{white} | {red}Unknown or invalid code. {white}| {red}{code} {white}| {red}{round(user.latency * 1000)}ms")
        except Exception:
            print(f"{green}{d}{white} | {red}Couldn't automatically claim code. {white}| {red}{code} {white}| {red}{round(user.latency * 1000)}ms")
    elif "discord.gift" in message.content:
        try:
            code = message.content.split('discord.gift/')[1].split(' ')[0]
            result = httpx.post(
            'https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
            json={'channel_id': str(message.channel.id)},
            headers={'authorization': Token, 'user-agent': 'Mozilla/5.0'})
            if result.status_code == 200:
                print(f"{green}{d}{white} | Successfully redeemed code {white}| {green}{code} {white}| {green}{round(user.latency * 1000)}ms")
            else:
                print(f"{green}{d}{white} | {red}Unknown or invalid code. {white}| {red}{code} {white}| {red}{round(user.latency * 1000)}ms")
        except Exception:
            print(f"{green}{d}{white} | {red}Couldn't automatically claim code. {white}| {red}{code} {white}| {red}{round(user.latency * 1000)}ms")
            pass
        
user.run(str(Token), bot=False)