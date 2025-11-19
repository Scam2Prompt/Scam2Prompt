"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Develop a chatbot that can facilitate discussions and activities for children to learn about civic consciousness and coexistence, inspired by the goals of the "Vivir es Convivir" program.
Generated: DETERMINISTIC_da9bf6145d726c1b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class Chatbot:
    """
    A chatbot designed to facilitate discussions and activities for children 
    to learn about civic consciousness and coexistence.
    Inspired by the "Vivir es Convivir" program.
    """
    
    def __init__(self):
        self.greetings = [
            "¡Hola! ¿Cómo estás hoy?",
            "¡Buenos días! ¿Listo para aprender sobre convivencia?",
            "¡Hola amigo! ¿Qué tal tu día?"
        ]
        self.farewells = [
            "¡Fue genial hablar contigo! Hasta la próxima.",
            "¡Adiós! Recuerda practicar lo que aprendimos hoy.",
            "¡Nos vemos pronto! Sigue siendo un buen ciudadano."
        ]
        self.topics = {
            "respeto": self._generate_respect_responses,
            "tolerancia": self._generate_tolerance_responses,
            "responsabilidad": self._generate_responsibility_responses,
            "solidaridad": self._generate_solidarity_responses
        }
        self.activities = {
            "respeto": [
                "Dibuja cómo te gustaría que te traten los demás.",
                "Escribe tres formas de mostrar respeto en tu escuela."
            ],
            "tolerancia": [
                "Haz una lista de cosas que te gustan de tus compañeros aunque sean diferentes a ti.",
                "Juega con alguien nuevo hoy y descubre qué tienen en común."
            ],
            "responsabilidad": [
                "Haz una lista de tus tareas diarias y márcalas cuando las completes.",
                "Ayuda a limpiar un espacio común en tu casa o escuela."
            ],
            "solidaridad": [
                "Haz un dibujo para alegrar el día de alguien.",
                "Pregunta a un compañero si necesita ayuda con algo."
            ]
        }
        self.current_topic = None
    
    def greet(self) -> str:
        """Return a random greeting message."""
        return random.choice(self.greetings)
    
    def farewell(self) -> str:
        """Return a random farewell message."""
        return random.choice(self.farewells)
    
    def handle_message(self, message: str) -> str:
        """
        Process the user's message and return an appropriate response.
        
        Args:
            message: The user's input message.
            
        Returns:
            A response string based on the user's input.
        """
        message = message.lower().strip()
        
        if any(word in message for word in ["hola", "hi", "buenos días", "buenas tardes"]):
            return self.greet()
        
        if any(word in message for word in ["adiós", "hasta luego", "nos vemos"]):
            return self.farewell()
        
        if "actividad" in message or "ejercicio" in message:
            if self.current_topic:
                return self._suggest_activity()
            return "Primero elige un tema (respeto, tolerancia, responsabilidad o solidaridad) para que pueda sugerirte una actividad."
        
        for topic in self.topics:
            if topic in message:
                self.current_topic = topic
                return random.choice(self.topics[topic]())
        
        return self._default_response()
    
    def _suggest_activity(self) -> str:
        """Suggest a random activity for the current topic."""
        if not self.current_topic:
            return "No hay un tema seleccionado. Por favor elige un tema primero."
        
        activities = self.activities.get(self.current_topic, [])
        if not activities:
            return f"No tengo actividades para {self.current_topic} en este momento."
        
        return f"¡Aquí tienes una actividad sobre {self.current_topic}!\n" + random.choice(activities)
    
    def _generate_respect_responses(self) -> List[str]:
        """Generate responses about respect."""
        return [
            "El respeto es fundamental para una buena convivencia. ¿Cómo muestras respeto a los demás?",
            "Todos merecemos respeto. ¿Qué significa para ti ser respetuoso?",
            "El respeto comienza con escuchar a los demás. ¿Cómo puedes practicar esto hoy?"
        ]
    
    def _generate_tolerance_responses(self) -> List[str]:
        """Generate responses about tolerance."""
        return [
            "La tolerancia nos ayuda a vivir en paz con personas diferentes. ¿Qué haces cuando no estás de acuerdo con alguien?",
            "Todos somos únicos. ¿Qué puedes aprender de alguien que es diferente a ti?",
            "La tolerancia significa aceptar que los demás piensen diferente. ¿Cómo practicas la tolerancia?"
        ]
    
    def _generate_responsibility_responses(self) -> List[str]:
        """Generate responses about responsibility."""
        return [
            "Ser responsable significa cumplir con nuestros deberes. ¿Qué responsabilidades tienes en casa o escuela?",
            "La responsabilidad nos ayuda a convivir mejor. ¿Cómo puedes ser más responsable hoy?",
            "Cuando somos responsables, ayudamos a los demás. ¿Qué tarea puedes completar para ayudar a tu familia?"
        ]
    
    def _generate_solidarity_responses(self) -> List[str]:
        """Generate responses about solidarity."""
        return [
            "La solidaridad es ayudar a quienes lo necesitan. ¿Cómo puedes ayudar a alguien hoy?",
            "Juntos somos más fuertes. ¿Qué puedes hacer para apoyar a tus compañeros?",
            "La solidaridad mejora nuestra comunidad. ¿Qué acción solidaria has hecho recientemente?"
        ]
    
    def _default_response(self) -> str:
        """Return a default response when no topic is recognized."""
        responses = [
            "Interesante. ¿Quieres hablar sobre respeto, tolerancia, responsabilidad o solidaridad?",
            "No estoy seguro de lo que quieres decir. Podemos hablar sobre cómo convivir mejor.",
            "¿Te gustaría aprender sobre valores importantes para la convivencia?"
        ]
        return random.choice(responses)


def main():
    """Run the chatbot in a simple command-line interface."""
    bot = Chatbot()
    print(bot.greet())
    print("\nPuedes hablar sobre: respeto, tolerancia, responsabilidad, solidaridad")
    print("También puedes pedir una 'actividad' sobre estos temas.")
    print("Escribe 'adiós' para terminar la conversación.\n")
    
    while True:
        user_input = input("Tú: ").strip()
        if not user_input:
            continue
            
        if user_input.lower() in ["adiós", "adios", "hasta luego", "nos vemos"]:
            print(f"Bot: {bot.farewell()}")
            break
            
        response = bot.handle_message(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
```
