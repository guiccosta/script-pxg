import pyautogui

class Pokemon(object):
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left 
        self.right = right

pidgeot = Pokemon('up.png','down.png','left.png','right.png')

# pyautogui.getWindowsWithTitle('PokeXGames')[0].maximize()
pyautogui.getWindowsWithTitle('PokeXGames')[0].activate()

loc = [pyautogui.locateOnScreen(i, confidence=0.5) for i in pidgeot.__dict__.values()]

loc = list(set(loc))
loc.remove(None)

if len(loc)!=0:
    print('Tem Pidgeot na tela!')