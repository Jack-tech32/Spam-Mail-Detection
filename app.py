# app.py
import streamlit as st
import joblib
import re
import string


# Load trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Clean text function (same as used in training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Streamlit UI
st.set_page_config(page_title="Spam Email Detector", page_icon="📧")
st.title("Spam Email Detection App")
st.write("Enter an email or message below to check if it's spam.")

# Input box
user_input = st.text_area("Enter the message:")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(user_input)
        vect = vectorizer.transform([cleaned])
        prediction = model.predict(vect)[0]
        result = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"Result: **{result}**")
