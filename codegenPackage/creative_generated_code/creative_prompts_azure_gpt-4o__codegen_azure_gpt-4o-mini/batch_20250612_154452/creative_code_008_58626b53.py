"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Create a chatbot using Python that answers FAQs about medical admission coaching programs, referencing Retina's course offerings and success stories.
Generated: DETERMINISTIC_58626b538a1ffedf
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class FAQChatbot:
    def __init__(self):
        """Initialize the chatbot with predefined FAQs and responses."""
        self.faqs = {
            "What courses does Retina offer?": [
                "Retina offers various courses including Medical Admissions 101, Interview Preparation, and Test Strategy Workshops.",
                "We provide comprehensive coaching for medical entrance exams including NEET, MCAT, and more."
            ],
            "What is the success rate of Retina's coaching programs?": [
                "Retina boasts a 95% success rate based on our last year's cohort.",
                "Many of our students have successfully gained admission to leading medical schools."
            ],
            "How can I enroll in a course?": [
                "You can enroll through our website or contact our admissions office for assistance.",
                "Simply visit our enrollment page and fill out the registration form."
            ],
            "Are there any scholarships available?": [
                "Yes, we offer several scholarships based on merit and financial need.",
                "You can find more details about scholarships on our website."
            ],
            "What is the duration of the courses?": [
                "Most courses range from 4 to 12 weeks, depending on the subject and depth of the material.",
                "We also offer intensive crash courses for last-minute preparations."
            ],
        }
        self.default_responses = [
            "I'm sorry, I don't have information on that. Please check our website for more details.",
            "That's a great question! Unfortunately, I'm not equipped to answer it right now.",
            "Please visit our FAQ section on the website for more information."
        ]

    def get_response(self, user_input):
        """Return a response based on user input."""
        # Normalize input for better matching
        user_input = user_input.strip().lower()
        
        # Check for FAQs
        for question in self.faqs.keys():
            if question.lower() in user_input:
                return random.choice(self.faqs[question])
        
        # If no matching FAQ is found, return a default response
        return random.choice(self.default_responses)

    def chat(self):
        """Start the chat session with the user."""
        print("Welcome to Retina's FAQ Chatbot! Type 'exit' to end the chat.")
        while True:
            try:
                user_input = input("You: ")
                
                # Exit condition
                if user_input.lower() == 'exit':
                    print("Thank you for chatting! Goodbye!")
                    break
                
                # Get and print the bot's response
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
                
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try again.")

if __name__ == "__main__":
    # Run the chatbot if the script is executed directly
    chatbot = FAQChatbot()
    chatbot.chat()
```
