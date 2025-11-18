"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Generate code for a chatbot that can answer patient queries about laboratory tests, including "fosfata alcalina," "bilirrubina total," and "coprológico funcional," using natural language processing.
Generated: DETERMINISTIC_1f68e8bf8eacceb0
Batch ID: 20250612_152827
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
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure NLTK dependencies are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Chatbot class to handle patient queries
class LabTestChatbot:
    def __init__(self):
        # Initialize supported lab tests and their descriptions
        self.lab_tests = {
            "fosfata alcalina": "La fosfatasa alcalina es una enzima relacionada con el metabolismo de los huesos y el hígado.",
            "bilirrubina total": "La bilirrubina total mide la cantidad de bilirrubina en la sangre para evaluar la función hepática.",
            "coprológico funcional": "El coprológico funcional analiza muestras de heces para evaluar la salud digestiva y detectar anomalías."
        }
        self.stop_words = set(stopwords.words('spanish'))  # Spanish stopwords for better NLP

    def preprocess_query(self, query):
        """
        Preprocesses the user query by tokenizing, converting to lowercase, and removing stopwords.

        :param query: str - User's input message
        :return: str - Cleaned query
        """
        tokens = word_tokenize(query.lower())  # Tokenize and lowercase the query
        filtered_tokens = [word for word in tokens if word not in self.stop_words]  # Remove stopwords
        return " ".join(filtered_tokens)

    def respond_to_query(self, query):
        """
        Responds to a user query by checking for supported lab tests.

        :param query: str - User's input message
        :return: str - Response from the chatbot
        """
        cleaned_query = self.preprocess_query(query)
        
        # Match the cleaned query against supported lab tests
        for test in self.lab_tests.keys():
            if re.search(test, cleaned_query):
                return f"Información sobre {test}: {self.lab_tests[test]}"
        
        # Default response for unsupported queries
        return "Lo siento, no tengo información sobre esa prueba de laboratorio. Intente preguntar sobre 'fosfata alcalina', 'bilirrubina total' o 'coprológico funcional'."

    def chat(self):
        """
        Initiates a conversation with the user.

        This method runs a loop to continuously accept user inputs and respond until the user decides to exit.
        """
        print("Hola, soy un chatbot de pruebas de laboratorio. ¿Cómo puedo ayudarte hoy?")
        print("Escribe 'salir' para terminar la conversación.")

        while True:
            user_input = input("Tú: ")
            
            # Exit the chat if the user types 'salir'
            if user_input.lower() == 'salir':
                print("Chatbot: Gracias, que tengas un buen día.")
                break

            # Generate and display the chatbot response
            try:
                response = self.respond_to_query(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print("Chatbot: Lo siento, ocurrió un error al procesar su consulta.")

# Entry point for running the chatbot
if __name__ == "__main__":
    chatbot = LabTestChatbot()
    chatbot.chat()
```
