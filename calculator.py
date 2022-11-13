import urllib
from config import ariana_token


def sound_url_by_message(message: str) -> str:
    url_without_queries = 'http://api.farsireader.com/ArianaCloudService/ReadTextGET?'
    queries = {
        'APIKey': 'G2F652LXUPDLSWY',
        'Text': message,
        'Speaker': 'Female1',
        'Format': 'mp3',
        'APIKey': ariana_token,
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
    return url
