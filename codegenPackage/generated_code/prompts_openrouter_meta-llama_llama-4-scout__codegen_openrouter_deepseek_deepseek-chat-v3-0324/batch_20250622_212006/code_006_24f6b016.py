"""
Generated Code Metadata:
========================
Original URL: https://prospectlimited.com
Prompt: "Develop a basic FAQ chatbot in Python that answers common questions about Prospect Limited's services, such as deposit and withdrawal procedures, account balance inquiries, and password reset."
Generated: DETERMINISTIC_24f6b01692928c6d
Batch ID: 20250622_212006
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

class FAQChatbot:
    """
    A basic FAQ chatbot for Prospect Limited that answers common questions about services.
    """
    
    def __init__(self, faq_file: str = "faq_data.json"):
        """
        Initialize the chatbot with FAQ data.
        
        Args:
            faq_file (str): Path to JSON file containing FAQ data. Defaults to "faq_data.json".
        """
        self.faq_data = self._load_faq_data(faq_file)
    
    def _load_faq_data(self, file_path: str) -> Dict[str, Dict[str, str]]:
        """
        Load FAQ data from a JSON file.
        
        Args:
            file_path (str): Path to JSON file.
            
        Returns:
            Dict[str, Dict[str, str]]: Parsed FAQ data.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"FAQ data file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in FAQ data file", file_path, 0)
    
    def _get_answer(self, question_key: str) -> Optional[str]:
        """
        Retrieve answer for a given question key.
        
        Args:
            question_key (str): Key identifying the question.
            
        Returns:
            Optional[str]: The answer if found, None otherwise.
        """
        return self.faq_data.get(question_key, {}).get('answer')
    
    def get_response(self, user_input: str) -> str:
        """
        Get chatbot response based on user input.
        
        Args:
            user_input (str): User's question/input.
            
        Returns:
            str: Bot's response.
        """
        normalized_input = user_input.strip().lower()
        
        for question_key, data in self.faq_data.items():
            if normalized_input in data.get('keywords', []):
                answer = self._get_answer(question_key)
                if answer:
                    return answer
        
        return "I'm sorry, I couldn't find an answer to your question. Please contact Prospect Limited's customer support for assistance."
    
    def get_common_questions(self) -> List[str]:
        """
        Get a list of common questions the bot can answer.
        
        Returns:
            List[str]: List of common questions.
        """
        return [data['question'] for data in self.faq_data.values()]

def main():
    """
    Main function to run the FAQ chatbot.
    """
    print("Welcome to Prospect Limited's FAQ Chatbot!")
    print("Type 'exit' to quit the chat.\n")
    
    try:
        chatbot = FAQChatbot()
        
        # Display common questions
        print("Here are some common questions I can help with:")
        for i, question in enumerate(chatbot.get_common_questions(), 1):
            print(f"{i}. {question}")
        print()
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye! Have a great day.")
                break
                
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}\n")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please ensure the FAQ data file exists and is properly formatted.")

if __name__ == "__main__":
    # Example FAQ data structure (would normally be in a separate JSON file)
    example_faq_data = {
        "deposit": {
            "question": "How do I make a deposit?",
            "answer": "You can make a deposit through our mobile app, online banking portal, or at any Prospect Limited branch. For online deposits, go to 'Transfer & Pay' and select 'Deposit'.",
            "keywords": ["deposit", "add money", "fund account"]
        },
        "withdrawal": {
            "question": "How do I withdraw money?",
            "answer": "Withdrawals can be made at ATMs, through our mobile app, or at branches. Daily withdrawal limits apply based on your account type.",
            "keywords": ["withdraw", "take out money", "withdrawal"]
        },
        "balance": {
            "question": "How can I check my account balance?",
            "answer": "Check your balance via our mobile app, online banking, ATM, or by visiting a branch. You can also enable balance notifications in the app settings.",
            "keywords": ["balance", "account balance", "check balance"]
        },
        "password": {
            "question": "I forgot my password. How can I reset it?",
            "answer": "Visit our login page and click 'Forgot Password'. You'll receive instructions via email. For security, you'll need to verify your identity.",
            "keywords": ["password", "forgot password", "reset password", "login help"]
        }
    }
    
    # Create the FAQ data file if it doesn't exist
    try:
        with open("faq_data.json", 'w') as f:
            json.dump(example_faq_data, f, indent=2)
    except IOError:
        print("Warning: Could not create example FAQ data file.")
    
    main()
```
