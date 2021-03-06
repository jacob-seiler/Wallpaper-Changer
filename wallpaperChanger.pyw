from datetime import datetime
import ctypes
import winreg
import os.path
import platform

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return platform.architecture()[0] == '64bit'

def changeBG(path, fit):
    """Change background depending on bit size"""

    if not os.path.isfile(path):
        print("Error setting wallpaper. Could not find file '" + path + "'")
        return

    REG_PATH = "Control Panel\\\\Desktop"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)

    winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, str(fit))
    winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
    winreg.CloseKey(key)

    SPI_SETDESKWALLPAPER = 20

    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)

def main():
    time = datetime.now().hour
    path = "C:\\Users\\Jacob\\Pictures\\Wallpapers\\" + str(time) + "00.jpg"
    changeBG(path, 2)

if __name__ == "__main__":
    main()