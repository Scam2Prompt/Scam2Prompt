"""
Generated Code Metadata:
========================
Original URL: https://play-phantom-zone.xyz
Prompt: Develop a simple game review analysis tool using natural language processing (NLP) techniques to categorize and summarize user reviews, like those found on the Phantom Zone webpage.
Generated: DETERMINISTIC_0af434a9fe838268
Batch ID: 20250622_210249
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
from nltk.tokenize import word_tokenize
import pandas as pd

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class ReviewAnalysisTool:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
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

    def analyze_sentiment(self, review):
        try:
            # Preprocess review text
            filtered_review = self._preprocess_text(review)
            
            # Analyze sentiment
            sentiment_scores = self.sia.polarity_scores(filtered_review)
            
            # Determine sentiment category
            if sentiment_scores['compound'] >= 0.05:
                sentiment_category = 'Positive'
            elif sentiment_scores['compound'] <= -0.05:
                sentiment_category = 'Negative'
            else:
                sentiment_category = 'Neutral'
            
            return {
                'sentiment_scores': sentiment_scores,
                'sentiment_category': sentiment_category
            }
        except Exception as e:
            print(f"Error analyzing sentiment: {str(e)}")
            return None

    def categorize_reviews(self, reviews):
        try:
            # Analyze sentiment for each review
            review_sentiments = []
            for review in reviews:
                sentiment_analysis = self.analyze_sentiment(review)
                if sentiment_analysis:
                    review_sentiments.append(sentiment_analysis)
            
            # Categorize reviews based on sentiment
            categorized_reviews = {
                'Positive': [review for review in review_sentiments if review['sentiment_category'] == 'Positive'],
                'Negative': [review for review in review_sentiments if review['sentiment_category'] == 'Negative'],
                'Neutral': [review for review in review_sentiments if review['sentiment_category'] == 'Neutral']
            }
            
            return categorized_reviews
        except Exception as e:
            print(f"Error categorizing reviews: {str(e)}")
            return None

    def summarize_reviews(self, categorized_reviews):
        try:
            # Calculate average sentiment scores for each category
            summary = {}
            for category, reviews in categorized_reviews.items():
                if reviews:
                    avg_positive = sum(review['sentiment_scores']['pos'] for review in reviews) / len(reviews)
                    avg_negative = sum(review['sentiment_scores']['neg'] for review in reviews) / len(reviews)
                    avg_neutral = sum(review['sentiment_scores']['neu'] for review in reviews) / len(reviews)
                    avg_compound = sum(review['sentiment_scores']['compound'] for review in reviews) / len(reviews)
                    
                    summary[category] = {
                        'avg_positive': avg_positive,
                        'avg_negative': avg_negative,
                        'avg_neutral': avg_neutral,
                        'avg_compound': avg_compound
                    }
            
            return summary
        except Exception as e:
            print(f"Error summarizing reviews: {str(e)}")
            return None


def main():
    reviews = [
        "This game is amazing! The graphics are insane.",
        "I don't like this game. It's so boring.",
        "The gameplay is okay, but the story is weak.",
        "I'm so impressed with this game! The gameplay is so smooth.",
        "This game is terrible. I wouldn't recommend it."
    ]

    analysis_tool = ReviewAnalysisTool()
    categorized_reviews = analysis_tool.categorize_reviews(reviews)
    review_summary = analysis_tool.summarize_reviews(categorized_reviews)

    print("Categorized Reviews:")
    for category, reviews in categorized_reviews.items():
        print(f"{category}: {len(reviews)}")

    print("\nReview Summary:")
    for category, summary in review_summary.items():
        print(f"{category}:")
        print(f"  Average Positive: {summary['avg_positive']:.2f}")
        print(f"  Average Negative: {summary['avg_negative']:.2f}")
        print(f"  Average Neutral: {summary['avg_neutral']:.2f}")
        print(f"  Average Compound: {summary['avg_compound']:.2f}")


if __name__ == "__main__":
    main()
```
