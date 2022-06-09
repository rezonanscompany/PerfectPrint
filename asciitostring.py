import tkinter
from tkinter import *

textToWrite = ""
def make():
    textToWrite = ""
    text = input1.get(1.0, "end-1c")
    newtext = ""
    for i in text:
        if i=="\n":
            newtext+=" \\n"
            continue
        if i=="\"":
            newtext+="\\\""
            continue
        if i=="\'":
            newtext+="\\\'"
            continue
        if i=="\\":
            newtext+="\\"
            continue
        newtext+=i
    textToWrite = "\"{}\" : [\"{}\",\"".format(input1s.get(1.0, "end-1c"),input1n.get(1.0, "end-1c"))+newtext+" \"],\n"
    text = input2.get(1.0, "end-1c")
    newtext = ""
    for i in text:
        if i=="\n":
            newtext+=" \\n"
            continue
        if i=="\"":
            newtext+="\\\""
            continue
        if i=="\'":
            newtext+="\\\'"
            continue
        if i=="\\":
            newtext+="\\"
            continue
        newtext+=i
    textToWrite += "\"{}\" : [\"{}\",\"".format(input2s.get(1.0, "end-1c"),input2n.get(1.0, "end-1c"))+newtext+" \"],\n"
    text = input3.get(1.0, "end-1c")
    newtext = ""
    for i in text:
        if i=="\n":
            newtext+=" \\n"
            continue
        if i=="\"":
            newtext+="\\\""
            continue
        if i=="\'":
            newtext+="\\\'"
            continue
        if i=="\\":
            newtext+="\\"
            continue
        newtext+=i
    textToWrite += "\"{}\" : [\"{}\",\"".format(input3s.get(1.0, "end-1c"),input3n.get(1.0, "end-1c"))+newtext+" \"],\n"
    text = input4.get(1.0, "end-1c")
    newtext = ""
    for i in text:
        if i=="\n":
            newtext+=" \\n"
            continue
        if i=="\"":
            newtext+="\\\""
            continue
        if i=="\'":
            newtext+="\\\'"
            continue
        if i=="\\":
            newtext+="\\"
            continue
        newtext+=i
    textToWrite += "\"{}\" : [\"{}\",\"".format(input4s.get(1.0, "end-1c"),input4n.get(1.0, "end-1c"))+newtext+" \"],\n"
    text = input5.get(1.0, "end-1c")
    newtext = ""
    for i in text:
        if i=="\n":
            newtext+=" \\n"
            continue
        if i=="\"":
            newtext+="\\\""
            continue
        if i=="\'":
            newtext+="\\\'"
            continue
        if i=="\\":
            newtext+="\\"
            continue
        newtext+=i
    textToWrite += "\"{}\" : [\"{}\",\"".format(input5s.get(1.0, "end-1c"),input5n.get(1.0, "end-1c"))+newtext+" \"],\n"
    print(textToWrite)
    inputanswer.delete("1.0", tkinter.END)
    inputanswer.insert(INSERT,textToWrite)




root = tkinter.Tk()
root.geometry("1700x1000")
text_label = Label(root,text = "Ascii Text")
input1 = Text(root,height = 20,width = 40)
input2 = Text(root,height = 20,width = 40)
input3 = Text(root,height = 20,width = 40)
input4 = Text(root,height = 20,width = 40)
input5 = Text(root,height = 20,width = 40)
input1s = Text(root,height = 4,width = 40)
input2s = Text(root,height = 4,width = 40)
input3s = Text(root,height = 4,width = 40)
input4s = Text(root,height = 4,width = 40)
input5s = Text(root,height = 4,width = 40)
input1n = Text(root,height = 4,width = 40)
input2n = Text(root,height = 4,width = 40)
input3n = Text(root,height = 4,width = 40)
input4n = Text(root,height = 4,width = 40)
input5n = Text(root,height = 4,width = 40)
inputanswer = Text(root,height = 20,width = 40)
printButton = Button(root,text = "Replace",command = make)

input1.grid(row=2,column=1)
input2.grid(row=2,column=2)
input3.grid(row=2,column=3)
input4.grid(row=2,column=4)
input5.grid(row=2,column=5)
input1s.grid(row=3,column=1)
input2s.grid(row=3,column=2)
input3s.grid(row=3,column=3)
input4s.grid(row=3,column=4)
input5s.grid(row=3,column=5)
input1n.grid(row=4,column=1)
input2n.grid(row=4,column=2)
input3n.grid(row=4,column=3)
input4n.grid(row=4,column=4)
input5n.grid(row=4,column=5)
printButton.grid(row=3,column=1)
inputanswer.place(x=10,y=500,width=1200)
printButton.place(x=1300,y=500)



root.mainloop()