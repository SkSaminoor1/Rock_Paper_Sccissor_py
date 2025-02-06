import random

print("This is a Guessing Game\n")
system_in=random.randint(0,50)
i=0
while(True):
    user_in=int(input("Enter your guess 0-50:"))
    if(user_in==system_in):
        print("Your Guess is right\n")
        print(f"System guess is {system_in}")
        print(f"you have tried {i} times")
        break
    elif(user_in<system_in):
        print("Enter larger value\n")
        i+=1
    elif(user_in>system_in and user_in<50):
        print("Enter smaller value\n")
        i+=1
    else:
        print("entered value is out of rannge\n")
        break