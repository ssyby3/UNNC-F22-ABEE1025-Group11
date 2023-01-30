# 科学计算器
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
from scipy import linalg


#  Function 1 Input vector in three ways

def finish_21():
    global l
    l = np.array([lt])
    t1.insert('end', l)


def f1_1():
    win1.destroy()
    global e1, e2, e3,t1,lt

    def add():
        num = e1.get()
        e1.delete(0, END)
        lt.append(num)

    win1_1 = tk.Tk()
    win1_1.title("calculator")
    win1_1.geometry("480x550")
    lt = []
    l1 = Label(win1_1, text="fill in vector numbers\n(Enter one numbers at a time and Fill once):", font="song 20")
    e1 = Entry(win1_1, font="song 30", width=15)
    b1 = Button(win1_1, text="log in", command=add, font="song 20")
    b2 = Button(win1_1, text="finish", command=finish_21, font="song 20")
    l2 = Label(win1_1, text="vector is:", font="song 20")
    t1 = Text(win1_1, font="song 20", width=30, height=5)
    l1.grid(row=0, column=0, columnspan=3, pady=20)
    e1.grid(row=1, column=0, columnspan=3, padx=10, pady=20)
    b1.grid(row=2, column=0, pady=20)
    b2.grid(row=2, column=2, pady=20)
    l2.grid(row=3, column=0)
    t1.grid(row=4, column=0, columnspan=3, padx=10)
    win1_1.mainloop()


def finish_22():
    global l
    begin = eval(e1.get())
    end = eval(e2.get())
    length = eval(e3.get())
    l = np.arange(begin, end, length)
    t1.insert('end', l)


def f1_2():
    global e1, e2, e3,t1
    win1.destroy()
    win1_2 = tk.Tk()
    win1_2.title("calculator")
    win1_2.geometry("480x550")
    l1 = Label(win1_2, text="origin:", font="song 20")
    e1 = Entry(win1_2, font="song 20", width=15)
    l2 = Label(win1_2, text="final(This figure is not included):", font="song 20")
    e2 = Entry(win1_2, font="song 20", width=15)
    l3 = Label(win1_2, text="step size:", font="song 20")
    e3 = Entry(win1_2, font="song 20", width=15)
    b1 = Button(win1_2, text="finish", command=finish_22, font="song 20")
    l4 = Label(win1_2, text="vector is:", font="song 20")
    t1 = Text(win1_2, font="song 20", width=30, height=5)
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    b1.grid(row=3, column=0, columnspan=2, pady=20)
    l4.grid(row=4, column=0)
    t1.grid(row=5, column=0, columnspan=2)
    win1_2.mainloop()


def finish_23():
    global l
    begin = eval(e1.get())
    end = eval(e2.get())
    n = eval(e3.get())
    l = np.linspace(begin, end, n)
    t1.insert('end', l)


def f1_3():
    global e1, e2, e3,t1
    win1.destroy()
    win1_2 = tk.Tk()
    win1_2.title("calculator")
    win1_2.geometry("480x550")
    l1 = Label(win1_2, text="origin:", font="song 20")
    e1 = Entry(win1_2, font="song 20", width=15)
    l2 = Label(win1_2, text="final(This figure is not included):", font="song 20")
    e2 = Entry(win1_2, font="song 20", width=15)
    l3 = Label(win1_2, text="number:", font="song 20")
    e3 = Entry(win1_2, font="song 20", width=15)
    b1 = Button(win1_2, text="finish", command=finish_23, font="song 20")
    l4 = Label(win1_2, text="vector is:", font="song 20")
    t1 = Text(win1_2, font="song 20", width=30, height=5)
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    b1.grid(row=3, column=0, columnspan=2, pady=20)
    l4.grid(row=4, column=0)
    t1.grid(row=5, column=0, columnspan=2)
    win1_2.mainloop()


def getvector():
    global win1
    # win.destroy()
    win1 = tk.Tk()
    win1.title("calculator")
    win1.geometry("550x480")
    b1 = Button(win1, text="manual filling", command=f1_1, font="song 20")
    b2 = Button(win1, text="fill in the step length method", command=f1_2, font="song 20")
    b3 = Button(win1, text="fill in the method of equal division", command=f1_3, font="song 20")
    b1.pack(pady=20)
    b2.pack(pady=20)
    b3.pack(pady=20)


# Function 2 Input matrix, divided into four matrices
def cw1():
    m2 = np.transpose(m)
    t1.delete('1.0', END)
    t1.insert('end', m2)


def cw2():
    m2 = np.linalg.det(m)
    t1.delete('1.0', END)
    t1.insert('end', m2)


def combine():
    global ls
    lt.append(ls)
    ls = []


def finish_1():
    global m
    try:  # If the matrix format is incorrect, the program will issue a corresponding warning, but does not affect the program to continue to execute
        m = np.array(lt)
    except:
        tm.showerror('error', 'please enter the correct matrix format')
    t1.insert('end', m)


