# Lam Thong Wan (S10275182A) – IM02 

import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

if a == 0:
    print("Value of a cannot be zero!")

else:
    x1_numerator = math.sqrt(b**2 - 4*a*c)
    x1_denominator = 2*a
    x1 = -b - (x1_numerator/x1_denominator)

    x2_numerator = math.sqrt(b**2 - 4*a*c)
    x2_denominator = 2*a
    x2 = -b + (x1_numerator/x1_denominator)

    print(f"The roots of the equation are {x1:.4f} and {x2:.4f}")
