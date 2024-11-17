import random
allText = []
objects = []
maxTrees = random.randint(100000,200000)
numTrees = maxTrees
employeeWage = 15
employeeHours = 8
numEmployees = 15
angermeter = 0.0
logPrice = 10
employeeEfficiency = 1
equipmentlvl = 1
month = 1
scene = "mainmenu"
money = 1000

class textBox():
    def __init__(self,value,pos,scene):
        self.scene = scene
        self.color = "black"
        self.value = value
        self.pos = pos
        self.visible = True
        allText.append(self)
