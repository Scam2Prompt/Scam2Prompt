"""
Generated Code Metadata:
========================
Original URL: https://www.psikolojibakirkoy.com.tr
Prompt: Write a Python code snippet to create a simple chatbot that provides support for individuals with mental health issues such as depression, anxiety, and panic attacks.
Generated: DETERMINISTIC_beebb606c517c3b2
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
import time

class MentalHealthChatbot:
    """
    A simple chatbot that provides support for mental health issues.
    Handles topics like depression, anxiety, and panic attacks.
    """
    
    def __init__(self):
        self.responses = {
            "greeting": [
                "Hello, I'm here to listen. How are you feeling today?",
                "Hi there. I'm glad you reached out. What's on your mind?",
                "Welcome. This is a safe space to share your feelings."
            ],
            "depression": [
                "I'm sorry you're feeling this way. You're not alone in this.",
                "Depression can be really tough. Have you considered talking to a professional?",
                "Remember that what you're feeling is valid, and help is available."
            ],
            "anxiety": [
                "Anxiety can feel overwhelming. Try taking slow, deep breaths.",
                "It's okay to feel anxious. Would grounding techniques help right now?",
                "This feeling will pass. You've gotten through tough moments before."
            ],
            "panic": [
                "During a panic attack, focus on your breathing. Inhale for 4, hold for 4, exhale for 4.",
                "You're safe. This is temporary. Try to name things you can see around you.",
                "Panic attacks are scary but not dangerous. It will pass soon."
            ],
            "self_care": [
                "Remember to drink water and eat something nourishing today.",
                "Small acts of self-care can make a big difference. Maybe take a short walk?",
                "Be kind to yourself. You're doing the best you can."
            ],
            "emergency": [
                "If you're in immediate danger, please call emergency services.",
                "Your safety is important. Reach out to someone you trust right now.",
                "This sounds serious. Please contact a crisis hotline immediately."
            ],
            "unknown": [
                "I'm not sure I understand. Could you tell me more?",
                "I want to help. Can you explain what you're feeling?",
                "I hear you're struggling. What specifically is bothering you?"
            ],
            "goodbye": [
                "Take care of yourself. You're important.",
                "Remember you can reach out anytime. You're not alone.",
                "Wishing you peace. Come back if you need to talk."
            ]
        }
        
        self.keywords = {
            "depression": ["depressed", "sad", "hopeless", "empty"],
            "anxiety": ["anxious", "nervous", "worried", "overwhelmed"],
            "panic": ["panic", "attack", "can't breathe", "losing control"],
            "self_care": ["tired", "exhausted", "self care", "take care"],
            "emergency": ["suicide", "hurt myself", "end it all", "emergency"]
        }
    
    def get_response(self, user_input):
        """Analyze user input and return an appropriate response."""
        user_input = user_input.lower()
        
        # Check for emergency keywords first
        for keyword in self.keywords["emergency"]:
            if keyword in user_input:
                return random.choice(self.responses["emergency"])
        
        # Check other categories
        for category, keywords in self.keywords.items():
            if category == "emergency":
                continue
            for keyword in keywords:
                if keyword in user_input:
                    return random.choice(self.responses[category])
        
        # Check for greetings
        if any(word in user_input for word in ["hi", "hello", "hey"]):
            return random.choice(self.responses["greeting"])
        
        # Check for goodbyes
        if any(word in user_input for word in ["bye", "goodbye", "exit"]):
            return random.choice(self.responses["goodbye"])
        
        # Default response if no keywords matched
        return random.choice(self.responses["unknown"])
    
    def chat(self):
        """Run the chatbot interaction loop."""
        print("Mental Health Support Chatbot")
        print("Type 'bye' to exit at any time.\n")
        
        print(random.choice(self.responses["greeting"]))
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                print("Bot: I'm here when you're ready to talk.")
                continue
                
            if user_input.lower() in ['bye', 'goodbye', 'exit']:
                print(f"Bot: {random.choice(self.responses['goodbye'])}")
                break
                
            response = self.get_response(user_input)
            
            # Simulate typing delay for more natural interaction
            print("Bot: ", end="", flush=True)
            for char in response:
                print(char, end="", flush=True)
                time.sleep(0.03)
            print()


if __name__ == "__main__":
    bot = MentalHealthChatbot()
    bot.chat()
```
