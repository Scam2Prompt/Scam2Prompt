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
# dental_chatbot.py

class DentalChatbot:
    def __init__(self):
        # Initialize the FAQ dictionary
        self.faq = {
            "qual o custo da consulta de avaliação?": "O custo da consulta de avaliação é de R$ 100,00.",
            "quais são as condições de pagamento?": "Nossas condições de pagamento incluem: à vista, parcelado em 2x, 3x ou 4x sem juros.",
            "o que é necessário para marcar uma consulta?": "Para marcar uma consulta, é necessário entrar em contato conosco pelo telefone ou e-mail.",
            "quais são os horários de atendimento?": "Nosso horário de atendimento é de segunda a sexta-feira, das 08h às 18h.",
        }

    def answer_question(self, question):
        """
        Answers a common dental question based on the FAQ.

        Args:
            question (str): The user's question.

        Returns:
            str: The answer to the user's question.
        """
        try:
            # Convert the question to lowercase for case-insensitive matching
            question = question.lower()

            # Check if the question exists in the FAQ
            if question in self.faq:
                return self.faq[question]
            else:
                return "Desculpe, não encontramos uma resposta para sua pergunta."
        except Exception as e:
            # Log any unexpected errors
            print(f"An error occurred: {e}")
            return "Desculpe, ocorreu um erro. Por favor, tente novamente."

    def run(self):
        """
        Runs the chatbot.
        """
        print("Bem-vindo ao chatbot da clínica do Dr. Celso Lemos!")

        while True:
            # Get the user's question
            question = input("Você tem alguma pergunta? (ou 'sair' para sair) ")

            # Exit the chatbot if the user types 'sair'
            if question.lower() == "sair":
                break

            # Answer the user's question
            answer = self.answer_question(question)
            print(answer)


if __name__ == "__main__":
    chatbot = DentalChatbot()
    chatbot.run()
```
