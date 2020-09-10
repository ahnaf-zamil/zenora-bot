import discord
from discord.ext import commands
import time
from datetime import datetime

start_time = datetime.utcnow()


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"github.com/ahnaf-zamil/zenora"
        ))
        print("Ready")

    @commands.command()
    async def ping(self, ctx):
        # Time the time required to send a message first.
        # This is the time taken for the message to be sent, awaited, and then
        # for discord to send an ACK TCP header back to you to say it has been
        # received; this is dependant on your bot's load (the event loop latency)
        # and generally how shit your computer is, as well as how badly discord
        # is behaving.
        start = time.monotonic()
        msg = await ctx.send("Pinging...")
        millis = (time.monotonic() - start) * 1000

        # Since sharded bots will have more than one latency, this will average them if needed.
        heartbeat = ctx.bot.latency * 1000

        await msg.edit(
            content=f"Gateway: {int(heartbeat):,.2f}ms\nRESTful API: {int(millis):,.2f}ms."
        )

    @commands.command()
    async def info(self, ctx):
        now = datetime.utcnow()  # Timestamp of when uptime function is run
        delta = now - start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days:
            time_format = (
                "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
            )
        else:
            time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
        uptime_stamp = time_format.format(
            d=days, h=hours, m=minutes, s=seconds)
        users = []
        for i in self.bot.users:
            if not i.bot:
                users.append(i)
        if not hasattr(self.bot, "appinfo"):
            self.bot.appinfo = await self.bot.application_info()
        embed = discord.Embed(
            title="Zenora Bot's Info",
            description=f"The Official Discord Bot of the Python module, **Zenora**.\nBot prefix is: 'zen '\n",
            color=discord.Color.blue(),
            rich=True,
        )
        from platform import python_version

        t = f"""py
Python Version: {python_version()}
Discord.py Version: {discord.__version__}
        """
        users = []
        for i in self.bot.users:
            if not i.bot:
                users.append(i)
        embed.set_footer(text=f"Requested by: {ctx.message.author}")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Name:", value=f"Exo", inline=False)
        embed.add_field(
            name="Developed by:",
            value=f":point_right: {self.bot.appinfo.owner} :point_left:",
        )
        embed.add_field(name="Programmed in:", value=f" Discord.py")
        embed.add_field(name="Version info",
                        value=f"\n```{t}```", inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
