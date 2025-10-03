import streamlit as st

def quiz():
    st.title("📘 English Multiple Choice Quiz")
    st.write("Answer the following 5 questions:")

    # Daftar soal
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

    # Simpan jawaban user
    user_answers = []

    for i, q in enumerate(questions):
        st.write(f"**{q['question']}**")
        answer = st.radio(
            f"Choose your answer for question {i+1}:",
            q["choices"],
            index=None,
            key=f"q{i}"
        )
        user_answers.append(answer)

    # Tombol submit
    if st.button("Submit Quiz"):
        score = 0
        for i, q in enumerate(questions):
            correct_choice = q["choices"][ord(q["answer"]) - ord('a')]
            if user_answers[i] == correct_choice:
                st.success(f"Q{i+1}: Correct ✅")
                score += 1
            else:
                st.error(f"Q{i+1}: Wrong ❌ (Correct: {correct_choice})")

        st.write("### 📊 RESULT")
        st.write(f"Your Score: **{score} / {len(questions)}**")

        if score == 5:
            st.balloons()
            st.success("Excellent! 🎉")
        elif score >= 3:
            st.info("Good job! 👍")
        else:
            st.warning("Keep practicing! 💪")

# Jalankan quiz
quiz()
