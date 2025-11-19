"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Develop a chatbot script to handle wholesale inquiries for kitchen utensils, similar to Varejão das Louças' atacado services.
Generated: DETERMINISTIC_63f558c607d0e022
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class WholesaleInquiryChatbot:
    """
    A chatbot to handle wholesale inquiries for kitchen utensils.
    Mimics the functionality of Varejão das Louças' atacado services.
    """

    def __init__(self):
        """
        Initialize the chatbot with product catalog and conversation state.
        """
        self.product_catalog = self._load_product_catalog()
        self.current_state = "GREETING"
        self.user_data = {}
        self.min_order_quantity = 10  # Minimum items for wholesale

    def _load_product_catalog(self) -> Dict[str, Dict]:
        """
        Load product catalog from a JSON file.
        
        Returns:
            Dict: Product catalog with product details
        """
        try:
            with open('product_catalog.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: Product catalog not found. Using empty catalog.")
            return {}
        except json.JSONDecodeError:
            print("Warning: Invalid product catalog format. Using empty catalog.")
            return {}

    def greet_user(self) -> str:
        """
        Generate greeting message.
        
        Returns:
            str: Welcome message
        """
        return ("Olá! Bem-vindo ao Atacado Varejão das Louças.\n"
                "Como posso ajudar com sua compra no atacado de utensílios de cozinha hoje?")

    def handle_inquiry(self, user_input: str) -> str:
        """
        Process user input and return appropriate response based on current state.
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Bot's response
        """
        user_input = user_input.lower().strip()
        
        if self.current_state == "GREETING":
            self.current_state = "PRODUCT_INQUIRY"
            return ("Temos uma variedade de produtos disponíveis para atacado.\n"
                    "Você pode perguntar sobre:\n"
                    "- Lista de produtos\n"
                    "- Preços\n"
                    "- Quantidades mínimas\n"
                    "- Condições de pagamento\n"
                    "Como posso ajudar?")

        elif self.current_state == "PRODUCT_INQUIRY":
            if "lista" in user_input or "produtos" in user_input:
                return self._list_products()
            elif "preço" in user_input or "valor" in user_input:
                self.current_state = "PRICE_INQUIRY"
                return "Por favor, informe o nome do produto que deseja consultar o preço."
            elif "quantidade" in user_input or "mínima" in user_input:
                return f"A quantidade mínima para compra no atacado é {self.min_order_quantity} itens por produto."
            elif "pagamento" in user_input or "condições" in user_input:
                return ("Condições de pagamento:\n"
                        "- À vista: 5% de desconto\n"
                        "- Cartão: Parcelamento em até 6x\n"
                        "- Boleto: Parcelamento em até 3x")
            else:
                return "Não entendi. Poderia reformular sua pergunta?"

        elif self.current_state == "PRICE_INQUIRY":
            product_response = self._get_product_price(user_input)
            self.current_state = "PRODUCT_INQUIRY"
            return product_response

        return "Desculpe, ocorreu um erro. Vamos começar novamente."

    def _list_products(self) -> str:
        """
        Generate a formatted list of available products.
        
        Returns:
            str: Formatted product list
        """
        if not self.product_catalog:
            return "No momento não temos produtos disponíveis para exibição."

        product_list = ["Nossos produtos disponíveis para atacado:"]
        for product_id, details in self.product_catalog.items():
            product_list.append(f"- {details['name']} (Código: {product_id})")
        
        return "\n".join(product_list)

    def _get_product_price(self, product_query: str) -> str:
        """
        Get price information for a product based on user query.
        
        Args:
            product_query (str): User's product query
            
        Returns:
            str: Price information or error message
        """
        found_products = []
        
        for product_id, details in self.product_catalog.items():
            if (product_query in details['name'].lower() or 
                product_query in product_id.lower()):
                found_products.append((product_id, details))
        
        if not found_products:
            return "Produto não encontrado. Por favor, verifique o nome e tente novamente."
        
        response = []
        for product_id, details in found_products:
            price_info = (f"Produto: {details['name']} (Código: {product_id})\n"
                         f"Preço unitário: R${details['price']:.2f}\n"
                         f"Preço atacado (10+ unidades): R${details['wholesale_price']:.2f}\n"
                         f"Estoque disponível: {details['stock']} unidades")
            response.append(price_info)
        
        return "\n\n".join(response)

    def reset_conversation(self):
        """Reset the conversation to initial state."""
        self.current_state = "GREETING"
        self.user_data = {}


def main():
    """Run the chatbot in interactive mode."""
    chatbot = WholesaleInquiryChatbot()
    print(chatbot.greet_user())
    
    while True:
        try:
            user_input = input("Você: ")
            if user_input.lower() in ['sair', 'exit', 'bye']:
                print("Obrigado por sua visita. Volte sempre!")
                break
                
            response = chatbot.handle_inquiry(user_input)
            print("Bot:", response)
            
        except KeyboardInterrupt:
            print("\nEncerrando o chat...")
            break
        except Exception as e:
            print("Desculpe, ocorreu um erro. Vamos recomeçar.")
            print(f"Erro: {str(e)}")
            chatbot.reset_conversation()
            print(chatbot.greet_user())


if __name__ == "__main__":
    main()
```
