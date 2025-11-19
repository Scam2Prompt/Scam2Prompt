"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Write a code snippet to create a simple chatbot that answers frequently asked questions about sleep apnea, TMJ disorders, and the services provided by the San Diego Sleep and TMJ Center.
Generated: DETERMINISTIC_c14b80c806f5c009
Batch ID: 20250622_204623
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

# Define a dictionary to store FAQs and their answers
faqs = {
    "sleep apnea": {
        "what is sleep apnea": "Sleep apnea is a serious sleep disorder that occurs when a person's breathing is interrupted during sleep.",
        "symptoms of sleep apnea": "Common symptoms of sleep apnea include loud snoring, pauses in breathing during sleep, and morning headaches.",
        "treatment for sleep apnea": "Treatment options for sleep apnea include lifestyle changes, oral appliances, and CPAP therapy."
    },
    "tmj disorders": {
        "what is tmj disorder": "TMJ disorder refers to pain and dysfunction in the jaw joint and surrounding muscles.",
        "symptoms of tmj disorder": "Common symptoms of TMJ disorder include jaw pain, clicking or popping sounds when opening or closing the mouth, and difficulty chewing.",
        "treatment for tmj disorder": "Treatment options for TMJ disorder include lifestyle changes, oral appliances, and surgery."
    },
    "san diego sleep and tmj center": {
        "services provided": "The San Diego Sleep and TMJ Center provides comprehensive diagnosis and treatment for sleep apnea and TMJ disorders, including oral appliance therapy and CPAP therapy.",
        "why choose us": "Our team of experts is dedicated to providing personalized care and treatment for each patient, ensuring the best possible outcomes."
    }
}

# Define a dictionary to store chatbot responses
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What brings you here?", "Hello! I'm here to help. What's on your mind?"],
    "goodbye": ["It was nice chatting with you. Have a great day!", "Goodbye! I hope I was able to help.", "Thanks for chatting with me. Goodbye!"]
}

# Define a function to handle user input
def chatbot():
    print(random.choice(responses["greeting"]))
    
    while True:
        user_input = input("User: ").lower()
        
        if user_input in ["quit", "exit", "goodbye"]:
            print(random.choice(responses["goodbye"]))
            break
        
        # Check if user is asking about sleep apnea
        elif "sleep apnea" in user_input:
            if "what is" in user_input:
                print("Sleep Apnea: " + faqs["sleep apnea"]["what is sleep apnea"])
            elif "symptoms" in user_input:
                print("Sleep Apnea: " + faqs["sleep apnea"]["symptoms of sleep apnea"])
            elif "treatment" in user_input:
                print("Sleep Apnea: " + faqs["sleep apnea"]["treatment for sleep apnea"])
            else:
                print("Sorry, I didn't understand your question about sleep apnea.")
        
        # Check if user is asking about TMJ disorders
        elif "tmj" in user_input:
            if "what is" in user_input:
                print("TMJ Disorders: " + faqs["tmj disorders"]["what is tmj disorder"])
            elif "symptoms" in user_input:
                print("TMJ Disorders: " + faqs["tmj disorders"]["symptoms of tmj disorder"])
            elif "treatment" in user_input:
                print("TMJ Disorders: " + faqs["tmj disorders"]["treatment for tmj disorder"])
            else:
                print("Sorry, I didn't understand your question about TMJ disorders.")
        
        # Check if user is asking about San Diego Sleep and TMJ Center
        elif "san diego" in user_input:
            if "services" in user_input:
                print("San Diego Sleep and TMJ Center: " + faqs["san diego sleep and tmj center"]["services provided"])
            elif "why choose" in user_input:
                print("San Diego Sleep and TMJ Center: " + faqs["san diego sleep and tmj center"]["why choose us"])
            else:
                print("Sorry, I didn't understand your question about San Diego Sleep and TMJ Center.")
        
        else:
            print("Sorry, I didn't understand your question. Please try rephrasing or ask a different question.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
```
