from tkinter import *
from translate import Translator

def trans():
    translator=Translator(from_lang=lan1.get(),to_lang=lan2.get())
    translation=translator.translate(var.get())
    var1.set(translation)


root=Tk()
root.title("Translator")

mf=Frame(root)
mf.grid(column=0,row=0, sticky=(N,W,E,S))
mf.columnconfigure(0,weight=1)
mf.rowconfigure(0,weight=1)
mf.pack(pady=100,padx=100)

lan1=StringVar(root)
lan2=StringVar(root)

choices={'English','Hindi','Gujarati','Spanish','German','Urdu'}
lan1.set('English')
lan2.set('Hindi')

lan1menu=OptionMenu(mf,lan1,*choices)
Label(mf,text="select a language").grid(row=0,column=1)
lan1menu.grid(row=1,column=1)

lan2menu=OptionMenu(mf,lan2,*choices)
Label(mf,text="select a language").grid(row=0,column=2)
lan2menu.grid(row=1,column=2)

Label(mf,text="Enter text").grid(row=2,column=0)
var=StringVar()

textbox=Entry(mf,textvariable=var).grid(row=2,column=1)

Label(mf,text="Output").grid(row=2,column=2)
var1=StringVar()
textbox=Entry(mf,textvariable=var1).grid(row=2,column=3)

b=Button(mf,text="Translate",command=trans).grid(row=3,column=1,columnspan=3)

root.mainloop()
