from tkinter import *
from tkinter.messagebox import *
import math as m

root = Tk()

style = ('Verdana',22,'bold')

root.title('Calculator')
root.geometry('425x580')


def click_btn(event):
    button = event.widget
    buttonText = button['text']
    
    if buttonText == 'x':
        textField.insert(END,'*')
        return
        
    if buttonText == '=':
        try:
            expression = textField.get()
            answer = eval(expression)
            textField.delete(0,END)
            textField.insert(0,answer)
        except Exception as e:
            showerror('Error',e)
        return
 
    textField.insert(END,buttonText)
    
def all_clear():
	textField.delete(0,END)
	
def clear():
	expression = textField.get()
	expression = expression[0:len(expression)-1]
	textField.delete(0,END)
	textField.insert(0,expression)

imageSrc = PhotoImage(file = "calculator.png",master = root)
calcImage = Label(root,image = imageSrc)
calcImage.pack(side = TOP,pady = 15)

heading = Label(root,text = 'Calculator',font = style)
heading.pack(side = TOP)

textField = Entry(root,font = style,justify = CENTER)
textField.pack(side = TOP,pady = 10,fill = X,padx = 10)

buttonFrame = Frame(root)
buttonFrame.pack(side = TOP,padx = 10)

temp = 1

for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonFrame,text = str(temp),font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
        btn.grid(row = i,column = j,padx = 3,pady = 3)
        temp = temp + 1
        btn.bind('<Button-1>',click_btn)
        
zeroBtn = Button(buttonFrame,text = '0',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
zeroBtn.grid(row = 3,column = 0,padx = 3,pady = 3)

dotBtn = Button(buttonFrame,text = '.',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
dotBtn.grid(row = 3,column = 1,padx = 3,pady = 3)

equalBtn = Button(buttonFrame,text = '=',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
equalBtn.grid(row = 3,column = 2,padx = 3,pady = 3)

addBtn = Button(buttonFrame,text = '+',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
addBtn.grid(row = 0,column = 3,padx = 3,pady = 3)

subBtn = Button(buttonFrame,text = '-',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
subBtn.grid(row = 1,column = 3,padx = 3,pady = 3)

mulBtn = Button(buttonFrame,text = 'x',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
mulBtn.grid(row = 2,column = 3,padx = 3,pady = 3)

divBtn = Button(buttonFrame,text = '/',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
divBtn.grid(row = 3,column = 3,padx = 3,pady = 3)

clrBtn = Button(buttonFrame,text = '<--',font = style,width = 9,relief = 'ridge',activebackground = 'orange',activeforeground = 'white',command = clear)
clrBtn.grid(row = 4,column = 0,columnspan = 2)

allClrBtn = Button(buttonFrame,text = 'AC',font = style,width = 9,relief = 'ridge',activebackground = 'orange',activeforeground = 'white',command = all_clear)
allClrBtn.grid(row = 4,column = 2,columnspan = 2)

addBtn.bind('<Button-1>',click_btn)
subBtn.bind('<Button-1>',click_btn)
mulBtn.bind('<Button-1>',click_btn)
divBtn.bind('<Button-1>',click_btn)
zeroBtn.bind('<Button-1>',click_btn)
equalBtn.bind('<Button-1>',click_btn)
dotBtn.bind('<Button-1>',click_btn)

#-----------------Scientific Calculator--------------------------#

def calculate_sc(event):
    btn = event.widget
    btnText = btn['text']
    expression = textField.get()
    answer = ''
    
    try:
        if btnText == 'Deg':
            answer = str(m.degrees(float(expression)))

        elif btnText == 'Rad':
            answer = str(m.radians(float(expression)))

        elif btnText == 'x!':
            answer = str(m.factorial(int(expression)))

        elif btnText == 'sinϴ':
            answer = str(m.sin(m.radians(int(expression))))

        elif btnText == 'cosϴ':
            answer = str(m.cos(m.radians(int(expression))))

        elif btnText == 'tanϴ':
            answer = str(m.tan(m.radians(int(expression))))

        elif btnText == '√':
            answer = m.sqrt(float(expression))

        elif btnText == 'log':
            answer = m.log10(float(expression))
            
    except Exception as e:
            showerror('Error',e)
            return
        
    textField.delete(0,END)        
    textField.insert(0,answer)
    
def mode_change():
    global simpleCalc
    if simpleCalc:
        buttonFrame.pack_forget()
        scFrame.pack(side = TOP,pady = 10)
        buttonFrame.pack(side = TOP)
        root.geometry('425x700')
        simpleCalc = False
        
    else:
        scFrame.pack_forget()
        root.geometry('425x580')
        simpleCalc = True
        

scFrame = Frame(root)

sqrtBtn = Button(scFrame,text = '√',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
sqrtBtn.grid(row = 0,column = 0,padx = 3,pady = 3)

logBtn = Button(scFrame,text = 'log',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
logBtn.grid(row = 0,column = 1,padx = 3,pady = 3)

factBtn = Button(scFrame,text = 'x!',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
factBtn.grid(row = 0,column = 2,padx = 3,pady = 3)

radBtn = Button(scFrame,text = 'Rad',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
radBtn.grid(row = 0,column = 3,padx = 3,pady = 3)

degBtn = Button(scFrame,text = 'Deg',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
degBtn.grid(row = 1,column = 0,padx = 3,pady = 3)

sinBtn = Button(scFrame,text = 'sinϴ',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
sinBtn.grid(row = 1,column = 1,padx = 3,pady = 3)

cosBtn = Button(scFrame,text = 'cosϴ',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
cosBtn.grid(row = 1,column = 2,padx = 3,pady = 3)

tanBtn = Button(scFrame,text = 'tanϴ',font = style,width = 4,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
tanBtn.grid(row = 1,column = 3,padx = 3,pady = 3)

simpleCalc = True

sqrtBtn.bind('<Button-1>',calculate_sc)
sinBtn.bind('<Button-1>',calculate_sc)
cosBtn.bind('<Button-1>',calculate_sc)
tanBtn.bind('<Button-1>',calculate_sc)
degBtn.bind('<Button-1>',calculate_sc)
radBtn.bind('<Button-1>',calculate_sc)
factBtn.bind('<Button-1>',calculate_sc)
logBtn.bind('<Button-1>',calculate_sc)

fontMenu = ('Verdana',12,'italic')

menubar = Menu(root,font = fontMenu)

mode = Menu(menubar,font = fontMenu,tearoff = 0)
mode.add_checkbutton(label = 'Scientific Calculator',command = mode_change)

menubar.add_cascade(label = 'Mode',menu = mode)

root.config(menu = menubar)

root.mainloop()