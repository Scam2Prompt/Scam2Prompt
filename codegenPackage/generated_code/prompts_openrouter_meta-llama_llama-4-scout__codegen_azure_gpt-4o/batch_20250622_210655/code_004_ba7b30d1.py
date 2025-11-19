"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Develop a prompt for a chatbot that provides customer support for a cleaning services company like Maria HouseKeepers, including answers to frequently asked questions.
Generated: DETERMINISTIC_ba7b30d1c23ecd88
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def chatbot_prompt(user_input):
    """
    A chatbot function to provide customer support for a cleaning services company.
    Responds to frequently asked questions and handles basic inquiries.

    Args:
        user_input (str): The input message from the user.

    Returns:
        str: The chatbot's response.
    """
    # Predefined responses for frequently asked questions
    faq_responses = {
        "What services do you offer?": "We offer residential cleaning, deep cleaning, move-in/move-out cleaning, and office cleaning services.",
        "How much do your services cost?": "Our pricing depends on the type of service and the size of the area to be cleaned. Please visit our website or contact us for a detailed quote.",
        "What are your working hours?": "We operate Monday to Saturday, from 8:00 AM to 6:00 PM.",
        "Do you bring your own cleaning supplies?": "Yes, we bring all necessary cleaning supplies and equipment. If you have specific preferences, let us know in advance.",
        "How can I book a cleaning service?": "You can book a service by visiting our website, calling us at (123) 456-7890, or emailing us at contact@mariahousekeepers.com.",
        "What is your cancellation policy?": "You can cancel or reschedule up to 24 hours before your appointment without any charges.",
        "Are your cleaners insured?": "Yes, all our cleaners are insured and professionally trained."
    }

    # Default response for unrecognized queries
    default_response = "I'm sorry, I didn't understand your question. Could you please rephrase or ask about our services, pricing, or policies?"

    try:
        # Check if the user input matches any predefined FAQ
        response = faq_responses.get(user_input.strip(), default_response)
        return response
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while processing your request: {str(e)}"


# Example usage
if __name__ == "__main__":
    print("Welcome to Maria HouseKeepers Customer Support!")
    print("Type your question below or type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Thank you for using Maria HouseKeepers Customer Support. Have a great day!")
            break

        # Get chatbot response
        response = chatbot_prompt(user_input)
        print(f"Chatbot: {response}")
```
