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
# Import required libraries
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

# Download required NLTK data
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_text(text):
    """
    Preprocess text data.

    Args:
        text (str): Text to preprocess.

    Returns:
        str: Preprocessed text.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize text
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    
    # Join tokens back into a string
    text = ' '.join(tokens)
    
    return text

def analyze_themes(data, num_themes):
    """
    Analyze themes in the data using Latent Dirichlet Allocation (LDA).

    Args:
        data (pd.DataFrame): Data to analyze.
        num_themes (int): Number of themes to extract.

    Returns:
        list: List of themes.
    """
    # Preprocess text data
    data['text'] = data['text'].apply(preprocess_text)
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_data = vectorizer.fit_transform(data['text'])
    
    # Perform LDA
    lda_model = LatentDirichletAllocation(n_components=num_themes)
    themes = lda_model.fit_transform(tfidf_data)
    
    # Get theme keywords
    feature_names = vectorizer.get_feature_names_out()
    theme_keywords = []
    for theme_idx, theme in enumerate(lda_model.components_):
        top_features_ind = np.argsort(theme)[::-1][:10]
        top_features = [feature_names[i] for i in top_features_ind]
        theme_keywords.append(top_features)
    
    return theme_keywords

def main():
    # Load data
    file_path = 'social_impact_heroes.csv'  # Replace with your file path
    data = load_data(file_path)
    
    if data is not None:
        # Analyze themes
        num_themes = 5
        themes = analyze_themes(data, num_themes)
        
        # Print themes
        for i, theme in enumerate(themes):
            print(f"Theme {i+1}: {theme}")

if __name__ == "__main__":
    main()
```
