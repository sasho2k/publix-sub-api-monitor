from datetime import datetime
import discord
from client_system.client import MyClient
from internals.internal import get_settings


def run():
    client = MyClient()
    print("\nStarting Process...\n")
    token, bot_prefix = get_settings()
    client.bot_prefix = bot_prefix

    try:
        print("CLIENT: Starting run process.\n")
        client.run(token)
    except discord.errors.HTTPException:
        print("FATAL: Invalid token.\n")
        exit(0)
    except discord.errors.LoginFailure:
        print("FATAL: Invalid token.\n")
        exit(0)
