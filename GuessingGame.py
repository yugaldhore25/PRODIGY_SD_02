import random

print('\n'"TASK:-2")
print('\n'"This code is represented by Yugal Dhore.")
print('\n'"------GUESSING GAME------")
#HINTS FOR GUESSING THE CORRECT NUMBER
def answer(guess,Number,org_attempts):
    if guess < Number:
        print('\n'f"The number {guess} you guess is TOO LOW! Try again.")
        return org_attempts - 1
    
    elif guess > Number:
        print('\n'f"The number {guess} you guess is TOO HIGH! Try again.")
        return org_attempts - 1
#MAIN BODY OF GAME
def game():
    print('\n'"THE GAME STARTS NOW.")
    print("You have 10 attempts to guess the number.")
    Number = random.randint(0, 100)
    guess = int(input("Guess a number between 0 to 100:"))
    org_attempts = 10
    attempts = 0
    if guess > 100:# PLAYER CANNOT ENTER NUMBER >100 IF THEY DO THEY LOOSE THE GAME
        print('\n'f"The number {guess} you enter is not in range of 0 to 100",'\n'"Please enter the number in given range.")
        
    elif guess <= 100:#WHEN PLAYER ENTER CORRECT NUMBER IN THE GIVEN RANGE
        while guess != Number :
        
            org_attempts = answer(guess, Number, org_attempts)
            print(f"You have only {org_attempts} attempt left.")
            attempts += 1
        
            if org_attempts == 0:
                print('\n'"SORRY."'\n'"You are out of attempts."'\n'"Please try again.")
                return
        
            else:
                print ("Guess again.")
        
            guess = int(input('\n'"Guess the number again:"))
    
        print('\n'"Congratulations."'\n',f"{Number} is the correct guess."'\n', f"Congrats you guess the correct number in {attempts} attempts.")
game() 