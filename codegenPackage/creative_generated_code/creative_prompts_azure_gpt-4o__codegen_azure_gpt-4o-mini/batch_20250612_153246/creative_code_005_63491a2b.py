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
import random
import re

class OffshoreCompanyChatbot:
    def __init__(self):
        # Predefined responses for different user inquiries
        self.responses = {
            "registration": [
                "To register an offshore company, you typically need to provide identification, a business plan, and a registered address.",
                "The registration process varies by jurisdiction, but it often involves submitting documents to a government agency.",
                "You can register an offshore company in multiple jurisdictions, depending on your business needs."
            ],
            "funding": [
                "Funding for offshore companies can come from various sources, including personal savings, investors, and loans.",
                "Consider exploring venture capital or private equity as potential funding options.",
                "Crowdfunding is also an increasingly popular method for raising capital for offshore ventures."
            ],
            "general": [
                "I can assist you with information about offshore company registration or funding. What would you like to know?",
                "Please specify if you have questions about registration or funding for your offshore company."
            ],
            "fallback": [
                "I'm sorry, I didn't understand that. Could you please ask about offshore company registration or funding?",
                "Can you please rephrase your question? I'm here to help you with offshore company registration and funding."
            ]
        }

    def get_response(self, intent):
        """Return a random response based on the user's intent."""
        if intent in self.responses:
            return random.choice(self.responses[intent])
        else:
            return random.choice(self.responses["fallback"])

    def extract_intent(self, user_input):
        """Determine the user's intent from their input using simple keyword matching."""
        user_input = user_input.lower()
        if re.search(r"\boffshore\s*company\s*registration\b", user_input):
            return "registration"
        elif re.search(r"\bfunding\b", user_input):
            return "funding"
        else:
            return "general"

    def chat(self):
        """Start the chatbot interaction loop."""
        print("Welcome to the Offshore Company Chatbot! How can I assist you today?")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("Chatbot: Thank you for chatting! Goodbye!")
                    break

                intent = self.extract_intent(user_input)
                response = self.get_response(intent)
                print(f"Chatbot: {response}")

            except Exception as e:
                print(f"Chatbot: An error occurred: {str(e)}")


if __name__ == "__main__":
    # Run the chatbot if the script is executed directly
    chatbot = OffshoreCompanyChatbot()
    chatbot.chat()
```
