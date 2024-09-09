# gui-dev
import random
import sys


strings = [
    "ฅ^•ﻌ•^ฅ OwOverlay is starting up. Count how many times you can say UwU while you wait.",
    "ദ്ദി（• ˕ •マ.ᐟ This cat is giving you a thumbs up because you dropped a star on GitHub, right? right?",
    "/ᐠ > ˕ <マ ₊˚⊹♡ Enjoy some love from this cat while you wait for OwOverlay to start.",
    "/ᐠﹷ ‸ ﹷ ᐟ\ﾉ Your GitHub stars feed this cat."
]
if "UwU" in sys.argv:
    import time
    print("Super Cat Mode Enabled!")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    while True:
        cat_faces = [
            "UwU",
            "/ᐠ - ˕ -マ",
            "ฅ^•ﻌ•^ฅ",
            "/ᐠ > ˕ <マ",
            "/ᐠ˵- ᴗ -˵マ ᶻ 𝗓 𐰁",
            "=^◕⩊◕^="
        ]
        print(random.choice(cat_faces))