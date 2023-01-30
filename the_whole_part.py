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


def mean(numbers):
    ans = 0
    for i in numbers:  # Sum the data in the list and calculate the average value according to the length
        ans = ans + i
    return ans / len(numbers)


def variance(numbers):
    ans = 0
    for nums in numbers:
        ans += pow(nums - mean(numbers), 2) / len(numbers)
    return ans  # Calculate the variance of the list data using the result of the mean function


def getmedia(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        i = len(numbers) // 2 - 1  # Sort the data in the list to find the median
        mid = (numbers[i] + numbers[i + 1]) / 2
    elif len(numbers) % 2 == 1:
        i = (len(numbers)) // 2
        mid = numbers[i]
    return mid


def getcharacter():  # Write the above three functions into a total function: denoted as calculating data eigenvalues
    global win4, e2, e3, e4
    win4 = tk.Tk()
    win4.title("calculator")
    win4.geometry("550x480")
    getnumber()
    l2 = Label(win4, text="The average value is:", font="song 20")
    e2 = Entry(win4, font="song 20", width=15)
    l3 = Label(win4, text="The variance is:", font="song 20")
    e3 = Entry(win4, font="song 20", width=15)
    l4 = Label(win4, text="The median is:", font="song 20")
    e4 = Entry(win4, font="song 20", width=15)
    l2.grid(row=3, column=0)
    e2.grid(row=3, column=1)
    l3.grid(row=4, column=0)
    e3.grid(row=4, column=1)
    l4.grid(row=5, column=0)
    e4.grid(row=5, column=1)
    win4.mainloop()


# Drawing function
# Plot sine function
def finish_12():
    w = eval(e1_1.get())
    A = eval(e2_1.get())
    d = eval(e3_1.get())
    y = A * np.sin(w * np.pi * x + d)
    plt.plot(x, y)
    plt.show()
    print("Image generation success")

def xx():
    global x
    x = l
def figuresin():
    global e1_1, e2_1, e3_1
    win5_1 = tk.Tk()
    win5_1.title("calculator")
    win5_1.geometry("550x480")
    b2 = Button(win5_1, text="Set the domain of definition", command=getvector, font="song 20")
    b3 = Button(win5_1, text="setup completed", command=xx, font="song 20")
    l1 = Label(win5_1, text="Set frequency:", font="song 20")
    e1_1 = Entry(win5_1, font="song 20", width=15)
    l2 = Label(win5_1, text="Set amplitude:", font="song 20")
    e2_1 = Entry(win5_1, font="song 20", width=15)
    l3 = Label(win5_1, text="Set phase:", font="song 20")
    e3_1 = Entry(win5_1, font="song 20", width=15)
    b1 = Button(win5_1, text="finish", command=finish_12, font="song 20")
    l1.grid(row=1, column=0)
    e1_1.grid(row=1, column=1)
    l2.grid(row=2, column=0)
    e2_1.grid(row=2, column=1)
    l3.grid(row=3, column=0)
    e3_1.grid(row=3, column=1)
    b1.grid(row=4, column=0, columnspan=2)
    b2.grid(row=0, column=0, pady=10)
    b3.grid(row=0, column=1, pady=10)
    win5_1.mainloop()

def finish_13():
    w = eval(e1_1.get())
    A = eval(e2_1.get())
    d = eval(e3_1.get())
    y = A * np.cos(w * np.pi * x + d)
    plt.plot(x, y)
    plt.show()
    print("Image generation success")

# Plot the cosine function
def figurecos():
    global e1_1, e2_1, e3_1
    win5_1 = tk.Tk()
    win5_1.title("calculator")
    win5_1.geometry("550x480")
    b2 = Button(win5_1, text="Set the domain of definition", command=getvector, font="song 20")
    b3 = Button(win5_1, text="setup completed", command=xx, font="song 20")
    l1 = Label(win5_1, text="Set frequency:", font="song 20")
    e1_1 = Entry(win5_1, font="song 20", width=15)
    l2 = Label(win5_1, text="Set amplitude:", font="song 20")
    e2_1 = Entry(win5_1, font="song 20", width=15)
    l3 = Label(win5_1, text="Set phase:", font="song 20")
    e3_1 = Entry(win5_1, font="song 20", width=15)
    b1 = Button(win5_1, text="finish", command=finish_13, font="song 20")
    l1.grid(row=1, column=0)
    e1_1.grid(row=1, column=1)
    l2.grid(row=2, column=0)
    e2_1.grid(row=2, column=1)
    l3.grid(row=3, column=0)
    e3_1.grid(row=3, column=1)
    b1.grid(row=4, column=0, columnspan=2)
    b2.grid(row=0, column=0, pady=10)
    b3.grid(row=0, column=1, pady=10)
    win5_1.mainloop()

def finish_14():
    w = eval(e1_1.get())
    A = eval(e2_1.get())
    d = eval(e3_1.get())
    y = 1 / pow(2 * np.pi, 0.5) * np.exp(-1 * pow(x, 2) / 2)
    plt.plot(x, y)
    plt.show()
    print("Image generation success")

# Plot a standard normal distribution
def figurenormal_distribution():
    global e1_1, e2_1, e3_1
    win5_1 = tk.Tk()
    win5_1.title("calculator")  # title
    win5_1.geometry("550x480")
    b2 = Button(win5_1, text="Set the domain of definition", command=getvector, font="song 20")
    b3 = Button(win5_1, text="setup completed", command=xx, font="song 20")
    l1 = Label(win5_1, text="Set frequency:", font="song 20")
    e1_1 = Entry(win5_1, font="song 20", width=15)
    l2 = Label(win5_1, text="Set amplitude:", font="song 20")
    e2_1 = Entry(win5_1, font="song 20", width=15)
    l3 = Label(win5_1, text="Set phase:", font="song 20")
    e3_1 = Entry(win5_1, font="song 20", width=15)
    b1 = Button(win5_1, text="finish", command=finish_14, font="song 20")
    l1.grid(row=1, column=0)
    e1_1.grid(row=1, column=1)
    l2.grid(row=2, column=0)
    e2_1.grid(row=2, column=1)
    l3.grid(row=3, column=0)
    e3_1.grid(row=3, column=1)
    b1.grid(row=4, column=0, columnspan=2)
    b2.grid(row=0, column=0, pady=10)
    b3.grid(row=0, column=1, pady=10)
    win5_1.mainloop()



# Temperature unit conversion
def tempshift():
    def zh():
        TempStr = e1.get()
        if TempStr[-1] in ["C", "c"]:
            F = (eval(TempStr[0:-1]) * 1.8 + 32)
            t1.insert('0.0', 'The converted temperature is{:.2f}F'.format(F))
        elif TempStr[-1] in ["F", "f"]:
            C = ((eval(TempStr[0:-1]) - 32) / 1.8)
            t1.insert('0.0', 'The converted temperature is{:.2f}C'.format(C))
        else:
            print("Input format error")

    win6 = tk.Tk()
    win6.title("calculator")  # title
    win6.geometry("550x480")
    l1 = Label(win6, text="Please enter the signed temperature:", font="song 20")
    e1 = Entry(win6, font="song 20", width=20)
    b1 = Button(win6, text="shift", command=zh, font="song 20")
    l2 = Label(win6, text="out put：", font="song 20")
    t1 = Text(win6, font="song 20", width=30, height=5)
    l1.grid(row=0, column=0, columnspan=2)
    e1.grid(row=1, column=0)
    b1.grid(row=1, column=1, padx=10)
    l2.grid(row=2, column=0)
    t1.grid(row=3, column=0, columnspan=2)
    win6.mainloop()

class Complex:
    def __init__(self, real, virtual):
        self.real = real
        self.virtual = virtual

    def __add__(self, other):
        return Complex(self.real + other.real, self.virtual + other.virtual)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.virtual - other.virtual)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.virtual * other.virtual,
                       self.real * other.virtual + other.real * self.virtual)

    def __truediv__(self, other):
        a = self.real
        b = self.virtual
        c = other.real
        d = other.virtual

        devide = c ** 2 + d ** 2
        return Complex((a * c + b * d) / devide, (b * c - a * d) / devide)

    def __repr__(self):
        return "%s + %si" % (self.real, self.virtual)


