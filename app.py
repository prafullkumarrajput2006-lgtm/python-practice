# app.py
import streamlit as st
import pandas as pd
import string
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# ----------------------------
# 1. Data Loading
# ----------------------------
@st.cache_data
def load_data():
    # News dataset (CSV with "text" and "label")
    df = pd.read_csv("news.csv")
    return df

# ----------------------------
# 2. Text Cleaning Function
# ----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", "", text)  # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove special chars & numbers
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

# ----------------------------
# 3. Train Model
# ----------------------------
@st.cache_resource
def train_model(data):
    data["text"] = data["text"].astype(str).apply(clean_text)
    X_train, X_test, y_train, y_test = train_test_split(
        data["text"], data["label"], test_size=0.2, random_state=42
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=5000)),
        ("nb", MultinomialNB())
    ])

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return model, acc

# ----------------------------
# 4. Streamlit App UI
# ----------------------------
st.set_page_config(page_title="Fake News Detection", layout="centered")

st.title("📰 Fake News Detection App")
st.write("यह ऐप न्यूज़ आर्टिकल/हेडलाइन को **FAKE** या **REAL** बताता है।")

# Load data
data = load_data()

# Train model
model, acc = train_model(data)

st.success(f"Model Training Completed ✅ (Accuracy: {acc*100:.2f}%)")

# User Input
st.subheader("🔎 Test a News Article")
user_input = st.text_area("यहाँ न्यूज़ हेडलाइन/आर्टिकल डालें:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("कृपया पहले कुछ टेक्स्ट डालें!")
    else:
        cleaned = clean_text(user_input)
        prediction = model.predict([cleaned])[0]
        if prediction.lower() == "fake":
            st.error("❌ यह न्यूज़ **FAKE** है")
        else:
            st.success("✅ यह न्यूज़ **REAL** है")
