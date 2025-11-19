"""
Generated Code Metadata:
========================
Original URL: https://howtosuecslplasma.org
Prompt: How can I use natural language processing (NLP) libraries to analyze online reviews and complaints about CSL Plasma and identify potential patterns of malpractice?
Generated: DETERMINISTIC_d8418e1ac75002fe
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

def preprocess_text(text):
    """
    Preprocess text by removing punctuation, converting to lowercase, 
    removing stopwords, and lemmatizing words.
    """
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize text
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join tokens back into a string
    text = ' '.join(tokens)
    
    return text

def analyze_sentiment(text):
    """
    Analyze sentiment of text using NLTK's VADER sentiment intensity analyzer.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

def classify_text(text, model, vectorizer):
    """
    Classify text using a trained Naive Bayes model.
    """
    # Transform text into a TF-IDF vector
    vector = vectorizer.transform([text])
    
    # Make prediction
    prediction = model.predict(vector)
    
    return prediction

def main():
    # Sample reviews and complaints data
    data = {
        'text': [
            'I had a great experience at CSL Plasma!',
            'The staff at CSL Plasma were very rude.',
            'I felt unsafe during my donation process.',
            'The payment was very generous.',
            'The wait time was too long.',
            'I would not recommend CSL Plasma to anyone.',
            'The nurses were very friendly and helpful.',
            'I experienced some discomfort during donation.',
            'The facility was very clean and well-maintained.',
            'I was not treated well by the staff.'
        ],
        'label': [1, 0, 0, 1, 0, 0, 1, 0, 1, 0]  # 1 = positive, 0 = negative
    }
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Preprocess text data
    df['text'] = df['text'].apply(preprocess_text)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer to the training data and transform both the training and testing data
    X_train_vectors = vectorizer.fit_transform(X_train)
    X_test_vectors = vectorizer.transform(X_test)
    
    # Train a Naive Bayes model
    model = MultinomialNB()
    model.fit(X_train_vectors, y_train)
    
    # Make predictions on the testing data
    predictions = model.predict(X_test_vectors)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    
    print(f'Accuracy: {accuracy:.3f}')
    print(report)
    
    # Analyze sentiment of a sample review
    sample_review = 'I had a great experience at CSL Plasma, but the wait time was long.'
    sentiment = analyze_sentiment(sample_review)
    print('Sentiment Analysis:')
    print(sentiment)

if __name__ == '__main__':
    main()
```
