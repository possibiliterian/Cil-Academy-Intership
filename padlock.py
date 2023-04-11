import os
os.system("cls")

import time


print(" _____________WELCOME TO THE PADLOCK CHALLENGE____________ " )

print("WHICH OF THE PADLOCK CODE CHALLENGE DO YOU NEED AN ANSWER TO: ")
print("1. pad1")
print("2. pad2")
print("3. pad3")
print("4. pad4")
print("5. pad5")


def pad_1():
    code = 0
    for i in range(1,41):
        code = code + i
        
    print("Code:")
    print(code)
    return

    
def pad_2():
    code = 0
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
      
                if (digit1 < digit2) and (digit2 < digit3):
                    code +=1
    print("Code:")
    print(code)
    return
       

def pad_3():
    code = 0
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if (digit1%2 == 0) and (digit2%2 == 0) and (digit3%2 == 0):
                    code +=1
    print("Code:")
    print(code)
    return  


def pad_4():
    code = 0

    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if (digit1 + digit2 +digit3) %2 != 1:
                    
                    code +=1

        
    print("Code:")
    print(code)
    return



def pad_5():
    code = 0

    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if (digit1 == digit2) or (digit1 == digit3) or (digit2 == digit3):
                    code +=1

    print("Code:")
    print(code)
    return





while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

 # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            '''print("WHICH OF THE PADLOCK CODE CHALLENGE DO YOU NEED AN ANSWER TO: ")
            print("1. pad1")
            print("2. pad2")
            print("3. pad3")
            print("4. pad4")
            print("5. pad5")'''
            
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue




    # check if choice is one of the four options
        if choice in ('1', '2', '3', '4' , '5'):
     
            if choice == '1':
                pad_1()

            elif choice == '2':
                pad_2()

            elif choice == '3':
                pad_3()
        
            elif choice == '4':
                pad_4()
        
            elif choice == '5':
                pad_5()
            
            
        # check if user wants another calculation
        # break the while loop if answer is no
        next_solution = input("Will you like to check another solution ? (yes/no): ")
        if next_solution == "no":
          break
    else:
        print("Invalid Input")
        
        
        

