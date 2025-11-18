"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a chatbot script that helps users find CMQLF products like "coffrets nomades" or "bains de bouche solides" based on their preferences for zero-waste and natural ingredients.
Generated: DETERMINISTIC_806a15cac488fa6d
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random


class CMQLFChatbot:
    def __init__(self):
        # Initialize the product catalog
        self.product_catalog = [
            {
                "name": "Coffrets Nomades",
                "description": "A collection of travel-friendly zero-waste personal care items.",
                "tags": ["zero-waste", "natural", "travel"]
            },
            {
                "name": "Bains de Bouche Solides",
                "description": "Solid mouthwash tablets for eco-friendly oral care.",
                "tags": ["zero-waste", "natural", "oral-care"]
            },
            {
                "name": "Savons à Froid",
                "description": "Cold-process soaps made from natural ingredients.",
                "tags": ["zero-waste", "natural", "soap"]
            },
            {
                "name": "Shampoings Solides",
                "description": "Solid shampoos with natural formulations.",
                "tags": ["zero-waste", "natural", "hair-care"]
            }
        ]

    def greet_user(self):
        # Initial greeting to the user
        print("Bonjour! Bienvenue chez CMQLF Chatbot.")
        print("Je suis ici pour vous aider à trouver des produits zéro déchet et naturels.")
        print("Quels sont vos préférences ou besoins aujourd'hui ? (ex: 'oral care', 'travel')")

    def get_user_preferences(self):
        # Ask the user for their preferences
        try:
            preferences = input("Entrez vos préférences: ").lower().strip()
            return preferences.split(",")
        except Exception as e:
            print("Erreur lors de l'analyse de vos préférences. Veuillez réessayer.")
            return []

    def find_products(self, preferences):
        # Find products matching the user's preferences
        matching_products = []
        for product in self.product_catalog:
            if any(pref.strip() in product["tags"] for pref in preferences):
                matching_products.append(product)
        return matching_products

    def display_products(self, products):
        # Display matching products to the user
        if not products:
            print("Désolé, aucun produit ne correspond à vos préférences.")
        else:
            print("\nVoici les produits que nous avons trouvés pour vous :")
            for product in products:
                print(f"- {product['name']}: {product['description']}")

    def chat(self):
        # Main chatbot logic
        self.greet_user()
        while True:
            preferences = self.get_user_preferences()
            if not preferences:
                print("Aucun préférence reçue. Voulez-vous essayer à nouveau ? (oui/non)")
                retry = input("Entrez votre choix: ").lower().strip()
                if retry != "oui":
                    print("Merci d'avoir utilisé CMQLF Chatbot. À bientôt!")
                    break
                continue

            matching_products = self.find_products(preferences)
            self.display_products(matching_products)

            print("\nVoulez-vous chercher autre chose ? (oui/non)")
            retry = input("Entrez votre choix: ").lower().strip()
            if retry != "oui":
                print("Merci d'avoir utilisé CMQLF Chatbot. À bientôt!")
                break


if __name__ == "__main__":
    try:
        # Run the chatbot
        chatbot = CMQLFChatbot()
        chatbot.chat()
    except KeyboardInterrupt:
        print("\nChat interrompu. Merci d'avoir utilisé CMQLF Chatbot. À bientôt!")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {str(e)}")
```
