"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Develop a natural language processing (NLP) model to identify and extract key phrases and sentiments from interviews with social impact heroes on the website, focusing on their strategies and impact.
Generated: DETERMINISTIC_4079d2884afbdc33
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import spacy
from textblob import TextBlob

class NLPProcessor:
    """
    A class to process text data for extracting key phrases and sentiments.
    """

    def __init__(self):
        """
        Initialize the NLPProcessor with necessary NLP models.
        """
        # Load the spaCy English model for key phrase extraction
        self.nlp = spacy.load("en_core_web_sm")

    def extract_key_phrases(self, text):
        """
        Extract key phrases from the given text using spaCy.

        Args:
            text (str): The input text to process.

        Returns:
            list: A list of extracted key phrases.
        """
        try:
            # Process the text using spaCy
            doc = self.nlp(text)
            key_phrases = []

            # Extract noun chunks as key phrases
            for chunk in doc.noun_chunks:
                # Clean up the key phrases by removing extra spaces and special characters
                cleaned_phrase = re.sub(r'\s+', ' ', chunk.text.strip())
                key_phrases.append(cleaned_phrase)

            return key_phrases
        except Exception as e:
            print(f"Error extracting key phrases: {e}")
            return []

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the given text using TextBlob.

        Args:
            text (str): The input text to process.

        Returns:
            dict: A dictionary containing sentiment polarity and subjectivity.
        """
        try:
            # Use TextBlob to analyze sentiment
            blob = TextBlob(text)
            sentiment = {
                "polarity": blob.sentiment.polarity,  # Sentiment polarity (-1 to 1)
                "subjectivity": blob.sentiment.subjectivity  # Sentiment subjectivity (0 to 1)
            }
            return sentiment
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return {"polarity": None, "subjectivity": None}

    def process_interview(self, text):
        """
        Process an interview text to extract key phrases and sentiment.

        Args:
            text (str): The input interview text.

        Returns:
            dict: A dictionary containing key phrases and sentiment analysis.
        """
        try:
            # Extract key phrases
            key_phrases = self.extract_key_phrases(text)

            # Analyze sentiment
            sentiment = self.analyze_sentiment(text)

            return {
                "key_phrases": key_phrases,
                "sentiment": sentiment
            }
        except Exception as e:
            print(f"Error processing interview: {e}")
            return {"key_phrases": [], "sentiment": {"polarity": None, "subjectivity": None}}


# Example usage
if __name__ == "__main__":
    # Sample interview text
    interview_text = """
    Our organization focuses on providing clean water to underprivileged communities. 
    We believe that access to clean water is a fundamental human right. 
    Through our efforts, we have impacted over 10,000 lives and aim to reach even more in the coming years.
    """

    # Initialize the NLPProcessor
    processor = NLPProcessor()

    # Process the interview text
    result = processor.process_interview(interview_text)

    # Print the results
    print("Key Phrases:", result["key_phrases"])
    print("Sentiment Analysis:", result["sentiment"])
```
