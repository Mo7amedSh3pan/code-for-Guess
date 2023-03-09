origionName="mohamed"
guess=""
guessCount=0
check=False
while not check and guessCount<3:
    guess=input("entre your guess\n")
    if guess == origionName :
        check=True
    guessCount+=1
if check==True :
    print("you are win")
else:
    print("you are lose")