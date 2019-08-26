from tkinter import *
from my import *

def search():
    t1.config(state='normal')
    l=translate(e1val.get())
    t1.delete('1.0', END)
    t1.insert(END,'\n*******************\n'.join(l))
    t1.config(state='disabled')

window=Tk(className="Dictionary")

e1val=StringVar()

e1=Entry(window,textvariable=e1val)
b1=Button(window,text='Search',command=search)
t1=Text(window,width=100,height=10)

e1.grid(row=0,column=0)
b1.grid(row=1,column=0)
t1.grid(row=0,column=1)

window.mainloop()
