import math                          # Arithmetic operations
from tqdm import tqdm                # Loading screen
import time                          # Loading screen
import matplotlib.pyplot as plt      # Plotting graphs
import numpy as np                   # Plotting graphs

user_name = input("Enter your name: ")

print("Hello ", user_name, " !!!")

# Loading ↓
for x in range(3):
    print('.', end='')
    time.sleep(0.5)
print("")

# Loading ↓
start = input("Enter \"E\" to start the calculator: ")
if start.lower() == "e":
    print("WELCOME TO MTS [Mathematical Tools for Students ]")
    for i in tqdm(range(100),
                  desc="Loading…",
                  ascii=False, ncols=100):
        time.sleep(0.01)
    print("Complete.")
else:
    quit()

# List of operations ↓
cmds = ("""Enter the operation you would like to perform:

⇒ Arithmetic Operations:

• Addition  -------------------------------  [a]
• Subtraction  ----------------------------  [s]
• Multiplication  -------------------------  [m]
• Division  -------------------------------  [d]
• Exponential multiplication  -------------  [exp]
• Percentage  -----------------------------  [%]
• Floor division  -------------------------  [f]
• Modulus  --------------------------------  [mod]
• Factorial  ------------------------------  [f]

⇒ Plotting graphs:
• Line graph  -----------------------------  [lg]
• Quadratic graph  ------------------------  [qg]
• Cubic graph  ----------------------------  [cg]
• Trigonometric graph  --------------------  [tg]

⇒ Relational Operations:
• Check for '>', '<' or '='  --------------  [rel]

⇒ Quadratic equations:
• Quadratic equation solver  --------------  [q]

⇒ Arithmetic / Geometric Progression:
• Operations on AP/GP  --------------------  [ag]


⇒ TERMINATE MTS CALCULATOR ----------------  [quit]
""")

x = 1

