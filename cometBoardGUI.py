import tkinter as tk
from tkinter.filedialog import askopenfilename
import scoreCalculate
import threading

pushTasks = []
colors = ['#FF8C00','#FFEE00','#4DE94C','#3783FF','#4815AA']

def onClick(a,b,c):
    if a == "" or b == "" or c == "":
        failLabel = tk.Label(frame,text="Input Failed! Try Again.",bg='#46d3f0',fg='red')
        failLabel.place(relwidth=.5,relheight=.05,relx=.25,rely=.58)
    else:
        pushTasks.append(a+", "+b+", "+c)
        classEntry.delete(0,'end')
        taskEntry.delete(0,'end')
        dateEntry.delete(0,'end')
        successLabel = tk.Label(frame,text=b+" successfully added!",bg='#46d3f0',fg='green')
        successLabel.place(relwidth=.5,relheight=.05,relx=.25,rely=.58)

def onClickEnd():
    if len(pushTasks) > 0:
        # frame.destroy()
        showResults()
    else:
        noItems = tk.Label(frame,text="You need to add items!",fg='red',bg='#46d3f0')
        noItems.place(relwidth=.5, relheight=.05,relx=.25,rely=.9)
    
def showResults():
    calendar,errors = scoreCalculate.readInputs(pushTasks)
    showTop = tk.Toplevel()
    newFrame = tk.Frame(showTop, height=800, width=700, bg='#46d3f0')
    newFrame.pack()
    count = 0
    position = 0.005
    for x in calendar:
        if x.late:
            newLabel = tk.Label(newFrame,text=str(count+1)+". "+x.toString()+" (LATE)",bg='#F60000')
            newLabel.place(relwidth=.99,relheight=.1,rely=position,relx=.005)
        else:
            newLabel = tk.Label(newFrame,text=str(count+1)+". "+x.toString(),bg=colors[count%4])
            newLabel.place(relwidth=.99,relheight=.1,rely=position,relx=.005)
        count+=1
        position += .1
    errorLabel = tk.Label(newFrame,text="There were: "+str(errors)+" errors in this conversion")
    errorLabel.place(relheight=.05,relwidth=1,rely=.95)

def removeTaskFunc():
    top = tk.Toplevel()
    removeFrame = tk.Frame(top,height=500, width=500, bg='#46d3f0')
    removeFrame.pack()
    title = tk.Label(removeFrame,text="VIEW/REMOVE A TASK",bg='#46d3f0').place(relwidth=.5,relheight=.2,relx=.25,rely=.01)
    choices = tk.Listbox(removeFrame)
    for x in range(len(pushTasks)):
        choices.insert(x,pushTasks[x])
    choices.place(relwidth=.7,relheight=.6,relx=.15,rely=.22,anchor='nw')
    deleteButton = tk.Button(removeFrame,text="DELETE",command=lambda:deleteFunc(choices.curselection()))
    deleteButton.place(relwidth=.1, relheight=.05,relx=.45,rely=.85)
    clearButton = tk.Button(removeFrame,text="CLEAR",command=lambda:clearFunc())
    clearButton.place(relwidth=.1,relheight=.05,relx=.45,rely=.91)
    def deleteFunc(itemToDelete):
        for x in itemToDelete:
            del pushTasks[x]
            choices.delete(x)
    def clearFunc():
            pushTasks.clear()
            choices.delete(0,'end')
    backButton = tk.Button(removeFrame,text="Back",command=lambda: top.destroy())
    backButton.place(relwidth=.1, relheight=.05,relx=.9,rely=.95)
    
height = 400
width = 700
root = tk.Tk()

frame = tk.Frame(root, height=height, width=width, bg='#46d3f0')
frame.pack()

titleLabel = tk.Label(frame,text="ADD ITEMS TO BE SORTED",bg='#0db2d4')
titleLabel.place(relwidth=1,relheight=.2,rely=.1)

classEntry = tk.Entry(frame)
classEntry.place(relwidth=.2, relheight=.1, relx=.01,rely=.45)
classEntryLabel = tk.Label(frame,text="Course Number ex. cs2337",bg='#46d3f0')
classEntryLabel.place(relwidth=.2,relheight=.05,relx=.01,rely=.4)

taskEntry = tk.Entry(frame)
taskEntry.place(relwidth=.4,relheight=.1, relx=.22, rely=.45)
taskEntryLabel = tk.Label(frame,text="Assignment Name",bg='#46d3f0')
taskEntryLabel.place(relwidth=.4,relheight=.05,relx=.22,rely=.4)

dateEntry = tk.Entry(frame)
dateEntry.place(relx=.63,rely=.45,relheight=.1,relwidth=.15)
dateEntryLabel = tk.Label(frame,text="Date: mm/dd/yyyy",bg='#46d3f0')
dateEntryLabel.place(relwidth=.15,relheight=.05,relx=.63,rely=.4)

submitTask = tk.Button(frame,text="Add Assignment",command=lambda: onClick(classEntry.get(),taskEntry.get(),dateEntry.get()))
submitTask.place(relx=.79, rely=.45, relwidth=.2, relheight=.1)

endEntries = tk.Button(frame,text="Calculate My List!",command=lambda: onClickEnd())
endEntries.place(relwidth=.3, relheight=.2,relx=.35,rely=.68)

removeTask = tk.Button(frame, text="Remove/View Tasks",command=lambda: removeTaskFunc())
removeTask.place(relwidth=.2,relheight=.1,relx=.79,rely=.56)

root.mainloop()