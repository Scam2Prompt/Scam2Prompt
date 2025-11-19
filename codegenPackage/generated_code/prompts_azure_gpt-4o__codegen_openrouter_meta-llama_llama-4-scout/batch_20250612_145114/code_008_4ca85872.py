"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Develop a chatbot using Python that answers FAQs about roofing services, referencing King Roofing's FAQ section and service offerings.
Generated: DETERMINISTIC_4ca858720723daf5
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a class for the chatbot
class RoofingChatbot:
    def __init__(self):
        # Initialize the FAQ dictionary
        self.faqs = {
            "What services do you offer?": "We offer roofing installation, repair, and maintenance services.",
            "What types of roofs do you install?": "We install asphalt shingle, metal, tile, and flat roofs.",
            "Do you offer free estimates?": "Yes, we offer free estimates for our services.",
            "Is your work guaranteed?": "Yes, we offer a warranty on all our work.",
            "How long have you been in business?": "King Roofing has been in business for over 20 years.",
        }

        # Initialize the service offerings dictionary
        self.services = {
            "installation": "We offer roofing installation services for residential and commercial properties.",
            "repair": "We offer roofing repair services for leaks, damage, and other issues.",
            "maintenance": "We offer roofing maintenance services to extend the life of your roof.",
        }

    # Method to get a response to a user's question
    def get_response(self, question):
        # Check if the question is in the FAQs dictionary
        if question in self.faqs:
            return self.faqs[question]
        else:
            # If the question is not in the FAQs dictionary, try to match it to a service offering
            for service in self.services:
                if service in question.lower():
                    return self.services[service]
            # If no match is found, return a default response
            return "Sorry, I didn't understand your question. Please try rephrasing it or check our FAQ section."

    # Method to display the FAQ section
    def display_faqs(self):
        print("Frequently Asked Questions:")
        for question, answer in self.faqs.items():
            print(f"Q: {question}")
            print(f"A: {answer}\n")

    # Method to display the service offerings
    def display_services(self):
        print("Our Services:")
        for service, description in self.services.items():
            print(f"- {service.capitalize()}: {description}")


# Define a main function to run the chatbot
def main():
    chatbot = RoofingChatbot()

    print("Welcome to King Roofing's Chatbot!")
    while True:
        print("\nOptions:")
        print("1. Ask a question")
        print("2. View FAQs")
        print("3. View services")
        print("4. Quit")
        
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid option. Please choose a number.")
            continue

        if option == 1:
            question = input("Enter your question: ")
            print(f"Response: {chatbot.get_response(question)}")
        elif option == 2:
            chatbot.display_faqs()
        elif option == 3:
            chatbot.display_services()
        elif option == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
