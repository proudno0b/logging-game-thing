import pgzrun
from tools import *
import ctypes
try:
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
except:
    try:
        screensize = 800,500
    except:
        screensize = int(input("please input your desired screen width")),int(input("please enter your desired screen height"))
textpos = []
WIDTH,HEIGHT = screensize


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
    global scene
    if scene == "mainmenu":
        scene = "game"
color = 255
def update():
    global color
    color += 0
    #color %= 256
    #print(color)
def draw():
    global WIDTH, HEIGHT
    screen.clear()
    screen.fill((color,color,color))
    menucoords = [WIDTH/2, HEIGHT /2]
    print(WIDTH,HEIGHT)
    print(menucoords)
    
    if scene == "mainmenu":
        screen.draw.text("Boilerplate logging game\n press any key to continue", center=menucoords,color="black")
        
        for obj in objects:
            object.draw()
    else:
        print("something is wrong")


pgzrun.go()