"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Develop a chatbot script in Python that can answer common questions about handyman services in Wellington, such as availability and pricing.
Generated: DETERMINISTIC_6a4ea76233399546
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# handyman_chatbot.py

class HandymanChatbot:
    """
    A simple chatbot that answers common questions about handyman services in Wellington.
    """

    def __init__(self):
        # Define common questions and answers
        self.qa_pairs = {
            "availability": "Our handyman services are available 7 days a week, 8am-6pm. Please contact us to schedule an appointment.",
            "pricing": "Our pricing varies depending on the task. Please contact us for a quote. We offer competitive rates and discounts for regular customers.",
            "services": "We offer a wide range of handyman services, including plumbing, electrical work, carpentry, and more. Please contact us for a full list of services.",
        }

    def process_question(self, question):
        """
        Process a user's question and return a response.

        Args:
            question (str): The user's question.

        Returns:
            str: A response to the user's question.
        """
        question = question.lower()

        if "available" in question or "availability" in question:
            return self.qa_pairs["availability"]
        elif "price" in question or "pricing" in question:
            return self.qa_pairs["pricing"]
        elif "service" in question or "services" in question:
            return self.qa_pairs["services"]
        else:
            return "Sorry, I didn't understand your question. Please contact us for more information."

    def run(self):
        """
        Run the chatbot.
        """
        print("Welcome to our handyman chatbot!")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                print("Goodbye!")
                break
            response = self.process_question(user_input)
            print("Chatbot: ", response)


if __name__ == "__main__":
    try:
        chatbot = HandymanChatbot()
        chatbot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
