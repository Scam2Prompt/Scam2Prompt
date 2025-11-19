"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: Develop a chatbot that replicates Syntera's AI manager features for a tattoo studio, including appointment scheduling, answering FAQs, and collecting post-visit feedback.
Generated: DETERMINISTIC_13787d05ee44c964
Batch ID: 20250612_154642
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
import json

class TattooStudioChatbot:
    def __init__(self):
        # Initialize chatbot with FAQs and appointment schedule
        self.faqs = {
            "What is your studio's address?": "123 Main St, Anytown, USA",
            "What are your business hours?": "Mon-Sat 10am-6pm, Sun 12pm-5pm",
            "Do you offer consultations?": "Yes, free consultations are available.",
        }
        self.appointments = {}

    def schedule_appointment(self, name, date, time):
        """
        Schedule an appointment for a customer.

        Args:
            name (str): Customer's name
            date (str): Date of appointment (YYYY-MM-DD)
            time (str): Time of appointment (HH:MM)

        Returns:
            str: Confirmation message
        """
        try:
            # Validate date and time
            datetime.datetime.strptime(date, "%Y-%m-%d")
            datetime.datetime.strptime(time, "%H:%M")

            # Check for existing appointments
            if date in self.appointments and time in self.appointments[date]:
                return "Sorry, that time slot is taken."

            # Schedule appointment
            if date not in self.appointments:
                self.appointments[date] = {}
            self.appointments[date][time] = name
            return f"Appointment scheduled for {name} on {date} at {time}."
        except ValueError:
            return "Invalid date or time format. Please use YYYY-MM-DD and HH:MM."

    def answer_faq(self, question):
        """
        Answer a frequently asked question.

        Args:
            question (str): Customer's question

        Returns:
            str: Answer to the question
        """
        return self.faqs.get(question, "Sorry, I don't have an answer to that question.")

    def collect_feedback(self, name, rating, comments):
        """
        Collect post-visit feedback from a customer.

        Args:
            name (str): Customer's name
            rating (int): Rating (1-5)
            comments (str): Additional comments

        Returns:
            str: Thank you message
        """
        try:
            # Validate rating
            if rating < 1 or rating > 5:
                return "Invalid rating. Please use a rating between 1 and 5."

            # Save feedback (in a real application, this would be saved to a database)
            with open("feedback.json", "a") as f:
                json.dump({"name": name, "rating": rating, "comments": comments}, f)
                f.write("\n")
            return f"Thank you, {name}, for your feedback!"
        except Exception as e:
            return f"Sorry, an error occurred: {str(e)}"

def main():
    chatbot = TattooStudioChatbot()

    while True:
        print("\n1. Schedule Appointment")
        print("2. Ask a Question")
        print("3. Provide Feedback")
        print("4. Exit")

        choice = input("What would you like to do? ")

        if choice == "1":
            name = input("What is your name? ")
            date = input("What date would you like to schedule an appointment? (YYYY-MM-DD) ")
            time = input("What time would you like to schedule an appointment? (HH:MM) ")
            print(chatbot.schedule_appointment(name, date, time))
        elif choice == "2":
            question = input("What is your question? ")
            print(chatbot.answer_faq(question))
        elif choice == "3":
            name = input("What is your name? ")
            rating = int(input("What rating would you give us? (1-5) "))
            comments = input("What comments do you have? ")
            print(chatbot.collect_feedback(name, rating, comments))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
