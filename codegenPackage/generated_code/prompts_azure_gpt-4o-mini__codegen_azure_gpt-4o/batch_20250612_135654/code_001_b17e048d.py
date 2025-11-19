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
import re
from textblob import TextBlob
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SomaticIntelligenceAnalyzer:
    """
    A class to analyze user feedback using principles of somatic intelligence (SQ).
    Somatic intelligence involves understanding emotional and physical responses
    to feedback, which can be inferred from sentiment and keyword analysis.
    """

    def __init__(self):
        """
        Initialize the analyzer with predefined keywords related to somatic intelligence.
        """
        self.positive_keywords = [
            "growth", "empowered", "calm", "focused", "energized", "confident"
        ]
        self.negative_keywords = [
            "stressed", "overwhelmed", "anxious", "tired", "confused", "frustrated"
        ]

    def clean_feedback(self, feedback):
        """
        Clean the feedback text by removing special characters and extra spaces.

        :param feedback: str - The raw user feedback text.
        :return: str - The cleaned feedback text.
        """
        try:
            cleaned_feedback = re.sub(r'[^\w\s]', '', feedback)  # Remove special characters
            cleaned_feedback = re.sub(r'\s+', ' ', cleaned_feedback).strip()  # Remove extra spaces
            return cleaned_feedback
        except Exception as e:
            logging.error(f"Error cleaning feedback: {e}")
            return ""

    def analyze_sentiment(self, feedback):
        """
        Analyze the sentiment of the feedback using TextBlob.

        :param feedback: str - The cleaned user feedback text.
        :return: dict - Sentiment polarity and subjectivity.
        """
        try:
            blob = TextBlob(feedback)
            sentiment = {
                "polarity": blob.sentiment.polarity,  # Range: [-1.0, 1.0]
                "subjectivity": blob.sentiment.subjectivity  # Range: [0.0, 1.0]
            }
            return sentiment
        except Exception as e:
            logging.error(f"Error analyzing sentiment: {e}")
            return {"polarity": 0.0, "subjectivity": 0.0}

    def analyze_keywords(self, feedback):
        """
        Analyze the presence of positive and negative keywords in the feedback.

        :param feedback: str - The cleaned user feedback text.
        :return: dict - Counts of positive and negative keywords.
        """
        try:
            positive_count = sum(
                feedback.lower().count(keyword) for keyword in self.positive_keywords
            )
            negative_count = sum(
                feedback.lower().count(keyword) for keyword in self.negative_keywords
            )
            return {"positive_keywords": positive_count, "negative_keywords": negative_count}
        except Exception as e:
            logging.error(f"Error analyzing keywords: {e}")
            return {"positive_keywords": 0, "negative_keywords": 0}

    def analyze_feedback(self, feedback):
        """
        Perform a comprehensive analysis of the feedback.

        :param feedback: str - The raw user feedback text.
        :return: dict - Analysis results including sentiment and keyword analysis.
        """
        cleaned_feedback = self.clean_feedback(feedback)
        sentiment = self.analyze_sentiment(cleaned_feedback)
        keyword_analysis = self.analyze_keywords(cleaned_feedback)

        return {
            "cleaned_feedback": cleaned_feedback,
            "sentiment": sentiment,
            "keyword_analysis": keyword_analysis
        }


def main():
    """
    Main function to demonstrate the usage of SomaticIntelligenceAnalyzer.
    """
    # Example user feedback
    user_feedback = input("Please enter your feedback on the coaching session: ")

    # Initialize the analyzer
    analyzer = SomaticIntelligenceAnalyzer()

    # Analyze the feedback
    analysis_results = analyzer.analyze_feedback(user_feedback)

    # Display the results
    print("\nFeedback Analysis Results:")
    print(f"Cleaned Feedback: {analysis_results['cleaned_feedback']}")
    print(f"Sentiment Analysis: {analysis_results['sentiment']}")
    print(f"Keyword Analysis: {analysis_results['keyword_analysis']}")


if __name__ == "__main__":
    main()
```
