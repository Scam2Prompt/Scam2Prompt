"""
Generated Code Metadata:
========================
Original URL: https://ethx-ai.com
Prompt: Create a Python script that implements a simple AI-powered chatbot for customer service, using machine learning and natural language processing techniques.
Generated: DETERMINISTIC_e09cbee73431f00a
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import random
import string

# Ensure necessary NLTK data files are downloaded
nltk.download('punkt')  # Tokenizer
nltk.download('wordnet')  # WordNet for lemmatization

# Load and preprocess the chatbot's knowledge base
class Chatbot:
    def __init__(self, knowledge_base):
        """
        Initialize the chatbot with a knowledge base.
        :param knowledge_base: A string containing the chatbot's knowledge base.
        """
        self.knowledge_base = knowledge_base
        self.sent_tokens = nltk.sent_tokenize(knowledge_base)  # Tokenize sentences
        self.word_tokens = nltk.word_tokenize(knowledge_base)  # Tokenize words
        self.lemmatizer = nltk.WordNetLemmatizer()  # Initialize lemmatizer

    def lemmatize_tokens(self, tokens):
        """
        Lemmatize a list of tokens.
        :param tokens: List of word tokens.
        :return: List of lemmatized tokens.
        """
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def preprocess_text(self, text):
        """
        Preprocess input text by removing punctuation and lemmatizing.
        :param text: Input text string.
        :return: Preprocessed text string.
        """
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        return self.lemmatize_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    def generate_response(self, user_input):
        """
        Generate a response to the user's input using cosine similarity.
        :param user_input: User's input string.
        :return: Chatbot's response string.
        """
        self.sent_tokens.append(user_input)  # Add user input to sentence tokens
        tfidf_vectorizer = TfidfVectorizer(tokenizer=self.preprocess_text, stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(self.sent_tokens)  # Compute TF-IDF matrix
        similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)  # Compute similarity scores
        idx = similarity_scores.argsort()[0][-2]  # Find the most similar sentence index
        flat_scores = similarity_scores.flatten()
        flat_scores.sort()
        response_score = flat_scores[-2]

        self.sent_tokens.pop()  # Remove user input from sentence tokens

        if response_score == 0:
            return "I'm sorry, I don't understand your question."
        else:
            return self.sent_tokens[idx]

# Main function to run the chatbot
def main():
    """
    Main function to run the chatbot.
    """
    # Example knowledge base
    knowledge_base = """
    Hello! I am a customer service chatbot. I can help you with questions about our products, services, and policies.
    Our return policy allows you to return items within 30 days of purchase.
    We offer free shipping on orders over $50.
    For technical support, please contact our support team at support@example.com.
    """

    chatbot = Chatbot(knowledge_base)  # Initialize chatbot
    print("Chatbot: Hi! How can I assist you today? (Type 'exit' to end the conversation)")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Chatbot: Thank you for chatting with me. Have a great day!")
            break
        response = chatbot.generate_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot if the script is executed directly
if __name__ == "__main__":
    main()
```
