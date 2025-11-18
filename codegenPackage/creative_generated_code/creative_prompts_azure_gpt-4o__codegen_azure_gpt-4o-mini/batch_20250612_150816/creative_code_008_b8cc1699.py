"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visa-pwr.com
Prompt: Create a chatbot script to assist users in navigating the visa application process, integrating insights from visapwr's customer experience priorities.
Generated: DETERMINISTIC_b8cc169964e29322
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re

class VisaChatbot:
    def __init__(self):
        """Initialize the chatbot with pre-defined responses and customer experience priorities."""
        self.responses = self.load_responses()
        self.customer_experience_priorities = self.load_customer_experience_priorities()

    def load_responses(self):
        """Load chatbot responses from a JSON file."""
        try:
            with open('responses.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: responses.json file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: responses.json file is not valid JSON.")
            return {}
    
    def load_customer_experience_priorities(self):
        """Load customer experience priorities from a JSON file."""
        try:
            with open('customer_experience_priorities.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: customer_experience_priorities.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: customer_experience_priorities.json file is not valid JSON.")
            return []

    def get_response(self, user_input):
        """Generate a response based on user input."""
        # Normalize user input for easier matching
        user_input = user_input.lower()
        
        for keyword, response in self.responses.items():
            if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
                return response
        
        # Fallback response if no keywords match
        return "I'm sorry, I didn't understand that. Can you please provide more details?"

    def start_chat(self):
        """Start the chatbot interaction with the user."""
        print("Welcome to the Visa Application Chatbot! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Chatbot: Thank you for using the Visa Application Chatbot. Goodbye!")
                break
            
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    visa_chatbot = VisaChatbot()
    visa_chatbot.start_chat()
```

**Note:** Ensure that two JSON files, `responses.json` and `customer_experience_priorities.json`, are created and populated with relevant data for the chatbot to function properly. The `responses.json` file should contain a dictionary of keywords and responses, while `customer_experience_priorities.json` can include insights that guide the conversation flow.
