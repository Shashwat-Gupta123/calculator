import tkinter as vk
import ipywidgets as widgets
from tkinter import END
root=vk.Tk()
def button_click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))

def delete_ce():
    root.config(bg="green",borderwidth=20)
    length=len(entry.get())
    entry.delete(length-1,END)
def delete_c():
    root.config(bg="orange",borderwidth=20)
    entry.delete(0,END)
def execute():
    try:
        root.config(bg="yellow",borderwidth=20)
        evaluate=entry.get()
        ans=eval(evaluate)
        entry.delete(0,END)
        entry.insert(0,str(ans))
    except ZeroDivisionError:
        entry.delete(0,END)
        entry.insert(0,"Division by zero is not possible")
        
 

root.title("Calcultor")
root.geometry("330x390")
root.config(bg="blue",borderwidth=20)
entry=vk.Entry(root,width=24,borderwidth=10,font=10)
button0=vk.Button(root,text="0",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(0))
button1=vk.Button(root,text="1",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(1))
button2=vk.Button(root,text="2",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(2))
button3=vk.Button(root,text="3",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(3))
button4=vk.Button(root,text="4",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(4))
button5=vk.Button(root,text="5",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(5))
button6=vk.Button(root,text="6",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(6))
button7=vk.Button(root,text="7",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(7))
button8=vk.Button(root,text="8",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(8))
button9=vk.Button(root,text="9",bg="yellow",borderwidth=10,padx=10,pady=5,font=10,command=lambda:button_click(9))
button_add=vk.Button(root,text="+",bg="red",borderwidth=10,padx=31,pady=5,font=7,command=lambda:button_click("+"))
button_minus=vk.Button(root,text="-",bg="red",borderwidth=10,padx=32,pady=5,font=7,command=lambda:button_click("-"))
button_mul=vk.Button(root,text="*",bg="red",borderwidth=10,padx=32,pady=5,font=7,command=lambda:button_click("*"))
button_divide=vk.Button(root,text="/",bg="red",borderwidth=10,padx=32,pady=5,font=7,command=lambda:button_click("/"))
button_equal=vk.Button(root,text="=",bg="red",borderwidth=10,padx=40,pady=5,font=7,command=execute)
button_ce=vk.Button(root,text="CE",bg="orange",borderwidth=10,padx=45,pady=5,font=3,command=delete_ce)
button_c=vk.Button(root,text="C",bg="orange",borderwidth=10,padx=46,pady=5,font=3,command=delete_c)

entry.insert(0,"Enter the Expression...")
entry.place(x=0,y=0)
button7.place(x=0,y=45)
button8.place(x=60,y=45)
button9.place(x=120,y=45)
button_add.place(x=180,y=45)

button4.place(x=0,y=107)
button5.place(x=60,y=107)
button6.place(x=120,y=107)
button_minus.place(x=182,y=107)
button1.place(x=0,y=170)
button2.place(x=60,y=170)
button3.place(x=120,y=170)
button0.place(x=0,y=233)
button_mul.place(x=182,y=170)
button_equal.place(x=61,y=233)
button_ce.place(x=0,y=295)
button_divide.place(x=183,y=233)
button_c.place(x=146,y=295)


root.mainloop()
