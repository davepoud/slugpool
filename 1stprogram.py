import sys

numberguesses=0
while numberguesses<5:
    guess=int(input("What is your password?"))
    if guess==1234:
        print ("welcome back")
        sys.exit()
    else:
        
        numberguesses+=1
        if numberguesses>=5:
            print ("You have tried more than 5 attempts, please wait 5 minutes before trying again")
            sys.exit()
        else:
            print ("try again")
