import random
import ctypes
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20

#number of points for each category
rich = 2
bow = 10
lobster = 10
moon = 10
sandwich = 10
blueberry = 12
strawberry = 12
cranberry = 12
homeless = 4
mad_face = 9
pickle = 9
x = [rich, bow, lobster, moon, sandwich, blueberry, strawberry, cranberry, homeless, mad_face, pickle]

#sets the results into an array from index 0 to 2
var = [0,1,2]

#function to find which number range the likelyhood of getting each category will be (the ones that have a higher chance to get will be a larger range of numbers)
def getResults():
    i = 0
    #will iterate 3 times since there are 3 outputs executed per spin
    while i <= 2: 
        #calculates a random number between 1 and 100
        randomNum = random.randint(0,100)
        print(randomNum)
        if 1 <= randomNum and randomNum <= 2:
            print("rich")
            #sets array "var[i]" to a certain number (each number represents a category)
            var[i] = 1
        #depending on which range the random number falls in will determine the category you get
        elif 3 <= randomNum and randomNum <= 12:
            print("bow")
            var[i] = 2
        elif 13 <= randomNum and randomNum <= 22:
            print("lobster")
            var[i] = 3
        elif 23 <= randomNum and randomNum <= 32:
            print("moon")
            var[i] = 4
        elif 33 <= randomNum and randomNum <= 42:
            print("sandwich")
            var[i] = 5
        elif 43 <= randomNum and randomNum <= 54:
            print("blueberry")
            var[i] = 6
        elif 55 <= randomNum and randomNum <= 66:
            print("strawberry")
            var[i] = 7
        elif 67 <= randomNum and randomNum <= 78:
            print("cranberry")
            var[i] = 8
        elif 79 <= randomNum and randomNum <= 82:
            print("homeless")
            var[i] = 9
        elif 83 <= randomNum and randomNum <= 91:
            print("mad_face")
            var[i] = 10
        elif 92 <= randomNum and randomNum <= 100:
            print("pickle")
            var[i] = 11
        i += 1
    #returns the array
    return var


#category assignation
#good ones
""" rich = 1
bow = 2
lobster = 3
moon = 4
sandwich = 5
"""
#neutral
"""
blueberry = 6
strawberry = 7
cranberry = 8
"""
#bad ones
"""
homeless = 9
mad_face = 10
pickle = 11
"""

#this function determines the amount of money earned or lose depending on whihc sudo generated number you get
def moneyEarned():
    money = 0
    # if statements for "unlucky" options
    if  9 <= var[0] <= 11 or 9 <= var[1] <= 11 or 9 <= var[2] <= 11:
        #if only 1 statement is true
        if var.count(9) == 1: 
            money = -1000
            print("lose $1000")
        #if 2 are true
        elif var.count(9) == 2:
            print("lose $2000")
            money = -2000
        #if 3 are true
        elif var.count(9) == 3:
            print("lose $5000")
            money = -5000
        # ie if either one are present
        elif var.count(10) + var.count(11) == 1:
            print("lose $40")   
            money = -40
        # ie if both are present
        elif var.count(10) + var.count(11) == 2:
            print("lose $50")  
            money = -50  
        # ie if 3 of either these are present
        elif var.count(10) + var.count(11) == 3:
            print("lose $60")
            money = -60
    #if statements for "lucky" options
    elif 1 <= var[0] <= 5 or 1 <= var[1] <= 5 or 1 <= var[2] <= 5:
        if var.count(1) == 1:
            print("gain $1000")
            money = 1000
        elif var.count(1) == 2:
            print("gain $2000")
            money = 2000
        elif var.count(1) == 3:
            print("gain $3000")
            money = 3000
        elif var.count(2) + var.count(3) + var.count(4) + var.count(5) == 1:
            print("gain $50")
            money = 50
        elif var.count(2) + var.count(3) + var.count(4) + var.count(5) == 2:
            print("gain $60")
            money = 60
        elif var.count(2) + var.count(3) + var.count(4) + var.count(5) == 3:
            print("gain $70")
            money = 70
    elif 6 <= var[0] <= 8 or 6 <= var[1] <= 8 or 6 <= var[2] <= 8:
        print("no money gained")
    return money
