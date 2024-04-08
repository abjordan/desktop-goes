import ctypes
import requests
import time

WALLPAPER_FILE = "C:\\tools\\wallpaper.jpg"

while True:
    print("Requesting newest GOES EAST Full Disk image")
    # Request the latest wallpaper
    r = requests.get("https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/1808x1808.jpg", allow_redirects=True)
    with open(WALLPAPER_FILE, "wb") as outfile:
        outfile.write(r.content)

    # Set the style of the wallpaper
    # 0: Center, 1: Stretch, 2: Tile, 6: Fit, 10: resize and fit
    wallpaper_style = 10

    # Load the image
    SPI_SETDESKWALLPAPER = 20
    image = ctypes.c_wchar_p(WALLPAPER_FILE)

    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)

    # Sleep for 10 minutes, since the image only updates every 10m 
    print("Sleeping for 10 minutes")
    time.sleep(10 * 60)
