import random

top_of_range = input("please enter the range of the random number you need: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("pleae enter the number which is larger then 0 next time")
        quit()
    else:
        random_number = random.randint(0,top_of_range)
else:
    print("please enter a valid number next time :( )")
    quit()


count = 0

while True:
    guessed_number = input("guess a number : ")
    count += 1
    if guessed_number.isdigit():
        guessed_number = int(guessed_number)
        if guessed_number <= 0:
            print("please enter a number which is larger then 0")
            continue
        elif guessed_number == random_number:
            print("you guessed correct answer :)\n")
            if random_number == 1:
                print("you guessed correct answer in",count,"round")
                break
            else:
                print("you guessed correct answer in",count,"rounds")
                break
        elif random_number > guessed_number:
            print("you guessed a smaller number")
        elif random_number < guessed_number:
            print("you guessed a larger number")        
    else:
        print("please enter a valid number!")
        continue

    

