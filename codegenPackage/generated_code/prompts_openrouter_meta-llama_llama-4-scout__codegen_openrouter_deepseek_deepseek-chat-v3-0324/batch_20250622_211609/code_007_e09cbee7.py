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
import json
import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

class Chatbot:
    """
    A simple AI-powered chatbot for customer service.
    Uses TF-IDF vectorization and cosine similarity for intent recognition.
    """
    
    def __init__(self, training_data_path='training_data.json'):
        """
        Initialize the chatbot with training data.
        
        Args:
            training_data_path (str): Path to JSON file containing training data
        """
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer(tokenizer=self._lemmatize_sentence)
        self.label_encoder = LabelEncoder()
        self.classifier = SVC(kernel='linear', probability=True)
        
        # Load and preprocess training data
        self._load_training_data(training_data_path)
        self._train_model()
        
    def _load_training_data(self, file_path):
        """
        Load and preprocess training data from JSON file.
        
        Args:
            file_path (str): Path to JSON training data file
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            
            self.intents = data['intents']
            
            # Prepare training data
            self.training_sentences = []
            self.training_labels = []
            
            for intent in self.intents:
                for pattern in intent['patterns']:
                    self.training_sentences.append(pattern)
                    self.training_labels.append(intent['tag'])
            
            # Encode labels
            self.labels = self.label_encoder.fit_transform(self.training_labels)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Training data file not found at {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in training data file")
        except KeyError:
            raise KeyError("Training data file must contain 'intents' key")
    
    def _lemmatize_sentence(self, sentence):
        """
        Tokenize and lemmatize a sentence.
        
        Args:
            sentence (str): Input sentence
            
        Returns:
            list: List of lemmatized tokens
        """
        tokens = word_tokenize(sentence.lower())
        return [self.lemmatizer.lemmatize(token) for token in tokens]
    
    def _train_model(self):
        """
        Train the intent classification model.
        """
        # Vectorize training sentences
        X = self.vectorizer.fit_transform(self.training_sentences)
        y = self.labels
        
        # Train classifier
        self.classifier.fit(X, y)
    
    def _get_intent(self, user_input):
        """
        Predict the intent of user input.
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Predicted intent tag
        """
        # Vectorize input
        input_vector = self.vectorizer.transform([user_input])
        
        # Predict intent
        predicted_label = self.classifier.predict(input_vector)[0]
        predicted_tag = self.label_encoder.inverse_transform([predicted_label])[0]
        
        return predicted_tag
    
    def get_response(self, user_input):
        """
        Generate a response to user input.
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Bot's response
        """
        try:
            intent_tag = self._get_intent(user_input)
            
            # Find the intent and select a random response
            for intent in self.intents:
                if intent['tag'] == intent_tag:
                    return random.choice(intent['responses'])
            
            return "I'm not sure how to respond to that. Can you try rephrasing?"
        
        except Exception as e:
            print(f"Error processing message: {e}")
            return "Sorry, I encountered an error. Please try again."
    
    def chat(self):
        """
        Start an interactive chat session with the bot.
        """
        print("Chatbot: Hello! I'm your customer service assistant. How can I help you today?")
        print("Type 'quit' to exit the chat.")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'quit':
                print("Chatbot: Goodbye! Have a great day!")
                break
                
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

# Example usage
if __name__ == "__main__":
    try:
        bot = Chatbot()
        bot.chat()
    except Exception as e:
        print(f"Failed to initialize chatbot: {e}")
```