def f2_1():
    global ls, lt, t1, e1, e2

    def add():
        num = e1.get()
        e1.delete(0, END)
        ls.append(eval(num))

    lt = []
    ls = []
    win2.destroy()
    win2_1 = tk.Tk()
    win2_1.title("calculator")
    win2_1.geometry("480x550")
    l1 = Label(win2_1, text="stuffing digit\n(Press once for each number entered):", font="song 20")
    e1 = Entry(win2_1, font="song 30", width=15)
    b1 = Button(win2_1, text="log in", command=add, font="song 20")
    b2 = Button(win2_1, text="Combine into a one-line array", command=combine, font="song 20")
    b3 = Button(win2_1, text="finish", command=finish_1, font="song 20")
    l2 = Label(win2_1, text="output:", font="song 20")
    b4 = Button(win2_1, text="Output the transpose matrix", command=cw1, font="song 20")
    b5 = Button(win2_1, text="Outputs the determinant of the matrix", command=cw2, font="song 20")
    t1 = Text(win2_1, font="song 20", width=30, height=5)
    l1.grid(row=0, column=0, columnspan=3, pady=20)
    e1.grid(row=1, column=0, columnspan=3, padx=10, pady=20)
    b1.grid(row=2, column=0, pady=20)
    b2.grid(row=2, column=1, pady=20)
    b3.grid(row=2, column=2, pady=20)
    l2.grid(row=3, column=0)
    b4.grid(row=5, column=0, columnspan=3)
    b5.grid(row=6, column=0, columnspan=3)
    t1.grid(row=4, column=0, columnspan=3, padx=10)
    win2_1.mainloop()


def finish_2():
    global m
    x = eval(e1.get())
    y = eval(e2.get())
    m = np.random.rand(x, y)
    t1.insert('end', m)


def f2_2():
    global t1, e1, e2
    win2.destroy()
    win2_2 = tk.Tk()
    win2_2.title("calculator")
    win2_2.geometry("480x550")
    l1 = Label(win2_2, text="The number of rows in this matrix:", font="song 20")
    e1 = Entry(win2_2, font="song 20", width=15)
    l2 = Label(win2_2, text="The number of columns of the matrix:", font="song 20")
    e2 = Entry(win2_2, font="song 20", width=15)
    b1 = Button(win2_2, text="finish", command=finish_2, font="song 20")
    l4 = Label(win2_2, text="vector is:", font="song 20")
    t1 = Text(win2_2, font="song 20", width=30, height=5)
    b2 = Button(win2_2, text="The output transpose matrix", command=cw1, font="song 20")
    b3 = Button(win2_2, text="Outputs the determinant of the matrix", command=cw2, font="song 20")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    b1.grid(row=2, column=0, columnspan=2, pady=20)
    l4.grid(row=3, column=0)
    t1.grid(row=4, column=0, columnspan=2)
    b2.grid(row=5, column=0, columnspan=2, pady=5)
    b3.grid(row=6, column=0, columnspan=2, pady=5)
    win2_2.mainloop()


def finish_3():
    global m
    x = eval(e1.get())
    y = eval(e2.get())
    m = np.ones((x, y))
    t1.insert('end', m)


def f2_3():
    global t1, e1, e2
    win2.destroy()
    win2_2 = tk.Tk()
    win2_2.title("calculator")
    win2_2.geometry("480x550")
    l1 = Label(win2_2, text="The number of rows in this matrix:", font="song 20")
    e1 = Entry(win2_2, font="song 20", width=15)
    l2 = Label(win2_2, text="The number of columns of the matrix:", font="song 20")
    e2 = Entry(win2_2, font="song 20", width=15)
    b1 = Button(win2_2, text="finish", command=finish_3, font="song 20")
    l4 = Label(win2_2, text="vector is:", font="song 20")
    t1 = Text(win2_2, font="song 20", width=30, height=5)
    b2 = Button(win2_2, text="The output transpose matrix", command=cw1, font="song 20")
    b3 = Button(win2_2, text="Outputs the determinant of the matrix", command=cw2, font="song 20")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    b1.grid(row=2, column=0, columnspan=2, pady=20)
    l4.grid(row=3, column=0)
    t1.grid(row=4, column=0, columnspan=2)
    b2.grid(row=5, column=0, columnspan=2, pady=5)
    b3.grid(row=6, column=0, columnspan=2, pady=5)
    win2_2.mainloop()


def finish_4():
    global m
    x = eval(e1.get())
    y = eval(e2.get())
    m = np.empty((x, y), int)
    t1.insert('end', m)


def f2_4():
    global t1, e1, e2
    win2.destroy()
    win2_2 = tk.Tk()
    win2_2.title("calculator")
    win2_2.geometry("480x550")
    l1 = Label(win2_2, text="The number of rows in this matrix:", font="song 20")
    e1 = Entry(win2_2, font="song 20", width=15)
    l2 = Label(win2_2, text="The number of columns of the matrix:", font="song 20")
    e2 = Entry(win2_2, font="song 20", width=15)
    b1 = Button(win2_2, text="finish", command=finish_4, font="song 20")
    l4 = Label(win2_2, text="vector is:", font="song 20")
    t1 = Text(win2_2, font="song 20", width=30, height=5)
    b2 = Button(win2_2, text="The output transpose matrix", command=cw1, font="song 20")
    b3 = Button(win2_2, text="Outputs the determinant of the matrix", command=cw2, font="song 20")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    b1.grid(row=2, column=0, columnspan=2, pady=20)
    l4.grid(row=3, column=0)
    t1.grid(row=4, column=0, columnspan=2)
    b2.grid(row=5, column=0, columnspan=2, pady=5)
    b3.grid(row=6, column=0, columnspan=2, pady=5)
    win2_2.mainloop()


