import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
from scipy import linalg


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
