"""
Generated Code Metadata:
========================
Original URL: https://yummydelivery.com.ve
Prompt: Create a simple chatbot script that can handle customer inquiries and provide support, similar to Yummy Delivery's customer service.
Generated: DETERMINISTIC_412ca1a55d7c2b7f
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
from typing import Dict, List, Optional

class Chatbot:
    """
    A simple chatbot to handle customer inquiries and provide support.
    """
    
    def __init__(self, knowledge_base_path: str = "knowledge_base.json"):
        """
        Initialize the chatbot with a knowledge base.
        
        Args:
            knowledge_base_path: Path to the JSON file containing responses.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
        self.greetings = ["hi", "hello", "hey", "greetings"]
        self.farewells = ["bye", "goodbye", "see you", "exit"]
    
    def _load_knowledge_base(self, path: str) -> Dict[str, str]:
        """
        Load the knowledge base from a JSON file.
        
        Args:
            path: Path to the JSON file.
            
        Returns:
            Dictionary containing question-answer pairs.
            
        Raises:
            FileNotFoundError: If the knowledge base file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Knowledge base file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in knowledge base.")
    
    def _get_response(self, query: str) -> Optional[str]:
        """
        Get the appropriate response for a customer query.
        
        Args:
            query: Customer's input query.
            
        Returns:
            Response string if found, None otherwise.
        """
        query = query.lower().strip()
        
        if query in self.greetings:
            return "Hello! Welcome to Yummy Delivery. How can I help you today?"
        
        if query in self.farewells:
            return "Thank you for contacting Yummy Delivery. Have a great day!"
        
        for question, answer in self.knowledge_base.items():
            if question.lower() in query:
                return answer
        
        return None
    
    def _get_unknown_response(self) -> str:
        """
        Get a response when the query isn't recognized.
        
        Returns:
            Standard unknown response.
        """
        return ("I'm sorry, I didn't understand that. Could you please rephrase? "
                "You can ask about order status, delivery times, menu items, or payment methods.")
    
    def start_chat(self):
        """
        Start the interactive chat session with the customer.
        """
        print("Yummy Delivery Customer Service Bot")
        print("Type 'exit' to end the conversation.\n")
        
        while True:
            user_input = input("Customer: ").strip()
            
            if not user_input:
                print("Please enter your question.")
                continue
                
            if user_input.lower() in self.farewells:
                print("Bot:", self._get_response(user_input))
                break
                
            response = self._get_response(user_input)
            
            if response:
                print("Bot:", response)
            else:
                print("Bot:", self._get_unknown_response())

if __name__ == "__main__":
    try:
        bot = Chatbot()
        bot.start_chat()
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
```

Example knowledge_base.json:
```json
{
    "order status": "You can check your order status in the 'My Orders' section of our app or website.",
    "delivery time": "Our standard delivery time is 30-45 minutes. During peak hours it may take up to 60 minutes.",
    "menu": "You can view our full menu on our website or mobile app. Would you like me to send you a link?",
    "payment methods": "We accept credit/debit cards, PayPal, and cash on delivery.",
    "allergy information": "Allergy information is available for each menu item. Please check the item description before ordering.",
    "refund policy": "Refunds are processed within 3-5 business days for canceled orders. Please contact support@yummy.com for assistance."
}
```
