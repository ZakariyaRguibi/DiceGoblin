from pypresence import Presence
import time
import random

client_id = "747156250612989963"  # please don't steal client id <3
RPC = Presence(client_id)  # Initialize the Presence class
RPC.connect()  # Start the handshake loop

myDetails = [
    [
        "Worshipping Annaha",
        "worshiping",
        [
            "Praying",
            "Striking evil",
            "Killing infidels",
            "Writing prayers",
            "Making the godess bleed",
            "Being a fanatic",
            "Eating souls",
            "Winking at the status",
        ],
        "Yu Mo Gui Gwai Fai Di Zao",
    ],
    [
        "Running from succubi",
        "running",
        [
            "Dashing away from brothel",
            "Rejecting advances",
            "Not playing chess",
            "Staying away from siblings",
            "Not thinking about cousins ",
            "Looking back",
            "No tail play",
            "Staying away from hell",
        ],
        "Beep, Beep....",
    ],
    [
        "Smiting drows",
        "smite",
        [
            "Sharpening tree logs",
            "Not shitting storms",
            "Thinking of hurtfull names",
            "Staying away from siblings",
            "Rolling D100",
            "Making pact with the devil",
            "Praying not to die",
            "Rolling HT to stay alive",
        ],
        "Bonk",
    ],
    [
        "Being an annoying bard",
        "tuning",
        [
            "Singing",
        ],
        "Toss a coin to your witcher...",
    ],
    [
        "Fudging dice",
        "dice",
        [
            "A (6,6,6) for you",
            "A (100) for you",
            "Thinking of hurtfull names",
            "Pushing dice a little bit",
            "Glaring real hard",
            "a (1,1,1) for the succi",
            "a (1,2,1) for hitting the bucket",
            "Ye DEAD",
        ],
        "Lemme roll that in secret",
    ],
]  # The quotes to choose from


def richPresence():
    while True:  # The presence will stay on as long as the program is running
        myDetail = random.choice(myDetails)
        for i in range(0, 5):
            mystate = random.choice(myDetail[2])
            RPC.update(
                details=myDetail[0],
                state=mystate,
                large_image=myDetail[1],
                large_text=myDetail[3],
                buttons=[
                    {
                        "label": "Customize rich presence here",
                        "url": "https://discord.gg/mBHRa4xG",
                    },
                ],
            )  # Set the presence, picking a random quote
            time.sleep(5)  # Wait a wee bit


richPresence()
