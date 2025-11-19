"""
Generated Code Metadata:
========================
Original URL: https://gstouristcentre.gr
Prompt: "Create a simple chatbot dialogue flow for a tourist information website, using keywords like 'Corfu Highlights Tour', 'Meteora Monasteries Tour', and 'Blue Lagoon Boat Trip'."
Generated: DETERMINISTIC_8c0125c9943ee5e7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def chatbot_response(user_input):
    """
    Generates a response based on user input for a tourist information chatbot.

    Args:
        user_input (str): The input message from the user.

    Returns:
        str: The chatbot's response.
    """
    # Normalize user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define keyword-response pairs
    responses = {
        "corfu highlights tour": "The Corfu Highlights Tour is a fantastic way to explore the island's rich history and stunning landscapes. Would you like to know the schedule or pricing?",
        "meteora monasteries tour": "The Meteora Monasteries Tour offers breathtaking views and a chance to visit ancient monasteries. Would you like more details about this tour?",
        "blue lagoon boat trip": "The Blue Lagoon Boat Trip is perfect for enjoying crystal-clear waters and relaxing on the beach. Would you like to book this trip or learn more?",
    }

    # Check for keywords in user input
    for keyword, response in responses.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
            return response

    # Default response if no keywords are matched
    return "I'm sorry, I didn't quite understand that. Could you please specify which tour or activity you're interested in?"

def main():
    """
    Main function to run the chatbot dialogue flow.
    """
    print("Welcome to the Tourist Information Chatbot!")
    print("You can ask about tours like 'Corfu Highlights Tour', 'Meteora Monasteries Tour', or 'Blue Lagoon Boat Trip'.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        try:
            # Get user input
            user_input = input("You: ")

            # Exit condition
            if user_input.lower() == "exit":
                print("Chatbot: Thank you for using the Tourist Information Chatbot. Have a great day!")
                break

            # Generate and display chatbot response
            response = chatbot_response(user_input)
            print(f"Chatbot: {response}")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: Oops! Something went wrong. Please try again later. (Error: {e})")

# Entry point for the script
if __name__ == "__main__":
    main()
```
