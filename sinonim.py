# Aplikasi Kuis Pilihan Ganda Bahasa Inggris (5 Soal)

def quiz():
    questions = [
        {
            "question": "1. What is the synonym of 'Happy'?",
            "choices": ["a. Sad", "b. Angry", "c. Joyful", "d. Tired"],
            "answer": "c"
        },
        {
            "question": "2. What is the past tense of 'Go'?",
            "choices": ["a. Goed", "b. Went", "c. Gone", "d. Going"],
            "answer": "b"
        },
        {
            "question": "3. Which one is a fruit?",
            "choices": ["a. Carrot", "b. Apple", "c. Potato", "d. Cabbage"],
            "answer": "b"
        },
        {
            "question": "4. Fill in the blank: She ___ reading a book.",
            "choices": ["a. is", "b. are", "c. am", "d. be"],
            "answer": "a"
        },
        {
            "question": "5. What is the antonym of 'Big'?",
            "choices": ["a. Small", "b. Large", "c. Huge", "d. Tall"],
            "answer": "a"
        }
    ]
    
    score = 0
    
    for q in questions:
        print("\n" + q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Your answer (a/b/c/d): ").lower()
        
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}")
    
    print("\n=== RESULT ===")
    print(f"Your Score: {score} / {len(questions)}")
    if score == 5:
        print("Excellent! 🎉")
    elif score >= 3:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")

# Jalankan program
quiz()