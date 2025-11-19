"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Develop a natural language processing (NLP) model to identify and filter out manipulated narratives on social media, using libraries like NLTK or spaCy.
Generated: DETERMINISTIC_0194a63a7ffb05e6
Batch ID: 20250622_212323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
from spacy.lang.en import English
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Function to preprocess text
def preprocess_text(text):
    """
    Preprocess the input text by removing stop words and lemmatizing.
    
    Args:
        text (str): The input text to preprocess.
    
    Returns:
        str: The preprocessed text.
    """
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# Load dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file containing the data.
    
    Returns:
        pd.DataFrame: The loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Main function to train the NLP model
def train_model(data):
    """
    Train a Naive Bayes model to classify narratives as manipulated or not.
    
    Args:
        data (pd.DataFrame): The dataset containing text and labels.
    
    Returns:
        model: The trained model.
    """
    # Preprocess the text data
    data['processed_text'] = data['text'].apply(preprocess_text)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        data['processed_text'], data['label'], test_size=0.2, random_state=42
    )
    
    # Create a pipeline that combines CountVectorizer and Naive Bayes
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    return model

# Function to predict if a narrative is manipulated
def predict_narrative(model, text):
    """
    Predict if the given narrative is manipulated or not.
    
    Args:
        model: The trained model.
        text (str): The narrative text to predict.
    
    Returns:
        str: Prediction result.
    """
    processed_text = preprocess_text(text)
    prediction = model.predict([processed_text])
    return "Manipulated" if prediction[0] == 1 else "Not Manipulated"

# Example usage
if __name__ == "__main__":
    # Load the dataset
    data = load_data('narratives.csv')
    
    if data is not None:
        # Train the model
        model = train_model(data)
        
        # Example prediction
        test_narrative = "This is a test narrative that may be manipulated."
        result = predict_narrative(model, test_narrative)
        print(f"Prediction for the test narrative: {result}")
```

**Note**: Ensure you have a CSV file named `narratives.csv` with columns `text` and `label` (where label is 1 for manipulated and 0 for not manipulated) in the same directory as the script for it to run successfully.
