![image](ears1.png)
# OwOverlay
Give all your windows a fursona, because why not?
# Usage:
- **Binary (recommended):** `./owoverlay <path to decoration pack>`
- **Python script:** `python3 overlay.py <path to decoration pack>`

`<path to decoration pack>` is an optional argument that will immediately launch
OwOverlay with the specified decoration pack, disabling the GUI. If a problem
is encountered loading the specified decoration pack, however, it will proceed to launch the GUI.

# Dependencies:
> Note that all non-pre-release binaries should be packaged with all dependencies
- **wxPython:** `pip3 install wxPython`
- **pyobjc:** `pip3 install pyobjc`