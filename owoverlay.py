import wx
import sys
import pathlib
import json
import random
import activewindow as aw
import zipfile


class Overlay(wx.Frame):
    def __init__(self, png, overlay_height, y_overlap):
        style = (wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR |
                 wx.NO_BORDER | wx.FRAME_SHAPED)
        wx.Frame.__init__(self, None, title='overlay', style=style)
        self.SetBackgroundColour(wx.TransparentColour)
        self.Size = wx.DisplaySize()
        self.PNGFile = png
        self.OverlayHeight = overlay_height
        self.YOverlap = y_overlap
        self.Position = (0, 0)
        self.Show(True)
        png = wx.Image(self.PNGFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        while True:
            awin = aw.get_active_window()
            if awin:
                break
        self.bmp = wx.StaticBitmap(self, -1, png,
                                   (awin.position[0], (awin.position[1] - self.OverlayHeight) + self.YOverlap),
                                   (awin.size[0], self.OverlayHeight))
        self.Show(True)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(1)

    def update(self, _):
        awin = aw.get_active_window()
        if awin:
            self.bmp.SetPosition((awin.position[0], (awin.position[1] - self.OverlayHeight) + self.YOverlap))
            self.bmp.SetSize(wx.Size(awin.size[0], self.OverlayHeight))


class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="OwOverlay Settings", pos=wx.DefaultPosition,
                          size=wx.Size(400, 150), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.Size(400, 150), wx.Size(400, 150))
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.fp_label = wx.StaticText(self, wx.ID_ANY, "Decoration Pack:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.fp_label.Wrap(-1)
        main_sizer.Add(self.fp_label, 0, wx.ALL, 5)
        self.file_picker = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, "Select a file",
                                             "ZIP and OWO files (*.zip;*.owo)|*.zip;*.owo|All Files (*.*)|*.*",
                                             wx.DefaultPosition, wx.Size(400, -1), wx.FLP_DEFAULT_STYLE)
        main_sizer.Add(self.file_picker, 0, wx.ALL, 5)
        self.start_button = wx.Button(self, wx.ID_ANY, "Start Overlay", wx.Point(100, -1), wx.DefaultSize, 0)
        main_sizer.Add(self.start_button, 1, wx.ALIGN_RIGHT | wx.TOP | wx.RIGHT | wx.LEFT, 5)
        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        # All non wxFB code below:
        self.overlay_running = False
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start_click)
        self.overlay = None

    def on_start_click(self, _):
        path = self.file_picker.GetPath()
        print(path)
        if self.overlay_running:
            self.overlay_running = False
            self.overlay.Hide()
            self.start_button.SetLabel("Start Overlay")
        elif pathlib.Path(path).exists() and zipfile.is_zipfile(path):
            try:
                self.overlay = get_overlay(path)
            except Exception as e:
                wx.MessageBox(f"Error loading decoration pack from path {path}: {repr(e)}",
                              caption="Error Loading File", style=wx.OK)
                print(e)
                return

            self.overlay.Show()
            self.overlay_running = True
            self.start_button.SetLabel("Stop Overlay")
        else:
            wx.MessageBox(f"Error loading decoration pack from path {path}: file does not exist or is not a zip archive",
                          caption="Error Loading File", style=wx.OK)


def get_overlay(path):
    with zipfile.ZipFile(path) as zipf:
        print(zipf.namelist())
        root = zipf.namelist()[0]
        cfg = json.loads(zipf.open(root + "config.json", "r").read())
        return Overlay(zipf.open(root + cfg.get("overlay_png")), cfg.get("height"),
                               cfg.get("y_overlap"))


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
print(random.choice(strings))

app = wx.App()
if 2 == len(sys.argv):
    try:
        path = sys.argv[1]
        overlay = get_overlay(path)
        overlay.Show()
        app.MainLoop()
        sys.exit(0)
    except Exception as e:
        print(f"Error loading decoration pack from path {path}: {e}, continuing to GUI.")
mainwin = MainWindow()
mainwin.Show()
app.SetExitOnFrameDelete(True)
app.MainLoop()
