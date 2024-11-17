import pgzrun
from tools import *
import ctypes
try:
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
except:
    try:
        screensize = 1920,1080
    except:
        screensize = int(input("please input your desired screen width")),int(input("please enter your desired screen height"))
textpos = []
HEIGHT, WIDTH = screensize

def restartgame():
    global numTrees,employeeWage,employeeHours,numEmployees,angermeter,logPrice,employeeEfficiency,equipmentlvl,month
    month = 1
    numTrees = random.randint(100000,200000)
    employeeWage = 15
    employeeHours = 8
    numEmployees = 15
    angermeter = 0.0
    logPrice = 10
    employeeEfficiency = 1
    equipmentlvl = 1
def on_mouse_down(pos,button):
    pass
def update():
    pass
def draw():
    screen.clear()
    screen.fill((255,255,255))
    if True: #scene == "mainmenu":
        screen.draw.text("Boilerplate logging game",(WIDTH/2,HEIGHT/2),fontsize=50)
        print("aaaa")
    else:
        print("help")
    for obj in objects:
        object.draw()


pgzrun.go()