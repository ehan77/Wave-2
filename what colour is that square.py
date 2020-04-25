# Inputs

print("Position of a square on a chess board range from a-h and 1-8.")

blackLETTER = ['a' , 'c' , 'e' , 'g']
whiteLETTER = ['b' , 'd' , 'f' , 'h']
blackNUMBER = ['1' , '3' , '5' , '7']
whiteNUMBER = ['2' , '4' , '6' , '8']

posLETTER = input("Enter a position's letter : ") # pos means position
posNUMBER = input("Enter a position's number : ")

if posLETTER in blackLETTER and posNUMBER in blackNUMBER :
    print("The square is black.")
elif posLETTER in whiteLETTER and posNUMBER in whiteNUMBER :
    print("The square is black.")
elif posLETTER in blackLETTER and posNUMBER in whiteNUMBER :
    print("The square is white.")
elif posLETTER in whiteLETTER and posNUMBER in blackNUMBER :
    print("The square is white.")