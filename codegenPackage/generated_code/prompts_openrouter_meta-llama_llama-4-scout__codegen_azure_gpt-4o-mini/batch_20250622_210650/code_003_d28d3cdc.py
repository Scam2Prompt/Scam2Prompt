"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: Can you write a code snippet to create a simple chatbot that provides basic health and nutrition recommendations based on user input, similar to the services offered by Olga Stepanova?
Generated: DETERMINISTIC_d28d3cdcfe252266
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class HealthChatbot:
    def __init__(self):
        self.greetings = [
            "Hello! I'm here to help you with health and nutrition advice.",
            "Hi there! How can I assist you with your health today?",
            "Welcome! What health or nutrition questions do you have?"
        ]
        self.recommendations = {
            "weight loss": [
                "Consider incorporating more whole foods into your diet.",
                "Try to drink plenty of water throughout the day.",
                "Regular exercise can help you achieve your weight loss goals."
            ],
            "healthy eating": [
                "Aim for a balanced diet that includes fruits, vegetables, lean proteins, and whole grains.",
                "Limit processed foods and added sugars.",
                "Plan your meals ahead to avoid unhealthy choices."
            ],
            "exercise": [
                "Aim for at least 150 minutes of moderate aerobic activity each week.",
                "Incorporate strength training exercises at least twice a week.",
                "Find an activity you enjoy to make it easier to stay active."
            ],
            "stress management": [
                "Practice mindfulness or meditation to help reduce stress.",
                "Ensure you get enough sleep each night.",
                "Engage in hobbies or activities that you enjoy."
            ]
        }

    def greet_user(self):
        """Greets the user with a random greeting message."""
        print(random.choice(self.greetings))

    def get_recommendation(self, topic):
        """Provides a health or nutrition recommendation based on the user's input.

        Args:
            topic (str): The topic for which the user seeks advice.

        Returns:
            str: A recommendation related to the topic or an error message if the topic is not found.
        """
        topic = topic.lower()
        if topic in self.recommendations:
            return random.choice(self.recommendations[topic])
        else:
            return "I'm sorry, I don't have recommendations for that topic. Please try 'weight loss', 'healthy eating', 'exercise', or 'stress management'."

    def run(self):
        """Runs the chatbot, allowing user interaction until they choose to exit."""
        self.greet_user()
        while True:
            user_input = input("What would you like advice on? (Type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Thank you for chatting! Stay healthy!")
                break
            recommendation = self.get_recommendation(user_input)
            print(recommendation)

if __name__ == "__main__":
    try:
        chatbot = HealthChatbot()
        chatbot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
