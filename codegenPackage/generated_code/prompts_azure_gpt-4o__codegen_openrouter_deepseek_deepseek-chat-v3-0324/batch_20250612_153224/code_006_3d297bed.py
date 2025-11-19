"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Develop a chatbot using Python and NLP libraries that can answer questions about the "Vivir es Convivir" program and its focus on fostering civic values in children.
Generated: DETERMINISTIC_3d297bed885eec43
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
from spacy.matcher import PhraseMatcher
from typing import Dict, List, Optional
import random

class VivirEsConvivirChatbot:
    """
    A chatbot that answers questions about the "Vivir es Convivir" program.
    Uses NLP to understand questions and provide relevant responses.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with NLP model and knowledge base.
        """
        try:
            # Load Spanish language model for NLP processing
            self.nlp = spacy.load("es_core_news_md")
            
            # Initialize phrase matcher for keyword detection
            self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
            
            # Knowledge base about the program
            self.knowledge_base = {
                "program_description": [
                    "Vivir es Convivir es un programa educativo que promueve valores cívicos en niños.",
                    "El programa busca fomentar la convivencia pacífica y el respeto mutuo entre los niños."
                ],
                "target_audience": [
                    "El programa está dirigido a niños entre 6 y 12 años de edad.",
                    "Vivir es Convivir trabaja principalmente con estudiantes de primaria."
                ],
                "values_taught": [
                    "El programa enseña valores como respeto, tolerancia, solidaridad y responsabilidad.",
                    "Los valores principales son: honestidad, empatía, cooperación y justicia."
                ],
                "activities": [
                    "El programa incluye talleres, juegos cooperativos y actividades grupales.",
                    "Se realizan dinámicas de role-playing para practicar situaciones de convivencia."
                ],
                "benefits": [
                    "Los niños desarrollan mejores habilidades sociales y emocionales.",
                    "Mejora el clima escolar y reduce los conflictos entre estudiantes."
                ],
                "implementation": [
                    "El programa se implementa en escuelas a través de sesiones semanales.",
                    "Los docentes reciben capacitación para aplicar la metodología."
                ]
            }
            
            # Prepare patterns for the matcher
            self._prepare_patterns()
            
        except Exception as e:
            raise Exception(f"Error initializing chatbot: {str(e)}")
    
    def _prepare_patterns(self):
        """
        Prepare keyword patterns for the phrase matcher.
        """
        patterns = {
            "program_description": ["vivir es convivir", "programa", "qué es", "en qué consiste"],
            "target_audience": ["niños", "edades", "a quién va dirigido", "público objetivo"],
            "values_taught": ["valores", "enseña", "principios", "ética"],
            "activities": ["actividades", "talleres", "juegos", "qué hacen"],
            "benefits": ["beneficios", "ventajas", "para qué sirve", "resultados"],
            "implementation": ["cómo se implementa", "metodología", "aplicación", "en la escuela"]
        }
        
        for category, phrases in patterns.items():
            patterns = [self.nlp(text) for text in phrases]
            self.matcher.add(category, patterns)
    
    def _get_response(self, category: str) -> str:
        """
        Get a random response from the specified category in the knowledge base.
        """
        responses = self.knowledge_base.get(category, [])
        if not responses:
            return "No tengo información sobre ese tema."
        return random.choice(responses)
    
    def _classify_question(self, question: str) -> Optional[str]:
        """
        Classify the question into one of the known categories.
        """
        doc = self.nlp(question.lower())
        matches = self.matcher(doc)
        
        if matches:
            # Get the highest scoring match
            match_id, start, end = max(matches, key=lambda x: x[2] - x[1])
            return self.nlp.vocab.strings[match_id]
        
        return None
    
    def respond(self, user_input: str) -> str:
        """
        Generate a response to the user's input/question.
        """
        try:
            if not user_input.strip():
                return "Por favor, hazme una pregunta sobre el programa Vivir es Convivir."
            
            # Check for greetings
            doc = self.nlp(user_input.lower())
            if any(token.text in ["hola", "buenos días", "buenas tardes"] for token in doc):
                return "¡Hola! Soy un chatbot sobre el programa Vivir es Convivir. ¿En qué puedo ayudarte?"
            
            # Check for thanks/goodbye
            if any(token.text in ["gracias", "adiós", "chao"] for token in doc):
                return "¡De nada! Si tienes más preguntas sobre Vivir es Convivir, estaré encantado de ayudarte."
            
            # Classify the question
            category = self._classify_question(user_input)
            
            if category:
                return self._get_response(category)
            else:
                return "No estoy seguro de cómo responder a eso. ¿Podrías reformular tu pregunta sobre el programa Vivir es Convivir?"
                
        except Exception as e:
            return f"Lo siento, ocurrió un error al procesar tu pregunta. Por favor, inténtalo de nuevo. Error: {str(e)}"


def main():
    """
    Main function to run the chatbot interactively.
    """
    try:
        print("Inicializando chatbot Vivir es Convivir...")
        chatbot = VivirEsConvivirChatbot()
        print("¡Chatbot listo! Escribe 'salir' para terminar la conversación.")
        
        while True:
            user_input = input("\nTú: ")
            if user_input.lower() == "salir":
                print("Chatbot: ¡Hasta luego! Espero haberte ayudado con el programa Vivir es Convivir.")
                break
                
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        print("El chatbot no pudo iniciarse correctamente.")


if __name__ == "__main__":
    main()
```
