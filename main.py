import sys
import pygame
import asyncio
from grid_display import draw_buttons_grid
from buttons import buttonsDict, mType
from api_requests import triggerLED, triggerVideo
from launchpad import lightLeds

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("ERROR: loading launchpad.py failed")

def main():

    # Init launchpad
    lp = launchpad.LaunchpadMk2()
    if not lp.Open(0, "mk2"):
        sys.exit("Launchpad Mk2 not found!")
    lp.ButtonFlush()

    # Draw grid
    draw_buttons_grid(buttonsDict)

    running = True

    try:
        while running:
            # Check for quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Light Launchpad LEDs
            lightLeds(lp)

            # track wled brightness
            wled_brightness = 255

            # Get Launchpad button state
            butts = lp.ButtonStateXY()

            # Check for button press and act accordingly
            if butts != []:
                if butts[1] in buttonsDict and butts[0] in buttonsDict[butts[1]]:
                    if butts[2] > 0 or ("double" in buttonsDict[butts[1]][butts[0]] and buttonsDict[butts[1]][butts[0]]["double"]):
                        # LED
                        if buttonsDict[butts[1]][butts[0]]["type"] == mType.LED:
                            asyncio.run(triggerLED(buttonsDict[butts[1]][butts[0]]["message"]))
                            pass

                        # Video
                        elif buttonsDict[butts[1]][butts[0]]["type"] == mType.VID:
                            asyncio.run(triggerVideo(buttonsDict[butts[1]][butts[0]]["message"]))
                            pass
                        
    finally:
        lp.Reset()
        lp.Close()

if __name__ == "__main__":
    main()