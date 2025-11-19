"""
Generated Code Metadata:
========================
Original URL: https://mluce-ginza.net
Prompt: Create a simple chatbot dialogue flow for an art makeup salon, answering common questions about services, pricing, and appointment booking like those offered by M luce.
Generated: DETERMINISTIC_324d9fa1975d726a
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class ArtMakeupSalonChatbot:
    def __init__(self):
        # Initialize chatbot with predefined responses
        self.responses = {
            "services": "We offer a variety of services including permanent makeup, microblading, lip blush, eyeliner tattoo, and more.",
            "pricing": "Our pricing varies depending on the service. For example, microblading starts at $250. Please visit our website or contact us for detailed pricing.",
            "booking": "You can book an appointment by visiting our website or calling us directly at (555) 123-4567.",
            "hours": "Our salon is open Monday to Saturday, from 9 AM to 6 PM.",
            "location": "We are located at 123 Artistry Lane, Beauty City, BC 12345.",
            "default": "I'm sorry, I didn't understand that. Could you please rephrase or ask about services, pricing, booking, hours, or location?"
        }

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.
        :param user_input: str - The user's message to the chatbot.
        :return: str - The chatbot's response.
        """
        # Normalize user input to lowercase for easier matching
        user_input = user_input.lower()

        # Match user input to predefined topics
        if re.search(r"\bservices\b", user_input):
            return self.responses["services"]
        elif re.search(r"\bpricing\b|\bcost\b|\bprice\b", user_input):
            return self.responses["pricing"]
        elif re.search(r"\bbook\b|\bappointment\b|\bschedule\b", user_input):
            return self.responses["booking"]
        elif re.search(r"\bhours\b|\btime\b|\bopen\b", user_input):
            return self.responses["hours"]
        elif re.search(r"\blocation\b|\baddress\b", user_input):
            return self.responses["location"]
        else:
            return self.responses["default"]

def main():
    """
    Main function to run the chatbot in a loop.
    """
    print("Welcome to M Luce Art Makeup Salon Chatbot!")
    print("You can ask about services, pricing, booking, hours, or location.")
    print("Type 'exit' to end the chat.\n")

    chatbot = ArtMakeupSalonChatbot()

    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() == "exit":
                print("Chatbot: Thank you for chatting with us! Have a great day!")
                break
            
            # Get chatbot response
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: Oops! Something went wrong. Please try again later. (Error: {e})")

# Run the chatbot
if __name__ == "__main__":
    main()
```
