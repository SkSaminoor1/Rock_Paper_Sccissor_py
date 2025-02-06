import random

a=[1,2,3]
i=0
game={1:"Rock", 2:"Paper", 3:"Sccissor"}
print("Enter 1 for Rock")
print("Enter 2 for Paper")
print("Enter 3 for Scissor")
print("Exit 4\n")

while(True):

    
    user=int(input())

    pc=random.choice(a)

    if(user==pc):
        
        print("Match Draw\n")
        i=i+1
    elif(user==1 and pc==2):
        print(f"YOur choose {game[1]} and Pc choose {game[2]}")
        print("PC win\n")
        i=i+1
    elif(user==1 and pc==3):
        print(f"YOur choose {game[1]} and Pc choose {game[3]}")
        print("user win\n")
        i=i+1
    elif(user==2 and pc==1):
        print(f"User choose {game[2]} and Pc choose {game[1]}")
        print("User win\n")
        i=i+1
    elif(user==2 and pc==3):
        print(f"User choose {game[2]} and Pc choose {game[3]}")
        print("PC win\n")
        i=i+1
    elif(user==3 and pc==1):
        print(f"User choose {game[3]} and Pc choose {game[1]}")
        print("PC win\n")
        i=i+1
    elif(user==3 and pc==2):
        print(f"User choose {game[3]} and Pc choose {game[2]}")
        print("User win\n")
        i=i+1
    elif(user==4):
        print(f"User have played {i} times\n")
        print("Exit.....")
    else:
        print("Input doesn't match\n")



