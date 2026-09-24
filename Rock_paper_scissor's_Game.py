import random

user_score = 0
computer_score = 0

options = ["rock","paper","scissor"]

while True:
    user_input = input("Wanna play {Rock/Paper/Scissor} choose 1 or Type q to {quit}").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        print("entered incorrect word")
        continue

    computer_number = random.randint(0,2)
    computer_input = options[computer_number]

    # Rock : 0 , Paper : 1 , Scissor : 2

    if user_input == 'rock' and computer_input == 'scissor':
        print("you won!")
        user_score += 1

    elif user_input == 'paper' and computer_input == 'rock':
        print("you won")
        user_score += 1

    elif user_input == 'scissor' and computer_input == 'paper':
        print("you won")
        user_score += 1

    else:
        print("you lost")
        computer_score += 1


print(f"User won {user_score} times.")
print(f"Computer won {computer_score} times.")
print("good bye")        
