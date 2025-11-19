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
import random

class DentalChatbot:
    def __init__(self):
        # Initialize the FAQ dictionary with common questions and answers
        self.faq = {
            "Qual o Custo da Consulta de Avaliação?": "O custo da consulta de avaliação é de R$150,00.",
            "Quais São as Condições de Pagamento?": "As condições de pagamento incluem cartão de crédito, débito e pagamento à vista.",
            "Quais Tratamentos Estão Disponíveis?": "Oferecemos tratamentos como limpeza, restaurações, ortodontia e implantes.",
            "Como Posso Agendar uma Consulta?": "Você pode agendar uma consulta pelo telefone ou pelo nosso site.",
            "Qual a Duração da Consulta?": "A duração da consulta varia, mas geralmente leva entre 30 a 60 minutos."
        }

    def get_response(self, question):
        """
        Retrieve the response for a given question from the FAQ.
        
        :param question: str - The question asked by the user.
        :return: str - The response to the question or a default message if not found.
        """
        # Normalize the question to improve matching
        normalized_question = question.strip()
        
        # Check if the question exists in the FAQ
        if normalized_question in self.faq:
            return self.faq[normalized_question]
        else:
            return "Desculpe, não tenho uma resposta para essa pergunta. Por favor, entre em contato com a clínica."

    def chat(self):
        """
        Start a chat session with the user, allowing them to ask questions.
        """
        print("Bem-vindo ao chatbot da clínica do Dr. Celso Lemos!")
        print("Você pode fazer perguntas sobre nossos serviços. Digite 'sair' para encerrar.")
        
        while True:
            user_input = input("Você: ")
            if user_input.lower() == 'sair':
                print("Chatbot: Obrigado por usar nosso serviço. Até logo!")
                break
            
            # Get the response from the chatbot
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Create an instance of the DentalChatbot and start the chat
    try:
        chatbot = DentalChatbot()
        chatbot.chat()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
```
