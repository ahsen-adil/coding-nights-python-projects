import streamlit as st
import random
import time

# Title of the Application
st.title("📝 Interactive Quiz Application")

# Define quiz questions, options, and answers
questions = [
    {"question": "What is the capital of Pakistan?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Islamabad"},
    {"question": "Who is the founder of Pakistan?", "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"], "answer": "Muhammad Ali Jinnah"},
    {"question": "Which is the national language of Pakistan?", "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"], "answer": "Urdu"},
    {"question": "What is the currency of Pakistan?", "options": ["Rupee", "Dollar", "Taka", "Riyal"], "answer": "Rupee"},
    {"question": "Which city is known as the 'City of Lights' in Pakistan?", "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], "answer": "Karachi"},
    {"question": "Which is the national sport of Pakistan?", "options": ["Cricket", "Hockey", "Football", "Kabaddi"], "answer": "Hockey"},
    {"question": "Which river is the longest in Pakistan?", "options": ["Indus", "Chenab", "Ravi", "Jhelum"], "answer": "Indus"},
    {"question": "Which mountain is the highest in Pakistan?", "options": ["K2", "Nanga Parbat", "Rakaposhi", "Broad Peak"], "answer": "K2"},
    {"question": "Which province is the largest by area in Pakistan?", "options": ["Punjab", "Sindh", "Balochistan", "KPK"], "answer": "Balochistan"},
    {"question": "Who wrote the national anthem of Pakistan?", "options": ["Faiz Ahmed Faiz", "Hafeez Jalandhari", "Allama Iqbal", "Josh Malihabadi"], "answer": "Hafeez Jalandhari"},
]

# Shuffle questions at the start
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))

# Initialize the current question index and score if not already in session state
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.timer = 10  # Timer for each question
    st.session_state.start_time = time.time()  # Store start time

# Get the current question
if st.session_state.current_index < len(st.session_state.shuffled_questions):
    question = st.session_state.shuffled_questions[st.session_state.current_index]

    # Display question number and question
    st.subheader(f"Question {st.session_state.current_index + 1} of {len(questions)}")
    st.markdown(f"**{question['question']}**")

    # Create radio buttons for options
    selected_option = st.radio("Choose your answer:", question["options"], key="answer")

    # Timer logic
    time_left = st.session_state.timer - (time.time() - st.session_state.start_time)
    if time_left <= 0:
        time_left = 0  # Ensure it doesn't go negative
        selected_option = None  # Auto-select as no answer

    # Display Timer
    st.warning(f"⏳ Time Left: {int(time_left)} seconds")

    # Submit button
    if st.button("Submit Answer") or time_left == 0:
        if selected_option == question["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1  # Increase score
        else:
            st.error(f"❌ Incorrect! The correct answer is **{question['answer']}**")

        # Move to the next question
        st.session_state.current_index += 1
        st.session_state.start_time = time.time()  # Reset timer
        st.rerun()  # Refresh page

else:
    st.success(f"🎉 Quiz Completed! Your Score: **{st.session_state.score} / {len(questions)}**")
    st.balloons()  # Celebrate with animations
    if st.button("Restart Quiz"):
        del st.session_state.shuffled_questions
        del st.session_state.current_index
        del st.session_state.score
        del st.session_state.timer
        del st.session_state.start_time
        st.rerun()  # Restart the quiz
