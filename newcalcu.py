import tkinter
from tkinter.ttk import *
import tkinter as tk
window = tkinter.Tk()
window.title("Calculator")
window.geometry("369x430")
window.resizable(0,0)
window.config(bg="white")

sample_text = tkinter.Entry(window)
sample_text.pack()

def set_text_1():
	sample_text.insert("end", "1")

def set_text_2():
	sample_text.insert("end", "2")

def set_text_3():
	sample_text.insert("end", "3")


def set_text_4():
	sample_text.insert("end", "4")

def set_text_5():
	sample_text.insert("end", "5")

def set_text_6():
	sample_text.insert("end", "6")

def set_text_7():
	sample_text.insert("end", "7")

def set_text_8():
	sample_text.insert("end", "8")

def set_text_9():
	sample_text.insert("end", "9")

def set_text(text):
    sample_text.insert("end", text)

def reset_text():
    sample_text.delete(0, "end")

def delete_text():
    text = sample_text.get()
    sample_text.delete(0, "end")
    sample_text.insert(0, text[:-1])

def calculate_result():
    try:
        res = eval(sample_text.get())
        sample_text.delete(0, "end")
        sample_text.insert(0, res)
    except Exception as e:
        sample_text.delete(0, "end")
        sample_text.insert(0, "Error")


btn1 = tkinter.Button(window, text="1", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("1")).place(x=20, y=285)
btn2 = tkinter.Button(window, text="2", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("2")).place(x=107, y=285)
btn3 = tkinter.Button(window, text="3", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("3")).place(x=193, y=285)
btn4 = tkinter.Button(window, text="4", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("4")).place(x=20, y=220)
btn5 = tkinter.Button(window, text="5", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("5")).place(x=107, y=220)
btn6 = tkinter.Button(window, text="6", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("6")).place(x=193, y=220)
btn7 = tkinter.Button(window, text="7", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("7")).place(x=20, y=155)
btn8 = tkinter.Button(window, text="8", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("8")).place(x=107, y=155)
btn9 = tkinter.Button(window, text="9", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="black", bg="white", command=lambda: set_text("9")).place(x=193, y=155)
dot = tkinter.Button(window, text=".", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="white", bg="gray35", command=lambda: set_text(".")).place(x=193, y=350)
zero = tkinter.Button(window, text="0", width=9, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="white", bg="gray35", command=lambda: set_text("0")).place(x=20, y=350)
plus = tkinter.Button(window, width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="gray5", bg="#6A0DAD", text="+", command=lambda: set_text("+")).place(x=280, y=285)
minus = tkinter.Button(window, text="-", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="gray5", bg="#6A0DAD", command=lambda: set_text("-")).place(x=280, y=220)
multiply = tkinter.Button(window, text="*", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="gray5", bg="#6A0DAD", command=lambda: set_text("*")).place(x=280, y=155)
divide = tkinter.Button(window, text="/", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="gray5", bg="#6A0DAD", command=lambda: set_text("/")).place(x=280, y=90)
equal = tkinter.Button(window, text="=", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="gray5", bg="#6A0DAD", command=calculate_result).place(x=280, y=350)
reset_btn = tkinter.Button(window, text="RE", width=4, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="white", bg="#6A0DAD", command=reset_text).place(x=193, y=90)
delete_btn = tkinter.Button(window, text="D", width=9, height=1, font=("Times New Roman", 20, "bold"), bd=1, fg="white", bg="#6A0DAD", command=delete_text).place(x=20, y=90)

window.mainloop()
