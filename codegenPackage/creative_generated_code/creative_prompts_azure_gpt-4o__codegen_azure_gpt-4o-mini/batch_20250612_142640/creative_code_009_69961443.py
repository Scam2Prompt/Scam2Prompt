"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Create a chatbot script using Python that answers questions about asset finance options for industries like leisure, construction, and manufacturing, based on Rhino Asset Finance's offerings.
Generated: DETERMINISTIC_69961443ebcf7dd0
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Chatbot:
    def __init__(self):
        # Define asset finance options based on industries
        self.asset_finance_options = {
            'leisure': [
                "Leisure businesses can benefit from asset finance by acquiring equipment like gym machines or recreational vehicles.",
                "Consider financing options for commercial vehicles or hospitality equipment."
            ],
            'construction': [
                "For construction, we offer financing for heavy machinery, tools, and vehicles.",
                "Asset finance can help you manage cash flow while acquiring essential construction equipment."
            ],
            'manufacturing': [
                "Manufacturing industries can access finance for machinery, production lines, and technology upgrades.",
                "Leverage asset finance to maintain and upgrade essential manufacturing equipment."
            ]
        }
    
    def greet_user(self):
        # Greet the user
        print("Hello! I'm here to help you with asset finance options.")
    
    def get_industry_response(self, industry):
        # Provide a response based on the user's industry
        industry = industry.lower()
        if industry in self.asset_finance_options:
            return random.choice(self.asset_finance_options[industry])
        else:
            return "I'm sorry, I don't have information on that industry. Please ask about leisure, construction, or manufacturing."
    
    def run(self):
        # Main loop to run the chatbot
        self.greet_user()
        while True:
            user_input = input("Please enter an industry (leisure, construction, manufacturing) or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Thank you for chatting! Goodbye!")
                break
            
            # Handle user input and provide answers
            try:
                response = self.get_industry_response(user_input)
                print(response)
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the chatbot script
    chatbot = Chatbot()
    chatbot.run()
```
