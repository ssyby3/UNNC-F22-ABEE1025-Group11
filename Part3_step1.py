
def get_Thermal_resistance(area,thickness,lamda):
    Thermal_resistance=area*thickness/lamda
    return Thermal_resistance

def get_U(R):
    U=1/R
    return U

def main():
    print('1.SimpleWindow:DOUBLE PANE WINDOW')
    print("2.SimpleWindow:SINGLE PANE WINDOW")
    kind=input("please choose what the kind of your window:")

    if kind =='1':
       # print("1.Thermal Resistance & U")
        #print("2.solar heat gain coefficient")
        control = input("Please input parameter which you want to calculate")

        if control=='1':
            print("Please input the original Parameters:")
            area =eval(input("The area of your window"))
            thickness =2 * eval(input("The thickness of glass"))
            lamda = eval(input("choose the thermal conductivity  range:(0.7-1.3)"))
            R=get_Thermal_resistance(area,thickness,lamda)
            U=get_U(R)

            print("your window:DOUBLE PANE WINDOW")
            print("Thermal Resistance :{}".format(R))
            print("U : {}".format(U))

    elif kind =='2':
       # print("1.Thermal Resistance & U")
        #print("2.solar heat gain coefficient")
        control = input("Please input parameter which you want to calculate")

        if control == '1':
            print("Please input the original Parameters:")
            area = eval(input("The area of your window"))
            thickness = eval(input("The thickness of glass"))
            lamda = eval(input("choose the thermal conductivity  range:(0.7-1.3)"))

            R = get_Thermal_resistance(area, thickness, lamda)
            U = get_U(R)

            print("your window:DOUBLE PANE WINDOW")
            print("Thermal Resistance :{}".format(R))
            print("U : {}".format(U))