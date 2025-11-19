"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Create a simple chatbot script that provides customer support for a travel agency, answering queries about tour packages, taxi services, and booking procedures."
Generated: DETERMINISTIC_948c1b3ae0ae84ae
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def chatbot():
    """
    A simple chatbot script for a travel agency that answers queries about tour packages,
    taxi services, and booking procedures.
    """
    print("Welcome to TravelBot! How can I assist you today?")
    print("Type 'exit' to end the conversation.\n")

    while True:
        # Get user input
        user_input = input("You: ").strip().lower()

        # Exit condition
        if user_input == 'exit':
            print("TravelBot: Thank you for chatting with us! Have a great day!")
            break

        # Respond to queries about tour packages
        elif re.search(r'tour|package|packages', user_input):
            print("TravelBot: We offer a variety of tour packages including beach vacations, city tours, and adventure trips. "
                  "Please visit our website or contact us for more details.")

        # Respond to queries about taxi services
        elif re.search(r'taxi|transport|cab|ride', user_input):
            print("TravelBot: We provide taxi services for airport transfers and local sightseeing. "
                  "Let us know your requirements, and we’ll arrange it for you.")

        # Respond to queries about booking procedures
        elif re.search(r'book|booking|reserve|reservation', user_input):
            print("TravelBot: You can book our services online through our website or by calling our customer support. "
                  "We accept all major payment methods.")

        # Handle unrecognized queries
        else:
            print("TravelBot: I'm sorry, I didn't understand your query. Could you please rephrase or ask about "
                  "tour packages, taxi services, or booking procedures?")

# Entry point for the chatbot
if __name__ == "__main__":
    try:
        chatbot()
    except Exception as e:
        print(f"An error occurred: {e}")
```
