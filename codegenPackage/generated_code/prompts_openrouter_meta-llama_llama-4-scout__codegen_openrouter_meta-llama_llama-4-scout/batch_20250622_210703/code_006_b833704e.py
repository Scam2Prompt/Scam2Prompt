"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Create a chatbot that provides guidance and support for ENEM students, using the Maratona do ENEM's methodology and resources as a knowledge base."
Generated: DETERMINISTIC_b833704e4761ffca
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random
from typing import Dict

# Define a class for the chatbot
class EnemChatbot:
    def __init__(self):
        # Initialize the knowledge base with Maratona do ENEM's methodology and resources
        self.knowledge_base: Dict[str, str] = {
            "greeting": "Olá! Estou aqui para ajudá-lo a se preparar para o ENEM.",
            "goodbye": "Tchau! Boa sorte na sua prova!",
            "what_is_enem": "O ENEM é um exame nacional que avalia a qualidade da educação básica no Brasil.",
            "study_tips": "Aqui estão algumas dicas de estudo: revise os conteúdos, faça exercícios e pratique a redação.",
            "resources": "Você pode encontrar recursos de estudo no site da Maratona do ENEM."
        }

    # Define a method to handle user input
    def handle_input(self, user_input: str) -> str:
        try:
            # Convert user input to lowercase
            user_input = user_input.lower()

            # Check if user wants to exit
            if user_input in ["tchau", "sair", "exit"]:
                return self.knowledge_base["goodbye"]

            # Check if user needs help with a specific topic
            elif user_input in ["o que é enem", "enem"]:
                return self.knowledge_base["what_is_enem"]

            # Check if user needs study tips
            elif user_input in ["dicas de estudo", "estudo"]:
                return self.knowledge_base["study_tips"]

            # Check if user needs resources
            elif user_input in ["recursos", "materiais de estudo"]:
                return self.knowledge_base["resources"]

            # If user input is not recognized, provide a default response
            else:
                return "Desculpe, não entendi sua pergunta. Posso ajudá-lo com algo mais?"

        except Exception as e:
            # Log any exceptions and provide a default response
            print(f"An error occurred: {e}")
            return "Desculpe, ocorreu um erro. Posso ajudá-lo com algo mais?"

    # Define a method to start the chatbot
    def start(self):
        print(self.knowledge_base["greeting"])
        while True:
            user_input = input("> ")
            response = self.handle_input(user_input)
            print(response)
            if response == self.knowledge_base["goodbye"]:
                break

# Create an instance of the chatbot and start it
if __name__ == "__main__":
    chatbot = EnemChatbot()
    chatbot.start()
```