def qr_3():
    sign = int(t1.get('0.0', END))
    t1.delete('0.0', END)
    if sign == 0:
        l2 = Label(win8_1, text="The sum is equal to：", font="song 20")
        e2 = Entry(win8_1, font="song 20", width=15)
        l2.grid(row=3, column=0)
        e2.grid(row=3, column=1)
        e2.insert(0, c1 + c2)
    elif sign == 1:
        l2 = Label(win8_1, text="So the subtraction is going to be：", font="song 20")
        e2 = Entry(win8_1, font="song 20", width=15)
        l2.grid(row=3, column=0)
        e2.grid(row=3, column=1)
        e2.insert(0, c1 - c2)
    elif sign == 2:
        l2 = Label(win8_1, text="The result of the multiplication is：", font="song 20")
        e2 = Entry(win8_1, font="song 20", width=15)
        l2.grid(row=3, column=0)
        e2.grid(row=3, column=1)
        e2.insert(0, c1 * c2)
    elif sign == 3:
        l2 = Label(win8_1, text="The result of the division is：", font="song 20")
        e2 = Entry(win8_1, font="song 20", width=15)
        l2.grid(row=3, column=0)
        e2.grid(row=3, column=1)
        e2.insert(0, c1 / c2)


def qr_2():
    global c1, c2, t1, win8_1
    a = int(e2.get())
    b = int(e3.get())
    c = int(e5.get())
    d = int(e6.get())
    c1 = Complex(a, b)
    c2 = Complex(c, d)
    win8_1 = tk.Tk()
    win8_1.title("calculator")  # title
    win8_1.geometry("550x480")
    l1 = Label(win8_1, text="===The operation you want to perform===\naddition(0);subtraction(1);multiplication(2);Division(3);exit(4)", font="song 20")
    t1 = Text(win8_1, font="song 20", width=30, height=3)
    b1 = Button(win8_1, text="确认", command=qr_3, font="song 20")
    l1.grid(row=0, column=0, columnspan=2)
    t1.grid(row=1, column=0, columnspan=2)
    b1.grid(row=2, column=0, columnspan=2)


