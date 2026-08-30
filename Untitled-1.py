import random

questions = {"What is the largest ocean on Earth?":"Pacific",
            "What is the rarest natural blood type?":"AB-negative",
            "Which country has the most natural lakes?":"Canada",
            "What is the main chemical element in diamond?":"Carbon",
            "What unit measures electrical resistance?":"Ohm",
            "What is the capital of Canada?":"Ottawa",
            "What is the study of fossils called?":"Paleontology",
            "What is the hottest planet in our solar system?":"Venus",
            "Which mammalian species can fly naturally?":"Bat",
            "What is the main component of glass?":"Silica",
            "What element does the chemical symbol Au represent?":"Gold",
            "What is the largest internal organ in humans?":"Liver",
            "Which nation invented paper?":"China",
            "What force keeps planets in orbit around stars?":"Gravity",
            "What is the capital of Japan?":"Tokyo"}

def Random_QA_game():
    listed_questions = list(questions)
    no_of_questions = 5
    total_questions = random.sample(listed_questions,no_of_questions)
    score = 0
    for idx,question in enumerate(total_questions):
        print(f"{idx+1}. {question}")
        correct_answer = questions[question]
        answer = input("Your anser : ").lower().strip()
        if answer == correct_answer.lower():
            print("Correct\n")
            score = score+1
        else:
            print(f"wrong anser. correct anser is : {correct_answer}\n")
    print(f"game is over. your score is : {score}/{no_of_questions}")

Random_QA_game()