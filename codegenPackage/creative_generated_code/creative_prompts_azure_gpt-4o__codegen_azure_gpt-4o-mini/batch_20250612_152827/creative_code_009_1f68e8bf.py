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
import random
import nltk
from nltk.chat.util import Chat, reflections

# Ensure necessary NLTK resources are available
nltk.download('punkt')

# Define a set of responses for the chatbot regarding laboratory tests
responses = {
    "fosfata alcalina": [
        "La fosfatasa alcalina es una enzima que se encuentra en varios tejidos del cuerpo, especialmente en el hígado, los huesos, y los riñones. Los niveles elevados pueden indicar problemas en estos órganos.",
        "Los niveles de fosfatasa alcalina pueden variar dependiendo de la edad y el estado de salud. Es importante discutir los resultados con su médico."
    ],
    "bilirrubina total": [
        "La bilirrubina total es un compuesto que se forma durante la descomposición de los glóbulos rojos. Altos niveles pueden indicar problemas hepáticos o hemolíticos.",
        "Es esencial analizar la bilirrubina total junto con otros parámetros hepáticos para obtener un diagnóstico claro."
    ],
    "coprológico funcional": [
        "El coprológico funcional es un análisis que evalúa la composición y características de las heces. Ayuda en el diagnóstico de trastornos digestivos.",
        "Este examen puede detectar infecciones, inflamaciones y problemas de absorción en el intestino."
    ],
}

# Define pairs of user inputs and responses for the chatbot
pairs = [
    [r'¿Qué es la fosfata alcalina?', ["¿Te gustaría saber más sobre la fosfata alcalina?"]],
    [r'¿Qué es la bilirrubina total?', ["¿Te gustaría conocer más sobre la bilirrubina total?"]],
    [r'¿Qué es el coprológico funcional?', ["¿Te gustaría saber más sobre el coprológico funcional?"]],
    [r'¿Cuáles son los niveles normales de fosfata alcalina?', random.choice(responses["fosfata alcalina"])],
    [r'¿Cuáles son los niveles normales de bilirrubina total?', random.choice(responses["bilirrubina total"])],
    [r'¿Cuáles son los niveles normales de coprológico funcional?', random.choice(responses["coprológico funcional"])],
    [r'Salir', ["¡Gracias por usar el chatbot!"]]
]

# Initialize the chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

def start_chat():
    """
    Start the chatbot interaction with the user.
    """
    print("¡Hola! Soy tu asistente de salud. Puedes preguntarme sobre pruebas de laboratorio.")
    print("Escribe 'Salir' para terminar la conversación.")
    
    try:
        # Continuously get input from the user until they decide to exit
        chatbot.converse()
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    start_chat()
```

### Requirements:
- Before running the code, ensure that the `nltk` library is installed. You can install it using pip:
  ```bash
  pip install nltk
  ```
