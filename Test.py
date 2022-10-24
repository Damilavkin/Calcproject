from tkinter import *
def add_num(num):
    value = score.get()
    if value=="0":
        value=value[1:]
    score.delete(0,END)
    score.insert(0,value+num)
    return value
def add_operation(symbol):
    value = score.get()
    if value[-1] in '-+/*^X':
        value=value[:-1]
    score.delete(0, END)
    score.insert(0, value+symbol)

def logic_score():
    value = score.get()
    if value[-1] in '+-*/':
        symbol =value[-1]
        value = value+value[:-1]
    score.delete(0, END)
    score.insert(0, eval(value))

def any_key():
    value=score.get()
    if value[-1]=="^X":
        x = value[-1]
        value = value + value[:-1]
    score.delete(0, END)
    score.insert(0, eval(value)**2)







def make_button(num):
    return Button(text=num, font=("Terminal", 20), bd=5, command=lambda: add_num(num))

def make_operation(symbol):
    return Button(text=symbol, font=("Terminal", 20), bd=5,command=lambda:add_operation(symbol))

def make_calculation(symbol):
    return Button(text=symbol, font=("Terminal", 20), bd=5, command=lambda:logic_score())

def make_any_key(x):
    return Button(text=x, font=("Terminal", 20), bd=5, command=lambda: any_key())



root =Tk()
root.geometry("560x580")
root.title("Калькулятор")
root["bg"]="black"
score=Entry(root,justify=RIGHT,font=("Roboto",20))
score.insert(0,"0")
score.grid(row=0,column=0,columnspan=4,stick="we")
make_button('1').grid(row=1,column=0,stick="wens",padx=3,pady=3)
make_button('2').grid(row=1,column=1,stick="wens",padx=3,pady=3)
make_button('3').grid(row=1,column=2,stick="wens",padx=3,pady=3)
make_button('4').grid(row=2,column=0,stick="wens",padx=3,pady=3)
make_button('5').grid(row=2,column=1,stick="wens",padx=3,pady=3)
make_button('6').grid(row=2,column=2,stick="wens",padx=3,pady=3)
make_button('7').grid(row=3,column=0,stick="wens",padx=3,pady=3)
make_button('8').grid(row=3,column=1,stick="wens",padx=3,pady=3)
make_button('9').grid(row=3,column=2,stick="wens",padx=3,pady=3)
make_button('0').grid(row=4,column=0,stick="wens",padx=3,pady=3)
make_operation("+").grid(row=1,column=3,stick="wens",padx=3,pady=3)
make_operation("-").grid(row=2,column=3,stick="wens",padx=3,pady=3)
make_operation("/").grid(row=3,column=3,stick="wens",padx=3,pady=3)
make_operation("*").grid(row=4,column=3,stick="wens",padx=3,pady=3)
make_operation(".").grid(row=5,column=3,stick="wens",padx=3,pady=3)
make_any_key("^X").grid(row=4,column=2,stick="wens",padx=3,pady=3)
make_calculation("=").grid(row=4,column=1,stick="wens",padx=3,pady=3)
root.grid_columnconfigure(0,minsize=60)
root.grid_columnconfigure(1,minsize=60)
root.grid_columnconfigure(2,minsize=60)
root.grid_columnconfigure(3,minsize=60)
root.rowconfigure(1,minsize=60)
root.rowconfigure(2,minsize=60)
root.rowconfigure(3,minsize=60)
root.rowconfigure(4,minsize=60)
root.rowconfigure(5,minsize=60)













root.mainloop()

