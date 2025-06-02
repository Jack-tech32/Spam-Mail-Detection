# 📧 Spam Email Detection 

Interactive Application Link ::   https://spam-mail-detection-w2xojn5ida5a6awclkj869.streamlit.app/


This project is an end-to-end machine learning application that detects whether a given message is **spam or not** using Natural Language Processing (NLP) and a trained classification model. 
Built with Python, scikit-learn, and Streamlit, it's designed to be simple, clean, and interactive.

 Project Overview

The goal of this project is to create a web-based application that:
- Accepts any text input (like an email or SMS)
- Processes and analyzes the text using TF-IDF
- Predicts whether the message is spam or ham using a trained model
- Displays the result instantly via a Streamlit UI

 Dataset

- **Source**: Kaggle
- **Total Samples**: 5,572 messages
- **Columns**:
  - "v1": Label ("ham" or "spam")
  - "v2": Message content (text)

After preprocessing, we used:

- "message": cleaned and lowercased
- "label_num": numeric version of "ham" (0) and "spam" (1)


Tech Stack

    Layer              Tool                     

 Language             Python                   
 Libraries            Scikit-learn, pandas, joblib 
 UI                   Streamlit                
 NLP                  TF-IDF Vectorizer        
 Model                Multinomial Naive Bayes  
 Deployment           Streamlit Cloud / GitHub 


 Machine Learning Flow

1. Text cleaning (lowercase, remove punctuation/numbers)
2. Vectorization using "TfidfVectorizer"
3. Train/Test Split (80/20)
4. Model: "MultinomialNB"
5. Evaluation: accuracy, confusion matrix, classification report
6. Model + Vectorizer saved using "joblib"


How to Run the Project Locally
locally run the app on the localhost 

Requirements
Install dependencies:

requirements.txt file 

command for run app on localhost using streamlit library:

streamlit run app.py

spam-email-detection: 
├── app.py
├── spam_model.pkl
├── tfidf_vectorizer.pkl
├── spam.csv
├── requirements.txt
└── README.md


Deploy on Streamlit Cloud
Push this project to a public GitHub repo

Go to https://streamlit.io/cloud

Sign in with GitHub and select your repo

Set app.py as the main entry point

Click "Deploy"

Application Overview ::
                       ![Screenshot 2025-06-01 195152](https://github.com/user-attachments/assets/4040f7d9-042e-43b8-b7c1-891efeb91b13)



Author

Name: Jayesh Sanjay Patil // USERNAME git : ["Jack-tech32"]

Final Year Engineering Student [B Tech]

Project: Spam Email Detection using NLP



Acknowledgements :


Dataset from  Kaggle

Built using scikit-learn, Streamlit, and Python

Special thanks to mentors, friends, and open-source contributors
