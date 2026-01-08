# Kaun Banega Crorepati (KBC) Game

questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. Pokhara", "B. Kathmandu", "C. Lalitpur", "D. Biratnagar"],
        "answer": "B"
    },
    {
        "question": "Who is known as the father of Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "How many continents are there in the world?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    }
]

prize_money = [1000, 5000, 10000, 50000]

print(" Welcome to Kaun Banega Crorepati ")
print("------------------------------------")

money = 0

for i in range(len(questions)):
    print(f"\nQuestion {i + 1} for Rs. {prize_money[i]}")
    print(questions[i]["question"])
    
    for option in questions[i]["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == questions[i]["answer"]:
        money = prize_money[i]
        print(f"Correct Answer! You have won Rs. {money}")
    else:
        print("Wrong Answer!")
        print(f"The correct answer was {questions[i]['answer']}")
        break

print("\n Game Over!")
print(f" Total Money Won: Rs. {money}")
