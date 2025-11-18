"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Develop a chatbot using Python and NLP libraries that answers user queries about Maya Finance's loan services, including "Prêt automobile," "Prêt immobilier," and "Regroupement de crédit."
Generated: DETERMINISTIC_456e04cdad930d2e
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
import random
from typing import Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample data for Maya Finance's loan services
faq_data = {
    "Prêt automobile": [
        "Quels sont les taux d'intérêt pour le prêt automobile?",
        "Quelles sont les conditions d'éligibilité pour obtenir un prêt automobile?",
        "Est-il possible de rembourser un prêt automobile par anticipation?"
    ],
    "Prêt immobilier": [
        "Quels sont les documents nécessaires pour un prêt immobilier?",
        "Quelle est la durée maximale pour un prêt immobilier?",
        "Offrez-vous des prêts immobiliers à taux fixe?"
    ],
    "Regroupement de crédit": [
        "Qu'est-ce que le regroupement de crédit?",
        "Quels avantages offre le regroupement de crédit?",
        "Puis-je regrouper plusieurs types de prêts avec le regroupement de crédit?"
    ]
}

responses = {
    "Prêt automobile": [
        "Les taux d'intérêt pour les prêts automobiles commencent à partir de 2.5% selon la durée et le montant.",
        "Les conditions d'éligibilité incluent un revenu stable et un historique de crédit positif.",
        "Oui, le remboursement anticipé est possible, mais des frais peuvent s'appliquer."
    ],
    "Prêt immobilier": [
        "Les documents nécessaires incluent une pièce d'identité, des justificatifs de revenus et un contrat de vente.",
        "La durée maximale pour un prêt immobilier est de 30 ans.",
        "Oui, nous offrons des prêts immobiliers à taux fixe ainsi que des options à taux variable."
    ],
    "Regroupement de crédit": [
        "Le regroupement de crédit consiste à fusionner plusieurs prêts en un seul pour simplifier la gestion et réduire les mensualités.",
        "Les avantages incluent une réduction des mensualités et une simplification de la gestion des dettes.",
        "Oui, il est possible de regrouper différents types de prêts, comme les prêts personnels, immobiliers et automobiles."
    ]
}

class MayaFinanceChatbot:
    def __init__(self, faq_data: dict, responses: dict):
        """
        Initializes the chatbot with FAQ data and predefined responses.
        :param faq_data: A dictionary containing FAQs categorized by loan types.
        :param responses: A dictionary containing responses categorized by loan types.
        """
        self.faq_data = faq_data
        self.responses = responses
        self.vectorizer = TfidfVectorizer()

    def preprocess_data(self) -> None:
        """
        Preprocesses FAQ data by creating a corpus and training a TF-IDF vectorizer.
        """
        self.corpus = []
        self.mapping = []  # Keeps track of which category each FAQ belongs to
        
        for category, faqs in self.faq_data.items():
            for faq in faqs:
                self.corpus.append(faq)
                self.mapping.append(category)

        # Train the TF-IDF vectorizer
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)

    def get_response(self, user_query: str) -> Optional[str]:
        """
        Generates a response based on the user's query.
        :param user_query: The user's input query string.
        :return: A response string or None if no match is found.
        """
        try:
            # Transform user query into TF-IDF vector
            user_query_vector = self.vectorizer.transform([user_query])
            
            # Compute similarity scores
            similarity_scores = cosine_similarity(user_query_vector, self.tfidf_matrix)
            
            # Find the best match
            best_match_index = similarity_scores.argmax()
            best_match_score = similarity_scores[0][best_match_index]
            
            # Threshold to determine whether a response should be provided
            if best_match_score >= 0.3:  # Arbitrary threshold for similarity
                matched_category = self.mapping[best_match_index]
                
                # Select a random response from the matched category
                return random.choice(self.responses[matched_category])
            else:
                return "Je suis désolé, je ne peux pas répondre à cette question. Pouvez-vous reformuler?"
        except Exception as e:
            # Handle any unexpected errors
            return f"Une erreur s'est produite : {str(e)}"

# Initialize the chatbot and preprocess data
chatbot = MayaFinanceChatbot(faq_data, responses)
chatbot.preprocess_data()

def main():
    """
    Main function to initiate the chatbot interaction with the user.
    """
    print("Bienvenue chez Maya Finance! Posez vos questions sur nos services de prêt (automobile, immobilier, regroupement de crédit).")
    print("Tapez 'quit' pour terminer.")

    while True:
        user_input = input("\nVotre question: ").strip()
        if re.match(r"^(quit|exit)$", user_input, re.IGNORECASE):
            print("Merci d'avoir utilisé notre service. Au revoir!")
            break
        
        response = chatbot.get_response(user_input)
        print("\nChatbot: " + response)

if __name__ == "__main__":
    main()
```
