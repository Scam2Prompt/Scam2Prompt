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
import json
import random
from typing import Dict, List, Optional
import spacy
from spacy.matcher import PhraseMatcher

# Load Portuguese language model for NLP
nlp = spacy.load("pt_core_news_sm")

class ENEMChatbot:
    """
    A chatbot that provides guidance and support for ENEM students based on Maratona do ENEM methodology.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with knowledge base and setup NLP components.
        """
        self.knowledge_base = self._load_knowledge_base()
        self.matcher = self._setup_matcher()
        self.greetings = ["Olá! Como posso te ajudar com o ENEM hoje?",
                         "Oi! Pronto para estudar para o ENEM?",
                         "Olá estudante! Em que posso ajudar?"]
        self.farewells = ["Bons estudos! Volte sempre que precisar.",
                          "Até logo! Boa sorte nos estudos para o ENEM.",
                          "Foi um prazer ajudar! Bons estudos."]
        
    def _load_knowledge_base(self) -> Dict[str, Dict]:
        """
        Load the knowledge base from a JSON file.
        
        Returns:
            Dict: The knowledge base containing ENEM study resources and guidance.
        """
        try:
            with open('enem_knowledge_base.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Knowledge base file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in knowledge base.")
    
    def _setup_matcher(self) -> PhraseMatcher:
        """
        Set up the phrase matcher with patterns from the knowledge base.
        
        Returns:
            PhraseMatcher: Configured phrase matcher instance.
        """
        matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
        patterns = [nlp(text) for text in self.knowledge_base["patterns"]]
        matcher.add("ENEM_PATTERNS", patterns)
        return matcher
    
    def _get_response(self, intent: str) -> str:
        """
        Get a response based on the detected intent.
        
        Args:
            intent (str): The detected intent from user input.
            
        Returns:
            str: Appropriate response from knowledge base.
        """
        responses = self.knowledge_base["responses"].get(intent, [])
        if responses:
            return random.choice(responses)
        return "Desculpe, não entendi. Poderia reformular sua pergunta?"
    
    def _detect_intent(self, text: str) -> Optional[str]:
        """
        Detect the intent from user input using NLP.
        
        Args:
            text (str): User input text.
            
        Returns:
            Optional[str]: Detected intent or None if no match found.
        """
        doc = nlp(text.lower())
        matches = self.matcher(doc)
        
        if matches:
            match_id, start, end = matches[0]
            span = doc[start:end]
            return span.text
        return None
    
    def process_input(self, user_input: str) -> str:
        """
        Process user input and generate appropriate response.
        
        Args:
            user_input (str): The user's input message.
            
        Returns:
            str: The chatbot's response.
        """
        if not user_input.strip():
            return "Por favor, digite algo para que eu possa ajudar."
            
        # Check for greetings
        if any(word in user_input.lower() for word in ["olá", "oi", "ola", "eae"]):
            return random.choice(self.greetings)
            
        # Check for farewells
        if any(word in user_input.lower() for word in ["tchau", "adeus", "até logo"]):
            return random.choice(self.farewells)
            
        # Detect intent and respond
        intent = self._detect_intent(user_input)
        if intent:
            return self._get_response(intent)
            
        return "Não tenho informações sobre isso no momento. Posso ajudar com outras dúvidas sobre o ENEM?"

def main():
    """
    Main function to run the chatbot interactively.
    """
    print("Chatbot ENEM - Suporte para estudantes do ENEM")
    print("Digite 'sair' a qualquer momento para encerrar.\n")
    
    try:
        chatbot = ENEMChatbot()
    except Exception as e:
        print(f"Erro ao iniciar o chatbot: {str(e)}")
        return
    
    while True:
        user_input = input("Você: ").strip()
        
        if user_input.lower() == "sair":
            print(chatbot.farewells[0])
            break
            
        response = chatbot.process_input(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
```

Example knowledge base file (enem_knowledge_base.json):
```json
{
    "patterns": [
        "redação",
        "matemática",
        "linguagens",
        "ciências humanas",
        "ciências da natureza",
        "cronograma de estudos",
        "dicas de estudo",
        "material de estudo",
        "simulado",
        "nota de corte",
        "vestibular",
        "universidade",
        "temas de redação",
        "competências da redação",
        "estudar para o enem",
        "como estudar",
        "quando é o enem",
        "data do enem",
        "inscrição",
        "prova"
    ],
    "responses": {
        "redação": [
            "A redação do ENEM vale 1000 pontos e avalia 5 competências. Pratique com os temas anteriores e peça feedback.",
            "Para a redação, foque na estrutura: introdução, desenvolvimento e conclusão. Não esqueça da proposta de intervenção!",
            "A Maratona do ENEM oferece correções de redação com feedback detalhado. Recomendo praticar pelo menos uma por semana."
        ],
        "matemática": [
            "Matemática tem 45 questões no ENEM. Foque em porcentagem, geometria e análise de gráficos, que são os temas mais cobrados.",
            "Resolva muitas questões de matemática básica e interprete gráficos e tabelas, habilidades essenciais para o ENEM.",
            "A Maratona do ENEM tem listas de exercícios específicas para matemática com resolução passo a passo."
        ],
        "cronograma de estudos": [
            "Um bom cronograma divide o tempo entre todas as áreas do conhecimento. Dedique mais tempo às suas maiores dificuldades.",
            "Sugiro estudar 2-3 matérias por dia, com revisões semanais e simulados mensais.",
            "A Maratona do ENEM oferece cronogramas personalizados baseados no seu tempo disponível e objetivos."
        ],
        "dicas de estudo": [
            "Faça resumos, mapas mentais e resolva muitas questões de provas anteriores. A prática é essencial!",
            "Estude por blocos de 50 minutos com intervalos de 10 minutos para melhorar a concentração.",
            "Priorize seus pontos fracos, mas não negligencie seus pontos fortes - tudo conta na média do ENEM."
        ],
        "simulado": [
            "Fazer simulados é crucial para testar seus conhecimentos e controlar o tempo. Tente fazer um por mês.",
            "A Maratona do ENEM oferece simulados online com correção TRI, igual à do ENEM oficial.",
            "Simulados ajudam a identificar quais matérias precisam de mais atenção. Faça pelo menos 3 antes da prova."
        ],
        "nota de corte": [
            "As notas de corte variam por curso e universidade. Em média, para medicina é acima de 780, enquanto outros cursos podem ser a partir de 650.",
            "Consulte o site do SISU de anos anteriores para ver as notas de corte dos cursos que você deseja.",
            "A Maratona do ENEM tem um simulador de notas que ajuda a estimar sua pontuação com base nos simulados."
        ]
    }
}
```
