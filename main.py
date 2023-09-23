import discord
from discord.ext import commands 
from discord import Intents , client
import loady
import distancefinder
import findloc
import re
import waythrough

def app_run(token):
    intents = Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!',intents=intents)
    data:dict = loady.load1("data/intents.json")
    coordinate_pattern = r'(-?\d+\.\d+),\s*(-?\d+\.\d+)'

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now running")

    
    @bot.command()
    async def findPolice(ctx,lat,long):
        lat = float(lat)
        long = float(long)
        result = distancefinder.nearbystation(lat,long)
        latitude = result[2]
        longitude = result[3]
        name = result[1]
        image = findloc.findy(latitude,longitude,name,lat,long)


        with open("images/output.png","rb") as im1:
            file1 = discord.File(im1 ,"output.png" )
        
        channel_id = 1153583047380303912
        channel = bot.get_channel(channel_id)

        await channel.send(result)
        await channel.send(file=file1)
    
    @bot.command()
    async def wayfinder(ctx,lat,lon):
        lat1 = float(lat)
        lon1 = float(lon)
        result = distancefinder.nearbystation(lat1,lon1)
        lat2 = result[2]
        lon2 = result[3]
        image1 = waythrough.wayy(lat1,lon1,lat2,lon2)

        with open("images/outputd.png","rb") as im2:
            file1 = discord.File(im2,"waytogo.png")
        
        channel_id = 1154632947375276083 
        channel = bot.get_channel(channel_id)

        
        await channel.send(result[0])
        await channel.send(file=file1)

    

    @bot.event
    async def on_message(message):
        if bot.user == message.author:
            return
        
        
        channel_id = 1147062396926562336
        channel = bot.get_channel(channel_id)
        
        match = re.search(coordinate_pattern , message.content)
        if match:
            latitude = float(match.group(1))
            longitude = float(match.group(2))
            await channel.send(latitude,longitude)
        
        print(f"({bot.user} {message.author}):{message.content}")
        
        await bot.process_commands(message)

    bot.run(token)

if __name__ == "__main__":
    token = "your-token"
    app_run(token)
