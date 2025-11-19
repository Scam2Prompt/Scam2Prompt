"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.org
Prompt: Develop a simple chatbot that provides investment advice and information on various asset classes, such as stocks, bonds, and real estate, using natural language processing (NLP) techniques.
Generated: DETERMINISTIC_3bdffb2214e0f0af
Batch ID: 20250622_211310
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

class InvestmentChatbot:
    def __init__(self):
        # Predefined responses for different asset classes
        self.asset_classes = {
            "stocks": [
                "Investing in stocks can provide high returns, but it also comes with higher risk.",
                "Consider diversifying your stock portfolio to mitigate risks."
            ],
            "bonds": [
                "Bonds are generally considered safer than stocks and provide fixed interest returns.",
                "Government bonds are usually less risky compared to corporate bonds."
            ],
            "real estate": [
                "Real estate can be a great long-term investment, but it requires significant capital.",
                "Consider location and market trends when investing in real estate."
            ]
        }
        self.vectorizer = TfidfVectorizer()
        self.responses = self.create_response_list()

    def create_response_list(self):
        """Create a list of all possible responses for similarity matching."""
        return [response for responses in self.asset_classes.values() for response in responses]

    def preprocess_input(self, user_input):
        """Preprocess user input by tokenizing and removing stopwords."""
        tokens = word_tokenize(user_input.lower())
        stop_words = set(stopwords.words('english'))
        return [word for word in tokens if word.isalnum() and word not in stop_words]

    def get_best_response(self, user_input):
        """Find the best response based on user input using cosine similarity."""
        try:
            # Preprocess user input
            processed_input = ' '.join(self.preprocess_input(user_input))
            # Create a matrix of TF-IDF features
            tfidf_matrix = self.vectorizer.fit_transform([processed_input] + self.responses)
            # Calculate cosine similarity
            cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
            # Get the index of the best response
            best_response_index = cosine_similarities.argmax()
            return self.responses[best_response_index]
        except Exception as e:
            return f"An error occurred while processing your request: {str(e)}"

    def chat(self):
        """Main chat loop for the chatbot."""
        print("Welcome to the Investment Chatbot! Ask me about stocks, bonds, or real estate.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            response = self.get_best_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Run the chatbot
    chatbot = InvestmentChatbot()
    chatbot.chat()
```
