"""
Generated Code Metadata:
========================
Original URL: https://simonscat.pages.dev
Prompt: Create a Simon's Cat character recommendation system using natural language processing (NLP) and machine learning.
Generated: DETERMINISTIC_efc7b1c46c8052d6
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import spacy
import string
import re

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

# Character traits dataset (example data)
characters = {
    'Simon\'s Cat': ['playful', 'mischievous', 'hungry', 'curious', 'determined'],
    'Kitten': ['energetic', 'playful', 'small', 'adorable', 'clumsy'],
    'Chloe': ['grumpy', 'independent', 'mature', 'calm', 'dignified'],
    'Jazz': ['friendly', 'social', 'outgoing', 'playful', 'affectionate'],
    'Maisie': ['shy', 'timid', 'gentle', 'quiet', 'sensitive']
}

# Sample user preferences dataset
user_data = {
    'text': [
        "I love playful and energetic cats",
        "I prefer calm and dignified cats",
        "I like mischievous and curious pets",
        "I enjoy shy and gentle animals",
        "I want a friendly and outgoing cat"
    ],
    'character': ['Kitten', 'Chloe', 'Simon\'s Cat', 'Maisie', 'Jazz']
}

# Create DataFrame from user data
df = pd.DataFrame(user_data)

# Text preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Lemmatization and stopword removal
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    
    return ' '.join(tokens)

# Preprocess user text data
df['processed_text'] = df['text'].apply(preprocess_text)

# Encode character labels
label_encoder = LabelEncoder()
df['character_encoded'] = label_encoder.fit_transform(df['character'])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df['processed_text'], 
    df['character_encoded'], 
    test_size=0.2, 
    random_state=42
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=1000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Random Forest Classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train_tfidf, y_train)

# Evaluate model
y_pred = classifier.predict(X_test_tfidf)
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Recommendation function
def recommend_character(user_input):
    try:
        # Preprocess input
        processed_input = preprocess_text(user_input)
        
        # Vectorize input
        input_vector = vectorizer.transform([processed_input])
        
        # Predict character
        prediction = classifier.predict(input_vector)
        
        # Get character name
        character = label_encoder.inverse_transform(prediction)[0]
        
        # Get character traits
        traits = characters.get(character, [])
        
        # Find similar characters using cosine similarity
        char_descriptions = [' '.join(traits) for traits in characters.values()]
        char_names = list(characters.keys())
        
        # Vectorize character descriptions
        char_vectorizer = TfidfVectorizer()
        char_vectors = char_vectorizer.fit_transform(char_descriptions)
        input_char_vector = char_vectorizer.transform([' '.join(traits)])
        
        # Calculate similarities
        similarities = cosine_similarity(input_char_vector, char_vectors)
        similar_chars = sorted(
            zip(char_names, similarities[0]), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        # Prepare response
        response = {
            'recommended_character': character,
            'character_traits': traits,
            'similar_characters': [char for char, score in similar_chars if char != character][:2]
        }
        
        return response
    
    except Exception as e:
        print(f"Error in recommendation: {e}")
        return {
            'error': 'Unable to process request',
            'details': str(e)
        }

# Example usage
if __name__ == "__main__":
    test_input = "I want a cat that is playful but not too energetic"
    recommendation = recommend_character(test_input)
    print("\nRecommendation:")
    print(f"Character: {recommendation['recommended_character']}")
    print(f"Traits: {', '.join(recommendation['character_traits'])}")
    print(f"Similar characters: {', '.join(recommendation['similar_characters'])}")
```
