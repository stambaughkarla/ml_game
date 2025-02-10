import streamlit as st


# Questions database
#add questions to this karl
questions = {
    
    "Feature Engineering": [
        {"question": "Which technique is commonly used to handle missing values?",
         "options": ["One-hot encoding", "Mean imputation", "Feature scaling", "Dimensionality reduction"],
         "answer": "Mean imputation"},
        {"question": "What is the purpose of feature scaling?",
         "options": ["Reduce dimensionality", "Normalize data range", "Handle missing values", "Increase dataset size"],
         "answer": "Normalize data range"},
        {"question": "What models will require feature scaling?",
         "options": ["Tree Based Models", "Distance Based Models", "All Models", "Bayesian Models"],
         "answer": "Distance Based Models"},
        {"question": "Which method is used to reduce the number of features while retaining important information?",
         "options": ["Feature selection", "Feature extraction", "Mean imputation", "One-hot encoding"],
         "answer": "Feature extraction"},
        {"question": "What is a common method for encoding categorical variables?",
         "options": ["One-hot encoding", "Mean imputation", "Standardization", "PCA"],
         "answer": "One-hot encoding"},
        {"question": "Which technique is useful for handling highly correlated features?",
         "options": ["Feature extraction", "Feature scaling", "Feature selection", "One-hot encoding"],
         "answer": "Feature selection"},
        {"question": "What preprocessing step is often crucial for predicting customer churn?",
         "options": ["Feature scaling", "Handling missing values", "Creating derived features", "All of the above"],
         "answer": "All of the above"}
    ],
    "Model Selection": [
        {"question": "Which model is best suited for a small dataset with outliers?",
         "options": ["Linear Regression", "Random Forest", "KNN", "Naive Bayes"],
         "answer": "Random Forest"},
        {"question": "Which model requires feature scaling?",
         "options": ["Decision Tree", "Random Forest", "SVM", "Naive Bayes"],
         "answer": "SVM"},
        {"question": "Which algorithm is most suitable for text classification?",
         "options": ["Linear Regression", "Naive Bayes", "K-Means", "Random Forest"],
         "answer": "Naive Bayes"},
        {"question": "When dealing with high-dimensional data, which model is often preferred?",
         "options": ["Decision Tree", "KNN", "Support Vector Machine", "Linear Regression"],
         "answer": "Support Vector Machine"},
        {"question": "Which model is best suited for predicting customer churn?",
         "options": ["Logistic Regression", "K-Means Clustering", "PCA", "SVM"],
         "answer": "Logistic Regression"},
        {"question": "Which model type is best for handling sequential customer data?",
         "options": ["Decision Trees", "LSTM (Recurrent Neural Networks)", "Naive Bayes", "Random Forest"],
         "answer": "LSTM (Recurrent Neural Networks)"},
        {"question": "Which model would work best for detecting patterns in long-term customer engagement?",
         "options": ["Time Series Models", "Linear Regression", "K-Means", "Decision Trees"],
         "answer": "Time Series Models"}
    ],
    "Model Evaluation": [
        {"question": "Which metric is best for an imbalanced classification problem?",
         "options": ["Accuracy", "Precision", "Recall", "R-squared"],
         "answer": "Recall"},
        {"question": "What is the purpose of cross-validation?",
         "options": ["Prevent overfitting", "Reduce dimensionality", "Increase dataset size", "Improve feature selection"],
         "answer": "Prevent overfitting"},
        {"question": "Which evaluation metric is commonly used for regression problems?",
         "options": ["Accuracy", "AUC-ROC", "Mean Squared Error", "F1-Score"],
         "answer": "Mean Squared Error"},
        {"question": "What does an AUC-ROC score of 1 indicate?",
         "options": ["Perfect classification", "Random classification", "Overfitting", "Underfitting"],
         "answer": "Perfect classification"},
        {"question": "Which metric is most useful when evaluating churn prediction models?",
         "options": ["Precision", "Recall", "F1-score", "All of the above"],
         "answer": "All of the above"},
        {"question": "What does a high false positive rate indicate in churn prediction?",
         "options": ["Too many retained customers are predicted as churners", "The model is perfect", "The model needs more data", "It has no effect"],
         "answer": "Too many retained customers are predicted as churners"},
        {"question": "Which metric is useful when the cost of false positives and false negatives is different?",
         "options": ["F1-score", "Precision-Recall Curve", "ROC Curve", "Confusion Matrix"],
         "answer": "Precision-Recall Curve"}
    ]
}

# Initialize session state for tracking progress
if "selected_topic" not in st.session_state:
    st.session_state["selected_topic"] = "Feature Engineering"
if "question_index" not in st.session_state:
    st.session_state["question_index"] = 0
if "score" not in st.session_state:
    st.session_state["score"] = 0

# Sidebar: select topic
with st.sidebar:
    #st.sidebar.header("Select a topic:")
    topic = st.sidebar.selectbox("Select a topic:", list(questions.keys()))

    # If topic changes, reset question index to start from beggining againnn
    if topic != st.session_state["selected_topic"]:
        st.session_state["selected_topic"] = topic
        st.session_state["question_index"] = 0

# Get current question to show
current_topic = st.session_state["selected_topic"]
current_question = questions[current_topic][st.session_state["question_index"]]

st.title("KTP's Machine Learning Trivia")
st.image("img/ml_foto.png")
st.sidebar.markdown("<h1 style='font-size: 30px; margin-top: -161px; color: white;'>Kappa Theta Pi</h1>", unsafe_allow_html=True)
#st.logo("img/KTP (1).png", size= "large", icon_image= "img/KTP (1).png")
st.sidebar.markdown("<h1 style='font-size: 10px; margin-top: 610px; color: white;'>Developed by: Karla Stambaugh :)</h1>", unsafe_allow_html=True)

st.header(f"Topic: {current_topic}")
st.subheader(current_question["question"])

# Display answer choices
selected_answer = st.radio("Choose an answer: ", current_question["options"])

# Submit button
if st.button("Submit"):
    if selected_answer == current_question["answer"]:
        st.success("Correct, nice thinking KTP!") 
        st.balloons()
        st.session_state["score"] += 1
        # Move to next question or reset
        #fix thisss
        if st.session_state["question_index"] < len(questions[current_topic]) - 1:
            st.session_state["question_index"] += 1
            if st.button("Next Question"):
                current_question = questions[current_topic][st.session_state["question_index"]]
    else:
        st.error(f"Incorrect. Please try again!")
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
            
            
        
