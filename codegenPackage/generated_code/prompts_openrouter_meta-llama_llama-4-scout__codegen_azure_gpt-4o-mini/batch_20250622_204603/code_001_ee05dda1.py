"""
Generated Code Metadata:
========================
Original URL: https://linkevent.net
Prompt: Create a chatbot with AI personalities like Judy, Beau, and Rafa that can answer user questions on various topics.
Generated: DETERMINISTIC_ee05dda1207b2290
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Chatbot:
    def __init__(self, name, personality):
        """
        Initialize the chatbot with a name and personality.

        :param name: str - The name of the chatbot.
        :param personality: str - The personality type of the chatbot.
        """
        self.name = name
        self.personality = personality
        self.responses = {
            "Judy": [
                "I'm here to help! What can I assist you with today?",
                "Let's tackle your questions together!",
                "I love learning new things! What do you want to know?"
            ],
            "Beau": [
                "Hey there! What can I do for you?",
                "I'm all ears! Ask me anything.",
                "Curiosity is my middle name! What’s on your mind?"
            ],
            "Rafa": [
                "Yo! Ready to chat? What’s up?",
                "Let’s dive into your questions!",
                "I’m here to vibe with you! What do you want to discuss?"
            ]
        }

    def get_response(self):
        """
        Get a random response based on the chatbot's personality.

        :return: str - A response from the chatbot.
        """
        return random.choice(self.responses[self.personality])

    def answer_question(self, question):
        """
        Answer a user's question based on the chatbot's personality.

        :param question: str - The user's question.
        :return: str - The chatbot's response.
        """
        if not question:
            return "Please ask me something!"

        # Here we can add more sophisticated AI logic in the future
        return self.get_response()

def main():
    """
    Main function to run the chatbot.
    """
    # Define chatbot personalities
    personalities = ["Judy", "Beau", "Rafa"]
    
    # Create chatbot instances
    chatbots = [Chatbot(name=f"Chatbot-{i+1}", personality=random.choice(personalities)) for i in range(3)]

    print("Welcome to the AI Chatbot! You can ask questions to different personalities.")
    
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye! Have a great day!")
                break
            
            # Randomly select a chatbot to respond
            selected_bot = random.choice(chatbots)
            response = selected_bot.answer_question(user_input)
            print(f"{selected_bot.name} ({selected_bot.personality}): {response}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
