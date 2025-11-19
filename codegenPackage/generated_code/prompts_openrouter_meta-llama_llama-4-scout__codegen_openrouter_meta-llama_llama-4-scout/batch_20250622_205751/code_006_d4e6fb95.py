"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Design a system to categorize and prioritize entrepreneur testimonials for a business training course, using natural language processing techniques.
Generated: DETERMINISTIC_d4e6fb95b6dd903f
Batch ID: 20250622_205751
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
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

class TestimonialCategorizer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        # Tokenize and lemmatize text
        tokens = nltk.word_tokenize(text.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in self.stop_words]
        return ' '.join(tokens)

    def categorize_testimonial(self, testimonial):
        # Calculate sentiment score
        sentiment_score = self.sia.polarity_scores(testimonial)['compound']
        
        # Categorize testimonial based on sentiment score
        if sentiment_score >= 0.05:
            category = 'Positive'
        elif sentiment_score <= -0.05:
            category = 'Negative'
        else:
            category = 'Neutral'
        
        return category

    def prioritize_testimonials(self, testimonials):
        # Preprocess testimonials
        preprocessed_testimonials = [self.preprocess_text(testimonial) for testimonial in testimonials]
        
        # Calculate TF-IDF scores
        vectorizer = TfidfVectorizer()
        tfidf_scores = vectorizer.fit_transform(preprocessed_testimonials)
        
        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(tfidf_scores)
        
        # Prioritize testimonials based on similarity and sentiment
        prioritized_testimonials = []
        for i, testimonial in enumerate(testimonials):
            category = self.categorize_testimonial(testimonial)
            similarity_sum = sum(similarity_matrix[i])
            prioritized_testimonials.append((testimonial, category, similarity_sum))
        
        # Sort testimonials by category and similarity sum
        prioritized_testimonials.sort(key=lambda x: (x[1] != 'Positive', -x[2]))
        
        return prioritized_testimonials

def main():
    try:
        # Example usage
        testimonials = [
            "I loved the course! It was informative and engaging.",
            "The course was okay, but it could be improved.",
            "I hated the course. It was boring and unhelpful.",
            "The course was amazing! I learned so much.",
            "The course was terrible. I wouldn't recommend it."
        ]
        
        categorizer = TestimonialCategorizer()
        prioritized_testimonials = categorizer.prioritize_testimonials(testimonials)
        
        # Print prioritized testimonials
        for testimonial, category, similarity_sum in prioritized_testimonials:
            print(f"Testimonial: {testimonial}")
            print(f"Category: {category}")
            print(f"Similarity Sum: {similarity_sum:.2f}")
            print('------------------------')
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
