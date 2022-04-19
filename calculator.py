from tkinter import*
from tkinter import font 
import tkinter.messagebox
import math
from turtle import right 
# creating instance of tk
root = Tk()
root.geometry("650x400+300+300")
root.iconbitmap(True,"C:/Users/ASUSH025T/Documents/python/image.ico")
root.title("Scientific Calculator")
switch= None

def btn1():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')
# getting zero and replacing it with the number in the function
def btn2():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')

def btn3():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')

def btn4():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')

def btn5():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')

def btn6():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')

def btn7():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')

def btn8():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')

def btn9():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')

def btn0():
    if disp.get()== '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')

def btnadd():
    pos= len(disp.get())
    disp.insert(pos, '+')

def btnsub():
    pos= len(disp.get())
    disp.insert(pos, '-')

def btnmul():
    pos= len(disp.get())
    disp.insert(pos, '*')

def btndiv():
    pos= len(disp.get())
    disp.insert(pos, '/')

def btnclear(*args):
    disp.delete(0, END)
    disp.insert(0, '0')

def btnsin():
    try:
        ans= float(disp.get())
        if switch is True:
            ans= math.sin(math.radians(ans))
        else:
            ans= math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error")

def btncos():
    try:
        ans= float(disp.get())
        if switch is True:
            ans= math.cos(math.radians(ans))
        else:
            ans= math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error")

def btntan():
    try:
        ans= float(disp.get())
        if switch is True:
            ans= math.tan(math.radians(ans))
        else:
            ans= math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error")

def btnarcsin():
    try:
        ans= float(disp.get())
        if switch is True:
            ans= math.degrees(math.asin(ans))
        else:
            ans= math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error")

def btnarccos():
    try:
        ans= float(disp.get())
        if switch is True:
            ans= math.degrees(math.acos(ans))
        else:
            ans= math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error")

def btnarctan():
    try:
        ans= float(disp.get())
        if switch is True:
            ans= math.degrees(math.atan(ans))
        else:
            ans= math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error")

def btnpow():
    pos = len(disp.get())
    disp.insert(pos, '^')

def btnround():
    try:
        ans= float(disp.get())
        ans= math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value error")

def btndot():
    pos = len(disp.get())
    disp.insert(pos, '.')

def btnpi():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))

def btne():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))

def btnbraco():
    pos = len(disp.get())
    disp.insert(pos, '(')

def btnbracc():
    pos = len(disp.get())
    disp.insert(pos, ')')

def btnlog():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def btnfact():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def btnsqr():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")

def btncancel():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])

def btnln():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")

def btnpercent():
    pos = len(disp.get())
    disp.insert(pos, '%')

def btnequal(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)
    except:
        tkinter.messagebox.showerror("Value Error")

def btnconvert():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Rad"

def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)
# trigerred whenever we click any number on the keyboard

# Entry widget is used to enter or display single line of text, disp is the reference of Entry
disp = Entry(root, font= "Verdana 20", fg= "black", bg= "#8F96C1", bd= 0, justify=RIGHT ,insertbackground="#8F96C1", cursor="arrow")
disp.bind("<Return>",btnequal)
disp.bind("<Escape>",btnclear)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
# initially calculator will display 0; focus is set on Entry by default; pack is showing on display
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons
# creating a frame [works like a container] to organise all the buttons [widgets]

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow1, text="π", font="Segoe 18", relief=GROOVE, bd=0, command=btnpi, fg="white", bg="#333333")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text=" x! ", font="Segoe 18", relief=GROOVE, bd=0, command=btnfact, fg="white", bg="#333333")
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="Segoe 18", relief=GROOVE, bd=0, command=btnsin, fg="white", bg="#333333")
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="Segoe 18", relief=GROOVE, bd=0, command=btncos, fg="white", bg="#333333")
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="Segoe 18", relief=GROOVE, bd=0, command=btntan, fg="white", bg="#333333")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_1 = Button(btnrow1, text="1", font="Segoe 23", relief=GROOVE, bd=0, command=btn1, fg="white", bg="#333333")
btn_1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_2 = Button(btnrow1, text="2", font="Segoe 23", relief=GROOVE, bd=0,  command=btn2, fg="white", bg="#333333")
btn_2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_3 = Button(btnrow1, text="3", font="Segoe 23", relief=GROOVE, bd=0, command=btn3, fg="white", bg="#333333")
btn_3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Segoe 23", relief=GROOVE, bd=0, command=btnadd, fg="white", bg="#333333")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

