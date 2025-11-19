"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: "Develop a simple chatbot that can provide information about CNU's online programs and admission process."
Generated: DETERMINISTIC_a419fc76ad77cfd4
Batch ID: 20250622_212748
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
class CNUChatbot:
    def __init__(self):
        # Initialize a dictionary with information about CNU's online programs
        self.online_programs = {
            "business": "CNU offers an online Bachelor of Science in Business Administration.",
            "education": "CNU offers an online Master of Education in Curriculum and Instruction.",
            "nursing": "CNU offers an online RN to BSN program."
        }
        
        # Initialize a dictionary with information about CNU's admission process
        self.admission_process = {
            "requirements": "The admission requirements for CNU's online programs include a completed application, official transcripts, and a minimum GPA of 2.5.",
            "deadlines": "The admission deadlines for CNU's online programs vary by program. Please contact the admissions office for specific deadlines.",
            "tuition": "The tuition for CNU's online programs varies by program. Please contact the admissions office for specific tuition information."
        }

    # Define a method to get information about online programs
    def get_online_program_info(self, program):
        try:
            return self.online_programs[program.lower()]
        except KeyError:
            return "Sorry, we don't have information about that program. Please try again."

    # Define a method to get information about the admission process
    def get_admission_info(self, topic):
        try:
            return self.admission_process[topic.lower()]
        except KeyError:
            return "Sorry, we don't have information about that topic. Please try again."

    # Define a method to handle user input
    def respond(self, user_input):
        user_input = user_input.lower()
        
        if "online program" in user_input or "online programs" in user_input:
            if "business" in user_input:
                return self.get_online_program_info("business")
            elif "education" in user_input:
                return self.get_online_program_info("education")
            elif "nursing" in user_input:
                return self.get_online_program_info("nursing")
            else:
                return "We offer several online programs, including business, education, and nursing. Which one would you like to know more about?"
        
        elif "admission" in user_input or "admissions" in user_input:
            if "requirement" in user_input or "requirements" in user_input:
                return self.get_admission_info("requirements")
            elif "deadline" in user_input or "deadlines" in user_input:
                return self.get_admission_info("deadlines")
            elif "tuition" in user_input:
                return self.get_admission_info("tuition")
            else:
                return "We can provide information about admission requirements, deadlines, and tuition. What would you like to know?"
        
        else:
            return "Sorry, we didn't understand that. Please try again."

# Create an instance of the chatbot
chatbot = CNUChatbot()

# Define a main function to interact with the chatbot
def main():
    print("Welcome to the CNU Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot: ", response)

# Run the main function
if __name__ == "__main__":
    main()
```