def complex():
    global win8, e2, e3, e5, e6
    win8 = tk.Tk()
    win8.title("calculator")  # title
    win8.geometry("550x480")
    l1 = Label(win8, text="===Enter the first complex number===", font="song 20")
    l2 = Label(win8, text="real part：", font="song 20")
    e2 = Entry(win8, font="song 20", width=15)
    l3 = Label(win8, text="imaginary part：", font="song 20")
    e3 = Entry(win8, font="song 20", width=15)
    l4 = Label(win8, text="===Enter the next complex number===", font="song 20")
    l5 = Label(win8, text="real part：", font="song 20")
    e5 = Entry(win8, font="song 20", width=15)
    l6 = Label(win8, text="imaginary part：", font="song 20")
    e6 = Entry(win8, font="song 20", width=15)
    b1 = Button(win8, text="ensure", command=qr_2, font="song 20")
    l1.grid(row=0, column=0, columnspan=2)
    l2.grid(row=1, column=0, padx=10)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0, padx=10)
    e3.grid(row=2, column=1)
    l4.grid(row=3, column=0, columnspan=2)
    l5.grid(row=4, column=0, padx=10)
    e5.grid(row=4, column=1)
    l6.grid(row=5, column=0, padx=10)
    e6.grid(row=5, column=1)
    b1.grid(row=6, column=0, columnspan=2)

    win8.mainloop()


def f1():
    getvector()


def f2():
    getmatrix()


def m1g():
    getmatrix()


def m2g():
    getmatrix()


def m1wc():
    global m1
    m1 = m
    print("m1 is:\n{}".format(m1))


def m2wc():
    global m2
    m2 = m
    print("m2 is:\n{}".format(m2))


def f3():
    def js():
        operatemartrix(m1, m2)

    win3 = tk.Tk()
    win3.title("calculator")  # title
    win3.geometry("480x550")
    l1 = Label(win3, text="Please enter the calculated matrix_1", font="song 20")
    b1 = Button(win3, text="To choose", command=m1g, font="song 20")
    l2 = Label(win3, text="Please enter the calculated matrix_2", font="song 20")
    b2 = Button(win3, text="To choose", command=m2g, font="song 20")
    b3 = Button(win3, text="finish", command=js, font="song 20")
    b4 = Button(win3, text="Select complete", command=m1wc, font="song 20")
    b5 = Button(win3, text="Select complete", command=m2wc, font="song 20")
    l1.grid(row=0, column=0, columnspan=2)
    l2.grid(row=2, column=0, columnspan=2)
    b1.grid(row=1, column=0)
    b2.grid(row=3, column=0)
    b3.grid(row=4, column=0, columnspan=2)
    b4.grid(row=1, column=1)
    b5.grid(row=3, column=1)
    win3.mainloop()


def f4():
    getcharacter()


def f5():
    win5 = tk.Tk()
    win5.title("calculator")  # title
    win5.geometry("480x550")
    b1 = Button(win5, text="Sine function graph", command=figuresin, font="song 20")
    b2 = Button(win5, text="Cosine function graph", command=figurecos, font="song 20")
    b3 = Button(win5, text="Standard normal distribution graph", command=figurenormal_distribution, font="song 20")
    b1.pack(pady=20)
    b2.pack(pady=20)
    b3.pack(pady=20)
    win5.mainloop()

def f6():
    tempshift()

def f7():
    complex()


# The main program, the method will be called selectively
def main():
    global win
    win = tk.Tk()
    win.title("calculator")  # title
    win.geometry("480x550")
    b1 = Button(win, text="Generating vector", command=f1, font="song 20")
    b2 = Button(win, text="generator matrix", command=f2, font="song 20")
    b3 = Button(win, text="Matrix/vector computation", command=f3, font="song 20")
    b4 = Button(win, text="Data eigenvalue analysis", command=f4, font="song 20")
    b5 = Button(win, text="Draw function image", command=f5, font="song 20")
    b6 = Button(win, text="Automatic conversion of temperature units", command=f6, font="song 20")
    b7 = Button(win, text="Complex operation", command=f7, font="song 20")
    b1.grid(row=0, column=0, padx=5, pady=20)
    b2.grid(row=0, column=1, padx=5, pady=20)
    b3.grid(row=1, column=0, padx=5, pady=20)
    b4.grid(row=1, column=1, padx=5, pady=20)
    b5.grid(row=2, column=0, padx=5, pady=20)
    b6.grid(row=2, column=1, padx=5, pady=20)
    b7.grid(row=3, column=0, padx=5, pady=20)
    win.mainloop()  # Enter the main event loop, which displays the form object.

main()
