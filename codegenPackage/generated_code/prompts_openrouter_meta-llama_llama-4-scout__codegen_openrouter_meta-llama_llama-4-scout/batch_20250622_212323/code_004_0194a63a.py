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
# Import required libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import spacy
from spacy.util import minibatch, compounding
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class NarrativeFilter:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        # Tokenize the text
        tokens = word_tokenize(text)

        # Remove stop words and punctuation
        tokens = [t for t in tokens if t.isalpha() and t not in self.stop_words]

        # Lemmatize the tokens
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens]

        # Join the tokens back into a string
        return ' '.join(tokens)

    def train_model(self, data):
        # Preprocess the text data
        data['text'] = data['text'].apply(self.preprocess_text)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

        # Create a TF-IDF vectorizer
        vectorizer = TfidfVectorizer()

        # Fit the vectorizer to the training data and transform both the training and testing data
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)

        # Train a random forest classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train_tfidf, y_train)

        # Make predictions on the testing data
        y_pred = model.predict(X_test_tfidf)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        return model, vectorizer, accuracy, report

    def filter_narratives(self, text, model, vectorizer):
        # Preprocess the text
        text = self.preprocess_text(text)

        # Transform the text into a TF-IDF vector
        text_tfidf = vectorizer.transform([text])

        # Make a prediction
        prediction = model.predict(text_tfidf)

        # Return the prediction
        return prediction[0]

def main():
    # Example usage
    data = pd.DataFrame({
        'text': ['This is a manipulated narrative', 'This is a real story', 'Another manipulated narrative', 'Another real story'],
        'label': [1, 0, 1, 0]
    })

    filter = NarrativeFilter()
    model, vectorizer, accuracy, report = filter.train_model(data)
    print(f'Accuracy: {accuracy:.3f}')
    print(report)

    text_to_filter = 'This is a manipulated narrative'
    prediction = filter.filter_narratives(text_to_filter, model, vectorizer)
    print(f'Prediction: {prediction}')

if __name__ == '__main__':
    main()
```
