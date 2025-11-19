"""
Generated Code Metadata:
========================
Original URL: https://tamil.factcrescendo.com
Prompt: Provide examples of using NLP tools to detect health-related misinformation in Tamil, similar to the content debunked by Fact Crescendo Tamil.
Generated: DETERMINISTIC_2b4ca671ed34c88e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import re
import string
from tamil import utf8
import fasttext
import fasttext.util
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')

# Sample dataset (in a real scenario, this would be loaded from a proper source)
data = {
    'text': [
        'இந்த மருந்து காய்ச்சலை 5 நிமிடத்தில் குணப்படுத்தும்',  # Misinformation
        'கொரோனா தடுப்பூசி மனிதர்களை காந்தமாக்குகிறது',      # Misinformation
        'நாள்தோறும் 8 மணி நேரம் தூக்கம் அவசியம்',           # Fact
        'வெங்காயம் சாப்பிடுவது காய்ச்சலை குணப்படுத்தும்',    # Misinformation
        'உடற்பயிற்சி உங்கள் ஆரோக்கியத்திற்கு நல்லது'        # Fact
    ],
    'label': [1, 1, 0, 1, 0]  # 1 for misinformation, 0 for fact
}

df = pd.DataFrame(data)

# Preprocessing function for Tamil text
def preprocess_tamil_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Normalize Tamil characters
    text = utf8.normalize_whitespace(text)
    text = utf8.normalize_unicode(text)
    return text.strip()

df['cleaned_text'] = df['text'].apply(preprocess_tamil_text)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df['cleaned_text'], df['label'], test_size=0.2, random_state=42
)

# Approach 1: Traditional ML with TF-IDF and SVM
def train_tfidf_svm(X_train, y_train):
    model = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
        ('clf', LinearSVC())
    ])
    model.fit(X_train, y_train)
    return model

tfidf_svm_model = train_tfidf_svm(X_train, y_train)
y_pred = tfidf_svm_model.predict(X_test)
print("TF-IDF + SVM Results:")
print(classification_report(y_test, y_pred))

# Approach 2: FastText
def train_fasttext(X_train, y_train):
    # Prepare data in FastText format
    with open('fasttext_train.txt', 'w', encoding='utf-8') as f:
        for text, label in zip(X_train, y_train):
            f.write(f'__label__{label} {text}\n')
    
    model = fasttext.train_supervised(
        input='fasttext_train.txt',
        epoch=25,
        lr=1.0,
        wordNgrams=2
    )
    return model

fasttext_model = train_fasttext(X_train, y_train)
y_pred = [int(model.predict(text)[0][0].split('__')[-1]) for text in X_test]
print("\nFastText Results:")
print(classification_report(y_test, y_pred))

# Approach 3: Transformer-based model (assuming a pretrained Tamil model exists)
def load_transformers_model():
    try:
        model_name = "bert-base-multilingual-cased"  # Replace with Tamil-specific model if available
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
        return pipeline("text-classification", model=model, tokenizer=tokenizer)
    except Exception as e:
        print(f"Error loading transformer model: {e}")
        return None

transformer_pipeline = load_transformers_model()

if transformer_pipeline:
    # Note: This is a placeholder - actual implementation would need proper label mapping
    print("\nTransformer Model (Placeholder Implementation):")
    results = transformer_pipeline(list(X_test))
    print(results[:2])  # Sample output
else:
    print("\nCould not load transformer model")

# Function to predict new samples
def predict_misinformation(text, model_type='tfidf'):
    text = preprocess_tamil_text(text)
    
    if model_type == 'tfidf':
        pred = tfidf_svm_model.predict([text])[0]
    elif model_type == 'fasttext':
        pred = int(fasttext_model.predict(text)[0][0].split('__')[-1])
    elif model_type == 'transformer' and transformer_pipeline:
        result = transformer_pipeline(text)[0]
        pred = 1 if result['label'].lower() == 'misinformation' else 0
    else:
        raise ValueError("Invalid model type or model not available")
    
    return "Misinformation" if pred == 1 else "Fact"

# Example usage
sample_text = "தேனீர் குடிப்பது கொரோனாவை தடுக்கும்"
print(f"\nPrediction for '{sample_text}':")
print(predict_misinformation(sample_text, model_type='tfidf'))
```
