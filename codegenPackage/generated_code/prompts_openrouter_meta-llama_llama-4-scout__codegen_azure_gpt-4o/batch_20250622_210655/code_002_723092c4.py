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
import re

class Chatbot:
    def __init__(self):
        # Initialize chatbot with predefined responses
        self.responses = {
            "trafik sigortası": "Trafik Sigortası, araç sahipleri için zorunlu bir sigorta türüdür. Daha fazla bilgi için Adel Sigorta ile iletişime geçebilirsiniz.",
            "tamamlayıcı sağlık": "Tamamlayıcı Sağlık Sigortası, SGK anlaşmalı özel hastanelerde ek ücret ödemeden sağlık hizmeti almanızı sağlar. Detaylar için Adel Sigorta'yı ziyaret edin.",
        }
        self.default_response = "Üzgünüm, bu konuda bilgi veremiyorum. Daha fazla bilgi için Adel Sigorta ile iletişime geçebilirsiniz."

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.
        :param user_input: str - The input message from the user.
        :return: str - The chatbot's response.
        """
        # Normalize user input to lowercase for case-insensitive matching
        normalized_input = user_input.lower()

        # Search for keywords in the predefined responses
        for keyword, response in self.responses.items():
            if re.search(r'\b' + re.escape(keyword) + r'\b', normalized_input):
                return response

        # Return default response if no keyword matches
        return self.default_response


def main():
    """
    Main function to run the chatbot in a loop.
    """
    print("Adel Sigorta Chatbot'a hoş geldiniz! Sorularınızı sorabilirsiniz ('çıkış' yazarak sohbeti sonlandırabilirsiniz).")

    chatbot = Chatbot()

    while True:
        try:
            # Get user input
            user_input = input("Siz: ")

            # Exit the chatbot loop if the user types 'çıkış'
            if user_input.lower() == "çıkış":
                print("Chatbot: Görüşmek üzere! Adel Sigorta'yı tercih ettiğiniz için teşekkür ederiz.")
                break

            # Get chatbot response
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: Bir hata oluştu. Lütfen tekrar deneyin. Hata: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
