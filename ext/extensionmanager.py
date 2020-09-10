import discord
from discord.ext import commands


class ExtensionManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def loadext(self, ctx, *, extension):
        """
        Loads the specified error if possible
        Otherwise returns the error
        """
        try:
            self.bot.load_extension(extension)
            await ctx.send("Extension Loaded Successfully")
        except Exception as e:
            await ctx.send(f"{extension} Failed To Load.")
            await ctx.send(e)

    @commands.command()
    @commands.is_owner()
    async def unloadext(self, ctx, *, extension):
        """
        Unloads the specified extension if possible
        Otherwise returns the error
        """
        try:
            self.bot.unload_extension(extension)
            await ctx.send("Extension Unloaded Successfully")
        except Exception as e:
            await ctx.send(f"{extension} Could Not Be Unloaded.")
            await ctx.send(e)

    @commands.command()
    @commands.is_owner()
    async def reloadext(self, ctx, *, extension):
        """
        Reloads the specified extension if possible
        Otherwise returns the error
        """
        try:
            self.bot.reload_extension(extension)
            await ctx.send("Extension Reloaded Successfully")
        except Exception as e:
            await ctx.send(f"{extension} Could Not Be Reloaded.")
            await ctx.send(e)

    @commands.command()
    @commands.is_owner()
    async def listext(self, ctx):
        """Lists all the currently loaded extensions"""
        extensions = ", ".join(self.bot.extensions)
        await ctx.send("Currently Loaded Extensions:")
        await ctx.send(f"```{extensions}```")


def setup(bot):
    bot.add_cog(ExtensionManager(bot))
