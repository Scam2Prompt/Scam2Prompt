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
import random
from datetime import datetime

class SafetyChatbot:
    """
    A simple chatbot for customer support related to workplace safety and hygiene (Seguridad e Higiene Laboral).
    Handles common queries and provides guidance based on ISIV's program standards.
    """

    def __init__(self):
        self.greetings = [
            "Hola, ¿en qué puedo ayudarte hoy?",
            "Bienvenido/a al chatbot de Seguridad e Higiene Laboral. ¿Cómo puedo asistirte?",
            "Hola, soy tu asistente de seguridad laboral. ¿Cuál es tu consulta?"
        ]
        self.goodbyes = [
            "Hasta luego. ¡Mantente seguro/a!",
            "Adiós. Recuerda seguir las normas de seguridad.",
            "Nos vemos. No dudes en contactarnos si necesitas más ayuda."
        ]
        self.responses = {
            "equipo de protección": "El equipo de protección personal (EPP) incluye cascos, guantes, gafas de seguridad, y calzado especial. Siempre debes usarlo en áreas de riesgo.",
            "primeros auxilios": "En caso de emergencia, llama al servicio médico inmediatamente. Aplica primeros auxilios básicos si estás capacitado/a.",
            "riesgos químicos": "Maneja sustancias químicas con precaución. Usa EPP adecuado y sigue las hojas de seguridad (MSDS).",
            "ergonomía": "Asegúrate de mantener una postura correcta y haz pausas activas cada hora para evitar lesiones.",
            "incendio": "En caso de incendio, activa la alarma, evacúa el área y usa extintores solo si es seguro hacerlo.",
            "default": "Lo siento, no entendí tu consulta. Por favor, pregunta sobre equipo de protección, primeros auxilios, riesgos químicos, ergonomía o incendio."
        }

    def greet(self):
        """Return a random greeting message."""
        return random.choice(self.greetings)

    def farewell(self):
        """Return a random farewell message."""
        return random.choice(self.goodbyes)

    def respond(self, user_input):
        """
        Generate a response based on user input.
        
        Args:
            user_input (str): The user's query.
            
        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.lower()
        
        for key in self.responses:
            if key in user_input:
                return self.responses[key]
        
        return self.responses["default"]

    def log_interaction(self, user_input, response):
        """
        Log the interaction to a file for record-keeping.
        
        Args:
            user_input (str): The user's query.
            response (str): The chatbot's response.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] User: {user_input} | Bot: {response}\n"
        
        try:
            with open("chatbot_logs.txt", "a", encoding="utf-8") as file:
                file.write(log_entry)
        except IOError as e:
            print(f"Error logging interaction: {e}")

def main():
    """Main function to run the chatbot interactively."""
    bot = SafetyChatbot()
    print(bot.greet())
    
    while True:
        user_input = input("> ").strip()
        
        if user_input.lower() in ["adios", "chao", "salir", "bye"]:
            print(bot.farewell())
            break
            
        response = bot.respond(user_input)
        print(response)
        bot.log_interaction(user_input, response)

if __name__ == "__main__":
    main()
```
