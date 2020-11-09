from datetime import date
from tkinter.filedialog import askopenfilename

classList = {
    "cs2337":{"exam1":.25,"exam2":.25,"assignment":.5},
    "cs1200":{"homework":.25,"quiz":.25,"test":.5,"project":.25},
    "cs2305":{"learnsmart":.1,"homework":.3,"exam":.3},
    "musi2322":{"participation":.1,"journal":.2,"discussion board":.1,"exam1":.15,"exam2":.15,"exam3":.15},
    "math2413":{"dhw":.1,"ghw":.15,"quiz":.15,"exam":.36,"final":.24}
}

class task:
    score = 0
    late = False
    def __init__(self,thisClass,name,weight,difficulty,dueDate):
        self.thisClass = thisClass
        self.name = name
        self.weight = weight
        self.difficulty = difficulty
        self.dueDate = dueDate
        self.score = calculateScore(self)
    def printTask(self):
        print(self.name, self.score)
    def toString(self):
        return str(self.thisClass)+": "+str(self.name)+": "+str(self.dueDate)

def calculateScore(tasktocalc):
    today = date.today()
    dateDelta = tasktocalc.dueDate-today
    if tasktocalc.weight > 1:
        tempWeight = tasktocalc.weight/100
    else:
        tempWeight = tasktocalc.weight
    if dateDelta.days < 0:
        tasktocalc.late = True
        score = tasktocalc.difficulty*2 + tempWeight*100
    else:
        score = (tasktocalc.difficulty*2 + tempWeight*100) - 7*(dateDelta.days)
    return score

def findWeight(classNum, taskName):
    while True:
        try:
            for x in classList[classNum]:
                if x in taskName:
                    return classList[classNum][x]
            return False
        except:
            return False

filename = askopenfilename()
myCalendar = []
f = open(filename)
for x in f:
    thisInput = x
    assignment = thisInput.split(',')
    classNum = assignment[0].lower()
    taskName = assignment[1].lower().strip()
    taskDate = assignment[2].split('/')
    dueDate = date(int(taskDate[2]),int(taskDate[0]),int(taskDate[1]))
    taskWeight = findWeight(classNum,taskName)
    if taskWeight == False:
        print("ERROR:TASK UNKNOWN! THIS TASK WAS SKIPPED:",classNum,taskName)
        continue
    else:
        tempTask = task(classNum,taskName,taskWeight,5,dueDate)
    myCalendar.append(tempTask)
count = 1
myCalendar.sort(key = lambda x: x.score, reverse = True)
print("Here is your ordering from the inputs:")
for x in myCalendar:
    if x.late:
        print(str(count)+". "+x.toString()+" (LATE)")
    else:
        print(str(count)+". "+x.toString())
    count += 1

