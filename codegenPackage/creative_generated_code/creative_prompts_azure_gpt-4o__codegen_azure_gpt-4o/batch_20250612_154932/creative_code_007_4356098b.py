"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whatthefluff.lol
Prompt: Create a machine learning model to classify social media posts as constructive or divisive based on their text content. Provide code and suggest libraries for natural language processing.
Generated: DETERMINISTIC_4356098b087f01e3
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.exceptions import NotFittedError
import re
import nltk
from nltk.corpus import stopwords

# Ensure NLTK has the required resources
nltk.download('stopwords')
nltk.download('punkt')

# Preprocessing function for text cleaning
def preprocess_text(text):
    """
    Preprocess text by removing special characters, converting to lowercase, 
    tokenizing, and removing stopwords.
    """
    try:
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize the text
        tokens = nltk.word_tokenize(text)
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        # Rejoin tokens into a single string
        return ' '.join(filtered_tokens)
    except Exception as e:
        raise ValueError(f"Error during text preprocessing: {e}")

# Example dataset (replace with actual data source)
data = {
    'text': [
        'I love how everyone is working together to solve this issue!',
        'This is just another example of people being unreasonable and divisive!',
        'The new policy is thoughtful and constructive.',
        'People are so divided these days. It is worrying.'
    ],
    'label': ['constructive', 'divisive', 'constructive', 'divisive']
}
# Convert to DataFrame
df = pd.DataFrame(data)

# Apply preprocessing to the text data
df['text'] = df['text'].apply(preprocess_text)

# Split dataset into features and labels
X = df['text']
y = df['label']

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a machine learning pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),  # Convert text data into TF-IDF features
    ('classifier', RandomForestClassifier(random_state=42))  # Use Random Forest for classification
])

try:
    # Train the model
    pipeline.fit(X_train, y_train)
except Exception as e:
    raise RuntimeError(f"Error during model training: {e}")

try:
    # Make predictions on the test set
    y_pred = pipeline.predict(X_test)
except NotFittedError:
    raise RuntimeError("Model has not been fitted yet. Ensure training is complete before predictions.")
except Exception as e:
    raise RuntimeError(f"Error during prediction: {e}")

# Evaluate and print model performance
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Save the trained model for future use (optional)
import joblib
try:
    joblib.dump(pipeline, 'social_media_post_classifier.pkl')
    print("Model saved as 'social_media_post_classifier.pkl'.")
except Exception as e:
    raise RuntimeError(f"Error saving the model: {e}")
```
