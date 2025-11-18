"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Design a chatbot flow using Python for answering FAQs about hair transplant techniques (FUE, FUT, PRP) and costs, referencing the details provided by Auqual Hair Services.
Generated: DETERMINISTIC_d8ca94b182bfe930
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class HairTransplantChatbot:
    def __init__(self):
        self.faqs = {
            "FUE": {
                "description": "FUE (Follicular Unit Extraction) is a minimally invasive technique where individual hair follicles are harvested and transplanted.",
                "cost": "The average cost for FUE is between $3,000 to $15,000, depending on the number of grafts required."
            },
            "FUT": {
                "description": "FUT (Follicular Unit Transplantation) involves removing a strip of scalp from the back of the head and dissecting it into follicular units.",
                "cost": "The average cost for FUT ranges from $2,500 to $10,000."
            },
            "PRP": {
                "description": "PRP (Platelet-Rich Plasma) therapy involves drawing blood, processing it to extract growth factors, and injecting it into the scalp.",
                "cost": "PRP treatments typically cost between $1,500 to $3,000 for a series of sessions."
            }
        }

    def get_response(self, user_input):
        """Processes user input and returns an appropriate response."""
        user_input = user_input.lower()

        if "fue" in user_input:
            return self.faqs["FUE"]["description"] + " " + self.faqs["FUE"]["cost"]
        elif "fut" in user_input:
            return self.faqs["FUT"]["description"] + " " + self.faqs["FUT"]["cost"]
        elif "prp" in user_input:
            return self.faqs["PRP"]["description"] + " " + self.faqs["PRP"]["cost"]
        elif re.search(r'cost', user_input):
            return "The costs vary based on the technique used. Please specify FUE, FUT, or PRP for more details."
        else:
            return "I'm sorry, I can only provide information about FUE, FUT, and PRP hair transplant techniques. Please ask me about one of these."

    def chat(self):
        """Starts a chat session with the user."""
        print("Welcome to Auqual Hair Services Chatbot! How can I help you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            
            try:
                response = self.get_response(user_input)
                print("Chatbot:", response)
            except Exception as e:
                print("Chatbot: I'm sorry, something went wrong. Please try again.")
                print(f"Error details: {e}")

if __name__ == "__main__":
    bot = HairTransplantChatbot()
    bot.chat()
```
