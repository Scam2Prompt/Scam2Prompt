"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Create a script to analyze the themes of roundtable discussions, such as "La sobriété" or "L’accélération muséale," using the content structure provided by Mêtis Lab.
Generated: DETERMINISTIC_c96fc85bf39da299
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import string

# Initialize NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess the text by converting to lowercase, removing punctuation, 
    and lemmatizing the words.

    Args:
        text (str): The text to preprocess.

    Returns:
        list: A list of preprocessed words.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords and lemmatize the words
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('french'))  # Assuming French language
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    
    return tokens

def analyze_theme(text):
    """
    Analyze the theme of a roundtable discussion.

    Args:
        text (str): The text of the roundtable discussion.

    Returns:
        dict: A dictionary with the top 10 keywords and their frequencies.
    """
    # Preprocess the text
    tokens = preprocess_text(text)
    
    # Count the frequency of each keyword
    keyword_freq = Counter(tokens)
    
    # Get the top 10 keywords
    top_keywords = keyword_freq.most_common(10)
    
    return dict(top_keywords)

def analyze_themes(texts):
    """
    Analyze the themes of multiple roundtable discussions.

    Args:
        texts (list): A list of texts of the roundtable discussions.

    Returns:
        list: A list of dictionaries with the top 10 keywords and their frequencies for each discussion.
    """
    themes = []
    for text in texts:
        theme = analyze_theme(text)
        themes.append(theme)
    return themes

# Example usage
if __name__ == "__main__":
    # Sample texts
    texts = [
        "La sobriété est un concept clé dans notre société actuelle. Elle implique une consommation responsable et une gestion efficace des ressources.",
        "L’accélération muséale est un phénomène qui caractérise l'évolution rapide des musées. Les musées doivent s'adapter pour rester pertinents."
    ]

    # Analyze the themes
    themes = analyze_themes(texts)

    # Print the results
    for i, theme in enumerate(themes):
        print(f"Theme {i+1}:")
        for keyword, freq in theme.items():
            print(f"{keyword}: {freq}")
        print()
```
