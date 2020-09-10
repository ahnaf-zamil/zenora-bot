import discord
from discord.ext import commands
from datetime import datetime


class Zen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['get-started'])
    async def get_started(self, ctx):
        msg = """

Zenora can be installed be Python's package manager, pip:

``$ pip install zenora``

__**Note:**__
This library is dependent on Requests and so naturally will only be available for Python versions that Requests also supports.

**Accessing the API**
--------------------

Your first API usage can be written in just a few lines of code:
```py
# Import the library
import zenora

# Instantiate a REST API instance
api = zenora.RESTAPI(token="your_token_here", token_type="your_token_type_here")

# Query API for getting channel
# Zenora parses API response into Python objects for accessing data
channel = api.get_channel(732595879747256371)

# Use the data
print(channel.name)
```

__**Note:**__
There are two types of tokens, ``Bot`` & ``Bearer``. Bot tokens are used for accessing the API in bot applications
Bearer tokens are used for accessing the API data on behalf of a user account for purposes such as Oauth2.

        """
        embed = discord.Embed(title="Getting Started with Zenora",
                              description=msg, color=discord.Color.blue())
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def about(self, ctx):
        msg = """
========
Zenora is a modern Python API wrapper for the Discord REST API.

It aims to provide an easy to use interface for accessing the API without the need of running a bot.

This library is currently unfinished but you can help speed up the development by contributing and submitting pull requests to the repository.
It is working in its current state but I'd love to see more functionality added further down the line!

Repository: [View on GitHub](https://github.com/ahnaf-zamil/zenora)

PyPi: [View on PyPi](https://pypi.org/project/zenora/)

Documentation: [View here](https://zenora-py.github.io/)

If you need any help with this library at any point feel free to DM me on Discord (Ahnaf#4346).

If you think you have found a bug or other problem with the library, or you would like to suggest a feature,
you should submit an issue on the GitHub repository [here](https://github.com/ahnaf-zamil/zenora/issues).
Before doing so you should make sure you are on the latest version of the library and check to see if an issue
already exists for your bug or feature.
"""
        embed = discord.Embed(title="Zenora",
                              description=msg, color=discord.Color.blue())
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Zen(bot))
