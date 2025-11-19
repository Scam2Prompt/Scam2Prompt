"""
Generated Code Metadata:
========================
Original URL: https://drcelsolemos.com.br
Prompt: Generate a code snippet for a chatbot that answers common dental questions, such as "Qual o Custo da Consulta de Avaliação?" and "Quais São as Condições de Pagamento?", based on Dr. Celso Lemos' clinic's FAQ.
Generated: DETERMINISTIC_80cafa3c3e9a14ba
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, Optional

class DentalChatbot:
    """
    A simple chatbot that answers common dental questions based on Dr. Celso Lemos' clinic FAQ.
    """
    
    def __init__(self):
        self.faq: Dict[str, str] = {
            "qual o custo da consulta de avaliação": "O custo da consulta de avaliação é de R$ 200,00.",
            "quais são as condições de pagamento": "Aceitamos cartões de crédito (até 12x), débito e transferência bancária.",
            "quais são os horários de atendimento": "Atendemos de segunda a sexta, das 8h às 19h, e aos sábados das 8h às 13h.",
            "vocês aceitam convênios": "Atendemos alguns convênios. Por favor, entre em contato para verificar se o seu está na lista.",
            "qual a especialidade do dr. celso lemos": "O Dr. Celso Lemos é especializado em Ortodontia e Implantodontia.",
            "qual o tempo de duração do tratamento": "O tempo de tratamento varia caso a caso, mas em média dura entre 12 a 24 meses."
        }
        
    def clean_input(self, text: str) -> str:
        """
        Normalizes user input by removing special characters and converting to lowercase.
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip()
    
    def get_answer(self, question: str) -> Optional[str]:
        """
        Returns the answer to a question if found in FAQ, otherwise returns None.
        """
        cleaned_question = self.clean_input(question)
        
        # Check for direct matches
        if cleaned_question in self.faq:
            return self.faq[cleaned_question]
            
        # Check for partial matches
        for key in self.faq:
            if key in cleaned_question:
                return self.faq[key]
                
        return None
    
    def respond(self, question: str) -> str:
        """
        Handles user questions and returns appropriate responses.
        """
        answer = self.get_answer(question)
        
        if answer:
            return answer
        else:
            return "Desculpe, não entendi sua pergunta. Por favor, entre em contato conosco pelo telefone (XX) XXXX-XXXX para mais informações."


# Example usage
if __name__ == "__main__":
    bot = DentalChatbot()
    
    questions = [
        "Qual o Custo da Consulta de Avaliação?",
        "Quais São as Condições de Pagamento?",
        "Vocês trabalham com plano de saúde?",
        "Como faço para marcar uma consulta?"
    ]
    
    for question in questions:
        print(f"Pergunta: {question}")
        print(f"Resposta: {bot.respond(question)}\n")
```
