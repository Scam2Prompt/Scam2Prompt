"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bscbhn.com
Prompt: Develop a customer service chatbot that can assist with "Centro de ayuda" queries, specifically for financial services like those on https://bscbhn.com.
Generated: DETERMINISTIC_acee3f9fbb485026
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import re

class Chatbot:
    """A simple customer service chatbot for handling 'Centro de ayuda' queries."""

    def __init__(self):
        """Initialize the chatbot with predefined responses."""
        self.responses = {
            "greeting": ["Hola! ¿En qué puedo ayudarte hoy?", "¡Bienvenido al Centro de ayuda!"],
            "farewell": ["Gracias por contactarnos. ¡Que tengas un buen día!", "Hasta luego!"],
            "financial_services": [
                "Ofrecemos una variedad de servicios financieros, incluyendo cuentas de ahorro y préstamos.",
                "Puedes consultar tus servicios financieros en nuestra página de servicios."
            ],
            "default": ["Lo siento, no entiendo tu consulta. Por favor, intenta de nuevo."]
        }

    def get_response(self, user_input):
        """Choose an appropriate response based on user input."""
        user_input = user_input.lower()
        
        if re.search(r'\b(hola|buenos días|buenas tardes|buenas noches)\b', user_input):
            return random.choice(self.responses["greeting"])
        elif re.search(r'\b(adiós|hasta luego|gracias)\b', user_input):
            return random.choice(self.responses["farewell"])
        elif re.search(r'\b(servicios financieros|cuentas|préstamos|ayuda financiera)\b', user_input):
            return random.choice(self.responses["financial_services"])
        else:
            return random.choice(self.responses["default"])

    def run(self):
        """Run the chatbot in a loop to interact with the user."""
        print("Chatbot: ¡Hola! Soy tu asistente virtual. ¿Cómo puedo ayudarte?")
        try:
            while True:
                user_input = input("Usuario: ")
                if user_input.lower() in ["salir", "exit"]:
                    print("Chatbot: Hasta luego!")
                    break
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
        except KeyboardInterrupt:
            print("\nChatbot: Hasta luego!")
        except Exception as e:
            print(f"Error: {e}. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()
```
