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
import random
import json

class ENEMChatbot:
    def __init__(self, knowledge_base_file):
        """
        Initializes the chatbot with a knowledge base loaded from a JSON file.

        :param knowledge_base_file: Path to the JSON file containing the knowledge base.
        """
        self.knowledge_base = self.load_knowledge_base(knowledge_base_file)

    def load_knowledge_base(self, file_path):
        """
        Loads the knowledge base from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing the knowledge base.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: The file {file_path} is not a valid JSON.")
            return {}

    def get_response(self, user_input):
        """
        Generates a response based on user input.

        :param user_input: The input string from the user.
        :return: A response string from the knowledge base or a default message.
        """
        user_input = user_input.lower()
        for key, responses in self.knowledge_base.items():
            if key in user_input:
                return random.choice(responses)
        return "Desculpe, não entendi sua pergunta. Pode reformular?"

    def chat(self):
        """
        Starts the chat session with the user.
        """
        print("Olá! Eu sou o chatbot do Maratona do ENEM. Como posso ajudar você hoje?")
        while True:
            user_input = input("Você: ")
            if user_input.lower() in ['sair', 'exit']:
                print("Chatbot: Até logo! Boa sorte nos seus estudos!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Path to the knowledge base JSON file
    knowledge_base_path = 'knowledge_base.json'
    
    # Create an instance of the ENEMChatbot
    chatbot = ENEMChatbot(knowledge_base_path)
    
    # Start the chat session
    chatbot.chat()
```

**Note:** The `knowledge_base.json` file should be structured as follows:

```json
{
    "matematica": [
        "Para matemática, é importante praticar exercícios diariamente.",
        "Recomendo revisar as fórmulas e fazer simulados."
    ],
    "redacao": [
        "A redação deve ter uma introdução clara e um desenvolvimento coerente.",
        "Pratique escrevendo sobre temas variados."
    ],
    "estudos": [
        "Organize um cronograma de estudos para cobrir todas as disciplinas.",
        "Estude em blocos de 25 minutos com intervalos de 5 minutos."
    ]
}
```

Make sure to create the `knowledge_base.json` file with appropriate content for the chatbot to function correctly.
