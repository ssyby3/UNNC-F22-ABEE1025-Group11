import numpy as np
def get_solar_heat_gain_coefficient(theata,weather,p):
    coefficient=np.sin(theata)*weather*p*0.87
    return coefficient
def main():
    print('1.SimpleWindow:DOUBLE PANE WINDOW')
    print("2.SimpleWindow:SINGLE PANE WINDOW")
    kind=input("please choose what the kind of your window:")
    if kind =='1':
        print("1.Thermal Resistance & U")
        print("2.solar heat gain coefficient")
        #control = input("Please input parameter which you want to calculate")
        print("Please input the original Parameters:")
        theata = eval(input("The Angle of the window and the light"))
        wheather_name = input("1.sunny  2.cloudy  3.rainy")
        if wheather_name == '1':
            wheather = 1
        elif wheather_name == '2':
            wheather = 0.8
        elif wheather_name == '3':
            wheather = 0.6
        p = 1 - eval(input("The density of the surrounding buildings (0.1~0.9)"))
        coefficient = get_solar_heat_gain_coefficient(theata, wheather, p)
        print("your window:DOUBLE PANE WINDOW")
        print("coefficent : {}".format(coefficient))
    elif kind == '2':
        print("Please input the original Parameters:")
        theata = eval(input("The Angle of the window and the light"))
        wheather_name = input("1.sunny  2.cloudy  3.rainy")
        if wheather_name == '1':
            wheather = 1
        elif wheather_name == '2':
            wheather = 0.8
        elif wheather_name == '3':
            wheather = 0.6
        p = 1 - eval(input("The density of the surrounding buildings (0.1~0.9)"))
        coefficient = get_solar_heat_gain_coefficient(theata, wheather, p)
        print("your window:SINGLE PANE WINDOW")
        print("coefficent : {}".format(coefficient))
main()