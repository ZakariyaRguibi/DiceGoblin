from pypresence import Presence
import time
import random

client_id = "747156250612989963"  # please don't steal client id <3
RPC = Presence(client_id)  # Initialize the Presence class
RPC.connect()  # Start the handshake loop


def richPresence(args):
    # a default button that point to DiceGoblin offical server
    button = [
        {
            "label": "Customize rich presence here",
            "url": "https://discord.gg/mBHRa4xG",
        },
    ]
    if len(args) >= 3:
        print("test")
        print(args)
        if args[2] and args[3]:
            button = [
                {
                    "label": args[2],
                    "url": args[3],
                },
            ] + button
        print("test")

    RPC.update(
        details=args[0],
        state=args[1],
        large_image="tuning",
        large_text="iLarge_text",
        buttons=button,
    )
