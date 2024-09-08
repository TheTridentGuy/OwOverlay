import wx
import sys
from tkinter import filedialog, simpledialog
import pathlib
import json
import random
import activewindow as aw


config_path = "config.json"


class Overlay(wx.Frame):
    def __init__(self):
        print(random.choice(strings))
        style = (wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR |
                  wx.NO_BORDER | wx.FRAME_SHAPED)
        wx.Frame.__init__(self, None, title='overlay', style=style)
        self.SetBackgroundColour(wx.TransparentColour)
        self.Size = wx.DisplaySize()
        if 4 == len(sys.argv):
            self.PNGFile = sys.argv[1]
            self.OverlayHeight = int(sys.argv[2])
            self.YOverlap = int(sys.argv[3])
        elif pathlib.Path(config_path).exists():
            cfg = json.load(open(config_path, "r"))
            self.PNGFile = cfg.get("file")
            self.OverlayHeight = cfg.get("height")
            self.YOverlap = cfg.get("y_overlap")
        else:
            self.PNGFile = filedialog.askopenfilename(title="Select Overlay PNG")
            self.OverlayHeight = simpledialog.askinteger("Set Overlay Height", "Set the overlay height in pixels:")
            self.YOverlap = simpledialog.askinteger("Set Overlay Y-Offset", "Set how far below the top of the window should the overlay go:")
        print(self.PNGFile, self.OverlayHeight, self.YOverlap)
        self.Position = (0, 0)
        self.Show(True)
        png = wx.Image(self.PNGFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        while True:
            awin = aw.get_active_window()
            if awin:
                break
        self.bmp = wx.StaticBitmap(self, -1, png, (awin.position[0], (awin.position[1]-self.OverlayHeight)+self.YOverlap), (awin.size[0], self.OverlayHeight))
        self.Show(True)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(100)

    def update(self, _):
        awin = aw.get_active_window()
        if awin:
            self.bmp.SetPosition((awin.position[0],  (awin.position[1]-self.OverlayHeight)+self.YOverlap))
            self.bmp.SetSize(wx.Size(awin.size[0], self.OverlayHeight))


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


app = wx.App()
f = Overlay()
app.MainLoop()
