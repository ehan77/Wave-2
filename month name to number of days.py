# Inputs

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

nameMONTH = input("Enter a month: ")

if nameMONTH == "February" : 
    print("There are 28 or 29 days in this month.")
elif nameMONTH in ("January", "March", "May", "July", "August", "October", "December") :
    print("There are 31 days in this month.")
elif nameMONTH in ("April", "June", "September", "November") :
    print("There are 30 days in this month.")