import random
count=10
i=['s','w','g']
ComputerWinCount=0
YourWinCount=0
while (count !=0):
    swg=str(input("Enter 's' or 'w' or 'g' :"))
    if swg.lower() in i:
        computerChoice= random.choice(i)
        count -=1
        if swg == computerChoice:
            print("It's Tie")
        elif computerChoice == 's' and swg.lower() == 'w':
            print(f"Computer Won with choice {computerChoice}")
            ComputerWinCount +=1
        elif computerChoice =='w' and swg.lower() == 'g':
            print(f"Computer Won with choice {computerChoice}")
            ComputerWinCount +=1
        elif computerChoice == 'g' and swg.lower() == 's':
            print(f"Computer Won with choice {computerChoice}")
            ComputerWinCount +=1
        else:
            print(f"You Won and computer choice was {computerChoice}")
            YourWinCount +=1
    else:
        print("You have entered wrong word :", swg)
if ComputerWinCount>YourWinCount:
    print("Over all Computer Won")
else:
    print("Over all You Won") 

                                          
