print("Hii.. Welcome to Computer Quiz Game")

playing = input("Do you wanna play this game (yes/no) : ").lower()

if playing != 'yes':
    quit()
else:

    Score = 0

    answer = input("What is the fullform of CRUD in SQL : ").lower()
    if answer == 'create read update delete':
        print("you are right!")
        Score += 1
    else:
        print("Incorrect")

    answer = input("What is the 25/5 : ").lower()
    if answer == '5':
        print("you are right!")
        Score += 1
    else:
        print("Incorrect")

    answer = input("What is the fullform of LOL : ").lower()
    if answer == 'laugh out load':
        print("you are right!")
        Score += 1
    else:
        print("Incorrect")

    answer = input("What is the fullform of FYI : ").lower()
    if answer == 'for your information':
        print("you are right!")
        Score += 1
    else:
        print("Incorrect")

    answer = input("What is the fullform of IMO : ").lower()
    if answer == 'in my opinion':
        print("you are right!")
        Score += 1
    else:
        print("Incorrect")

print("you got " + str(Score) + " correct out of 5")
print("you got "+ str(Score/5 * 100) +"%"+" Correct")
