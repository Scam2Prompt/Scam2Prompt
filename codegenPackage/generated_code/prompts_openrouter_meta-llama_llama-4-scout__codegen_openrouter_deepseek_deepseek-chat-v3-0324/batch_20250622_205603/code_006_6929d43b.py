"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Write a code snippet to analyze the most common themes and topics among the "Social Impact Heroes Helping Our Planet" category, using text analysis techniques and machine learning algorithms.
Generated: DETERMINISTIC_6929d43bdb87c946
Batch ID: 20250622_205603
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
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import re

# Text preprocessing function
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Load and preprocess data
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        df['processed_text'] = df['text'].apply(preprocess_text)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Perform topic modeling
def analyze_topics(texts, num_topics=5, num_words=10):
    try:
        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=1000)
        tfidf = vectorizer.fit_transform(texts)
        
        # Apply Non-Negative Matrix Factorization
        nmf = NMF(n_components=num_topics, random_state=42)
        nmf.fit(tfidf)
        
        # Get feature names
        feature_names = vectorizer.get_feature_names_out()
        
        # Display topics
        topics = {}
        for topic_idx, topic in enumerate(nmf.components_):
            top_words = [feature_names[i] for i in topic.argsort()[:-num_words - 1:-1]]
            topics[f"Topic {topic_idx + 1}"] = top_words
        
        return topics
    except Exception as e:
        print(f"Error in topic analysis: {e}")
        return None

# Visualize topics
def visualize_topics(topics):
    try:
        plt.figure(figsize=(12, 8))
        for i, (topic, words) in enumerate(topics.items()):
            plt.subplot(1, len(topics), i+1)
            plt.barh(range(len(words)), [1]*len(words), tick_label=words)
            plt.title(topic)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing topics: {e}")

# Main execution
if __name__ == "__main__":
    # Example usage (replace with actual data path)
    data_path = "social_impact_heroes.csv"
    
    # Load and preprocess data
    data = load_data(data_path)
    if data is not None:
        # Analyze topics
        topics = analyze_topics(data['processed_text'])
        
        if topics:
            # Print and visualize results
            print("Identified Topics:")
            for topic, words in topics.items():
                print(f"{topic}: {', '.join(words)}")
            
            visualize_topics(topics)
```
