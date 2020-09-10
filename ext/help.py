import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Zenora Help Command", color=discord.Color.blue())
        embed.add_field(
            name="about", value="Introduces you to Zenora\n**Usage**\n`zen about`", inline=False)
        embed.add_field(
            name="docs", value="Shows you an entity from the Zenora documentation\n**Usage**\n`zen docs get_channel`", inline=False)
        embed.add_field(
            name="get-started", value="Shows you how to get started using Zenora\n**Usage**\n`zen get-started`", inline=False)
        embed.set_thumbnail(url="https://i.ibb.co/yVWTTJJ/logo.png")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
