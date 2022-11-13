import os


def env_or_input(env: str) -> str:
    if env not in os.environ:
        os.environ[env] = input(
            f'your environment variable "{env}" not found, '
            f'please set all environment variables and run again or inter your "{env}" here: '
        )

    return os.environ[env]


discord_token: str = env_or_input('DISCORD_TOKEN')
ariana_token: str = env_or_input('ARIANA_TOKEN')
