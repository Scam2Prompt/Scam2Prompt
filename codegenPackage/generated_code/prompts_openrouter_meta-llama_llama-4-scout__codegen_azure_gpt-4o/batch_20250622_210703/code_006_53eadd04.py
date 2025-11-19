"""
Generated Code Metadata:
========================
Original URL: https://cbienetre.com
Prompt: "Develop a chatbot script in Python to provide customer support for a massage therapy clinic, including answering frequently asked questions and scheduling appointments."
Generated: DETERMINISTIC_53eadd042b948786
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import re

# Define a dictionary for frequently asked questions (FAQs)
FAQS = {
    "What are your hours?": "We are open Monday to Friday, 9 AM to 7 PM, and Saturday, 10 AM to 5 PM.",
    "Where are you located?": "We are located at 123 Wellness Street, Springfield.",
    "What services do you offer?": "We offer Swedish massage, deep tissue massage, hot stone therapy, and aromatherapy.",
    "How much does a massage cost?": "Our prices range from $50 to $120 depending on the type and duration of the massage.",
    "Do you accept walk-ins?": "We recommend scheduling an appointment, but we do accept walk-ins if availability permits."
}

# Define a list of available appointment slots
AVAILABLE_SLOTS = [
    "2023-10-01 10:00 AM",
    "2023-10-01 11:00 AM",
    "2023-10-01 2:00 PM",
    "2023-10-02 9:00 AM",
    "2023-10-02 3:00 PM",
]

# Function to handle FAQs
def handle_faq(question):
    """
    Responds to frequently asked questions.
    :param question: The user's question as a string.
    :return: The answer to the question or a default response if not found.
    """
    return FAQS.get(question, "I'm sorry, I don't have an answer to that question. Can I help you with something else?")

# Function to handle appointment scheduling
def schedule_appointment(preferred_date):
    """
    Schedules an appointment based on user input.
    :param preferred_date: The user's preferred date as a string.
    :return: Confirmation of the appointment or an error message if no slots are available.
    """
    try:
        # Validate date format
        datetime.datetime.strptime(preferred_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    # Filter available slots for the preferred date
    matching_slots = [slot for slot in AVAILABLE_SLOTS if slot.startswith(preferred_date)]
    if matching_slots:
        return f"Available slots on {preferred_date}: {', '.join(matching_slots)}. Please choose one."
    else:
        return f"Sorry, no available slots on {preferred_date}. Please choose another date."

# Main chatbot function
def chatbot():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Massage Therapy Clinic Chatbot!")
    print("How can I assist you today? (Type 'exit' to end the chat)")

    while True:
        user_input = input("\nYou: ").strip()

        # Exit condition
        if user_input.lower() == "exit":
            print("Thank you for using the chatbot. Have a great day!")
            break

        # Check if the user is asking a FAQ
        if user_input in FAQS:
            response = handle_faq(user_input)
            print(f"Chatbot: {response}")
        # Check if the user wants to schedule an appointment
        elif re.match(r"schedule appointment on \d{4}-\d{2}-\d{2}", user_input.lower()):
            preferred_date = user_input.lower().split("on ")[1]
            response = schedule_appointment(preferred_date)
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase or ask about our services, hours, or appointments?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
```
