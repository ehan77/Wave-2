# Inputs

import math

aVALUE = int(input("Enter the A value in a quadratic equation: "))
bVALUE = int(input("Enter the B value in a quadratic equation: "))
cVALUE = int(input("Enter the C value in a quadratic equation: "))

discriminant = bVALUE ** 2 - 4 * aVALUE * cVALUE

if discriminant < 0 :
    print("This equation has 0 roots.")
elif discriminant == 0 :
    print("This equation has 1 real root.")
elif discriminant > 0 :
    firstroot = ( -bVALUE + math.sqrt(discriminant) ) / ( 2 * aVALUE )
    secndroot = ( -bVALUE - math.sqrt(discriminant) ) / ( 2 * aVALUE )
    print("This equation has 2 real roots: " , firstroot , "and" , secndroot )