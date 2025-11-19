"""
Generated Code Metadata:
========================
Original URL: https://realogs.space
Prompt: Design a simple chatbot that can detect and respond to off-topic messages, such as cryptocurrency speculation, in a community chat forum like realogs.space.
Generated: DETERMINISTIC_3b380a029130016d
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import random

class Chatbot:
    def __init__(self, name="Chatbot"):
        """
        Initializes the Chatbot with a given name.
        
        Args:
            name (str): The name of the chatbot.
        """
        self.name = name
        self.off_topic_keywords = [
            "cryptocurrency", "bitcoin", "ethereum", "dogecoin", "speculation", "invest", "trade"
        ]
        self.responses = [
            "Let's keep the conversation on topic!",
            "I think we should focus on the main discussion.",
            "That's an interesting point, but let's stick to the topic at hand.",
            "I prefer to talk about things related to our community."
        ]

    def is_off_topic(self, message):
        """
        Checks if the message contains off-topic keywords.
        
        Args:
            message (str): The message to check.
        
        Returns:
            bool: True if the message is off-topic, False otherwise.
        """
        # Normalize the message to lower case for case-insensitive matching
        message_lower = message.lower()
        return any(re.search(r'\b' + re.escape(keyword) + r'\b', message_lower) for keyword in self.off_topic_keywords)

    def respond(self, message):
        """
        Generates a response based on the message content.
        
        Args:
            message (str): The message to respond to.
        
        Returns:
            str: The chatbot's response.
        """
        if self.is_off_topic(message):
            return random.choice(self.responses)
        else:
            return "Thanks for your message! How can I assist you today?"

def main():
    """
    Main function to run the chatbot.
    """
    chatbot = Chatbot()
    
    print("Welcome to the community chat! Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break
            
            response = chatbot.respond(user_input)
            print(f"{chatbot.name}: {response}")
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
