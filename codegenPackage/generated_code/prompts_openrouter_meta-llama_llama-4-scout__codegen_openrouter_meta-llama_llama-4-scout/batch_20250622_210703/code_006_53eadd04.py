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
# Import required libraries
import datetime
import re

# Define a dictionary to store frequently asked questions and answers
faq_dict = {
    "What are your business hours?": "Our business hours are Monday to Friday, 9am to 7pm, and Saturday, 10am to 5pm.",
    "What types of massages do you offer?": "We offer Swedish massage, deep tissue massage, sports massage, and aromatherapy.",
    "How long are massages?": "Massages range from 30 minutes to 2 hours.",
    "Do you offer gift certificates?": "Yes, we do offer gift certificates.",
    "What is your cancellation policy?": "We require a 24-hour notice for cancellations. A fee may apply for late cancellations."
}

# Define a dictionary to store available appointment times
appointment_times = {
    "Monday": ["9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm"],
    "Tuesday": ["9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm"],
    "Wednesday": ["9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm"],
    "Thursday": ["9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm"],
    "Friday": ["9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm"],
    "Saturday": ["10:00am", "11:00am", "12:00pm", "1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm"]
}

class Chatbot:
    def __init__(self):
        self.appointments = {}

    def answer_faq(self, question):
        """Answers frequently asked questions"""
        if question in faq_dict:
            return faq_dict[question]
        else:
            return "Sorry, I don't have an answer to that question."

    def schedule_appointment(self, name, date, time):
        """Schedules an appointment"""
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            time = datetime.datetime.strptime(time, "%I:%M%p").time()
            if date.strftime("%A") in appointment_times:
                if time.strftime("%I:%M %p") in appointment_times[date.strftime("%A")]:
                    self.appointments[name] = (date, time)
                    return f"Appointment scheduled for {name} on {date} at {time}."
                else:
                    return "Sorry, that time is not available."
            else:
                return "Sorry, we are not open on that day."
        except ValueError:
            return "Invalid date or time."

    def cancel_appointment(self, name):
        """Cancels an appointment"""
        if name in self.appointments:
            del self.appointments[name]
            return f"Appointment for {name} has been cancelled."
        else:
            return f"No appointment found for {name}."

def main():
    chatbot = Chatbot()
    print("Welcome to our massage therapy clinic chatbot!")
    while True:
        user_input = input("How can I help you today? Type 'quit' to exit.\n").strip().lower()
        if user_input == "quit":
            break
        elif user_input.startswith("faq"):
            question = input("What is your question? Type 'back' to go back.\n").strip().capitalize()
            if question.lower() == "back":
                continue
            print(chatbot.answer_faq(question))
        elif user_input.startswith("schedule"):
            name = input("What is your name?\n").strip().capitalize()
            date = input("What date would you like to schedule an appointment? (YYYY-MM-DD)\n").strip()
            time = input("What time would you like to schedule an appointment? (12-hour clock, e.g. 02:00PM)\n").strip()
            print(chatbot.schedule_appointment(name, date, time))
        elif user_input.startswith("cancel"):
            name = input("What is your name?\n").strip().capitalize()
            print(chatbot.cancel_appointment(name))
        else:
            print("Sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()
```
