from tkinter import *
root=Tk()
root.title("CALCULETOR")
root.geometry("300x355")
root.config(bg="red")
root.resizable(0,0)

def click(number):
    global operator
    operator=operator+str(number)
    variable.set(operator)
operator=""
def clear():
    global operator
    operator=""
    variable.set(operator)
    
def sum():
    global operator
    operator=str(eval(operator))
    variable.set(operator)
    

variable=StringVar()

mainFrame=Frame(root,bg="white")
mainFrame.grid()
HeadFrame=Frame(mainFrame,bd=1,padx=50,pady=20,relief=RIDGE)
HeadFrame.pack(side=TOP)
wrokEntry=Entry(HeadFrame,font=("arial",12,"bold"),bd=10,textvariable=variable)
wrokEntry.grid()
bodyFrame=Frame(mainFrame,width=1330,height=1200,padx=10,pady=10)
bodyFrame.pack(side=BOTTOM)
button7=Button(bodyFrame,text="7",padx=20,pady=20,command=lambda : click(7))
button7.grid(row=0,column=0)
button8=Button(bodyFrame,text="8",padx=20,pady=20,command=lambda : click(8))
button8.grid(row=0,column=1)
button9=Button(bodyFrame,text="9",padx=20,pady=20,command=lambda : click(9))
button9.grid(row=0,column=2)

button=Button(bodyFrame,text="/",padx=20,pady=20,command=lambda : click("/"))
button.grid(row=0,column=3)





button4=Button(bodyFrame,text="4",padx=20,pady=20,command=lambda : click(4))
button4.grid(row=1,column=0)
button5=Button(bodyFrame,text="5",padx=20,pady=20,command=lambda : click(5))
button5.grid(row=1,column=1)
button6=Button(bodyFrame,text="6",padx=20,pady=20,command=lambda : click(6))
button6.grid(row=1,column=2)

button=Button(bodyFrame,text="*",padx=20,pady=20,command=lambda : click("*"))
button.grid(row=1,column=3)


button1=Button(bodyFrame,text="1",padx=20,pady=20,command=lambda : click(1))
button1.grid(row=2,column=0)
button2=Button(bodyFrame,text="2",padx=20,pady=20,command=lambda : click(2))
button2.grid(row=2,column=1)
button3=Button(bodyFrame,text="3",padx=20,pady=20,command=lambda : click(3))
button3.grid(row=2,column=2)

buttonminus=Button(bodyFrame,text="-",padx=20,pady=20,command=lambda : click("-"))
buttonminus.grid(row=2,column=3)


button=Button(bodyFrame,text="0",padx=20,pady=20,command=lambda : click(0))
button.grid(row=3,column=0)

button=Button(bodyFrame,text="C",padx=20,pady=20,command=clear)
button.grid(row=3,column=1)

button=Button(bodyFrame,text="=",padx=20,pady=20,command=sum)
button.grid(row=3,column=2)

button=Button(bodyFrame,text="+",padx=20,pady=20,command=lambda : click("+"))
button.grid(row=3,column=3)




root.mainloop()
