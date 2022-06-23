import random 
print("number guessing game")
num=random.randint(1,9)
chances=0
print("Guess the number between 1 and 9")
while chances<5:
    guess=int(input("Enter your guess"))
    if guess==num:
        print("Congratulations you won")
        break
    elif guess<num:
        print("Guess was too low")
    else:
        print("The guess was too high")
    chances=chances+1
if not chances<5:
    print("You lost")
    print("The number is ",num)