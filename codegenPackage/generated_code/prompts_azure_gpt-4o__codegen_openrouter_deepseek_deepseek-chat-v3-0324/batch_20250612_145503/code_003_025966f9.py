"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: Provide an example of a Python-based AI project for beginners, aligning with the "Inteligencia artificial basico" content from https://ejecutortecnico.github.io.
Generated: DETERMINISTIC_025966f96428d7bf
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Basic AI Project: Simple Chatbot
# This is a beginner-friendly AI project that demonstrates a rule-based chatbot

import random
import time

class SimpleChatbot:
    """
    A simple rule-based chatbot that responds to user input based on predefined rules.
    """
    
    def __init__(self):
        self.greetings = ["hola", "hi", "hello", "hey", "buenos dias"]
        self.goodbyes = ["adios", "bye", "hasta luego", "nos vemos"]
        self.questions = {
            "como estas?": ["Estoy bien, gracias!", "Muy bien, ¿y tú?", "Excelente!"],
            "que puedes hacer?": ["Puedo responder preguntas simples y charlar contigo.", 
                                "Soy un chatbot básico para demostrar conceptos de IA."],
            "cual es tu nombre?": ["Me llamo ChatBot.", "Soy SimpleBot, un chatbot básico."],
            "que hora es?": self.get_current_time
        }
    
    def get_current_time(self):
        """Returns the current time"""
        return f"La hora actual es: {time.strftime('%H:%M')}"
    
    def respond(self, user_input):
        """Generates a response based on user input"""
        user_input = user_input.lower().strip()
        
        # Check for greetings
        if any(greeting in user_input for greeting in self.greetings):
            return random.choice(["¡Hola!", "¡Buenos días!", "¡Hola! ¿Cómo estás?"])
        
        # Check for goodbyes
        if any(goodbye in user_input for goodbye in self.goodbyes):
            return random.choice(["¡Adiós!", "¡Hasta luego!", "Fue un placer hablar contigo."])
        
        # Check for questions
        for question, response in self.questions.items():
            if question in user_input:
                if callable(response):
                    return response()
                return random.choice(response)
        
        # Default response if no matches found
        return random.choice([
            "No estoy seguro de entender.", 
            "¿Podrías reformular eso?", 
            "Interesante, dime más."
        ])

def main():
    """Main function to run the chatbot"""
    bot = SimpleChatbot()
    print("ChatBot: ¡Hola! Soy un chatbot simple. Escribe 'salir' para terminar la conversación.")
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("ChatBot: ¡Hasta luego!")
            break
        
        response = bot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
```