# row 2 buttons
btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

e_btn = Button(btnrow2, text="e", font="Segoe 18", relief=GROOVE, bd=0, command=btne, fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow2, text=" √x ", font="Segoe 18", relief=GROOVE, bd=0, command=btnsqr, fg="white", bg="#333333")
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(btnrow2, text="sin-1", font="Segoe 11 bold", relief=GROOVE, bd=0, command=btnarcsin, fg="white", bg="#333333")
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(btnrow2, text="cos-1", font="Segoe 11 bold", relief=GROOVE, bd=0, command=btnarccos, fg="white", bg="#333333")
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(btnrow2, text="tan-1", font="Segoe 11 bold", relief=GROOVE, bd=0, command=btnarctan, fg="white", bg="#333333")
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_4 = Button(btnrow2, text="4", font="Segoe 23", relief=GROOVE, bd=0, command=btn4, fg="white", bg="#333333")
btn_4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_5 = Button(btnrow2, text="5", font="Segoe 23", relief=GROOVE, bd=0, command=btn5, fg="white", bg="#333333")
btn_5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_6 = Button(btnrow2, text="6", font="Segoe 23", relief=GROOVE, bd=0, command=btn6, fg="white", bg="#333333")
btn_6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Segoe 23", relief=GROOVE, bd=0, command=btnsub, fg="white", bg="#333333")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# row 3 buttons
btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

conv_btn = Button(btnrow3, text="Rad", font="Segoe 12 bold", relief=GROOVE, bd=0, command=btnconvert, fg="white", bg="#333333")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text="round", font="Segoe 10 bold", relief=GROOVE, bd=0, command=btnround, fg="white", bg="#333333")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="Segoe 18", relief=GROOVE, bd=0, command=btnln, fg="white", bg="#333333")
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Segoe 17", relief=GROOVE, bd=0, command=btnlog, fg="white", bg="#333333")
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Segoe 17", relief=GROOVE, bd=0, command=btnpow, fg="white", bg="#333333")
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_7 = Button(btnrow3, text="7", font="Segoe 23", relief=GROOVE, bd=0, command=btn7, fg="white", bg="#333333")
btn_7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_8 = Button(btnrow3, text="8", font="Segoe 23", relief=GROOVE, bd=0, command=btn8, fg="white", bg="#333333")
btn_8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_9 = Button(btnrow3, text="9", font="Segoe 23", relief=GROOVE, bd=0, command=btn9, fg="white", bg="#333333")
btn_9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Segoe 23", relief=GROOVE, bd=0, command=btnmul, fg="white", bg="#333333")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

# row 4 buttons
btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

mod_btn = Button(btnrow4, text="%", font="Segoe 21", relief=GROOVE, bd=0, command=btnpercent, fg="white", bg="#333333")
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Segoe 21", relief=GROOVE, bd=0, command=btnbraco, fg="white", bg="#333333")
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Segoe 21", relief=GROOVE, bd=0, command=btnbracc, fg="white", bg="#333333")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Segoe 21", relief=GROOVE, bd=0, command=btndot, fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="⌫", font="Segoe 23", relief=GROOVE, bd=0, command=btncancel, fg="white", bg="#333333")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="C", font="Segoe 20", relief=GROOVE, bd=0, command=btnclear, fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn_0 = Button(btnrow4, text="0", font="Segoe 23", relief=GROOVE, bd=0, command=btn0, fg="white", bg="#333333")
btn_0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Segoe 23", relief=GROOVE, bd=0, command=btnequal, fg="white", bg="#333333")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Segoe 23", relief=GROOVE, bd=0, command=btndiv, fg="white", bg="#333333")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)
    
root.mainloop()