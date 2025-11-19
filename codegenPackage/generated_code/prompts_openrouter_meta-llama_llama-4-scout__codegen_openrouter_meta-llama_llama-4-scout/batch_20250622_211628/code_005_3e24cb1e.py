"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Write a Python program to create a simple chatbot that answers frequently asked questions about L-Zero's basketball leagues and training programs at Courtside Fitness, such as league rules, registration deadlines, and coach qualifications.
Generated: DETERMINISTIC_3e24cb1ec690bc8a
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class Chatbot:
    def __init__(self):
        # Define a dictionary to store FAQs
        self.faqs = {
            "What are the league rules?": "The league rules can be found on our website at Courtside Fitness. Generally, we emphasize sportsmanship and fair play.",
            "What are the registration deadlines?": "Registration deadlines vary by league. Please check our website for specific dates.",
            "What are the coach qualifications?": "Our coaches are certified and experienced in their respective sports.",
            "How do I register for a league?": "You can register online through our website or in-person at Courtside Fitness.",
            "What is the cost of registration?": "The cost of registration varies by league and program. Please check our website for specific pricing."
        }

        # Define a dictionary to store league information
        self.leagues = {
            "youth": {"registration_deadline": datetime.date(2024, 9, 15), "cost": 100},
            "adult": {"registration_deadline": datetime.date(2024, 8, 15), "cost": 150}
        }

    def answer_question(self, question):
        try:
            # Check if the question is in the FAQs dictionary
            if question in self.faqs:
                return self.faqs[question]
            else:
                # If not, try to parse the question for league information
                if "registration deadline" in question.lower():
                    league_type = self._parse_league_type(question)
                    if league_type:
                        return f"The registration deadline for the {league_type} league is {self.leagues[league_type]['registration_deadline']}."
                elif "cost" in question.lower():
                    league_type = self._parse_league_type(question)
                    if league_type:
                        return f"The cost of registration for the {league_type} league is ${self.leagues[league_type]['cost']}."
                return "Sorry, I didn't understand your question."
        except Exception as e:
            # Log any exceptions
            print(f"An error occurred: {e}")
            return "Sorry, I didn't understand your question."

    def _parse_league_type(self, question):
        # Try to parse the league type from the question
        for league_type in self.leagues:
            if league_type in question.lower():
                return league_type
        return None

def main():
    chatbot = Chatbot()
    print("Welcome to the Courtside Fitness L-Zero Chatbot!")
    while True:
        user_input = input("Please enter a question (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        print(chatbot.answer_question(user_input))

if __name__ == "__main__":
    main()
```
