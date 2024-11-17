import pgzrun
from tools import *
import ctypes
try:
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
except:
    screensize = 800,500
WIDTH,HEIGHT = screensize

 #format ("text", (pos) (isVisible))



amogus = Actor("test",(100,100))

def restartgame():


    global maxTrees,numTrees,employeeWage,employeeHours,numEmployees,angermeter,logPrice,employeeEfficiency,equipmentlvl,month,scene
    month = 1
    numTrees = random.randint(100000,200000)
    maxTrees = numTrees
    employeeWage = 15
    employeeHours = 8
    numEmployees = 15
    angermeter = 0.0
    logPrice = 10
    employeeEfficiency = 1
    equipmentlvl = 1
    scene ="mainmenu"


def on_mouse_down(pos,button):  
    global scene
    if scene == "mainmenu":
        scene ="game"
    else:
        print("skibidi rizz")
    print("mouse was pressed")
    print(allText)
    for i in range(len(allText)):
        print(f"scene of obj is {allText[i].scene}, current scene is {scene},value of obj is \'{allText[i].value}\'")
    amogus.center = pos

color = 255 

mainMenu = textBox("Boilerplate logging game\n press any mouse button to continue",(WIDTH /2, HEIGHT /2),scene="mainmenu")
monthFlavorText = textBox(f"Welcome Mr./Ms/Mx. Debug! this is month {month} of your tenure as CEO of Debug's Logging company\n Current Company Treasury Balance:{money}",(HEIGHT/2,WIDTH*0.75),"game")
def update():
    global color,monthFlavorText  
    monthFlavorText.value = f"Welcome Mr./Ms./Mx. Debug! this is month {month} of your tenure as CEO of Debug's Logging company\n Current Company Treasury Balance:{money}"



def draw():
    global WIDTH, HEIGHT,scene
    screen.clear()
    screen.fill((color,color,color))
    #amogus.draw()
    for text in allText:
        #if text.visible:
        if text.scene == scene:
            screen.draw.text(text.value,text.pos,color=text.color)
        else:
            


pgzrun.go()