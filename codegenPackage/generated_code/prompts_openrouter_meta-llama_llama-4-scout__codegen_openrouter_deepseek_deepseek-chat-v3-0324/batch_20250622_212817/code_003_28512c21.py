"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Compare and contrast the themes of exploration in 'Space Odyssey' with those found in Arthur C. Clarke's works, highlighting unique elements in James W. Raven's writing.
Generated: DETERMINISTIC_28512c2143e1143a
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script analyzes and compares themes of exploration in 'Space Odyssey' 
with Arthur C. Clarke's works, highlighting unique elements in James W. Raven's writing.
It uses NLP techniques to extract and compare themes from text samples.
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Ensure required NLTK data is downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

class ThemeAnalyzer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def preprocess_text(self, text):
        """Preprocess text by tokenizing, removing stopwords, and lemmatizing."""
        try:
            tokens = word_tokenize(text.lower())
            filtered_tokens = [
                self.lemmatizer.lemmatize(token) 
                for token in tokens 
                if token.isalpha() and token not in self.stop_words
            ]
            return ' '.join(filtered_tokens)
        except Exception as e:
            print(f"Error preprocessing text: {e}")
            return ""

    def extract_key_themes(self, texts, top_n=10):
        """Extract top themes using TF-IDF vectorization."""
        try:
            processed_texts = [self.preprocess_text(text) for text in texts]
            tfidf_matrix = self.vectorizer.fit_transform(processed_texts)
            feature_names = self.vectorizer.get_feature_names_out()
            
            themes = []
            for i in range(len(texts)):
                top_indices = np.argsort(tfidf_matrix[i].toarray().flatten())[-top_n:]
                themes.append([feature_names[idx] for idx in top_indices])
            
            return themes
        except Exception as e:
            print(f"Error extracting themes: {e}")
            return []

    def compare_themes(self, odyssey_text, clarke_texts, raven_texts):
        """Compare themes across different authors' works."""
        try:
            all_texts = [odyssey_text] + clarke_texts + raven_texts
            labels = ['Space Odyssey'] + ['Clarke'] * len(clarke_texts) + ['Raven'] * len(raven_texts)
            
            themes = self.extract_key_themes(all_texts)
            
            # Generate comparison report
            comparison = {
                'common_themes': set(themes[0]).intersection(*themes[1:]),
                'unique_odyssey': set(themes[0]) - set().union(*themes[1:]),
                'unique_clarke': set().union(*themes[1:1+len(clarke_texts)]) - set(themes[0]) - set().union(*themes[1+len(clarke_texts):]),
                'unique_raven': set().union(*themes[1+len(clarke_texts):]) - set(themes[0]) - set().union(*themes[1:1+len(clarke_texts)])
            }
            
            return comparison
        except Exception as e:
            print(f"Error comparing themes: {e}")
            return {}

    def visualize_comparison(self, comparison):
        """Visualize theme comparison results."""
        try:
            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
            
            # Common themes
            axes[0,0].barh(list(comparison['common_themes']), [1]*len(comparison['common_themes']))
            axes[0,0].set_title('Common Themes')
            
            # Unique to Odyssey
            axes[0,1].barh(list(comparison['unique_odyssey']), [1]*len(comparison['unique_odyssey']))
            axes[0,1].set_title('Unique to Space Odyssey')
            
            # Unique to Clarke
            axes[1,0].barh(list(comparison['unique_clarke']), [1]*len(comparison['unique_clarke']))
            axes[1,0].set_title('Unique to Clarke')
            
            # Unique to Raven
            axes[1,1].barh(list(comparison['unique_raven']), [1]*len(comparison['unique_raven']))
            axes[1,1].set_title('Unique to Raven')
            
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error visualizing comparison: {e}")

# Example usage
if __name__ == "__main__":
    analyzer = ThemeAnalyzer()
    
    # Sample texts (in a real application, these would be loaded from files)
    odyssey_text = "Space exploration reveals humanity's place in the cosmos..."
    clarke_texts = [
        "The technological advancement enables interstellar travel...",
        "Human evolution is shaped by encounters with alien intelligence..."
    ]
    raven_texts = [
        "The psychological impact of deep space isolation...",
        "Cosmic mysteries challenge human perception of reality..."
    ]
    
    comparison = analyzer.compare_themes(odyssey_text, clarke_texts, raven_texts)
    analyzer.visualize_comparison(comparison)
```
