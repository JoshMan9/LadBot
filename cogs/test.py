import discord
from discord.ext import commands
from .utils.chat_formatting import *
from random import randint
from random import choice as randchoice

class Jerm:
    def __init__(self, bot):
        self.bot = bot
        self.triggeredLinks = ["http://i.imgur.com/wnIaRyJ.gif",
                          "http://i.imgur.com/3X0KnbH.gif",
                          "https://media.giphy.com/media/2kVi3pspuXXYA/giphy.gif",
                          "https://media.giphy.com/media/ZEVc9uplCUJFu/giphy.gif",
                          "http://i.imgur.com/avHnbUZ.gif"]
        self.adoptedLines = ["╭━━━━━━━╮ ", " ┃　　● ══　 █ ┃ ", "┃██████████┃ ",
                             "┃██████████┃ ", "┃██████████┃", "┃█ ur adopted. █┃ ",
                             "┃█ -Mom&Dad █┃ ", "┃██████████┃ ", "┃██████████┃ ",
                             "┃██████████┃ ", "┃　　　○　　　 ┃ ", "╰━━━━━━━╯"]
        self.lookSonLines = ["─────────────────────────▄▀▄",
                             "─────────────────────────█─█",
                             "─────────────────────────█─█",
                             "─────────────────────────█─█",
                             "─────────────────────────█─█",
                             "─────────────────────────█─█",
                             "─────────────────────────█─▀█▀█▄",
                             "─────────────────────────█──█──█",
                             "─────────────────────────█▄▄█──▀█",
                             "────────────────────────▄█──▄█▄─▀█",
                             "────────────────────────█─▄█─█─█─█",
                             "────────────────────────█──█─█─█─█",
                             "────────────────────────█──█─█─█─█",
                             "────▄█▄──▄█▄────────────█──▀▀█─█─█",
                             "──▄█████████────────────▀█───█─█▄▀",
                            "─▄███████████────────────██──▀▀─█",
                            "▄█████████████────────────█─────█",
                            "██████████───▀▀█▄─────────▀█────█",
                            "████████───▀▀▀──█──────────█────█",
                            "██████───────██─▀█─────────█────█",
                            "████──▄──────────▀█────────█────█ Look son!",
                            "███──█──────▀▀█───▀█───────█────█ A Retard!",
                            "███─▀─██──────█────▀█──────█────█",
                            "███─────────────────▀█─────█────█",
                            "███──────────────────█─────█────█",
                            "███─────────────▄▀───█─────█────█",
                            "████─────────▄▄██────█▄────█────█",
                            "████────────██████────█────█────█",
                            "█████────█──███████▀──█───▄█▄▄▄▄█",
                            "██▀▀██────▀─██▄──▄█───█───█─────█",
                            "██▄──────────██████───█───█─────█",
                            "─██▄────────────▄▄────█───█─────█",
                            "─███████─────────────▄█───█─────█",
                            "──██████─────────────█───█▀─────█",
                            "──▄███████▄─────────▄█──█▀──────█",
                            "─▄█─────▄▀▀▀█───────█───█───────█",
                            "▄█────────█──█────▄███▀▀▀▀──────█",
                            "█──▄▀▀────────█──▄▀──█──────────█",
                            "█────█─────────█─────█──────────█",
                            "█────────▀█────█─────█─────────██",
                            "█───────────────█──▄█▀─────────█",
                            "█──────────██───█▀▀▀───────────█",
                            "█───────────────█──────────────█",
                            "█▄─────────────██──────────────█",
                            "─█▄────────────█───────────────█",
                            "──██▄────────▄███▀▀▀▀▀▄────────█",
                            "─█▀─▀█▄────────▀█──────▀▄──────█",
                            "─█────▀▀▀▀▄─────█────────▀─────█",
                            "─█─────────▀▄──▀───────────────█"]


    @commands.command(hidden=True)
    async def triggered(self):
        await self.bot.say(randchoice(self.triggeredLinks))

    @commands.command(hidden=True)
    async def superTriggered(self):
        for x in range(0, 10):
            await self.bot.say(randchoice(self.triggeredLinks))

    @commands.command(hidden=True)
    async def fuckYeah(self):
        for x in range(0, 10):
            await self.bot.say("Fuck Yeah!")

    @commands.command(hidden=True)
    async def adopted(self):
        for x in range(0, 12):
            await self.bot.say(self.adoptedLines[x])

    @commands.command(hidden=True)
    async def lookSon(self):
        for x in range(0, 48):
            await self.bot.say(self.lookSonLines[x])
            
    @commands.command(hidden=True)
    async def noticeMe(self, *, user : discord.Member):
        name = " *" + user.name + "*"
        for x in range(0, 10):
            await self.bot.say("Notice me " + name + " !")
    

def setup(bot):
    bot.add_cog(Jerm(bot))
