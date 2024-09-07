import random 
playing = True
number=str(random.randint(10,20))
print("Ill generate a number for you from 10 to 20")
while playing: 
    Guess = int(input("Enter your guess: "))
    if number == Guess:
        print("You win the game")
    else:
        print("you lose")
