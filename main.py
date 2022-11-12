import time
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import urllib

client = commands.Bot()


@client.event
async def on_ready():
    print('im online')


@client.slash_command(force_global=True)
async def say(interaction: Interaction, message: str):
    try:
        vc: nextcord.VoiceClient = await interaction.user.voice.channel.connect()
    except nextcord.errors.ClientException:
        await interaction.response.send_message('bot is busy, try later')
        return
    except AttributeError:
        await interaction.response.send_message('you need to join a voice channel')
        return

    await interaction.response.send_message(message)
    url_without_queries = 'http://api.farsireader.com/ArianaCloudService/ReadTextGET?'
    queries = {
        'APIKey': 'G2F652LXUPDLSWY',
        'Text': message,
        'Speaker': 'Female1',
        'Format': 'mp3',
        'APIKey': 'G2F652LXUPDLSWY',
        'GainLevel': '0',
        'PitchLevel': '0',
        'PunctuationLevel': '0',
        'SpeechSpeedLevel': '0',
        'ToneLevel': '0',
        'Quality': 'normal',
        'BeginningSilence': '0',
        'EndingSilence': '0',
        'Base64Encode': '0',
    }
    queries_encoded = urllib.parse.urlencode(queries)
    url = url_without_queries + queries_encoded
    # url = 'https://dl4.fara-download.ir/audio/sound_effect/alarms/ding/ding%20sound%20effect.mp3' # for test
    source = nextcord.FFmpegPCMAudio(url)
    vc.play(source)
    while vc.is_playing():
        time.sleep(1)

    await vc.disconnect()


client.run('MTA0MDc2OTMzNDM0NTIxMjAzNQ.GBtJfX.m6-sF3vA1_idr49-66fDmYwCPn2KC7oRhi8aTo')
