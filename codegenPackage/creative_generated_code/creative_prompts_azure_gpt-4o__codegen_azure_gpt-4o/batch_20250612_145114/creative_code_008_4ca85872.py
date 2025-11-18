"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Develop a chatbot using Python that answers FAQs about roofing services, referencing King Roofing's FAQ section and service offerings.
Generated: DETERMINISTIC_4ca858720723daf5
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class RoofingChatbot:
    """
    A simple chatbot to answer FAQs about roofing services.
    This chatbot is based on King Roofing's FAQ section and service offerings.
    """

    def __init__(self):
        # Initialize the FAQ database
        self.faq_database = {
            "What services do you offer?": "King Roofing provides roof installation, repair, inspection, and maintenance.",
            "Do you provide free roof inspections?": "Yes, King Roofing offers free roof inspections to determine the condition of your roof.",
            "How long does a roof installation take?": "Typically, a roof installation takes 1-3 days depending on the size and complexity.",
            "What materials do you use for roofing?": "We use high-quality materials, including asphalt shingles, metal roofing, tiles, and more.",
            "Are you licensed and insured?": "Yes, King Roofing is fully licensed and insured for your peace of mind.",
            "Do you offer warranties?": "Yes, we provide warranties on both materials and workmanship. Please contact us for details.",
            "How can I schedule an appointment?": "You can schedule an appointment by calling us at (555-ROOFING) or visiting our website at kingroofing.com.",
            "What areas do you serve?": "We serve the entire metropolitan area and surrounding regions.",
            "How much does a roof repair cost?": "Repair costs vary depending on the extent of damage. Contact us for a free quote.",
        }
        self.default_response = "I'm sorry, I don't have information on that. Please contact King Roofing directly."

    def get_response(self, user_input):
        """
        Get a response from the chatbot based on the user's input.
        :param user_input: str, the user's question or statement
        :return: str, the chatbot's response
        """
        # Normalize user input for case-insensitive matching
        user_input = user_input.strip().lower()

        # Search the FAQ database for a matching question
        for question, answer in self.faq_database.items():
            if user_input in question.lower():
                return answer

        # Return the default response if no match is found
        return self.default_response


def run_chatbot():
    """
    Run the roofing chatbot in a loop to interact with the user.
    """
    print("Welcome to King Roofing's FAQ chatbot!")
    print("Type your question below or type 'exit' to end the chat.")

    chatbot = RoofingChatbot()

    while True:
        # Get user input
        user_input = input("\nYou: ")

        # Exit condition
        if user_input.strip().lower() == "exit":
            print("Chatbot: Thank you for chatting with King Roofing! Have a great day!")
            break

        try:
            # Get response from the chatbot
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            # Handle unexpected errors gracefully
            print("Chatbot: Oops! Something went wrong. Please try again later.")
            print(f"Error details: {e}")


# Run the chatbot program
if __name__ == "__main__":
    try:
        run_chatbot()
    except KeyboardInterrupt:
        print("\nChatbot: Chat ended. Goodbye!")
```