def getmatrix():
    global win2
    # win.destroy()
    win2 = tk.Tk()
    win2.title("calculator")
    win2.geometry("480x550")
    b1 = Button(win2, text="Manual input matrix", command=f2_1, font="song 20")
    b2 = Button(win2, text="Create a random matrix", command=f2_2, font="song 20")
    b3 = Button(win2, text="Create an all-1 matrix", command=f2_3, font="song 20")
    b4 = Button(win2, text="Create an all-0 matrix", command=f2_4, font="song 20")
    b1.pack(pady=20)
    b2.pack(pady=20)
    b3.pack(pady=20)
    b4.pack(pady=20)


# Matrix, vector operation function
def operatemartrix(a, b):
    def finish_11():
        e = e1.get()
        print(e)
        if e == '+':
            try:
                c = np.add(a, b)  # Matrix addition implementation
            except:
                tm.showerror('error', 'Please enter the correct matrix format')
                c = 0
        elif e == '.*':
            try:
                c = np.dot(a, b)  # Matrix multiplication realization
            except:
                tm.showerror('error', 'Please enter the correct matrix format')
                c = 0
        elif e == 'x':
            try:
                c = np.multiply(a, b)  # Multiply the corresponding elements
            except:
                tm.showerror('error', 'Please enter the correct matrix format')
                c = 0
        elif e == '/':
            try:
                c = np.divide(a, b)  # Division implementation of matrix
            except:
                tm.showerror('error', 'Please enter the correct matrix format')
                c = 0
        elif e == '//':
            try:
                c = np.floor_divide(a, b)  # The realization of matrix divisor
            except:
                tm.showerror('error', 'Please enter the correct matrix format')
                c = 0
        elif e == '-':
            try:
                c = np.subtract(a, b)  # Matrix subtraction implementation
            except:
                tm.showerror('error', 'Please enter the correct matrix format')
                c = 0
        elif e == '**':
            try:
                c = np.power(a, b)  # Realization of the power of a matrix
            except:
                tm.showerror('error', 'Please enter the correct matrix format')
                c = 0
        t1.insert('0.0', c)
        return c

    win3_1 = tk.Tk()
    win3_1.title("calculator")
    win3_1.geometry("550x480")
    l1 = Label(win3_1, text="Matrix addition calculation:+", font="song 20")
    l2 = Label(win3_1, text="Matrix multiplication calculation:.*", font="song 20")
    l3 = Label(win3_1, text="Multiplication of corresponding elements:x", font="song 20")
    l4 = Label(win3_1, text="Matrix division calculation:、", font="song 20")
    l5 = Label(win3_1, text="Matrix divisible computation://", font="song 20")
    l6 = Label(win3_1, text="Matrix subtraction calculation:-", font="song 20")
    l7 = Label(win3_1, text="Matrix power calculation:**", font="song 20")
    l8 = Label(win3_1, text="Please enter an operation symbol", font="song 20")
    e1 = Entry(win3_1, font="song 20", width=15)
    b1 = Button(win3_1, text="ensure", command=finish_11, font="song 20")
    l9 = Label(win3_1, text="out put:", font="song 20")
    t1 = Text(win3_1, font="song 20", width=30)
    l1.grid(row=0, column=0)
    l2.grid(row=0, column=1)
    l3.grid(row=1, column=0)
    l4.grid(row=1, column=1)
    l5.grid(row=2, column=0)
    l6.grid(row=2, column=1)
    l7.grid(row=3, column=0)
    l8.grid(row=3, column=1)
    e1.grid(row=4, column=0)
    b1.grid(row=4, column=1)
    l9.grid(row=5, column=0)
    t1.grid(row=6, column=0, columnspan=2)
    win3_1.mainloop()


# Data characteristic value analysis function: divided into input data, calculate the mean value, calculate the variance, calculate the median three functions
def getnumber():
    def tj():
        i = e1.get()
        e1.delete(0, END)
        ls.append(eval(i))  # Write the input data to the list for later data analysis

    def finish():
        e2.insert(0, mean(ls))
        e3.insert(0, variance(ls))
        e4.insert(0, getmedia(ls))

    ls = []
    l1 = Label(win4, text="Enter the data you want to calculate", font="song 20")
    e1 = Entry(win4, font="song 20", width=15)
    b1 = Button(win4, text="ensure", command=tj, font="song 20")
    b2 = Button(win4, text="finish", command=finish, font="song 20")
    l1.grid(row=0, column=0, columnspan=2)
    e1.grid(row=1, column=0, columnspan=2)
    b1.grid(row=2, column=0, pady=10)
    b2.grid(row=2, column=1, pady=10)



