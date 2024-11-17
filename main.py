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



#amogus = Actor("test",(100,100))
option1 = "shop"
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
    print("mouse was pressed")
    print(allText)
    for i in range(len(allText)):
        print(f"scene of obj is {allText[i].scene}, current scene is {scene},value of obj is \'{allText[i].value}\'")
    #amogus.center = pos

color = 255 

mainMenu = textBox("Boilerplate logging game\n press any mouse button to continue",(WIDTH /2, HEIGHT /2),scene="mainmenu")
monthFlavorText = textBox(f"Welcome Mr./Ms/Mx. Debug! this is month {month} of your tenure as CEO of Debug's Logging company\n Current Company Treasury Balance:{money}",(WIDTH*0,HEIGHT * 0),"game")
statistics = textBox(f"STATISTICS \ntrees left in forest: {(numTrees/maxTrees)*100}%\n current employees: {numEmployees} employee pay rate: ${employeeWage}/hr\n employee shift length {employeeHours} hrs/day",(0,40),"game")
projectedRevenue = textBox(f"Projected revenue/expenses for the month: ${numEmployees*employeeEfficiency*employeeHours*20*logPrice} - ${employeeHours*employeeWage}",(0,200),"game")
options = textBox(f"Options (press number key to select): 1:shop",(WIDTH/2,HEIGHT/2),"game")
shopOptions = textBox(f"SHOP:\nhire more employees\nupgrade logging equipment:$1000/employee\nbuy more land\n",(0,0),"shop")
def update():
    global color,monthFlavorText  
    monthFlavorText.value = f"Welcome Mr./Ms./Mx. Debug! this is month {month} of your tenure as CEO of Debug's Logging company\n Current Company Treasury Balance:{money}"


def on_key_down(key):
    if key == keys.K_1:
        scene = "shop"
    else:
        scene = "mainmenu"
def draw():
    global WIDTH, HEIGHT,scene
    screen.clear()
    screen.fill((color,color,color))
    #amogus.draw()
    for text in allText:
        #if text.visible:
        if text.scene == scene:
            screen.draw.text(text.value,text.pos,color=text.color)

            


pgzrun.go()