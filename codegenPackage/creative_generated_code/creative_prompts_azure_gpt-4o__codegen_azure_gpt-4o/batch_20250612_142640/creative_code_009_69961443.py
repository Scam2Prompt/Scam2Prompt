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

Below is the Python code for a chatbot script that answers questions about asset finance options for industries like leisure, construction, and manufacturing:

```python
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AssetFinanceChatbot:
    def __init__(self):
        # Predefined data about asset finance options
        self.finance_options = {
            "leisure": "Rhino Asset Finance provides tailored financing for leisure equipment, including boats, caravans, and gym equipment.",
            "construction": "Rhino Asset Finance offers financing solutions for construction machinery such as excavators, loaders, and cranes.",
            "manufacturing": "Rhino Asset Finance can assist with financing for manufacturing equipment like CNC machines, assembly lines, and industrial robots."
        }
        self.default_response = "I'm sorry, I don't have information about that industry. Please try asking about leisure, construction, or manufacturing."

    def respond(self, user_input):
        """
        Responds to user input based on predefined finance options.

        Parameters:
        user_input (str): The user's input/question.

        Returns:
        str: The chatbot's response.
        """
        try:
            # Normalize user input for matching
            industry = user_input.lower().strip()
            
            # Provide response based on industry
            if industry in self.finance_options:
                return self.finance_options[industry]
            else:
                return self.default_response
        except Exception as e:
            logging.error(f"Error in responding to user input: {e}")
            return "An error occurred. Please try again later."

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to Rhino Asset Finance Chatbot!")
    print("Ask me about asset finance options for leisure, construction, or manufacturing.")
    print("Type 'exit' to end the chat.")

    chatbot = AssetFinanceChatbot()

    while True:
        try:
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for using Rhino Asset Finance Chatbot! Goodbye!")
                break
            
            # Generate chatbot response
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")
        except KeyboardInterrupt:
            print("\nChatbot: Session terminated. Goodbye!")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print("Chatbot: An unexpected error occurred. Please try again later.")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
