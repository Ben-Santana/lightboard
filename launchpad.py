from buttons import buttonsDict, brightnessScale
        
def lightLeds(lp):
    for i in range(9):
        for j in range(9):
            if i in buttonsDict and j in buttonsDict[i]:
                colorValues = buttonsDict[i][j]["color"]
                lp.LedCtrlXY(j, i, int(colorValues[0]*brightnessScale), int(colorValues[1]*brightnessScale), int(colorValues[2]*brightnessScale))