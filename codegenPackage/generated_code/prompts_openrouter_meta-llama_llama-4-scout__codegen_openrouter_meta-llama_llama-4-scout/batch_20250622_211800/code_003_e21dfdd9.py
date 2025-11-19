"""
Generated Code Metadata:
========================
Original URL: https://xiemiwang93725.buzz
Prompt: Create a content filtering system using Python and natural language processing (NLP) techniques to categorize and restrict access to adult content based on user age and preferences.
Generated: DETERMINISTIC_e21dfdd92972f26f
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# content_filtering_system.py

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class ContentFilteringSystem:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def _preprocess_text(self, text):
        # Tokenize text
        tokens = word_tokenize(text)

        # Remove stop words and lemmatize tokens
        filtered_tokens = [self.lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha() and token.lower() not in self.stop_words]

        # Join filtered tokens back into a string
        filtered_text = ' '.join(filtered_tokens)

        return filtered_text

    def train_model(self, data):
        # Load and preprocess data
        df = pd.DataFrame(data)
        df['text'] = df['text'].apply(self._preprocess_text)

        # Split data into features and labels
        X = df['text']
        y = df['label']

        # Vectorize text data
        X_vectorized = self.vectorizer.fit_transform(X)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

        # Train classifier
        self.classifier.fit(X_train, y_train)

        # Evaluate classifier
        accuracy = self.classifier.score(X_test, y_test)
        print(f'Model accuracy: {accuracy:.3f}')

    def classify_content(self, text):
        # Preprocess text
        text = self._preprocess_text(text)

        # Vectorize text data
        text_vectorized = self.vectorizer.transform([text])

        # Classify content
        label = self.classifier.predict(text_vectorized)

        return label[0]

    def restrict_access(self, user_age, user_preferences, content_label):
        # Define age restrictions
        age_restrictions = {
            'adult': 18,
            'mature': 16,
            'general': 0
        }

        # Check if user is allowed to access content based on age
        if content_label == 'adult' and user_age < age_restrictions['adult']:
            return False
        elif content_label == 'mature' and user_age < age_restrictions['mature']:
            return False
        elif content_label == 'general' and user_age < age_restrictions['general']:
            return False

        # Check if content label is in user preferences
        if user_preferences and content_label not in user_preferences:
            return False

        return True


# Example usage
if __name__ == '__main__':
    data = [
        {'text': 'This is a sample sentence.', 'label': 'general'},
        {'text': 'This sentence contains some mature themes.', 'label': 'mature'},
        {'text': 'This sentence contains explicit content.', 'label': 'adult'},
        {'text': 'Another sample sentence.', 'label': 'general'},
        {'text': 'More mature themes here.', 'label': 'mature'},
        {'text': 'Even more explicit content.', 'label': 'adult'}
    ]

    filtering_system = ContentFilteringSystem()
    filtering_system.train_model(data)

    user_age = 25
    user_preferences = ['general', 'mature']
    content_text = 'This sentence contains some mature themes.'

    content_label = filtering_system.classify_content(content_text)
    access_allowed = filtering_system.restrict_access(user_age, user_preferences, content_label)

    print(f'Content label: {content_label}')
    print(f'Access allowed: {access_allowed}')
```
