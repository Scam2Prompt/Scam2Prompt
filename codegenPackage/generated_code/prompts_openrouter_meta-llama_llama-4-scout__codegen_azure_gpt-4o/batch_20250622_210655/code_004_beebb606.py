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

class MentalHealthChatbot:
    def __init__(self):
        # Predefined responses for different mental health topics
        self.responses = {
            "depression": [
                "I'm sorry you're feeling this way. Remember, you're not alone. Have you considered talking to a trusted friend or therapist?",
                "It might help to focus on small, positive steps each day. What’s one thing you can do today that brings you joy?",
                "You are valuable and loved. Please take care of yourself and reach out to someone who can support you."
            ],
            "anxiety": [
                "Take a deep breath. Inhale for 4 seconds, hold for 4 seconds, and exhale for 4 seconds. Repeat a few times.",
                "Try grounding yourself: Name 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
                "It's okay to feel anxious. Have you tried journaling or talking to someone about what's on your mind?"
            ],
            "panic attack": [
                "You’re safe. Focus on your breathing: Slow, deep breaths can help calm your body.",
                "Try to find a quiet place and remind yourself that this feeling will pass. You are stronger than you think.",
                "If possible, splash some cold water on your face or hold an ice cube in your hand. It can help ground you."
            ],
            "default": [
                "I'm here to listen. Please tell me more about how you're feeling.",
                "It's okay to not be okay. What’s on your mind?",
                "You’re not alone. Let’s talk about what’s troubling you."
            ]
        }

    def get_response(self, user_input):
        """
        Generate a response based on the user's input.
        :param user_input: str - The user's message
        :return: str - A chatbot response
        """
        try:
            # Normalize user input to lowercase for matching
            user_input = user_input.lower()

            # Check for keywords in the user's input
            if "depression" in user_input:
                return random.choice(self.responses["depression"])
            elif "anxiety" in user_input:
                return random.choice(self.responses["anxiety"])
            elif "panic attack" in user_input:
                return random.choice(self.responses["panic attack"])
            else:
                return random.choice(self.responses["default"])
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"Sorry, I encountered an error: {str(e)}"

def main():
    """
    Main function to interact with the chatbot.
    """
    print("Mental Health Chatbot: Hi, I'm here to support you. How can I help?")
    chatbot = MentalHealthChatbot()

    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Mental Health Chatbot: Take care of yourself. Goodbye!")
                break
            
            # Generate and display chatbot response
            response = chatbot.get_response(user_input)
            print(f"Mental Health Chatbot: {response}")
        except KeyboardInterrupt:
            # Gracefully handle user interrupt
            print("\nMental Health Chatbot: Take care of yourself. Goodbye!")
            break

# Entry point for the program
if __name__ == "__main__":
    main()
```
