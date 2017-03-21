import discord
from discord.ext import commands
from __main__ import send_cmd_help

try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import aiohttp

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="sdtd", pass_context=True)
    async def sdtd(self, ctx):
        """sdtd group"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @sdtd.command(pass_context=True, no_pm=True)
    async def online(self, ctx):
        """This shows players online"""

        #Online player
        url = "https://7daystodie-servers.com/server/50729/" #Change this into your own address
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(class_='table table-bordered').findAll("tr")[3].findAll("td")[1].text
            await self.bot.say(online + ' players are playing this game at the moment')
        except:
            await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")

    @sdtd.command(pass_context=True, no_pm=True)
    async def address(self, ctx):
        """This shows server address"""

        #Adress of the server
        url = "https://7daystodie-servers.com/server/50729/" #Change this into your own address
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            address = soupObject.find(class_='table table-bordered').findAll("tr")[0].findAll("td")[1].text
            await self.bot.say(address + ' is de address for the server')
        except:
            await self.bot.say("Couldn't load address. Contact admin")

    @sdtd.command(pass_context=True, no_pm=True)
    async def status(self, ctx):
        """This shows the server status"""

        #Server status
        url = "https://7daystodie-servers.com/server/50729/" #Change this into your own address
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            status = soupObject.find(class_='table table-bordered').findAll("tr")[2].findAll("td")[1].text
            await self.bot.say(status)
        except:
            await self.bot.say("Couldn't load status. This is bad.")

def setup(bot):
    if soupAvailable:
        bot.add_cog(Mycog(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
