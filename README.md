![image](ears1.png)
# OwOverlay
Give all your windows a fursona, because why not?
# Usage:
- **Binary (recommended):** `./owoverlay <path to decoration pack>`
- **Python script:** `python3 overlay.py <path to decoration pack>`

`<path to decoration pack>` is an optional argument that will immediately launch
OwOverlay with the specified decoration pack, disabling the GUI. If a problem
is encountered loading the specified decoration pack, however, it will proceed to launch the GUI.
# Decoration Packs:
**Format:** decoration packs are a zipped directory containing a `config.json` and overlay pngs.
> **OwOverlay includes a few built-in decoration packs in the `decorations` directory:**
> - `ears1.zip`: simple brown cat ears
> - `ears2.zip`: simple pink cat ears
> - `mikeears.zip`: simple cat ears based on Mike Goutokuji from Touhou project.
> - `huhat.zip`: hat of Hu Tao from Genshin Impact, based on original art by @TheTridentGuy
# Dependencies:
> Note that all non-pre-release binaries should be packaged with all dependencies
- **wxPython:** `pip3 install wxPython`
- **pyobjc:** `pip3 install pyobjc`