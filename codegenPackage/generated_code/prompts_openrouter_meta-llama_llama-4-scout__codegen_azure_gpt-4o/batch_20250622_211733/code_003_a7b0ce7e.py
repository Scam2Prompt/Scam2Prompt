"""
Generated Code Metadata:
========================
Original URL: https://tante4dx41.com
Prompt: Create a simple FAQ chatbot using natural language processing (NLP) that can answer common questions about an online gaming platform, such as TANTE4D.
Generated: DETERMINISTIC_a7b0ce7efc6f6d72
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQChatbot:
    def __init__(self, faq_file):
        """
        Initialize the chatbot with a FAQ file.
        :param faq_file: Path to the JSON file containing FAQs.
        """
        self.faq_data = self.load_faq_data(faq_file)
        self.questions = [faq['question'] for faq in self.faq_data]
        self.answers = [faq['answer'] for faq in self.faq_data]
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def load_faq_data(self, faq_file):
        """
        Load FAQ data from a JSON file.
        :param faq_file: Path to the JSON file containing FAQs.
        :return: List of FAQs.
        """
        try:
            with open(faq_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"FAQ file '{faq_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"FAQ file '{faq_file}' is not a valid JSON file.")

    def preprocess_input(self, user_input):
        """
        Preprocess user input by removing special characters and extra spaces.
        :param user_input: Raw user input string.
        :return: Cleaned user input string.
        """
        return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', '', user_input)).strip().lower()

    def get_response(self, user_input):
        """
        Get the most relevant response to the user's input.
        :param user_input: User's input string.
        :return: Response string.
        """
        user_input = self.preprocess_input(user_input)
        user_vector = self.vectorizer.transform([user_input])
        similarity_scores = cosine_similarity(user_vector, self.question_vectors)
        best_match_index = similarity_scores.argmax()
        best_match_score = similarity_scores[0, best_match_index]

        # Threshold for similarity score to ensure meaningful responses
        if best_match_score > 0.5:
            return self.answers[best_match_index]
        else:
            return "I'm sorry, I couldn't find an answer to your question. Please try rephrasing."

def main():
    """
    Main function to run the FAQ chatbot.
    """
    faq_file = 'faq_data.json'  # Path to the FAQ JSON file
    chatbot = FAQChatbot(faq_file)

    print("Welcome to the TANTE4D FAQ Chatbot!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break

        try:
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Chatbot: An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Example `faq_data.json` file:
```json
[
    {
        "question": "What is TANTE4D?",
        "answer": "TANTE4D is an online gaming platform offering various lottery games."
    },
    {
        "question": "How do I create an account on TANTE4D?",
        "answer": "To create an account, visit the TANTE4D website and click on 'Sign Up'. Fill in the required details and submit the form."
    },
    {
        "question": "What payment methods are accepted on TANTE4D?",
        "answer": "TANTE4D accepts credit cards, debit cards, and various online payment methods such as PayPal and Skrill."
    },
    {
        "question": "How can I contact customer support?",
        "answer": "You can contact customer support via the 'Contact Us' page on the TANTE4D website or email support@tante4d.com."
    }
]
```
