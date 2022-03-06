import pyautogui

def rgb_2_hex(r: int, g: int, b: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

while True:
    posXY = pyautogui.position()
    pix = pyautogui.pixel(posXY[0], posXY[1])
    print(f'{posXY} RGB:{pix} HEX:{rgb_2_hex(pix[0], pix[1], pix[2])}')
    if posXY[0] < 2:
        break

input("\nPress Enter to quit the program.")
