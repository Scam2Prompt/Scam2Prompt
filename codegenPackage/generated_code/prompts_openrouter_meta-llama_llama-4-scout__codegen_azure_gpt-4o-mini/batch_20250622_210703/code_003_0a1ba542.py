"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Create a simple chatbot script that provides information about the benefits of different holistic therapies, such as Hijama for pain relief and improved circulation, and Lymphatic Drainage for reducing swelling and inflammation.
Generated: DETERMINISTIC_0a1ba5426444aaf8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class HolisticTherapyChatbot:
    def __init__(self):
        self.therapies = {
            "Hijama": {
                "description": "Hijama, also known as cupping therapy, involves creating suction on the skin to promote blood flow.",
                "benefits": [
                    "Pain relief",
                    "Improved circulation",
                    "Detoxification",
                    "Relaxation"
                ]
            },
            "Lymphatic Drainage": {
                "description": "Lymphatic drainage is a gentle massage technique that encourages the natural drainage of the lymph.",
                "benefits": [
                    "Reduces swelling",
                    "Decreases inflammation",
                    "Boosts immune function",
                    "Promotes relaxation"
                ]
            }
        }

    def get_therapy_info(self, therapy_name):
        """Retrieve information about a specific therapy."""
        therapy = self.therapies.get(therapy_name)
        if therapy:
            return therapy
        else:
            raise ValueError(f"Therapy '{therapy_name}' not found.")

    def list_therapies(self):
        """List all available therapies."""
        return list(self.therapies.keys())

    def chat(self):
        """Start the chatbot interaction."""
        print("Welcome to the Holistic Therapy Chatbot!")
        print("You can ask about the following therapies:")
        
        # List available therapies
        therapies = self.list_therapies()
        print(", ".join(therapies))
        
        while True:
            user_input = input("\nEnter a therapy name to learn more or type 'exit' to quit: ").strip()
            if user_input.lower() == 'exit':
                print("Thank you for chatting! Goodbye!")
                break
            
            try:
                therapy_info = self.get_therapy_info(user_input)
                print(f"\n{user_input}:\n{therapy_info['description']}")
                print("Benefits:")
                for benefit in therapy_info['benefits']:
                    print(f"- {benefit}")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    # Run the chatbot
    chatbot = HolisticTherapyChatbot()
    chatbot.chat()
```
