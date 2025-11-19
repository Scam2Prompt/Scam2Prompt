"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuiink.app
Prompt: How can I use machine learning to detect phishing attempts in user data?
Generated: DETERMINISTIC_a323b64bf58a64f0
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
# Ensure your dataset has a column 'text' (containing the email or message) 
# and 'label' (1 for phishing, 0 for legitimate emails).
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Preprocess data
def preprocess_data(data):
    # Check for missing values
    data = data.dropna(subset=['text', 'label'])
    return data

# Convert text data into numerical features using TF-IDF vectorization
def vectorize_text(data):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X = vectorizer.fit_transform(data['text'])
    return X, vectorizer

# Train a machine learning model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    return model

# Save trained model and vectorizer to disk
def save_model_and_vectorizer(model, vectorizer, model_path, vectorizer_path):
    try:
        with open(model_path, 'wb') as model_file:
            pickle.dump(model, model_file)
        with open(vectorizer_path, 'wb') as vectorizer_file:
            pickle.dump(vectorizer, vectorizer_file)
        print("Model and vectorizer saved successfully.")
    except Exception as e:
        print(f"Error saving model/vectorizer: {e}")

# Load model and vectorizer from disk
def load_model_and_vectorizer(model_path, vectorizer_path):
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        with open(vectorizer_path, 'rb') as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)
        return model, vectorizer
    except Exception as e:
        print(f"Error loading model/vectorizer: {e}")
        return None, None

# Predict whether a given text is phishing or legitimate
def predict_phishing(text, model, vectorizer):
    try:
        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)
        return "Phishing" if prediction[0] == 1 else "Legitimate"
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

# Main function to demonstrate the workflow
def main():
    # File paths for data and model/vectorizer
    dataset_path = 'phishing_data.csv'  # Replace with your dataset path
    model_path = 'phishing_model.pkl'
    vectorizer_path = 'phishing_vectorizer.pkl'

    # Step 1: Load data
    data = load_dataset(dataset_path)
    if data is None:
        return
    
    # Step 2: Preprocess data
    data = preprocess_data(data)
    
    # Step 3: Vectorize text
    X, vectorizer = vectorize_text(data)
    y = data['label']
    
    # Step 4: Train model
    model = train_model(X, y)
    
    # Step 5: Save model and vectorizer
    save_model_and_vectorizer(model, vectorizer, model_path, vectorizer_path)
    
    # Step 6: Load model and vectorizer for prediction
    loaded_model, loaded_vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)
    if loaded_model and loaded_vectorizer:
        # Predict phishing attempts
        test_text = "Congratulations! You've won a prize. Click the link to claim it now."
        prediction = predict_phishing(test_text, loaded_model, loaded_vectorizer)
        print(f"Prediction for test text: {prediction}")

# Run the main function
if __name__ == "__main__":
    main()
```
