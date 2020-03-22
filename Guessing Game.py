import random

x = random.randint(0,20)


print("\n \t \t Welcome to the gessing number game!!!")
print("\t","-"*55)

while 1:
    
    try:
        a=1
        while a!=x and 0<=a<=20:
            a=int(input("Enter a number between 0 and 20:\n"))
            if a>20 or a<0:
                print("Please, Pick a number between 0 and 20")
            elif a>x:
                print("Your guess is too high. :(")
            elif a<x:
                print("Your guess is too low. :(")
            elif a==x:
                print("Congratulations Fam, you've won $100!!!")
        break
    except (TypeError, ValueError):
        
        print("Oops! That was not a valid number. Try again...")
