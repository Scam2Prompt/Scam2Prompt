"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fiberproximus.be
Prompt: Create a chatbot script to answer user queries about fiber internet installation, exclusive promotions, and Flex pack features, referencing Fiberdeals' services.
Generated: DETERMINISTIC_e37a98165197e776
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import Dict, Tuple

class FiberDealsChatbot:
    def __init__(self):
        # Define service details and promotions
        self.services = {
            "installation": "Fiber internet installation is free with a 1-year contract.",
            "promotions": "We currently have a limited-time offer: 50% off your first 6 months!",
            "flex_pack": "Our Flex Pack allows you to customize your internet and TV bundle to fit your needs."
        }
    
    def get_response(self, user_query: str) -> str:
        """
        Generates a response based on user query.
        
        Args:
            user_query (str): The question asked by the user.
        
        Returns:
            str: The response to the user's query.
        """
        try:
            # Normalize the user query
            query = user_query.lower()

            # Check for keywords in the query
            if re.search(r'install|installation', query):
                return self.services["installation"]
            elif re.search(r'promotion|offer', query):
                return self.services["promotions"]
            elif re.search(r'flex pack|features', query):
                return self.services["flex_pack"]
            else:
                return "I'm sorry, I can only provide information about installation, promotions, and Flex Pack features."
        
        except Exception as e:
            return f"An error occurred while processing your request: {str(e)}"

def main():
    chatbot = FiberDealsChatbot()
    print("Welcome to FiberDeals Chatbot! Ask me about fiber internet installation, promotions, or Flex Pack features.")
    
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == 'exit':
            print("Chatbot: Thank you for chatting! Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
```
