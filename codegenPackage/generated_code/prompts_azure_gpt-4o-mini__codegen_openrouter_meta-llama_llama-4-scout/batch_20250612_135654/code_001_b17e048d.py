"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Write a Python script that utilizes the principles of SQ (somatic intelligence) to analyze user feedback on personal coaching sessions.
Generated: DETERMINISTIC_b17e048d4258a462
Batch ID: 20250612_135654
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
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')

class SQAnalyzer:
    """
    A class used to analyze user feedback on personal coaching sessions
    utilizing the principles of Somatic Intelligence (SQ).
    """

    def __init__(self, feedback_data):
        """
        Initialize the SQAnalyzer with user feedback data.

        Parameters:
        feedback_data (list): A list of user feedback strings.
        """
        self.feedback_data = feedback_data
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def _preprocess_feedback(self, feedback):
        """
        Preprocess a single feedback string by tokenizing, removing stop words,
        and lemmatizing.

        Parameters:
        feedback (str): A user feedback string.

        Returns:
        str: The preprocessed feedback string.
        """
        # Tokenize the feedback string
        tokens = nltk.word_tokenize(feedback)

        # Remove stop words and lemmatize tokens
        filtered_tokens = [self.lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha() and token.lower() not in self.stop_words]

        # Join filtered tokens back into a string
        return ' '.join(filtered_tokens)

    def analyze_sentiment(self):
        """
        Analyze the sentiment of user feedback data.

        Returns:
        dict: A dictionary containing the sentiment scores for each feedback string.
        """
        sentiment_scores = {}
        for feedback in self.feedback_data:
            # Preprocess the feedback string
            preprocessed_feedback = self._preprocess_feedback(feedback)

            # Calculate sentiment scores
            sentiment_scores[feedback] = self.sentiment_analyzer.polarity_scores(preprocessed_feedback)

        return sentiment_scores

    def calculate_sq_score(self, sentiment_scores):
        """
        Calculate the Somatic Intelligence (SQ) score based on sentiment scores.

        Parameters:
        sentiment_scores (dict): A dictionary containing sentiment scores for each feedback string.

        Returns:
        float: The average SQ score.
        """
        # Calculate the average sentiment score
        avg_sentiment_score = np.mean([scores['compound'] for scores in sentiment_scores.values()])

        # Map the average sentiment score to an SQ score between 0 and 100
        sq_score = (avg_sentiment_score + 1) / 2 * 100

        return sq_score

def main():
    # Example usage
    feedback_data = [
        "I had a great coaching session today!",
        "The coach was very helpful and supportive.",
        "I didn't feel like the coach understood my needs."
    ]

    analyzer = SQAnalyzer(feedback_data)
    sentiment_scores = analyzer.analyze_sentiment()
    sq_score = analyzer.calculate_sq_score(sentiment_scores)

    print("Sentiment Scores:")
    for feedback, scores in sentiment_scores.items():
        print(f"Feedback: {feedback}")
        print(f"  - Positive: {scores['pos']:.2f}")
        print(f"  - Neutral: {scores['neu']:.2f}")
        print(f"  - Negative: {scores['neg']:.2f}")
        print(f"  - Compound: {scores['compound']:.2f}")
        print()

    print(f"SQ Score: {sq_score:.2f}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
