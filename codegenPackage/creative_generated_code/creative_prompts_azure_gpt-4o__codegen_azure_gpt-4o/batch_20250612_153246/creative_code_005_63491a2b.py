"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initialmile.com
Prompt: Develop a chatbot script to assist users with questions about offshore company registration and funding, inspired by the Help Center on Initial Mile.
Generated: DETERMINISTIC_63491a2b30707659
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class OffshoreCompanyChatbot:
    def __init__(self):
        """
        Initializes the chatbot with predefined knowledge base.
        """
        self.knowledge_base = {
            "offshore registration": (
                "Offshore company registration typically involves selecting a jurisdiction, "
                "preparing necessary documents, and working with a local agent to file paperwork. "
                "Popular jurisdictions include Cayman Islands, Seychelles, and Belize."
            ),
            "funding options": (
                "Funding options for offshore companies include private investments, "
                "venture capital, loans from international banks, and internal revenue generation. "
                "It's important to comply with local and international financial regulations."
            ),
            "tax benefits": (
                "Offshore companies can offer tax benefits such as reduced tax rates or exemptions. "
                "These benefits are highly dependent on the jurisdiction where the company is registered."
            ),
            "legal compliance": (
                "To ensure legal compliance, offshore companies must adhere to both the laws of the home "
                "country and the jurisdiction where they are established. This includes reporting and anti-money laundering laws."
            ),
        }

    def respond_to_query(self, user_input):
        """
        Responds to the user's query based on the predefined knowledge base.
        
        Parameters:
            user_input (str): The user's query.

        Returns:
            str: The chatbot's response.
        """
        # Normalize and match the user input to keywords
        user_input = user_input.lower()
        for keyword, response in self.knowledge_base.items():
            if re.search(r"\b" + re.escape(keyword) + r"\b", user_input):
                return response

        return "I'm sorry, I didn't understand your question. Can you please provide more details?"

    def chat(self):
        """
        Initiates the chatbot conversation loop.
        """
        print("Welcome to the Offshore Company Assistance Chatbot!")
        print("Ask me anything about offshore company registration, funding, or compliance.")
        print("Type 'exit' to end the conversation.")

        while True:
            try:
                user_input = input("\nYou: ")
                if user_input.lower() == "exit":
                    print("Chatbot: Thank you for using the Offshore Company Assistance Chatbot. Goodbye!")
                    break

                response = self.respond_to_query(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"Chatbot: An error occurred while processing your request: {e}")


if __name__ == "__main__":
    try:
        chatbot = OffshoreCompanyChatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An unexpected error occurred while starting the chatbot: {e}")
```
