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
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class TestimonialAnalyzer:
    def __init__(self, testimonials):
        """
        Initializes the TestimonialAnalyzer with a list of testimonials.
        
        :param testimonials: List of strings containing testimonials from athletes.
        """
        self.testimonials = testimonials
        self.vectorizer = CountVectorizer(stop_words='english')
        self.lda_model = None

    def preprocess_data(self):
        """
        Preprocesses the testimonials to create a document-term matrix.
        
        :return: Document-term matrix.
        """
        try:
            doc_term_matrix = self.vectorizer.fit_transform(self.testimonials)
            return doc_term_matrix
        except Exception as e:
            print(f"Error in preprocessing data: {e}")
            return None

    def fit_lda_model(self, n_topics=3):
        """
        Fits an LDA model to the document-term matrix to extract topics.

        :param n_topics: Number of topics to extract. Default is 3.
        """
        doc_term_matrix = self.preprocess_data()
        if doc_term_matrix is None:
            return
        
        try:
            self.lda_model = LDA(n_components=n_topics, random_state=42)
            self.lda_model.fit(doc_term_matrix)
        except Exception as e:
            print(f"Error in fitting LDA model: {e}")

    def display_topics(self, n_words=5):
        """
        Displays the topics extracted by the LDA model.

        :param n_words: Number of words to display per topic. Default is 5.
        """
        if self.lda_model is None:
            print("LDA model has not been fitted. Please fit the model first.")
            return
        
        try:
            for index, topic in enumerate(self.lda_model.components_):
                print(f"Topic {index + 1}:")
                print(" ".join([self.vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-n_words:]]))
        except Exception as e:
            print(f"Error in displaying topics: {e}")

    def plot_topic_distribution(self):
        """
        Plots the distribution of topics across testimonials.
        """
        if self.lda_model is None:
            print("LDA model has not been fitted. Please fit the model first.")
            return

        try:
            doc_term_matrix = self.preprocess_data()
            topic_distribution = self.lda_model.transform(doc_term_matrix)
            topic_names = [f'Topic {i+1}' for i in range(topic_distribution.shape[1])]
            
            plt.figure(figsize=(10, 6))
            sns.heatmap(topic_distribution, cmap='viridis', yticklabels=range(1, len(self.testimonials)+1), xticklabels=topic_names)
            plt.title('Topic Distribution Across Testimonials')
            plt.xlabel('Topics')
            plt.ylabel('Testimonials')
            plt.show()
        except Exception as e:
            print(f"Error in plotting topic distribution: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample testimonials from athletes
    testimonials = [
        "I improved my speed significantly over the last season.",
        "The training helped me build strength and prevent injuries.",
        "I've noticed a huge difference in my sprinting times.",
        "My overall strength has increased, and I feel more resilient.",
        "I have avoided injuries thanks to a better training regimen."
    ]

    # Initialize the analyzer
    analyzer = TestimonialAnalyzer(testimonials)
    
    # Fit the LDA model
    analyzer.fit_lda_model(n_topics=2)
    
    # Display topics
    analyzer.display_topics(n_words=3)
    
    # Plot topic distribution
    analyzer.plot_topic_distribution()
```
