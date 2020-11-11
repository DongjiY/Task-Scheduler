import tkinter as tk
from tkinter.filedialog import askopenfilename
import scoreCalculate
import threading

pushTasks = []
colors = ['#FF8C00','#FFEE00','#4DE94C','#3783FF','#4815AA']

def onClick(a,b,c):
    pushTasks.append(a+", "+b+", "+c)
    classEntry.delete(0,'end')
    taskEntry.delete(0,'end')
    dateEntry.delete(0,'end')
    successLabel = tk.Label(frame,text=b+" successfully added!",bg='#46d3f0',fg='red')
    successLabel.place(relwidth=.7,relheight=.05,relx=.15,rely=.58)

def onClickEnd():
    frame.destroy()
    showResults()
    pushTasks.clear()
    
def showResults():
    calendar,errors = scoreCalculate.readInputs(pushTasks)
    newFrame = tk.Frame(root, height=800, width=700, bg='#46d3f0')
    newFrame.pack()
    count = 0
    position = 0
    for x in calendar:
        if x.late:
            newLabel = tk.Label(newFrame,text=str(count+1)+". "+x.toString()+" (LATE)",bg='#F60000')
            newLabel.place(relwidth=1,relheight=.1,rely=position)
        else:
            newLabel = tk.Label(newFrame,text=str(count+1)+". "+x.toString(),bg=colors[count%4])
            newLabel.place(relwidth=1,relheight=.1,rely=position)
        count+=1
        position += .1
    errorLabel = tk.Label(newFrame,text="There were: "+str(errors)+" errors in this conversion")
    errorLabel.place(relheight=.05,relwidth=1,rely=.95)

height = 400
width = 700
root = tk.Tk()

frame = tk.Frame(root, height=height, width=width, bg='#46d3f0')
frame.pack()

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
dateEntryLabel = tk.Label(frame,text="Date:mm/dd/yyyy",bg='#46d3f0')
dateEntryLabel.place(relwidth=.15,relheight=.05,relx=.63,rely=.4)

submitTask = tk.Button(frame,text="Add Assignment",command=lambda: onClick(classEntry.get(),taskEntry.get(),dateEntry.get()))
submitTask.place(relx=.79, rely=.45, relwidth=.2, relheight=.1)

endEntries = tk.Button(frame,text="Calculate My List!",command=lambda: onClickEnd())
endEntries.place(relwidth=.3, relheight=.2,relx=.35,rely=.68)

root.mainloop()