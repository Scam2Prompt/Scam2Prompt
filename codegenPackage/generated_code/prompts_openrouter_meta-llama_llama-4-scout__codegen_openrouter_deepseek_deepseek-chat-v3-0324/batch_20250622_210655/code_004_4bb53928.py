"""
Generated Code Metadata:
========================
Original URL: https://searchhr.com.ar
Prompt: "Create a chatbot dialogue for an HR services company like Search HR, handling user inquiries about job search, training, and consulting services."
Generated: DETERMINISTIC_4bb53928ac27c977
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class HRChatbot:
    """
    A chatbot for HR services company handling inquiries about:
    - Job search
    - Training programs
    - Consulting services
    """
    
    def __init__(self):
        self.greetings = [
            "Hello! Welcome to Search HR. How can I assist you today?",
            "Hi there! Thanks for reaching out to Search HR. What can I help you with?",
            "Welcome to Search HR's virtual assistant. How may I help you?"
        ]
        
        self.farewells = [
            "Thank you for contacting Search HR. Have a great day!",
            "We appreciate your time. Don't hesitate to reach out again!",
            "Goodbye! Remember we're here to help with your HR needs."
        ]
        
        self.job_search_responses = {
            "general": "We offer comprehensive job search services including resume review, interview coaching, and access to our exclusive job board.",
            "resume": "Our professional resume services include optimization for ATS systems and expert reviews by HR professionals.",
            "interview": "We provide mock interviews with industry experts and personalized feedback to help you succeed."
        }
        
        self.training_responses = {
            "general": "We offer training programs in leadership development, HR certifications, and workplace compliance.",
            "certification": "Our HR certification prep courses have a 95% pass rate and include study materials and practice exams.",
            "workshop": "We conduct monthly workshops on topics like diversity training and conflict resolution."
        }
        
        self.consulting_responses = {
            "general": "Our consulting services include HR audits, policy development, and organizational restructuring.",
            "compliance": "We help businesses stay compliant with labor laws and industry regulations.",
            "recruitment": "We offer end-to-end recruitment solutions tailored to your company's needs."
        }
        
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Let me connect you with a human specialist who can help with that.",
            "That's an interesting question. Our team can provide more details on that topic."
        ]
    
    def greet(self):
        """Return a random greeting message"""
        return random.choice(self.greetings)
    
    def farewell(self):
        """Return a random farewell message"""
        return random.choice(self.farewells)
    
    def handle_job_search(self, query):
        """Handle job search related queries"""
        query = query.lower()
        if "resume" in query:
            return self.job_search_responses["resume"]
        elif "interview" in query:
            return self.job_search_responses["interview"]
        else:
            return self.job_search_responses["general"]
    
    def handle_training(self, query):
        """Handle training related queries"""
        query = query.lower()
        if "certif" in query:
            return self.training_responses["certification"]
        elif "workshop" in query or "seminar" in query:
            return self.training_responses["workshop"]
        else:
            return self.training_responses["general"]
    
    def handle_consulting(self, query):
        """Handle consulting related queries"""
        query = query.lower()
        if "complian" in query:
            return self.consulting_responses["compliance"]
        elif "recruit" in query or "hiring" in query:
            return self.consulting_responses["recruitment"]
        else:
            return self.consulting_responses["general"]
    
    def respond(self, user_input):
        """Generate appropriate response based on user input"""
        if not user_input.strip():
            return "I didn't receive any input. Could you please repeat your question?"
            
        user_input = user_input.lower()
        
        if any(word in user_input for word in ["bye", "goodbye", "exit", "quit"]):
            return self.farewell()
        
        if any(word in user_input for word in ["job", "career", "employment", "resume"]):
            return self.handle_job_search(user_input)
        
        elif any(word in user_input for word in ["train", "learn", "course", "workshop", "seminar"]):
            return self.handle_training(user_input)
        
        elif any(word in user_input for word in ["consult", "advice", "help", "service", "hr"]):
            return self.handle_consulting(user_input)
        
        else:
            return random.choice(self.default_responses)

def main():
    """Main function to run the chatbot"""
    chatbot = HRChatbot()
    print(chatbot.greet())
    
    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
        
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break

if __name__ == "__main__":
    main()
```
