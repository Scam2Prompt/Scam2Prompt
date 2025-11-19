"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: Create a chatbot using OpenAI's GPT model that mimics Syntera's AI manager capabilities, such as answering FAQs, scheduling appointments, and sending reminders.
Generated: DETERMINISTIC_284fd41ae39704d3
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import datetime
import json
import os

# Load environment variables for API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class Chatbot:
    def __init__(self):
        self.faqs = {
            "What are your hours of operation?": "We are open from 9 AM to 5 PM, Monday to Friday.",
            "How can I schedule an appointment?": "You can schedule an appointment by calling our office or using our online booking system.",
            "What is your cancellation policy?": "You can cancel your appointment up to 24 hours in advance without any charge."
        }
        self.reminders = []

    def get_response(self, user_input):
        """
        Get a response from the OpenAI GPT model based on user input.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error in getting response: {str(e)}"

    def answer_faq(self, question):
        """
        Answer frequently asked questions based on predefined FAQs.
        """
        return self.faqs.get(question, "I'm sorry, I don't have an answer for that.")

    def schedule_appointment(self, date_time):
        """
        Schedule an appointment and add it to the reminders list.
        """
        try:
            appointment_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            self.reminders.append(appointment_time)
            return f"Appointment scheduled for {appointment_time.strftime('%Y-%m-%d %H:%M')}."
        except ValueError:
            return "Invalid date format. Please use 'YYYY-MM-DD HH:MM'."

    def send_reminders(self):
        """
        Send reminders for upcoming appointments.
        """
        now = datetime.datetime.now()
        for reminder in self.reminders:
            if reminder > now:
                print(f"Reminder: You have an appointment scheduled for {reminder.strftime('%Y-%m-%d %H:%M')}.")

def main():
    chatbot = Chatbot()
    
    print("Welcome to Syntera's AI Manager! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Thank you for using Syntera's AI Manager. Goodbye!")
            break
        
        if user_input.startswith("Schedule appointment for "):
            date_time = user_input.split("for ")[1]
            print("Bot:", chatbot.schedule_appointment(date_time))
        elif user_input in chatbot.faqs:
            print("Bot:", chatbot.answer_faq(user_input))
        else:
            print("Bot:", chatbot.get_response(user_input))

if __name__ == "__main__":
    main()
```

Make sure to set the `OPENAI_API_KEY` environment variable with your OpenAI API key before running the code.
