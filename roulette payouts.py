# Inputs

import time
import random

green = ['0' , '00']
red = ['1' , '3' , '5' , '7' , '9' , '12' , '14' , '16' , '18' , '19' , '21' , '23' , '25' , '27' , '30' , '32' , '34' , '36']
redNUM = ['1' , '3' , '5' , '7' , '9' , '12' , '14' , '16' , '18' , '19' , '21' , '23' , '25' , '27' , '30' , '32' , '34' , '36']
black = ['2' , '4' , '6' , '8' , '10' , '11' , '13' , '15' , '17' , '20' , '22' , '24' , '26' , '28' , '29' , '31' , '33' , '35']
blackNUM = ['2' , '4' , '6' , '8' , '10' , '11' , '13' , '15' , '17' , '20' , '22' , '24' , '26' , '28' , '29' , '31' , '33' , '35']
even = ['2' , '4' , '6' , '8' , '10' , '12' , '14' , '16' , '18' , '20' , '22' , '24' , '26' , '28' , '30' , '32' , '34' , '36']
odd = ['1' , '3' , '5' , '7' , '9' , '11' , '13' , '15' , '17' , '19' , '21' , '23' , '25' , '27' , '29' , '31' , '33' , '35']
set_one = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18']
set_two = ['19' , '20' , '21' , '22' , '23' , '24' , '25' , '26' , '27' , '28' , '29' , '30' , '31' , '32' , '33' , '34' , '35' , '36']

print("Welcome to Roulette Payouts!")
print('\n')
print("Press [Enter] to spin the wheel.")
x = input()
if x == '':
    print("The roulette is spinning...")
    time.sleep(3)
    spin = str(random.randint(0 , 36))
    print(spin)
    if spin in green :
        print("Pay 0 or 00.")
    elif spin in red and spin in redNUM and spin in even and spin in set_one :
        print("Pay" , spin , ", \n" , "Pay Red, \n Pay Even, \n Pay 1-18.")
    elif spin in red and spin in redNUM and spin in odd and spin in set_one :
        print("Pay" , spin , ", \n" , "Pay Red, \n Pay Odd, \n Pay 1-18.")
    elif spin in red and spin in redNUM and spin in even and spin in set_two :
        print("Pay" , spin , ", \n" , "Pay Red, \n Pay Even, \n Pay 19-36.")
    elif spin in red and spin in redNUM and spin in odd and spin in set_two :
        print("Pay" , spin , ", \n" , "Pay Red, \n Pay Odd, \n Pay 19-36.")
    elif spin in black and spin in blackNUM and spin in even and spin in set_one :
        print("Pay" , spin , ", \n" , "Pay Black, \n Pay Even, \n Pay 1-18.")
    elif spin in black and spin in blackNUM and spin in odd and spin in set_one : 
        print("Pay" , spin , ", \n" , "Pay Black, \n Pay Odd, \n Pay 1-18.")
    elif spin in black and spin in blackNUM and spin in even and spin in set_two :
        print("Pay" , spin , ", \n" , "Pay Black, \n Pay Even, \n Pay 19-36.")
    elif spin in black and spin in blackNUM and spin in odd and spin in set_two :
        print("Pay" , spin , ", \n" , "Pay Black, \n Pay Odd, \n Pay 19-36.")
    else :
        print("Try again!")