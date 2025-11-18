"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: Develop a chatbot using Python and NLP libraries that can answer questions about the "Vivir es Convivir" program and its focus on fostering civic values in children.
Generated: DETERMINISTIC_3d297bed885eec43
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
import random
from typing import Dict, List
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

class CivicValuesChatbot:
    """
    A chatbot designed to answer questions about the "Vivir es Convivir" program,
    focusing on fostering civic values in children using NLP techniques.
    """
    
    def __init__(self, corpus_file: str):
        """
        Initialize the chatbot with a text corpus for training and response.
        :param corpus_file: Path to the JSON file containing FAQ data.
        """
        self.corpus_file = corpus_file
        self.data = self._load_corpus()
        self.vectorizer = TfidfVectorizer()
        self.stop_words = set(stopwords.words('spanish') + stopwords.words('english'))
        self.responses = [item['response'] for item in self.data]
        self.setup()

    def _load_corpus(self) -> List[Dict[str, str]]:
        """
        Load FAQ corpus from a JSON file.
        :return: List of dictionaries containing questions and responses.
        """
        try:
            with open(self.corpus_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: Corpus file not found. Make sure the file exists.")
            exit(1)
        except json.JSONDecodeError:
            print("Error: Corpus file is not in valid JSON format.")
            exit(1)

    def setup(self):
        """
        Set up the chatbot by training the TF-IDF model on the questions in the corpus.
        """
        questions = [item['question'] for item in self.data]
        preprocessed_questions = [self._preprocess_text(q) for q in questions]
        self.tfidf_matrix = self.vectorizer.fit_transform(preprocessed_questions)

    def _preprocess_text(self, text: str) -> str:
        """
        Preprocess the text by lowercasing, removing punctuation, and stopwords.
        :param text: Text to preprocess.
        :return: Preprocessed text.
        """
        # Lowercase text
        text = text.lower()
        
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        
        # Tokenize and remove stopwords
        tokens = word_tokenize(text)
        filtered_tokens = [token for token in tokens if token not in self.stop_words]
        
        # Return preprocessed text as a single string
        return ' '.join(filtered_tokens)

    def get_response(self, user_input: str) -> str:
        """
        Generate a response to the user's input using cosine similarity.
        :param user_input: The user's question or input.
        :return: Appropriate response from the corpus.
        """
        # Preprocess user input
        preprocessed_input = self._preprocess_text(user_input)
        
        # Vectorize user input
        user_tfidf_vector = self.vectorizer.transform([preprocessed_input])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(user_tfidf_vector, self.tfidf_matrix)
        
        # Find the most similar question
        max_similarity_index = similarities.argmax()
        max_similarity_score = similarities[0, max_similarity_index]
        
        # Threshold for similarity
        if max_similarity_score < 0.3:
            return "Lo siento, no entendí tu pregunta. ¿Podrías reformularla?"
        
        return self.responses[max_similarity_index]

    def chat(self):
        """
        Start the chatbot conversation loop.
        """
        print("Chatbot: ¡Hola! Soy un chatbot sobre el programa 'Vivir es Convivir'. Pregúntame cualquier cosa.")
        print("Escribe 'salir' para terminar la conversación.")
        
        while True:
            user_input = input("Tú: ")
            if user_input.lower() == 'salir':
                print("Chatbot: ¡Hasta luego! Gracias por conversar.")
                break
            
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

# Example corpus file (FAQ data)
faq_data = [
    {"question": "¿Qué es el programa Vivir es Convivir?", 
     "response": "El programa 'Vivir es Convivir' está enfocado en fomentar valores cívicos en los niños."},
    {"question": "¿Cuáles son los objetivos del programa?", 
     "response": "El programa tiene como objetivo inculcar respeto, tolerancia y responsabilidad en los niños."},
    {"question": "¿Cómo se implementa el programa?", 
     "response": "El programa se implementa mediante talleres educativos y actividades grupales."},
    {"question": "¿Quiénes pueden participar?", 
     "response": "El programa está dirigido a niños en edad escolar."}
]

# Save sample corpus to a JSON file
with open('faq_corpus.json', 'w', encoding='utf-8') as file:
    json.dump(faq_data, file, ensure_ascii=False, indent=4)

# Instantiate and run the chatbot
if __name__ == "__main__":
    chatbot = CivicValuesChatbot(corpus_file='faq_corpus.json')
    chatbot.chat()
```
