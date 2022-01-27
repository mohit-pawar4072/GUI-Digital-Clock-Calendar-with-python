from tkinter import *
from tkcalendar import *
from time import strftime

root = Tk()
root.title('Digital Clock & Calendar')
root.geometry('500x500')
root.config(bg='lightblue')

def selectdate():
    mydate = mycal.get_date()
    select = Label(text=mydate)
    select.pack(padx=2,pady=2)


mycal = Calendar(root,setmode='day',date_pattern='d/m/yy')
mycal.pack(padx=15,pady=15)

btn = Button(root,text='Select date',width=10,command=selectdate)
btn.pack(padx=15,pady=15)

def none():
    text = strftime(' %I:%M:%S %p')
    lbl.config(text=text)
    lbl.after(1000,none)

lbl = Label(root,font=('digital-7',50,'bold'),background='black',foreground='red')
lbl.pack(anchor=CENTER,pady=15)

none()

root.mainloop()