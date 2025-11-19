"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Create a chatbot script using Python that answers questions about asset finance options for industries like leisure, construction, and manufacturing, based on Rhino Asset Finance's offerings.
Generated: DETERMINISTIC_69961443ebcf7dd0
Batch ID: 20250612_142640
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

class AssetFinanceChatbot:
    """
    A chatbot that provides information about asset finance options for various industries.
    Based on Rhino Asset Finance's offerings.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with industry-specific finance options.
        """
        self.finance_options = {
            "leisure": {
                "description": "Finance options for the leisure industry",
                "options": [
                    "Equipment leasing for gyms and fitness centers",
                    "Vehicle finance for tour operators",
                    "Refinancing for existing leisure businesses",
                    "Short-term loans for seasonal businesses"
                ],
                "contact": "Contact our leisure finance specialist at leisure@rhinoassetfinance.com"
            },
            "construction": {
                "description": "Finance solutions for the construction sector",
                "options": [
                    "Plant and machinery finance",
                    "Commercial vehicle loans",
                    "Equipment hire purchase",
                    "Asset refinancing for construction firms"
                ],
                "contact": "Contact our construction finance team at construction@rhinoassetfinance.com"
            },
            "manufacturing": {
                "description": "Funding options for manufacturing businesses",
                "options": [
                    "Factory equipment financing",
                    "Technology upgrade loans",
                    "Working capital solutions",
                    "Export finance facilities"
                ],
                "contact": "Contact our manufacturing finance advisor at manufacturing@rhinoassetfinance.com"
            }
        }
        
        self.general_options = [
            "Asset refinancing",
            "Equipment leasing",
            "Commercial vehicle finance",
            "Working capital loans"
        ]
        
        self.greetings = [
            "hello", "hi", "hey", "greetings"
        ]
        
        self.exit_commands = [
            "exit", "quit", "bye", "goodbye"
        ]

    def get_industry_options(self, industry: str) -> Optional[Dict]:
        """
        Retrieve finance options for a specific industry.
        
        Args:
            industry: The industry to query (leisure, construction, manufacturing)
            
        Returns:
            Dictionary of options if industry exists, None otherwise
        """
        return self.finance_options.get(industry.lower())

    def handle_general_query(self) -> str:
        """
        Provide general information about available finance options.
        
        Returns:
            Formatted string with general options
        """
        return (
            "We offer various general asset finance options:\n"
            + "\n".join(f"- {option}" for option in self.general_options)
            + "\n\nPlease specify an industry (leisure, construction, manufacturing) "
            "for more specific information."
        )

    def process_input(self, user_input: str) -> str:
        """
        Process user input and generate appropriate response.
        
        Args:
            user_input: The text input from the user
            
        Returns:
            Appropriate response based on user input
        """
        if not user_input.strip():
            return "Please enter your query about asset finance options."
            
        lower_input = user_input.lower()
        
        # Check for greetings
        if any(greeting in lower_input for greeting in self.greetings):
            return (
                "Hello! I'm here to help with Rhino Asset Finance options. "
                "You can ask about finance for leisure, construction, or manufacturing industries, "
                "or ask about general options."
            )
            
        # Check for exit commands
        if any(exit_cmd in lower_input for exit_cmd in self.exit_commands):
            return "Goodbye! Feel free to contact us if you have more questions about asset finance."
            
        # Check for specific industries
        for industry in self.finance_options.keys():
            if industry in lower_input:
                industry_data = self.get_industry_options(industry)
                response = (
                    f"{industry_data['description']}:\n"
                    + "\n".join(f"- {option}" for option in industry_data["options"])
                    + f"\n\n{industry_data['contact']}"
                )
                return response
                
        # Check for general finance queries
        if "general" in lower_input or "options" in lower_input:
            return self.handle_general_query()
            
        # Default response for unrecognized input
        return (
            "I'm not sure I understand. Please ask about finance options for:\n"
            "- Leisure\n"
            "- Construction\n"
            "- Manufacturing\n"
            "Or ask about 'general options' for broader information."
        )

def run_chatbot():
    """
    Run the chatbot in an interactive loop.
    """
    chatbot = AssetFinanceChatbot()
    print(
        "Welcome to Rhino Asset Finance Chatbot!\n"
        "I can provide information about asset finance options for:\n"
        "- Leisure\n"
        "- Construction\n"
        "- Manufacturing\n"
        "Or ask about 'general options'.\n"
        "Type 'exit' to end the conversation.\n"
    )
    
    while True:
        try:
            user_input = input("You: ")
            response = chatbot.process_input(user_input)
            print("\nChatbot:", response, "\n")
            
            if any(exit_cmd in user_input.lower() for exit_cmd in chatbot.exit_commands):
                break
                
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye! Have a great day.")
            break
        except Exception as e:
            print("\nChatbot: Sorry, something went wrong. Please try again.")
            # In production, you might want to log this error
            # import logging
            # logging.error(f"Chatbot error: {str(e)}")

if __name__ == "__main__":
    run_chatbot()
```
