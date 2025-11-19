"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Generate a code snippet for a chatbot that can handle customer inquiries for a plumbing services company, using the services listed on Limpieza de Tubos Costablanca's website.
Generated: DETERMINISTIC_5db917979e2dc4d6
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class PlumbingChatbot:
    def __init__(self):
        # List of services offered by Limpieza de Tubos Costablanca
        self.services = [
            "Desatascos",
            "Limpieza de tuberías",
            "Reparación de fugas",
            "Instalación de grifos",
            "Mantenimiento de sistemas de fontanería",
            "Inspección de tuberías con cámara",
            "Desinfección de sistemas de agua"
        ]
        self.greetings = [
            "Hola, ¿en qué puedo ayudarte hoy?",
            "¡Bienvenido! ¿Cómo puedo asistirte?",
            "¡Hola! Estoy aquí para responder tus preguntas sobre nuestros servicios."
        ]
        self.farewells = [
            "Gracias por contactarnos. ¡Que tengas un buen día!",
            "Si necesitas más ayuda, no dudes en preguntar. ¡Hasta luego!",
            "¡Adiós! Espero verte pronto."
        ]

    def get_greeting(self):
        """Return a random greeting message."""
        return random.choice(self.greetings)

    def get_services(self):
        """Return the list of services offered."""
        return self.services

    def handle_inquiry(self, inquiry):
        """Handle customer inquiries and provide appropriate responses."""
        inquiry = inquiry.lower()
        
        if "servicios" in inquiry:
            return self.list_services()
        elif "ayuda" in inquiry:
            return "Claro, ¿qué tipo de ayuda necesitas?"
        elif "gracias" in inquiry:
            return random.choice(self.farewells)
        else:
            return "Lo siento, no entiendo tu pregunta. ¿Puedes reformularla?"

    def list_services(self):
        """List all available plumbing services."""
        services_list = "Ofrecemos los siguientes servicios:\n"
        services_list += "\n".join(f"- {service}" for service in self.services)
        return services_list

def main():
    """Main function to run the chatbot."""
    chatbot = PlumbingChatbot()
    print(chatbot.get_greeting())
    
    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() in ["salir", "exit"]:
                print(chatbot.handle_inquiry("gracias"))
                break
            response = chatbot.handle_inquiry(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Error: {str(e)}. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
```
