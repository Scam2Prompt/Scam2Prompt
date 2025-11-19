"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Develop a simple chatbot for customer support, using concepts from the Seguridad e Higiene Laboral program at ISIV."
Generated: DETERMINISTIC_39c4abbdf3a53098
Batch ID: 20250622_211504
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

class Chatbot:
    """
    A simple chatbot for customer support.
    """

    def __init__(self):
        # Initialize a dictionary with Seguridad e Higiene Laboral program topics
        self.topics: Dict[str, str] = {
            "salud": "La salud en el trabajo se refiere a las condiciones que permiten prevenir y proteger la integridad física y mental de los trabajadores.",
            "seguridad": "La seguridad laboral se enfoca en identificar y controlar los riesgos en el lugar de trabajo para prevenir accidentes y lesiones.",
            "higiene": "La higiene laboral se centra en mantener un ambiente de trabajo limpio y saludable para prevenir enfermedades ocupacionales.",
            "riesgos": "Los riesgos laborales son situaciones o condiciones que pueden causar daños a la salud o integridad física de los trabajadores.",
            "protocolos": "Los protocolos de seguridad y higiene laboral son procedimientos establecidos para garantizar la seguridad y salud en el lugar de trabajo."
        }

        # Initialize a dictionary with common questions and answers
        self.questions: Dict[str, str] = {
            "¿qué es la seguridad laboral?": self.topics["seguridad"],
            "¿qué es la higiene laboral?": self.topics["higiene"],
            "¿qué es la salud en el trabajo?": self.topics["salud"],
            "¿cuáles son los riesgos laborales?": self.topics["riesgos"],
            "¿qué son los protocolos de seguridad y higiene laboral?": self.topics["protocolos"]
        }

    def process_input(self, user_input: str) -> str:
        """
        Process user input and return a response.

        Args:
        user_input (str): The user's question or message.

        Returns:
        str: A response to the user's question or message.
        """
        try:
            # Convert user input to lowercase
            user_input = user_input.lower()

            # Check if the user's question is in the questions dictionary
            if user_input in self.questions:
                return self.questions[user_input]
            else:
                # If not, return a generic response
                return self.get_generic_response(user_input)

        except Exception as e:
            # Log any exceptions and return an error message
            print(f"An error occurred: {e}")
            return "Lo siento, no puedo procesar su solicitud en este momento."

    def get_generic_response(self, user_input: str) -> str:
        """
        Return a generic response to the user's question or message.

        Args:
        user_input (str): The user's question or message.

        Returns:
        str: A generic response to the user's question or message.
        """
        responses = [
            "Gracias por contactarnos. ¿En qué podemos ayudarlo?",
            "Por favor, revise nuestra documentación en línea para obtener más información.",
            "¿Podría proporcionar más detalles sobre su consulta?"
        ]
        return random.choice(responses)


def main():
    chatbot = Chatbot()

    print("Bienvenido al chatbot de Seguridad e Higiene Laboral")
    while True:
        user_input = input("Usuario: ")
        if user_input.lower() == "salir":
            break
        response = chatbot.process_input(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
```
