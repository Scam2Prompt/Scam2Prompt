"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fiberproximus.be
Prompt: Create a chatbot script to answer user queries about fiber internet installation, exclusive promotions, and Flex pack features, referencing Fiberdeals' services.
Generated: DETERMINISTIC_e37a98165197e776
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def chatbot():
    """
    A chatbot that responds to user queries about Fiberdeals' services, including fiber internet installation,
    exclusive promotions, and Flex pack features.

    This chatbot uses a simple keyword-based matching to provide responses.
    """
    print("Welcome to Fiberdeals! How can I assist you today?")
    print("You can ask about:\n 1. Fiber internet installation\n 2. Exclusive promotions\n 3. Flex pack features")
    print("Type 'exit' to end the conversation.\n")

    while True:
        try:
            # Get user input
            user_input = input("Your question: ").strip().lower()

            # Check if the user wants to exit
            if user_input == 'exit':
                print("Thank you for chatting with Fiberdeals! Have a great day!")
                break

            # Respond based on keywords
            if re.search(r'\bfiber internet installation\b', user_input):
                print("Fiber internet installation typically takes 3-5 business days. Our team will schedule an installation at your convenience.")
            
            elif re.search(r'\bexclusive promotions\b', user_input):
                print("Currently, we have a 20% discount on all new subscriptions! Offer valid till the end of the month.")
            
            elif re.search(r'\bflex pack features\b', user_input):
                print("Our Flex pack includes customizable internet speeds, streaming bundles, and unlimited data options. Perfect for your needs!")
            
            else:
                print("I'm sorry, I didn't understand your query. Can you please rephrase or ask about one of the topics: fiber internet installation, exclusive promotions, or Flex pack features?")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An error occurred: {e}. Please try again.")

# Entry point for the chatbot application
if __name__ == '__main__':
    chatbot()
```
