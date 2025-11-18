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
    """
    A chatbot for answering FAQs about hair transplant techniques and costs 
    based on the details provided by Auqual Hair Services.
    """

    def __init__(self):
        # Initialize the FAQ data
        self.faq_data = {
            "techniques": {
                "FUE": "FUE (Follicular Unit Extraction) involves extracting individual hair follicles from the donor area and transplanting them to the thinning or balding area.",
                "FUT": "FUT (Follicular Unit Transplantation) involves removing a strip of skin with hair follicles from the donor area and transplanting them to the recipient area.",
                "PRP": "PRP (Platelet-Rich Plasma) therapy is a non-surgical procedure that uses the patient’s own platelets to stimulate natural hair growth."
            },
            "cost": {
                "FUE": "The cost of FUE typically ranges from $3,000 to $10,000 depending on the clinic and number of grafts.",
                "FUT": "The cost of FUT typically ranges from $4,000 to $12,000 depending on the clinic and number of grafts.",
                "PRP": "The cost of PRP therapy is usually between $500 to $1,500 per session."
            }
        }

    def get_response(self, user_input):
        """
        Generate a response based on user input.

        Parameters:
        user_input (str): The user's query.

        Returns:
        str: The chatbot's response.
        """
        # Normalize the input to lowercase for easier matching
        user_input = user_input.lower()

        # Check for keywords in the input and respond accordingly
        if "fue" in user_input:
            return self._generate_technique_response("FUE")
        elif "fut" in user_input:
            return self._generate_technique_response("FUT")
        elif "prp" in user_input:
            return self._generate_technique_response("PRP")
        elif "cost" in user_input or "price" in user_input:
            return self._generate_cost_response(user_input)
        else:
            return "I'm sorry, I don't understand your query. Please ask about FUE, FUT, PRP, or their costs."

    def _generate_technique_response(self, technique):
        """
        Generate a response describing a specific technique.

        Parameters:
        technique (str): The technique to describe.

        Returns:
        str: The response describing the technique.
        """
        info = self.faq_data["techniques"].get(technique, "Sorry, I don't have information about that technique.")
        return f"{info} Would you like to know about costs for {technique}?"

    def _generate_cost_response(self, user_input):
        """
        Generate a response about costs based on user input.

        Parameters:
        user_input (str): The user's query.

        Returns:
        str: The response about costs.
        """
        costs = []
        for key in self.faq_data["cost"]:
            if key.lower() in user_input:
                costs.append(f"{key}: {self.faq_data['cost'][key]}")
        
        if costs:
            return "\n".join(costs)
        return "Please specify whether you'd like cost details for FUE, FUT, or PRP."

# Entry point of the chatbot interaction
def main():
    """
    Main function to simulate chatbot interaction with the user.
    """
    print("Welcome to Auqual Hair Services FAQ Chatbot!")
    print("You can ask about FUE, FUT, PRP techniques and their costs.")

    chatbot = HairTransplantChatbot()

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if re.match(r"\b(exit|quit|bye)\b", user_input, re.IGNORECASE):
                print("Chatbot: Thank you for chatting. Goodbye!")
                break
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Chatbot: An error occurred: {e}")
            break

# Run the chatbot
if __name__ == "__main__":
    main()
```
