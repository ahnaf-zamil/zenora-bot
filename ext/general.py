import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"github.com/ahnaf-zamil/zenora"
        ))
        print("Ready")


def setup(bot):
    bot.add_cog(General(bot))
