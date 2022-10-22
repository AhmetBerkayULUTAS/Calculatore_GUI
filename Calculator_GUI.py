from tkinter import *
from turtle import width

check = 5
numberlistNumber1 = 0
numberlistNumber2 = 0
s = 0

def number_refl(x):
    global s
    s = len(screen.get())
    screen.insert(s, str(x))

def char_refl(x):
    global check
    check = x
    global numberlistNumber1
    numberlistNumber1 = float(screen.get())
    if(check==4): screen.delete(number_delete(), "end")
    else : screen.delete(0, 'end')

def calculate():
    global numberlistNumber2
    numberlistNumber2 = float(screen.get())
    global check
    sonuc = 0
    if(check==0): sonuc = numberlistNumber1+ numberlistNumber2
    elif(check==1): sonuc = numberlistNumber1 - numberlistNumber2
    elif(check==2): sonuc = numberlistNumber1 * numberlistNumber2
    elif(check==3): sonuc = numberlistNumber1 / numberlistNumber2
    elif(check==5): sonuc = numberlistNumber1 ** numberlistNumber2
    elif(check==6): sonuc = numberlistNumber1 ** (1/numberlistNumber2)
    elif(check==7): sonuc = numberlistNumber1 % numberlistNumber2
    screen.delete(0, 'end')
    screen.insert(0, str(sonuc))
    
def number_delete():
    global s
    s = len(screen.get())
    return s-1

mywindow = Tk()
mywindow.minsize(270, 260)
mywindow.maxsize(270, 260)
mywindow.title("Calculator")

screen = Entry(font="Verdana 14 bold", width=16, justify=RIGHT)
screen.place(x=20,y=15)

numberlist = []

for i in range(1,10):
    numberlist.append(Button(text=str(i),font="Verdana 14 bold", command= lambda x=i:number_refl(x)))

var = 0
for i in range(0,3):
    for j in range(0,3):
        numberlist[var].place(x=20+j*50,y=50+i*50)
        var += 1

charlist = []

for i in range (0,8):
    charlist.append(Button(font="Verdana 14 bold", width = 2, command= lambda x=i :char_refl(x)))

charlist[0]['text'] = "+"
charlist[1]['text'] = "-"
charlist[2]['text'] = "x"
charlist[3]['text'] = "/"
charlist[4]['text'] = "<x"
charlist[5]['text'] = "xʸ"
charlist[6]['text'] = "ʸ√"
charlist[7]['text'] = "%"


numberlist = 0
for i in range(0,2):
    for j in range(0,4):
        charlist[numberlist].place(x=170+i*49, y=50+j*50)
        numberlist +=1

zerobutton = Button(text=0, font="Verdana 14 bold",command= lambda x=0:number_refl(x))
zerobutton.place(x=20, y = 200)

dotbutton = Button(text= "." , font="Verdana 14 bold", width=2, command= lambda x=".": number_refl(x))
dotbutton.place(x=70, y=200)

equalbutton = Button(text="=", font="Verdana 14 bold", command= calculate)
equalbutton.place(x=120, y=200)

mywindow.mainloop()