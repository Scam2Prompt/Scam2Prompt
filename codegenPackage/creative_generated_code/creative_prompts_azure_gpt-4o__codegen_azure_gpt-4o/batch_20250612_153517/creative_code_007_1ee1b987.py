"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Create a chatbot that provides hearing aid support, including cleaning instructions and battery replacement guidance, inspired by Otex's support section.
Generated: DETERMINISTIC_1ee1b98765b80e56
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class HearingAidSupportChatbot:
    def __init__(self):
        """
        Initialize the chatbot with predefined responses for hearing aid support.
        """
        self.responses = {
            "cleaning_instructions": (
                "To clean your hearing aids:\n"
                "1. Remove the hearing aid from your ear.\n"
                "2. Use a soft, dry cloth to wipe the exterior.\n"
                "3. Ensure the microphone port is clear of debris using a small brush.\n"
                "4. Avoid using water or cleaning solutions.\n"
                "5. Regularly check and replace wax guards if applicable."
            ),
            "battery_replacement_guidance": (
                "To replace the battery in your hearing aid:\n"
                "1. Open the battery compartment using your fingernail.\n"
                "2. Remove the old battery and dispose of it properly.\n"
                "3. Insert the new battery with the positive side (+) facing up.\n"
                "4. Close the battery compartment securely.\n"
                "5. Test the hearing aid to ensure it's functioning correctly."
            ),
            "default": (
                "I'm sorry, I couldn't understand your query. "
                "Please ask about 'cleaning instructions' or 'battery replacement guidance'."
            )
        }

    def get_response(self, user_input):
        """
        Get a response based on the user's input.
        
        Args:
            user_input (str): The input message provided by the user.

        Returns:
            str: A response message based on the user's query.
        """
        # Clean and standardize user input
        user_input = user_input.strip().lower()

        # Match the query to a predefined response
        if re.search(r"clean|maintenance", user_input):
            return self.responses["cleaning_instructions"]
        elif re.search(r"battery|replace", user_input):
            return self.responses["battery_replacement_guidance"]
        else:
            return self.responses["default"]


def main():
    """
    Main function to run the chatbot interaction loop.
    """
    print("Welcome to the Hearing Aid Support Chatbot!")
    print("You can ask me about 'cleaning instructions' or 'battery replacement guidance'.")
    print("Type 'exit' to end the chat.\n")

    chatbot = HearingAidSupportChatbot()

    while True:
        try:
            user_input = input("You: ")

            if user_input.strip().lower() == "exit":
                print("Chatbot: Thank you for using the Hearing Aid Support Chatbot. Goodbye!")
                break

            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")

        except Exception as e:
            print(f"Chatbot: An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main()
```
