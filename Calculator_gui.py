from tkinter import *

root = Tk()

num_input = Entry(root, width=40, borderwidth=5)
num_input.grid(row=0, column=0, columnspan=4, padx=7, pady=5)

# functions
# add functionalities hernum_input...

def btn_click(n):
    current = num_input.get()
    num_input.delete(0, END)
    num_on_screen = num_input.insert(0, current + str(n))
    return num_on_screen

def btn_add():
    global operator
    global prev_num
    prev = num_input.get()
    prev_num = int(prev)
    num_input.delete(0, END)
    operator = "+"
    


def btn_sub():
    global operator
    global prev_num
    prev = num_input.get()
    prev_num = int(prev)
    num_input.delete(0, END)
    operator = "-"
    


def btn_mul():
    global operator
    global prev_num
    prev = num_input.get()
    prev_num = int(prev)
    num_input.delete(0, END)
    operator = "*"
    


def btn_div():
    global operator
    global prev_num
    prev = num_input.get()
    prev_num = int(prev)
    num_input.delete(0, END)
    operator = "/"
    


def btn_eq():
    if operator == '+':
        next = num_input.get()
        num_input.delete(0, END)
        next_num = num_input.insert(0, prev_num + int(next))
        return next_num
    elif operator == '-':
        next = num_input.get()
        num_input.delete(0, END)
        next_num = num_input.insert(0, prev_num - int(next))
        return next_num
    elif operator == '*':
        next = num_input.get()
        num_input.delete(0, END)
        next_num = num_input.insert(0, prev_num * int(next))
        return next_num
    elif operator == '/':
        next = num_input.get()
        num_input.delete(0, END)
        next_num = num_input.insert(0, prev_num / int(next))
        return next_num
    
def btn_clear():
    num_input.delete(0, END)

# Buttons

btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))

btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))

btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))

btn_plus = Button(root, text="+", padx=37, pady=20, command=btn_add)
btn_minus = Button(root, text="-", padx=40, pady=20, command=btn_sub)
btn_mult = Button(root, text="*", padx=40, pady=20, command=btn_mul)
btn_divi = Button(root, text="/", padx=40, pady=20, command=btn_div)
btn_equal = Button(root, text="=", padx=40, pady=20, command=btn_eq)
btn_del = Button(root, text="C", padx=40, pady=20, fg="red", command=btn_clear)

# Buttons layout

# row 1
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_plus.grid(row=1, column=3)
# #row 2
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_minus.grid(row=2, column=3)
# row 3
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_mult.grid(row=3, column=3)
# row 4
btn0.grid(row=4, column=0)
btn_del.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_divi.grid(row=4, column=3)

root.mainloop()
