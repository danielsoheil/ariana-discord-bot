from nextcord import Interaction
from nextcord.ext import commands
import nextcord
import calculator
import time


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(force_global=True)
    async def ariana(self, interaction: Interaction, message: str):
        try:
            vc: nextcord.VoiceClient = await interaction.user.voice.channel.connect()
        except nextcord.errors.ClientException:
            await interaction.response.send_message('bot is busy, try later')
            return
        except AttributeError:
            await interaction.response.send_message('you need to join a voice channel')
            return

        await interaction.response.send_message(message)
        url = calculator.sound_url_by_message(message)
        source = nextcord.FFmpegPCMAudio(url)
        vc.play(source)
        while vc.is_playing():
            time.sleep(1)
        await vc.disconnect()