# While loop for repeating the program ↓
while x > 0:
    print(cmds)

    operation = input("""Enter the operation you would like to perform ↓
    >>> Enter the characters given in square brackets [] : """)

    # ARITHMETIC OPERATORS ↓

    # Addition:
    if operation.lower() == "a":
        num1 = int(input("Enter the first number (addend 1): "))
        num2 = int(input("Enter the second number (addend 2): "))
        Sum = num1 + num2
        print("The sum of", num1, "and", num2, "is", str(Sum) + ".")

    # Subtraction:
    elif operation.lower() == "s":
        num1 = int(input("Enter the first number (minuend): "))
        num2 = int(input("Enter the second number (subtrahend): "))
        Difference = num1 - num2
        print("The difference of", num1, "and", num2, "is", str(Difference) + ".")

    # Multiplication:
    elif operation.lower() == "m":
        num1 = int(input("Enter the first number (multiplier 1): "))
        num2 = int(input("Enter the second number (multiplier 2): "))
        product = num1 * num2
        print("The product of", num1, "and", num2, "is", str(product) + ".")

    # Division:
    elif operation.lower() == "d":
        num1 = int(input("Enter the first number (dividend): "))
        num2 = int(input("Enter the second number (divisor): "))
        quotient = num1 / num2
        print("The quotient of", num1, "and", num2, "is", str(quotient) + ".")

    # Exponential function:
    elif operation.lower() == "exp":
        num1 = int(input("Enter the first number (base): "))
        num2 = int(input("Enter the second number (exponent): "))
        exp = num1 ** num2
        print("The exponent of", num1, "raised to", num2, "is", str(exp) + ".")

    # Percentage:
    elif operation.lower() == "%":
        num1 = int(input("Enter the first number (numerator): "))
        num2 = int(input("Enter the second number (denominator): "))
        perc = num1 / num2 * 100
        print(num1, "by", num2, "is", str(perc) + "%" + ".")

    # Floor division:
    elif operation.lower() == "f":
        num1 = int(input("Enter the first number (dividend): "))
        num2 = int(input("Enter the second number (divisor): "))
        quotient = num1 // num2
        print("The floor division of", num1, "divided by", num2, "is", str(quotient) + ".")

    # Modulus:
    elif operation.lower() == "mod":
        num1 = int(input("Enter the first number (dividend): "))
        num2 = int(input("Enter the second number (divisor): "))
        remainder = num1 % num2
        print("The remainder when", num1, "is divided by", num2, "is", str(remainder) + ".")

    # Factorial:
    elif operation.lower() == "f":
        num1 = int(input("Enter the number: "))
        factorial = math.factorial(num1)
        print("The factorial of", num1, "is", factorial, ".")

    # PLOTTING GRAPHS

    # Line graph:
    elif operation.lower() == 'lg':
        print("The formula for line graph is: y = mx + c ")
        m = int(input("Enter the value for m: "))
        c = int(input("Enter the value for c: "))
        x_axis = []
        y_axis = []
        for i in range(-100, 100):
            x = i
            y = (x * m) + c
            y_axis.append(y)
            x_axis.append(i)
            plt.plot(x_axis, y_axis, color='green', lw=3)
        plt.title('x-y graph')
        plt.ylabel('y')
        plt.ylim(-100, 100)
        plt.xlabel('x')
        plt.xlim(-100, 100)
        plt.show()

    # Quadratic graph:
    elif operation.lower() == 'qg':
        print("General form of quadratic equation is a𝑥² + b𝑥 + c")
        a = int(input("Input value of a: "))
        b = int(input("Input value of b: "))
        c = int(input("Input value of c: "))
        x_axis = []
        y_axis = []
        for i in range(-100, 100):
            x = i
            y = (a * x ** 2) + (b * x) + c
            y_axis.append(y)
            x_axis.append(i)
            plt.plot(x_axis, y_axis, color='blue', lw=3)
        plt.title('x-y graph')
        plt.ylabel('y')
        plt.ylim(-100, 100)
        plt.xlabel('x')
        plt.xlim(-100, 100)
        plt.show()

    # Cubic graph:
    elif operation.lower() == 'cg':
        print("General form of cubic equation is a𝑥³ + b𝑥² + cx + d")
        a = int(input("Input value of a: "))
        b = int(input("Input value of b: "))
        c = int(input("Input value of c: "))
        d = int(input("Input value of d: "))
        x_axis = []
        y_axis = []
        for j in range(-100, 100):
            x = j
            y = (a * x ** 3) + (b * x ** 2) + (c * x) + d
            if y == 0:
                z = x
            y_axis.append(y)
            x_axis.append(j)
            plt.plot(x_axis, y_axis, color='red', lw=3)
        plt.title('x-y graph')
        plt.ylabel('y')
        plt.ylim(-100, 100)
        plt.xlabel('x')
        plt.xlim(-100, 100)
        plt.show()

    # Trigonometric graphs:
    elif operation.lower() == 'tg':
        trig_operation = input("""
        • Sin  ---------------------------------  [s]
        • Cos  ---------------------------------  [c]
        • Tan  ---------------------------------  [t]
        • Cosec  -------------------------------  [cs]
        • Sec  ---------------------------------  [sc]
        • Cot  ---------------------------------  [ct]

        ⇒ Enter the trigonometric operation you would like to perform: """)

        # Sin graph:
        if trig_operation.lower() == 's':
            x = np.arange(0, 5 * np.pi, 0.1)
            y = np.sin(x)
            plt.title('Sin graph')
            plt.ylabel('y →')
            plt.xlabel('x →')
            plt.plot(x, y, color='red')
            plt.show()

        # Cos graph
        elif trig_operation.lower() == 'c':
            x = np.arange(0, 5 * np.pi, 0.1)
            y = np.cos(x)
            plt.title('Cos graph')
            plt.ylabel('y →')
            plt.xlabel('x →')
            plt.plot(x, y, color='blue')
            plt.show()

        # Tan graph
        elif trig_operation.lower() == 't':
            x = np.arange(0, 5 * np.pi, 0.1)
            y = np.tan(x)
            plt.title('Tan graph')
            plt.ylabel('y →')
            plt.xlabel('x →')
            plt.plot(x, y, color='green')
            plt.show()

        # Cosec graph:
        elif trig_operation.lower() == 'cs':
            x = np.arange(0, 5 * np.pi, 0.1)
            y = np.arcsin(x)
            plt.title('Cosec graph')
            plt.ylabel('y →')
            plt.xlabel('x →')
            plt.plot(x, y, color='red')
            plt.show()

        # Sec graph:
        elif trig_operation.lower() == 'sc':
            x = np.arange(0, 5 * np.pi, 0.1)
            y = np.arccos(x)
            plt.title('Sec graph')
            plt.ylabel('y →')
            plt.xlabel('x →')
            plt.plot(x, y, color='blue')
            plt.show()

        # Cot graph:
        elif trig_operation.lower() == 'ct':
            x = np.arange(0, 5 * np.pi, 0.1)
            y = np.arctan(x)
            plt.title('Cot graph')
            plt.ylabel('y →')
            plt.xlabel('x →')
            plt.plot(x, y, color='green')
            plt.show()

    # RELATIONAL OPERATORS

    elif operation.lower() == "rel":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num1 > num2:
            print(num1, "is greater than", str(num2) + ".")
        elif num1 < num2:
            print(num1, " is less than ", str(num2) + ".")
        else:
            print(num1, " is equal to ", str(num2) + ".")

    # QUADRATIC EQ. SOLVER

    elif operation.lower() == 'q':
        print("General form of quadratic equation is a𝑥^2 + b𝑥 + c")
        a = int(input("Input value of a: "))
        b = int(input("Input value of b: "))
        c = int(input("Input value of c: "))
        print(str(a) + "𝑥²+", str(b), "𝑥+", c, "is your quadratic equation.")
        d = (b ** 2) - (4 * a * c)
        if d < 0:
            print("The roots of the equation", str(a) + "𝑥² +", str(b), "𝑥 +", c, "are", "[" + str(-b),
                  "+ √" + "(" + str(d) + ")" + "] /", 2 * a, " and ", "[" + str(-b),
                  "- √" + "(" + str(d) + ")" + "] /", 2 * a)
            print("The roots are Imaginary.")
        elif d > 0:
            x_1 = (-b + (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
            x_2 = (-b - (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
            print("The roots of the equation", str(a) + "𝑥² +", str(b), "𝑥 +", c, " are ", x_1, " and ", x_2, )
            print("The roots are real.")
        elif d == 0:
            print("Both the roots are equal and they are: ", (-b) / (2 * a))

    # AP / GP

    elif operation.lower() == 'ag':
        print("""
        Arithmetic progression  ---------------  [ap]
        Geometric progression  ----------------  [gp]
        .""")

        # Arithmetic progression:
        choice_ap_gp = input("Do you want to find A.P or G.P: ")
        if choice_ap_gp.lower() == 'ap':
            print("""
            Finding the index (given number) --------------- [i]
            Finding the number (given index) --------------- [n]
            Sum of the A.P  ------------------------------- [s]
            .""")
            choice_ap = input("Enter the operation you would like to perform on ap: ")
            if choice_ap.lower() == 'i':
                a_1 = float(input("Enter the first element of the A.P: "))
                d = float(input("Enter the common difference of the A.P: "))
                n = float(input("Enter the number you want to find the index for: "))
                print("The number", str(n) + " is the", str((n - a_1 + d) / d) + " th term.")
            elif choice_ap.lower() == 'n':
                a_1 = float(input("Enter the first element of the A.P: "))
                d = float(input("Enter the common difference of the A.P: "))
                n = int(input("Enter the index: "))
                print("The", str(n) + "th", "term of the ap is:", str(a_1 + ((n - 1) * d)) + ".")
            elif choice_ap.lower() == 's':
                a_1 = float(input("Enter the first element of the A.P: "))
                d = float(input("Enter the common difference of the A.P: "))
                n = int(input("Enter the number of terms in the A.P: "))
                print("The sum of the A.P up to", n, "terms is", str((n / 2) * ((2 * a_1) + ((n - 1) * d))) + ".")

        # Geometric progression:
        elif choice_ap_gp.lower() == 'gp':
            print("""
            Finding the index (given number)  ----------------  [i]
            Finding the number (given index)  ----------------  [n]
            Finding the common ratio  ------------------------  [cr]
            Sum of the G.P  ----------------------------------  [si]
            .""")
            choice_gp = input("Enter the operation you would like to perform on the G.P: ")
            if choice_gp.lower() == 'i':
                a = float(input("Enter the first element of the G.P: "))
                cr = float(input("Enter the common ratio: "))
                tn = float(input("Enter the number you want to find the index for: "))
                if tn < a:
                    print("The number cannot be smaller than the first term.")
                else:
                    print("The index of", tn, "is", str(int((math.log(tn) / math.log(a * cr)) + 1)) + ".")

            elif choice_gp.lower() == 'n':
                a = float(input("Enter the first element of the G.P: "))
                cr = float(input("Enter the common ratio: "))
                n = int(input("Enter the index of the number you want to find: "))
                if n <= 0:
                    print("Index cannot be less than or equal to 0.")
                else:
                    print("The number present in the index", n, "is", str(a * (cr ** (n - 1))) + ".")
            elif choice_gp.lower() == 'cr':
                a = float(input("Enter the first element of the G.P: "))
                tn = float(input("Enter the nth number: "))
                n = int(input("Enter the index of the above entered number: "))
                print("The common ratio of the G.P. is", (tn / a) ** (1 / (n - 1)))
            elif choice_gp.lower() == 'si':
                a = float(input("Enter the first element of the G.P: "))
                cr = float(input("Enter the common ratio: "))
                if cr > 1:
                    n = int(input("Enter the index of the nth term to find sum: "))
                    print("Sum of", n, "terms of the G.P. is", str((a * (1 - (cr ** n))) / (1 - cr)) + ".")
                elif cr < 1:
                    print("Sum of infinite terms of the G.P. is", str(a / (1 - cr)) + ".")
                else:
                    print("Common ratio cannot be 1")

    print("")

    # Calculator loop
    start_again = input("Do you want to restart MTS? [y/n]: ")
    if start_again.lower() == "y":
        print("Restarting", end='')
        for x in range(3):
            print('.', end='')
            time.sleep(0.5)
        end = ''
    elif start_again.lower() == "n":
        print("Thank you. Have a nice day")
        x = 0
    else:
        print("Thank you. Have a nice day")
        x = 0
