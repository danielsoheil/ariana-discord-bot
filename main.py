from nextcord.ext import commands
from config import discord_token
import cogs

client = commands.Bot()


@client.event
async def on_ready():
    print('successfully connected to discord')

client.add_cog(cogs.SlashCommands(client))

if __name__ == "__main__":
    client.run(discord_token)
