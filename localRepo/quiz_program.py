questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Paris", "c) Rome", "d) Madrid"],
        "answer": "b"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["a) Python", "b) Java", "c) JavaScript", "d) All of the above"],
        "answer": "d"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["a) Central Process Unit", "b) Central Processing Unit", "c) Computer Personal Unit", "d) Central Power Unit"],
        "answer": "b"
    }
]
score =0
for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    answer = input("enter the correct answer(a/b/c/d): ")
    if answer == q["answer"]:
        print("answer is correct")
        score +=1
    else:
        print("wrong! the correct answer is :",q["answer"])
    

print(f"your final score is :{score}/{len(questions)}")