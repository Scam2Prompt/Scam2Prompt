"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: "Develop a simple chatbot script that provides basic tax consultancy services for Egyptian clients, answering questions about tax regulations, filing procedures, and deadlines."
Generated: DETERMINISTIC_82c99a8601548567
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
import json
from datetime import datetime

class TaxConsultancyChatbot:
    def __init__(self):
        # Load tax regulations and deadlines from a JSON file
        self.tax_info = self.load_tax_info()

    def load_tax_info(self):
        """Load tax information from a JSON file."""
        try:
            with open('tax_info.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: tax_info.json file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from tax_info.json.")
            return {}

    def get_response(self, user_input):
        """Generate a response based on user input."""
        user_input = user_input.lower()
        
        if re.search(r'\b(what|how|when)\b.*\btax\b', user_input):
            return self.handle_tax_questions(user_input)
        elif re.search(r'\b(deadline|due date)\b', user_input):
            return self.get_deadline_info()
        else:
            return "I'm sorry, I can only provide information about tax regulations and deadlines."

    def handle_tax_questions(self, question):
        """Provide answers to tax-related questions."""
        if 'filing' in question:
            return "You can file your taxes online through the Egyptian Tax Authority's website."
        elif 'regulations' in question:
            return "Tax regulations in Egypt vary based on income type. Please specify your income type for more details."
        else:
            return "Please specify your question regarding tax regulations or filing procedures."

    def get_deadline_info(self):
        """Provide information about tax filing deadlines."""
        current_year = datetime.now().year
        deadlines = self.tax_info.get('deadlines', {})
        
        if current_year in deadlines:
            return f"The tax filing deadline for {current_year} is {deadlines[current_year]}."
        else:
            return "I don't have the deadline information for this year."

def main():
    """Main function to run the chatbot."""
    chatbot = TaxConsultancyChatbot()
    print("Welcome to the Egyptian Tax Consultancy Chatbot!")
    print("You can ask me about tax regulations, filing procedures, and deadlines.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Thank you for using the Tax Consultancy Chatbot. Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `tax_info.json` file in the same directory with the following structure:

```json
{
    "deadlines": {
        "2023": "April 30, 2023",
        "2024": "April 30, 2024"
    }
}
```
