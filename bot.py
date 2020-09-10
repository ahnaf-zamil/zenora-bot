from discord.ext import commands
import time
import logging


logging.basicConfig(level=logging.INFO)
# Sets up parser and reads the file containing the bot token

# List of all extensions to be loaded
extensions = ["ext.extensionmanager", "ext.api",
              "ext.help", "ext.general", "ext.zencommands"]

# Link to root of the documentation page
DOCUMENTATION_LINK = "https://zenora-py.github.io"

# Declares the bot prefix and token, taking values from files
prefix = "zen "
with open("token.txt") as fp:
    token = fp.read().strip()

# Main function creates bot, loads extensions and runs the bot


def run_bot():
    bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
    bot.remove_command("help")
    bot.docs_link = DOCUMENTATION_LINK
    if len(extensions) != 0:
        for ext in extensions:
            bot.load_extension(ext)
            print(f"Loaded ext {ext}")
    bot.load_extension("libneko.extras.superuser")
    bot.run(token)


# Keeps the bot alive
while True:
    run_bot()
    time.sleep(5)
