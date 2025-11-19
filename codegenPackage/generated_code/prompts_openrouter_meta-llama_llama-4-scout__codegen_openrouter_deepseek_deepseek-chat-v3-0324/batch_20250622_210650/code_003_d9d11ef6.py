"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Compare and contrast the themes and plot of "Nuclear Power Nuclear Game" with another novel that explores similar topics, such as nuclear proliferation and espionage.
Generated: DETERMINISTIC_d9d11ef69cdd2ca7
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script compares and contrasts the themes and plots of two novels dealing with nuclear proliferation and espionage.
It uses NLP techniques to analyze text similarities and differences.
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import numpy as np

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class NovelAnalyzer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
    
    def preprocess_text(self, text):
        """Preprocess text by tokenizing, removing stopwords, and lemmatizing."""
        try:
            tokens = word_tokenize(text.lower())
            filtered_tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                             if token.isalpha() and token not in self.stop_words]
            return ' '.join(filtered_tokens)
        except Exception as e:
            print(f"Error preprocessing text: {e}")
            return ""
    
    def compare_novels(self, novel1_text, novel2_text, novel1_title="Novel 1", novel2_title="Novel 2"):
        """Compare two novels using TF-IDF and cosine similarity."""
        try:
            # Preprocess texts
            preprocessed1 = self.preprocess_text(novel1_text)
            preprocessed2 = self.preprocess_text(novel2_text)
            
            if not preprocessed1 or not preprocessed2:
                raise ValueError("Preprocessing failed for one or both texts")
            
            # Vectorize texts
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform([preprocessed1, preprocessed2])
            
            # Calculate similarity
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            
            # Get top features
            feature_names = vectorizer.get_feature_names_out()
            top_features1 = self.get_top_features(tfidf_matrix[0], feature_names)
            top_features2 = self.get_top_features(tfidf_matrix[1], feature_names)
            
            # Visualize comparison
            self.plot_comparison(top_features1, top_features2, novel1_title, novel2_title)
            
            return {
                'similarity_score': similarity,
                f'{novel1_title}_top_features': top_features1,
                f'{novel2_title}_top_features': top_features2
            }
        except Exception as e:
            print(f"Error comparing novels: {e}")
            return None
    
    def get_top_features(self, tfidf_vector, feature_names, top_n=10):
        """Extract top features from TF-IDF vector."""
        try:
            tfidf_array = tfidf_vector.toarray().flatten()
            sorted_indices = np.argsort(tfidf_array)[::-1]
            return [feature_names[i] for i in sorted_indices[:top_n]]
        except Exception as e:
            print(f"Error getting top features: {e}")
            return []
    
    def plot_comparison(self, features1, features2, title1, title2):
        """Visualize the top features comparison."""
        try:
            plt.figure(figsize=(12, 6))
            
            # Plot for first novel
            plt.subplot(1, 2, 1)
            plt.barh(range(len(features1)), [1]*len(features1), tick_label=features1)
            plt.title(f"Top Themes in {title1}")
            plt.gca().invert_yaxis()
            
            # Plot for second novel
            plt.subplot(1, 2, 2)
            plt.barh(range(len(features2)), [1]*len(features2), tick_label=features2)
            plt.title(f"Top Themes in {title2}")
            plt.gca().invert_yaxis()
            
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting comparison: {e}")

# Example usage
if __name__ == "__main__":
    # Sample texts (in a real scenario, these would be full novel texts)
    nuclear_power_text = """
    Nuclear Power Nuclear Game explores the dangerous world of nuclear proliferation 
    through the eyes of a CIA operative uncovering a secret nuclear weapons program. 
    Themes include political intrigue, the morality of deterrence, and the thin line 
    between national security and global catastrophe.
    """
    
    other_novel_text = """
    The alternative novel examines nuclear espionage during the Cold War, focusing on 
    a double agent smuggling nuclear secrets. Central themes are betrayal, the arms race, 
    and the psychological toll of living with apocalyptic consequences.
    """
    
    analyzer = NovelAnalyzer()
    comparison = analyzer.compare_novels(
        nuclear_power_text, 
        other_novel_text,
        "Nuclear Power Nuclear Game",
        "Cold War Secrets"
    )
    
    if comparison:
        print(f"Similarity Score: {comparison['similarity_score']:.2f}")
        print("\nTop Features Comparison:")
        print(f"Nuclear Power Nuclear Game: {', '.join(comparison['Nuclear Power Nuclear Game_top_features'])}")
        print(f"Cold War Secrets: {', '.join(comparison['Cold War Secrets_top_features'])}")
```
