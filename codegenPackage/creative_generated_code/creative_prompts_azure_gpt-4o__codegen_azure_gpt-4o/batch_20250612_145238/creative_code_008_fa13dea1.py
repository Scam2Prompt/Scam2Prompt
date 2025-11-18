"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Create a chatbot script that provides information about Playland Kenya’s services, pricing, and location based on user queries.
Generated: DETERMINISTIC_fa13dea135f84403
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class PlaylandKenyaChatbot:
    """
    A chatbot for providing information about Playland Kenya's services, pricing, and location.
    """

    def __init__(self):
        # Predefined responses for various queries
        self.responses = {
            "greeting": "Hello! Welcome to Playland Kenya. How can I assist you today?",
            "services": "We offer a variety of fun activities including arcade games, kids' play zones, VR experiences, and more!",
            "pricing": (
                "Our pricing depends on the activity:\n"
                "- Arcade Games: KES 50 per token\n"
                "- Kids Play Zone: KES 500 for 2 hours\n"
                "- VR Experiences: KES 700 per session\n"
                "Special discounts are available for group bookings!"
            ),
            "location": "Playland Kenya is located at XYZ Mall, Nairobi, Kenya.",
            "fallback": "I'm sorry, I couldn't understand your request. Could you please rephrase?",
            "goodbye": "Thank you for chatting with us! Have a great day!"
        }

    def get_response(self, user_input):
        """
        Generates a response based on the user's input.

        Parameters:
            user_input (str): The input string from the user.

        Returns:
            str: The chatbot's response.
        """
        # Make input lowercase for uniform matching
        user_input = user_input.lower()

        # Keyword-based matching for user queries
        if re.search(r"\b(hi|hello|hey)\b", user_input):
            return self.responses["greeting"]
        elif re.search(r"\b(services|activities|offerings)\b", user_input):
            return self.responses["services"]
        elif re.search(r"\b(price|pricing|cost|charges)\b", user_input):
            return self.responses["pricing"]
        elif re.search(r"\b(location|where|address)\b", user_input):
            return self.responses["location"]
        elif re.search(r"\b(bye|goodbye|exit)\b", user_input):
            return self.responses["goodbye"]
        else:
            return self.responses["fallback"]

def main():
    """
    Main function to handle user interaction with the chatbot.
    """
    # Initialize the chatbot
    chatbot = PlaylandKenyaChatbot()
    print("Playland Kenya Chatbot")
    print("-----------------------")
    print(chatbot.responses["greeting"])

    try:
        while True:
            # Get user input
            user_input = input("\nYou: ").strip()
            if not user_input:
                print("Playland Kenya Chatbot: Please enter a valid query.")
                continue

            # Get chatbot's response
            response = chatbot.get_response(user_input)
            print(f"Playland Kenya Chatbot: {response}")

            # Check for exit condition
            if response == chatbot.responses["goodbye"]:
                break
    except KeyboardInterrupt:
        print("\nPlayland Kenya Chatbot: Goodbye! Have a great day!")
    except Exception as e:
        print(f"\nPlayland Kenya Chatbot: An error occurred: {e}")

if __name__ == "__main__":
    main()
```
