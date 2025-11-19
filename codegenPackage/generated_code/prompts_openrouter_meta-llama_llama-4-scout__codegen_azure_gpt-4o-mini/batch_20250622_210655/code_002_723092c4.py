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
import random

class Chatbot:
    def __init__(self):
        self.products = {
            "Trafik Sigortası": "Trafik Sigortası, araç sahiplerinin yasal olarak zorunlu kıldığı bir sigorta türüdür. Bu sigorta, trafik kazalarında üçüncü şahıslara verebileceğiniz zararları karşılar.",
            "Tamamlayıcı Sağlık": "Tamamlayıcı Sağlık Sigortası, devlet sağlık sigortası kapsamındaki eksiklikleri tamamlamak için sunulan bir sigorta ürünüdür. Özel hastanelerde daha iyi hizmet almanızı sağlar."
        }
        self.greetings = [
            "Merhaba! Size nasıl yardımcı olabilirim?",
            "Selam! Hangi sigorta ürünleri hakkında bilgi almak istersiniz?",
            "Hoş geldiniz! Sorularınızı bekliyorum."
        ]

    def greet_user(self):
        """Greets the user with a random greeting message."""
        print(random.choice(self.greetings))

    def get_product_info(self, product_name):
        """Returns information about the specified product.

        Args:
            product_name (str): The name of the product to retrieve information for.

        Returns:
            str: Information about the product or an error message if not found.
        """
        return self.products.get(product_name, "Ürün bulunamadı. Lütfen 'Trafik Sigortası' veya 'Tamamlayıcı Sağlık' yazın.")

    def run(self):
        """Runs the chatbot, allowing user interaction."""
        self.greet_user()
        while True:
            user_input = input("Sormak istediğiniz ürün ismini yazın (çıkmak için 'çık' yazın): ")
            if user_input.lower() == 'çık':
                print("Görüşmek üzere!")
                break
            product_info = self.get_product_info(user_input)
            print(product_info)

if __name__ == "__main__":
    try:
        chatbot = Chatbot()
        chatbot.run()
    except Exception as e:
        print(f"Hata oluştu: {e}")
```
