"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamil.factcrescendo.com
Prompt: Provide examples of using NLP tools to detect health-related misinformation in Tamil, similar to the content debunked by Fact Crescendo Tamil.
Generated: DETERMINISTIC_2b4ca671ed34c88e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
from langdetect import detect
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from googletrans import Translator

# Suppress warnings
warnings.filterwarnings("ignore")

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Initialize global objects
translator = Translator()
stop_words = set(stopwords.words('tamil'))  # Tamil stop words; should be extended for better accuracy

# Function to preprocess Tamil text
def preprocess_text(text):
    """
    Preprocess the given Tamil text by removing special characters, 
    converting to lowercase, and removing stop words.
    """
    # Remove special characters, numbers, and extra white spaces
    text = re.sub(r'[^அ-ஔக-ஹ0-9\s]', '', text)
    text = text.lower().strip()
    
    # Tokenize and remove stop words
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Return cleaned text
    return ' '.join(filtered_tokens)

# Function to detect language and translate non-Tamil text
def detect_and_translate(text):
    """
    Detect the language of the input text. If the text is not in Tamil, 
    translate it to Tamil.
    """
    try:
        language = detect(text)
        if language != 'ta':  # 'ta' is the code for Tamil
            translated = translator.translate(text, src=language, dest='ta')
            return translated.text
        return text
    except Exception as e:
        print(f"Error detecting/translating language: {e}")
        return text

# Sample dataset creation (replace with real data in production)
data = {
    'text': [
        'கொரோனாவுக்கு இலவச மருத்துவம் கிடைக்காது!', 
        'கொரோனா வைரஸ் மாக்சின் உடனே எடுங்க!', 
        'சாப்பிட்டு உடல் ஆரோக்கியமாக இருக்கலாம்.',
        'Drink hot water to kill Coronavirus.',
        'Vaccines cause autism.'
    ],
    'label': [1, 0, 0, 1, 1]  # 1 = misinformation, 0 = genuine
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Preprocess the dataset
df['text'] = df['text'].apply(detect_and_translate)  # Translate non-Tamil text
df['text'] = df['text'].apply(preprocess_text)       # Clean and preprocess text

# Split data into training and testing sets
X = df['text']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data into numerical features using TF-IDF
tfidf = TfidfVectorizer(max_features=500)  # Limit features for performance
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Initialize and train the model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Predict on the test set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

# Function to predict misinformation
def predict_misinformation(text):
    """
    Predict whether the given Tamil text contains health-related misinformation.
    """
    try:
        translated_text = detect_and_translate(text)
        cleaned_text = preprocess_text(translated_text)
        vectorized_text = tfidf.transform([cleaned_text])
        prediction = model.predict(vectorized_text)
        return 'Misinformation' if prediction[0] == 1 else 'Genuine'
    except Exception as e:
        print(f"Error predicting misinformation: {e}")
        return 'Error'

# Example usage
example_text = "கொரோனாவுக்கு நீர் குடி சிகிச்சை உதவும்."
result = predict_misinformation(example_text)
print(f"Prediction for example text: {result}")
```
