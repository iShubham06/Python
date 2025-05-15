questions = [
    {
        "question": "What is the most culture-based city in India?",
        "options": ["A. Kolkata", "B. Jaipur", "C. Varanasi", "D. Madurai"],
        "answer": "C. Varanasi"
    },
    {
        "question": "Which city is known as the 'Pink City' of India?",
        "options": ["A. Udaipur", "B. Jaipur", "C. Jodhpur", "D. Bikaner"],
        "answer": "B. Jaipur"
    },
    {
        "question": "Who was the first Prime Minister of independent India?",
        "options": ["A. Mahatma Gandhi", "B. Sardar Patel", "C. Jawaharlal Nehru", "D. Rajendra Prasad"],
        "answer": "C. Jawaharlal Nehru"
    },
    {
        "question": "Which river is considered the holiest in India?",
        "options": ["A. Yamuna", "B. Godavari", "C. Ganga", "D. Narmada"],
        "answer": "C. Ganga"
    },
    {
        "question": "What is the national bird of India?",
        "options": ["A. Sparrow", "B. Parrot", "C. Peacock", "D. Swan"],
        "answer": "C. Peacock"
    },
    {
        "question": "Which Indian state is famous for its classical dance form Kathakali?",
        "options": ["A. Tamil Nadu", "B. Kerala", "C. Andhra Pradesh", "D. Karnataka"],
        "answer": "B. Kerala"
    }
]


score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_input = input("Enter your answer (e.g., A. Kolkata): ").strip()

    if user_input.lower() == q["answer"].lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {q['answer']}")

print(f"\n🎯 Final Score: {score}/{len(questions)}")