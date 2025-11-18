"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Write code to design a chatbot for a university like Uni4Kashmir, capable of answering queries about courses in Cybersecurity, Big Data, and Humanities.
Generated: DETERMINISTIC_c909d746f064f273
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class UniversityChatbot:
    """
    A chatbot class designed to interact with users and answer queries
    related to courses in Cybersecurity, Big Data, and Humanities.
    """

    def __init__(self):
        # Initialize available courses
        self.courses = {
            "Cybersecurity": [
                "Introduction to Cybersecurity",
                "Ethical Hacking",
                "Network Security",
                "Digital Forensics"
            ],
            "Big Data": [
                "Big Data Analytics",
                "Data Mining",
                "Machine Learning",
                "Cloud Computing"
            ],
            "Humanities": [
                "Philosophy",
                "Psychology",
                "History",
                "Cultural Studies"
            ]
        }
        # Predefined responses for common queries
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! What would you like to know?"],
            "farewell": ["Thank you for chatting! Have a great day!", "Goodbye! Feel free to reach out anytime!"],
            "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
        }

    def get_courses(self, category):
        """
        Retrieve the list of courses for the specified category.
        :param category: The category of courses to retrieve.
        :return: List of courses or error message.
        """
        try:
            if category in self.courses:
                return self.courses[category]
            else:
                return f"Sorry, we do not offer courses in {category}."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def handle_query(self, query):
        """
        Process user queries and return appropriate responses.
        :param query: The user's input query.
        :return: Response string.
        """
        query = query.lower().strip()
        
        if "course" in query and "cybersecurity" in query:
            return self.get_courses("Cybersecurity")
        elif "course" in query and "big data" in query:
            return self.get_courses("Big Data")
        elif "course" in query and "humanities" in query:
            return self.get_courses("Humanities")
        elif "hello" in query or "hi" in query:
            return random.choice(self.responses["greeting"])
        elif "bye" in query or "exit" in query:
            return random.choice(self.responses["farewell"])
        else:
            return self.responses["default"]

def main():
    """
    Main function to run the university chatbot in a loop.
    """
    chatbot = UniversityChatbot()
    print("Welcome to Uni4Kashmir Chatbot!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print("Chatbot:", chatbot.handle_query(user_input))
            break
        response = chatbot.handle_query(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
```
