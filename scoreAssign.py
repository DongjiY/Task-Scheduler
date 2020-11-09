classList = {
    "cs2337":{"exam1":.25,"exam2":.25,"assignment":.5},
    "cs1200":{"homework":.25,"quiz":.25,"test":.5,"project":.25},
    "cs2305":{"learnsmart":.1,"homework":.3,"exam":.3},
    "musi2322":{"participation":.1,"journal":.2,"discussion board":.1,"exam1":.15,"exam2":.15,"exam3":.15},
    "math2413":{"dhw":.1,"ghw":.15,"quiz":.15,"exam":.36,"final":.24}
}

class task:
    score = 0
    def __init__(self,thisClass,name,weight,difficulty):
        self.thisClass = thisClass
        self.name = name
        self.weight = weight
        self.difficulty = difficulty
        self.score = calculateScore(self)
    def printTask(self):
        print(self.name, self.score)
    def toString(self):
        return str(self.thisClass)+": "+str(self.name)+": "+str(self.score)

def calculateScore(tasktocalc):
    if tasktocalc.weight > 1:
        tempWeight = tasktocalc.weight/100
    else:
        tempWeight = tasktocalc.weight
    score = tasktocalc.difficulty*2 + tempWeight*100
    return score

def findWeight(classNum, taskName):
    while True:
        try:
            for x in classList[classNum]:
                if x in taskName:
                    return classList[classNum][x]
            return False
        except:
            # print("Could not find the task! You must manually input the weight")
            return False

myCalendar = []
while True:
    print("Enter a task in the form classNum, hwName. Type stop to exit")
    thisInput = input()
    if thisInput.lower() == "stop":
        print("You have exited the input mode\n")
        break
    assignment = thisInput.split(',')
    classNum = assignment[0].lower()
    taskName = assignment[1].lower().strip()
    taskWeight = findWeight(classNum,taskName)
    if taskWeight == False:
        print("Could not find the task! You must manually input the weight as a percent value")
        while True:    
            try:
                manualWeight = int(input())/100
            except:
                print("Failed! Enter a valid number 1-100!")
            else:
                tempTask = task(classNum,taskName,manualWeight,5)
                break
    else:
        tempTask = task(classNum,taskName,taskWeight,5)
    myCalendar.append(tempTask)
    print("task entered!\n")
count = 1
myCalendar.sort(key = lambda x: x.score, reverse = True)
print("Here is your ordering for today:")
for x in myCalendar:
    print(str(count)+". "+x.toString())
    count += 1
    
# testItem = task("Drink water",.45,6)
# testItemTwo = task("Do math homework",.3,10)
# testItemThree = task("Discrete Math Test",.7,2)
# allScores = [testItem, testItemTwo, testItemThree]
# testItemFour = task("Play League",0,10)
# allScores.append(testItemFour)
# allScores.sort(key = lambda x: x.score, reverse = True)
# for x in allScores:
#     x.printTask()