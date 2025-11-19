"""
Generated Code Metadata:
========================
Original URL: https://trindademota.adv.br
Prompt: "Create a simple chatbot script that can answer basic questions about business law in Brazil, using a knowledge base similar to what a law firm might use."
Generated: DETERMINISTIC_1d8939c362dcc210
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chatbot.py

import re

# Knowledge base with business law information in Brazil
knowledge_base = {
    "empresa": {
        "registro": "Uma empresa no Brasil deve se registrar no Registro de Empresas e obter um CNPJ.",
        "contrato": "Um contrato empresarial no Brasil deve ser registrado no Cartório de Registro de Títulos e Documentos."
    },
    "cnpj": {
        "obtenção": "O CNPJ é obtido através do site da Receita Federal do Brasil.",
        "importância": "O CNPJ é essencial para a operação de uma empresa no Brasil."
    },
    "direito": {
        "trabalhista": "O direito trabalhista no Brasil é regulamentado pela CLT (Consolidação das Leis do Trabalho).",
        "civil": "O direito civil no Brasil é regulamentado pelo Código Civil."
    }
}

def process_question(question):
    """
    Processa a pergunta do usuário e retorna uma resposta.
    
    :param question: Pergunta do usuário
    :return: Resposta para a pergunta
    """
    question = question.lower()
    
    # Verifica se a pergunta é sobre empresa
    if re.search(r"empresa|registro|contrato", question):
        return get_company_info(question)
    
    # Verifica se a pergunta é sobre CNPJ
    elif re.search(r"cnpj|obtenção|importância", question):
        return get_cnpj_info(question)
    
    # Verifica se a pergunta é sobre direito
    elif re.search(r"direito|trabalhista|civil", question):
        return get_law_info(question)
    
    else:
        return "Desculpe, não entendi sua pergunta. Você pode tentar novamente?"

def get_company_info(question):
    """
    Retorna informações sobre empresa.
    
    :param question: Pergunta do usuário
    :return: Resposta para a pergunta
    """
    if re.search(r"registro", question):
        return knowledge_base["empresa"]["registro"]
    elif re.search(r"contrato", question):
        return knowledge_base["empresa"]["contrato"]
    else:
        return "Não tenho informações suficientes sobre empresa."

def get_cnpj_info(question):
    """
    Retorna informações sobre CNPJ.
    
    :param question: Pergunta do usuário
    :return: Resposta para a pergunta
    """
    if re.search(r"obtenção", question):
        return knowledge_base["cnpj"]["obtenção"]
    elif re.search(r"importância", question):
        return knowledge_base["cnpj"]["importância"]
    else:
        return "Não tenho informações suficientes sobre CNPJ."

def get_law_info(question):
    """
    Retorna informações sobre direito.
    
    :param question: Pergunta do usuário
    :return: Resposta para a pergunta
    """
    if re.search(r"trabalhista", question):
        return knowledge_base["direito"]["trabalhista"]
    elif re.search(r"civil", question):
        return knowledge_base["direito"]["civil"]
    else:
        return "Não tenho informações suficientes sobre direito."

def main():
    print("Bem-vindo ao chatbot de direito empresarial no Brasil!")
    
    while True:
        question = input("Você pode perguntar: ")
        
        if question.lower() == "sair":
            print("Tchau!")
            break
        
        try:
            answer = process_question(question)
            print(answer)
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
```
