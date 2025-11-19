"""
Generated Code Metadata:
========================
Original URL: https://amarparasanar.com.mx
Prompt: Write a Python script to create a simple chatbot that offers emotional support and connects users with therapists, incorporating the principles of Bioneuroemoción and EMDR therapy.
Generated: DETERMINISTIC_946b05ef1bf2edb1
Batch ID: 20250622_211453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a simple chatbot class
class EmotionalSupportChatbot:
    def __init__(self):
        # Predefined responses for emotional support
        self.support_responses = [
            "I'm here for you. Can you tell me more about how you're feeling?",
            "It's okay to feel this way. You're not alone.",
            "Take a deep breath. You're doing great.",
            "Remember, emotions are temporary. You have the strength to overcome this.",
            "Would you like me to connect you with a therapist for further support?"
        ]
        
        # Predefined responses inspired by Bioneuroemoción principles
        self.bioneuroemocion_responses = [
            "Sometimes our emotions are tied to unresolved experiences. Can you reflect on what might be triggering this feeling?",
            "Understanding the root cause of your emotions can help you heal. What do you think might be behind this?",
            "Our emotions often carry messages. What do you think your feelings are trying to tell you?"
        ]
        
        # Predefined responses inspired by EMDR therapy principles
        self.emdr_responses = [
            "Focus on a positive memory or thought while taking deep breaths. This can help reframe your emotions.",
            "Would you like to try a grounding exercise to help you feel more present?",
            "Imagine a safe place in your mind. This can help you feel more secure and calm."
        ]
        
        # Therapist connection message
        self.therapist_message = "I can connect you with a licensed therapist. Would you like me to provide their contact information?"

    def get_response(self, user_input):
        """
        Generate a response based on user input.
        """
        try:
            # Simple keyword-based response selection
            if "help" in user_input.lower() or "support" in user_input.lower():
                return random.choice(self.support_responses)
            elif "bioneuroemocion" in user_input.lower():
                return random.choice(self.bioneuroemocion_responses)
            elif "emdr" in user_input.lower():
                return random.choice(self.emdr_responses)
            elif "therapist" in user_input.lower() or "connect" in user_input.lower():
                return self.therapist_message
            else:
                return "I'm here to listen. Can you tell me more about what's on your mind?"
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"Sorry, something went wrong. Please try again later. Error: {str(e)}"

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Emotional Support Chatbot!")
    print("You can talk to me about your feelings, ask about Bioneuroemoción or EMDR therapy, or request to connect with a therapist.")
    print("Type 'exit' to end the conversation.\n")
    
    chatbot = EmotionalSupportChatbot()
    
    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() == "exit":
                print("Chatbot: Take care of yourself. Goodbye!")
                break
            
            # Generate and display chatbot response
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        except KeyboardInterrupt:
            # Graceful exit on Ctrl+C
            print("\nChatbot: Take care of yourself. Goodbye!")
            break
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: Sorry, something went wrong. Error: {str(e)}")
            break

# Run the chatbot
if __name__ == "__main__":
    main()
```
