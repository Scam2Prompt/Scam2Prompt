"""
Generated Code Metadata:
========================
Original URL: https://www.adelsigorta.com
Prompt: Generate a code snippet for creating a simple chatbot that provides information on Adel Sigorta's products, such as Trafik Sigortası and Tamamlayıcı Sağlık.
Generated: DETERMINISTIC_723092c428c02e0c
Batch ID: 20250622_210655
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

class AdelSigortaChatbot:
    """
    A simple chatbot that provides information about Adel Sigorta's products.
    """

    def __init__(self):
        self.products = {
            "trafik_sigortasi": {
                "name": "Trafik Sigortası",
                "description": "Zorunlu Trafik Sigortası, motorlu araç sahiplerinin yasal yükümlülüğüdür.",
                "coverage": [
                    "Üçüncü şahıslara verilen zararlar",
                    "Maddi hasarlar",
                    "Yaralanma ve ölüm halleri"
                ],
                "contact": "444 0 233"
            },
            "tamamlayici_saglik": {
                "name": "Tamamlayıcı Sağlık Sigortası",
                "description": "SGK kapsamındaki eksikleri tamamlayan özel sağlık sigortasıdır.",
                "coverage": [
                    "SGK anlaşmalı özel hastaneler",
                    "Ek teminat seçenekleri",
                    "Yatarak ve ayakta tedavi"
                ],
                "contact": "444 0 233"
            }
        }

    def get_product_info(self, product_key: str) -> Optional[Dict]:
        """
        Retrieve information about a specific product.
        
        Args:
            product_key: Key identifying the product (e.g., 'trafik_sigortasi')
            
        Returns:
            Dictionary containing product info or None if not found
        """
        return self.products.get(product_key.lower())

    def list_products(self) -> List[str]:
        """
        List all available products.
        
        Returns:
            List of product names
        """
        return [info["name"] for info in self.products.values()]

    def handle_user_input(self, user_input: str) -> str:
        """
        Process user input and generate appropriate response.
        
        Args:
            user_input: User's text input
            
        Returns:
            Bot's response as string
        """
        user_input = user_input.lower().strip()
        
        if "merhaba" in user_input or "selam" in user_input:
            return "Merhaba! Adel Sigorta hakkında bilgi almak istediğiniz ürün nedir?"
        
        elif "ürün" in user_input or "sigorta" in user_input:
            products_list = "\n- ".join(self.list_products())
            return f"Mevcut ürünlerimiz:\n- {products_list}\n\nDetay bilgi için ürün adını yazın."
        
        elif "trafik" in user_input:
            product = self.get_product_info("trafik_sigortasi")
            return self._format_product_response(product)
        
        elif "tamamlayıcı" in user_input or "sağlık" in user_input:
            product = self.get_product_info("tamamlayici_saglik")
            return self._format_product_response(product)
        
        elif "teşekkür" in user_input:
            return "Rica ederim! Başka bir konuda yardımcı olabilir miyim?"
        
        else:
            return "Üzgünüm, anlayamadım. Adel Sigorta ürünleri hakkında bilgi almak ister misiniz?"

    def _format_product_response(self, product: Dict) -> str:
        """
        Format product information into a user-friendly string.
        
        Args:
            product: Product information dictionary
            
        Returns:
            Formatted response string
        """
        if not product:
            return "Ürün bulunamadı."
            
        coverage = "\n- ".join(product["coverage"])
        return (
            f"{product['name']}:\n"
            f"{product['description']}\n\n"
            f"Kapsam:\n- {coverage}\n\n"
            f"Daha fazla bilgi için: {product['contact']}"
        )

# Example usage
if __name__ == "__main__":
    chatbot = AdelSigortaChatbot()
    print("Adel Sigorta Chatbot'a hoş geldiniz. Çıkmak için 'exit' yazın.")
    
    while True:
        user_input = input("\nSoru: ")
        if user_input.lower() == "exit":
            break
        response = chatbot.handle_user_input(user_input)
        print(f"Bot: {response}")
```
