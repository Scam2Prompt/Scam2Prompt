"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Write code to analyze testimonials from athletes and extract common themes in performance improvement (e.g., speed, strength, injury prevention) using natural language processing.
Generated: DETERMINISTIC_51bc1936ac3783c7
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nltk
from nltk.corpus import stopwords
import string

# Ensure necessary NLTK data is downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Set up stopwords and punctuation
STOPWORDS = set(stopwords.words('english'))
PUNCTUATION = string.punctuation

def preprocess_text(text):
    """
    Preprocesses the input text by:
    1. Lowercasing
    2. Removing punctuation
    3. Removing stopwords
    4. Tokenizing
    :param text: Original text
    :return: List of clean tokens
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(f"[{re.escape(PUNCTUATION)}]", "", text)  # Remove punctuation
    tokens = nltk.word_tokenize(text)  # Tokenize text
    tokens = [word for word in tokens if word not in STOPWORDS]  # Remove stopwords
    return tokens

def extract_common_themes(testimonials, num_topics=3, num_words=5):
    """
    Extracts common themes from a list of testimonials using LDA (Latent Dirichlet Allocation).
    :param testimonials: List of testimonial strings
    :param num_topics: Number of topics to extract
    :param num_words: Number of words to describe each topic
    :return: List of common themes (topics) with their keywords
    """
    # Preprocess all testimonials
    processed_testimonials = [" ".join(preprocess_text(text)) for text in testimonials]
    
    # Convert text to a document-term matrix
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(processed_testimonials)
    
    # Apply Latent Dirichlet Allocation (LDA) to extract topics
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(dtm)
    
    # Extract common themes
    themes = []
    for topic_idx, topic in enumerate(lda.components_):
        keywords = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-num_words - 1:-1]]
        themes.append({"Topic": f"Topic {topic_idx+1}", "Keywords": keywords})
    return themes

if __name__ == "__main__":
    # Example testimonials from athletes
    testimonials = [
        "After working on my speed drills, I noticed a significant improvement in my sprint times.",
        "The strength training program helped me increase my muscle mass and overall power.",
        "Focusing on injury prevention exercises has kept me on the field longer without setbacks.",
        "Speed and agility training were crucial for enhancing my performance on the court.",
        "The recovery techniques taught me how to prevent injuries and stay consistent in my training.",
    ]
    
    try:
        # Extract and display common themes
        common_themes = extract_common_themes(testimonials, num_topics=3, num_words=5)
        print("Extracted Common Themes:")
        for theme in common_themes:
            print(f"{theme['Topic']}: {', '.join(theme['Keywords'])}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
