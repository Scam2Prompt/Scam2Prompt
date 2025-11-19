"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Develop a prompt for a chatbot that provides customer support for a cleaning services company, answering common questions about services and scheduling.
Generated: DETERMINISTIC_e4600f4b355d7e72
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class CleaningServiceChatbot:
    """
    A chatbot for providing customer support for a cleaning services company.
    It answers common questions about services and scheduling.
    """

    def __init__(self):
        # Initialize the chatbot with predefined responses
        self.responses = {
            "services": "We offer residential and commercial cleaning services, including deep cleaning, regular cleaning, and move-in/move-out cleaning.",
            "pricing": "Our pricing depends on the type of service and the size of the area to be cleaned. Please provide more details for an accurate quote.",
            "availability": "We are available Monday through Saturday, from 8 AM to 6 PM. Let us know your preferred date and time.",
            "contact": "You can contact us at support@cleaningservices.com or call us at (555) 123-4567.",
            "reschedule": "To reschedule your appointment, please provide your current booking details and the new preferred date and time.",
            "default": "I'm sorry, I didn't understand your question. Could you please rephrase or provide more details?"
        }

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.

        Args:
            user_input (str): The user's query or message.

        Returns:
            str: The chatbot's response.
        """
        try:
            # Normalize user input for better matching
            normalized_input = user_input.lower().strip()

            # Match user input to predefined responses
            if "service" in normalized_input or "cleaning" in normalized_input:
                return self.responses["services"]
            elif "price" in normalized_input or "cost" in normalized_input:
                return self.responses["pricing"]
            elif "available" in normalized_input or "schedule" in normalized_input:
                return self.responses["availability"]
            elif "contact" in normalized_input or "phone" in normalized_input:
                return self.responses["contact"]
            elif "reschedule" in normalized_input or "change" in normalized_input:
                return self.responses["reschedule"]
            else:
                return self.responses["default"]
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"An error occurred while processing your request: {str(e)}"

def main():
    """
    Main function to simulate chatbot interaction.
    """
    print("Welcome to Cleaning Services Chatbot!")
    print("Type 'exit' to end the conversation.\n")

    chatbot = CleaningServiceChatbot()

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for using our services. Have a great day!")
            break

        # Get chatbot response
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
```
