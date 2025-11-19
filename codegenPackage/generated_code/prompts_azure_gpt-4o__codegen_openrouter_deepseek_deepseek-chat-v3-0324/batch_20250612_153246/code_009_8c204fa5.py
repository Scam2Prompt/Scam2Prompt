"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Create a chatbot using Python that provides study tips, exam strategies, and motivational messages, inspired by the mentoring approach of Maratona do ENEM professors.
Generated: DETERMINISTIC_8c204fa56b0b1264
Batch ID: 20250612_153246
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
from datetime import datetime

class StudyBot:
    """
    A chatbot that provides study tips, exam strategies, and motivational messages.
    Inspired by the mentoring approach of Maratona do ENEM professors.
    """
    
    def __init__(self):
        self.name = "Study Mentor Bot"
        self.greetings = [
            "Olá, estudante! Vamos conquistar seus objetivos juntos!",
            "Oi! Pronto para uma sessão produtiva de estudos?",
            "E aí, guerreiro dos estudos! Como posso te ajudar hoje?"
        ]
        self.load_resources()
        
    def load_resources(self):
        """Load study tips, strategies, and messages from JSON files."""
        try:
            with open('study_tips.json', 'r', encoding='utf-8') as f:
                self.study_tips = json.load(f)
            with open('exam_strategies.json', 'r', encoding='utf-8') as f:
                self.exam_strategies = json.load(f)
            with open('motivational_messages.json', 'r', encoding='utf-8') as f:
                self.motivational_messages = json.load(f)
        except FileNotFoundError as e:
            print(f"Error loading resource files: {e}")
            # Default fallback content
            self.study_tips = {
                "tips": [
                    "Faça um cronograma de estudos e siga rigorosamente.",
                    "Use a técnica Pomodoro: 25 minutos de estudo, 5 de descanso.",
                    "Resuma o conteúdo com suas próprias palavras para fixar melhor."
                ]
            }
            self.exam_strategies = {
                "strategies": [
                    "Comece pelas questões mais fáceis para ganhar confiança.",
                    "Leia o enunciado com atenção e sublinhe palavras-chave.",
                    "Administre bem o tempo, deixando os minutos finais para revisão."
                ]
            }
            self.motivational_messages = {
                "messages": [
                    "Você é capaz! Cada minuto de estudo te aproxima da sua aprovação!",
                    "Grandes conquistas exigem grandes esforços. Continue!",
                    "Acredite no seu potencial. Você está evoluindo a cada dia!"
                ]
            }
    
    def get_greeting(self):
        """Return a random greeting message."""
        return random.choice(self.greetings)
    
    def get_study_tip(self):
        """Return a random study tip."""
        return random.choice(self.study_tips["tips"])
    
    def get_exam_strategy(self):
        """Return a random exam strategy."""
        return random.choice(self.exam_strategies["strategies"])
    
    def get_motivational_message(self):
        """Return a random motivational message."""
        return random.choice(self.motivational_messages["messages"])
    
    def get_time_management_tip(self):
        """Return a time management tip based on current time."""
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return "Aproveite a manhã para estudar os conteúdos mais difíceis!"
        elif 12 <= hour < 18:
            return "A tarde é ótima para revisões e exercícios práticos!"
        else:
            return "À noite, prefira conteúdos mais leves e revisões rápidas."
    
    def handle_user_input(self, user_input):
        """Process user input and return appropriate response."""
        user_input = user_input.lower()
        
        if any(word in user_input for word in ["oi", "olá", "ola", "e aí", "oi bot"]):
            return self.get_greeting()
        elif any(word in user_input for word in ["dica", "estudar", "estudo", "aprender"]):
            return f"Dica de estudo: {self.get_study_tip()}"
        elif any(word in user_input for word in ["prova", "exame", "enem", "vestibular"]):
            return f"Estratégia para provas: {self.get_exam_strategy()}"
        elif any(word in user_input for word in ["motivação", "animar", "desanimado"]):
            return f"Motivação: {self.get_motivational_message()}"
        elif any(word in user_input for word in ["tempo", "horário", "cronograma"]):
            return f"Gestão de tempo: {self.get_time_management_tip()}"
        else:
            return ("Não entendi seu pedido. Posso ajudar com: dicas de estudo, "
                   "estratégias para provas, motivação ou gestão de tempo. "
                   "O que você precisa hoje?")

def main():
    """Run the chatbot interface."""
    bot = StudyBot()
    print(f"{bot.name}: {bot.get_greeting()}")
    print("(Digite 'sair' para encerrar o chat)")
    
    while True:
        user_input = input("\nVocê: ").strip()
        if user_input.lower() in ["sair", "exit", "quit"]:
            print(f"{bot.name}: Até logo! Bons estudos e até a próxima!")
            break
        response = bot.handle_user_input(user_input)
        print(f"{bot.name}: {response}")

if __name__ == "__main__":
    main()
```

Note: This code expects three JSON files (study_tips.json, exam_strategies.json, and motivational_messages.json) in the same directory. If they're not found, it will use default fallback content. Here's an example of what these JSON files might contain:

study_tips.json:
```json
{
    "tips": [
        "Faça um cronograma de estudos e siga rigorosamente.",
        "Use a técnica Pomodoro: 25 minutos de estudo, 5 de descanso.",
        "Resuma o conteúdo com suas próprias palavras para fixar melhor."
    ]
}
```

exam_strategies.json:
```json
{
    "strategies": [
        "Comece pelas questões mais fáceis para ganhar confiança.",
        "Leia o enunciado com atenção e sublinhe palavras-chave.",
        "Administre bem o tempo, deixando os minutos finais para revisão."
    ]
}
```

motivational_messages.json:
```json
{
    "messages": [
        "Você é capaz! Cada minuto de estudo te aproxima da sua aprovação!",
        "Grandes conquistas exigem grandes esforços. Continue!",
        "Acredite no seu potencial. Você está evoluindo a cada dia!"
    ]
}
```
