import streamlit as st
import random

# Questions database
questions = {
    "Feature Engineering": [
        {"question": "Which technique is commonly used to handle missing values?",
         "options": ["One-hot encoding", "Mean imputation", "Feature scaling", "Dimensionality reduction"],
         "answer": "Mean imputation"},
        {"question": "What is the purpose of feature scaling?",
         "options": ["Reduce dimensionality", "Normalize data range", "Handle missing values", "Increase dataset size"],
         "answer": "Normalize data range"}
    ],
    "Model Selection": [
        {"question": "Which model is best suited for a small dataset with outliers?",
         "options": ["Linear Regression", "Random Forest", "KNN", "Naive Bayes"],
         "answer": "Random Forest"},
        {"question": "Which model requires feature scaling?",
         "options": ["Decision Tree", "Random Forest", "SVM", "Naive Bayes"],
         "answer": "SVM"}
    ],
    "Model Evaluation": [
        {"question": "Which metric is best for an imbalanced classification problem?",
         "options": ["Accuracy", "Precision", "Recall", "R-squared"],
         "answer": "Recall"},
        {"question": "What is the purpose of cross-validation?",
         "options": ["Prevent overfitting", "Reduce dimensionality", "Increase dataset size", "Improve feature selection"],
         "answer": "Prevent overfitting"}
    ]
}

# Initialize session state for tracking progress
if "selected_topic" not in st.session_state:
    st.session_state["selected_topic"] = "Feature Engineering"
if "question_index" not in st.session_state:
    st.session_state["question_index"] = 0
if "score" not in st.session_state:
    st.session_state["score"] = 0

# Sidebar for topic selection
topic = st.sidebar.radio("Select a topic:", list(questions.keys()))

# If topic changes, reset question index
if topic != st.session_state["selected_topic"]:
    st.session_state["selected_topic"] = topic
    st.session_state["question_index"] = 0

# Get current question
current_topic = st.session_state["selected_topic"]
current_question = questions[current_topic][st.session_state["question_index"]]

st.title("ML Model Selection Game")
st.header(f"Topic: {current_topic}")
st.subheader(current_question["question"])

# Display answer choices
selected_answer = st.radio("Choose an answer:", current_question["options"])

# Submit button
if st.button("Submit"):
    if selected_answer == current_question["answer"]:
        st.success("Correct!")
        st.session_state["score"] += 1
    else:
        st.error(f"Incorrect. The correct answer is {current_question['answer']}")
    
    # Move to next question or reset
    if st.session_state["question_index"] < len(questions[current_topic]) - 1:
        st.session_state["question_index"] += 1
    else:
        st.write("You've completed this topic! Choose another one from the sidebar.")
        st.session_state["question_index"] = 0
