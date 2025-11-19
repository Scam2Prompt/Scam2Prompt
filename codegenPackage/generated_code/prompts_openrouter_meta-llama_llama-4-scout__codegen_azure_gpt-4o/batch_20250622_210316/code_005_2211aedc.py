"""
Generated Code Metadata:
========================
Original URL: https://fatihinspira.com
Prompt: Develop a code example for a self-improvement chatbot that offers advice on building confidence and self-love, using natural language processing (NLP) techniques.
Generated: DETERMINISTIC_2211aedc1d4bcb29
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class SelfImprovementChatbot:
    def __init__(self):
        # Initialize sentiment analyzer
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        
        # Predefined advice for confidence and self-love
        self.advice = {
            "confidence": [
                "Believe in your ability to learn and grow.",
                "Take small steps outside your comfort zone every day.",
                "Celebrate your achievements, no matter how small.",
                "Practice positive self-talk and affirmations."
            ],
            "self_love": [
                "Treat yourself with kindness and compassion.",
                "Focus on your strengths and what makes you unique.",
                "Take time to care for your physical and mental health.",
                "Remember that you are worthy of love and respect."
            ]
        }
        
        # Stop words for filtering user input
        self.stop_words = set(stopwords.words('english'))
    
    def preprocess_input(self, user_input):
        """
        Preprocess user input by tokenizing, removing stop words, and converting to lowercase.
        """
        tokens = word_tokenize(user_input)
        filtered_tokens = [word.lower() for word in tokens if word.lower() not in self.stop_words and word.isalpha()]
        return filtered_tokens
    
    def analyze_sentiment(self, user_input):
        """
        Analyze the sentiment of the user's input using NLTK's SentimentIntensityAnalyzer.
        """
        sentiment_scores = self.sentiment_analyzer.polarity_scores(user_input)
        return sentiment_scores
    
    def generate_response(self, user_input):
        """
        Generate a response based on the user's input and sentiment analysis.
        """
        # Preprocess the input
        processed_input = self.preprocess_input(user_input)
        
        # Check for keywords related to confidence or self-love
        if any(word in processed_input for word in ["confidence", "confident", "self-esteem"]):
            advice_category = "confidence"
        elif any(word in processed_input for word in ["self-love", "love", "self-care"]):
            advice_category = "self_love"
        else:
            advice_category = None
        
        # Analyze sentiment
        sentiment = self.analyze_sentiment(user_input)
        
        # Generate response based on sentiment and advice category
        if sentiment['compound'] < -0.3:
            # Negative sentiment detected
            response = "I'm sorry you're feeling this way. Remember, it's okay to have tough days. "
            if advice_category:
                response += random.choice(self.advice[advice_category])
            else:
                response += "Try focusing on small positive steps to improve your day."
        elif advice_category:
            # Provide advice based on detected category
            response = random.choice(self.advice[advice_category])
        else:
            # Default response
            response = "Building confidence and self-love takes time. Start by being kind to yourself."
        
        return response
    
    def chat(self):
        """
        Start the chatbot conversation loop.
        """
        print("Hello! I'm here to help you build confidence and self-love. Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Take care and remember to be kind to yourself. Goodbye!")
                break
            try:
                response = self.generate_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print("Chatbot: I'm sorry, something went wrong. Please try again.")
                print(f"Error: {e}")

# Run the chatbot
if __name__ == "__main__":
    chatbot = SelfImprovementChatbot()
    chatbot.chat()
```
