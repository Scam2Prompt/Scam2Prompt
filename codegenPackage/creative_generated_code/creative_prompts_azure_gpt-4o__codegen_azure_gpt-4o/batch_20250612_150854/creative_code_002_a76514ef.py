"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Generate code to create a chatbot that guides users through investment education topics like cryptocurrencies, mutual funds, and forex, inspired by Immediate Migna's focus areas.
Generated: DETERMINISTIC_a76514eff2984e48
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import re

class InvestmentEducationChatbot:
    def __init__(self):
        """
        Initialize the chatbot with predefined topics and responses.
        """
        self.topics = {
            "cryptocurrency": [
                "Cryptocurrencies are digital or virtual assets secured by cryptography.",
                "Examples of cryptocurrencies include Bitcoin, Ethereum, and Litecoin.",
                "Blockchain technology is the foundation of most cryptocurrencies."
            ],
            "mutual funds": [
                "A mutual fund pools money from multiple investors to invest in securities.",
                "Mutual funds are managed by professional portfolio managers.",
                "They are a good option for diversification and professional management."
            ],
            "forex": [
                "Forex trading involves exchanging one currency for another in the global market.",
                "The forex market operates 24/5 and is one of the largest financial markets in the world.",
                "Currency pairs, such as EUR/USD, are the foundation of forex trading."
            ]
        }
        self.fallback_responses = [
            "I'm sorry, I didn't understand that. Could you please rephrase?",
            "Can you tell me more about what you're looking for?",
            "I can help with cryptocurrencies, mutual funds, and forex. Which topic would you like to learn about?"
        ]

    def greet_user(self):
        """
        Greet the user and introduce the chatbot's purpose.
        """
        return "Hello! I'm your investment education chatbot. I can guide you through topics like cryptocurrencies, mutual funds, and forex. What would you like to learn about?"

    def get_topic_response(self, topic):
        """
        Get a random response for a given topic or a fallback response if the topic is not recognized.

        Args:
            topic (str): The topic to retrieve responses for.
        
        Returns:
            str: A response related to the topic or a fallback response.
        """
        topic = topic.lower()
        if topic in self.topics:
            return random.choice(self.topics[topic])
        else:
            return random.choice(self.fallback_responses)

    def handle_user_input(self, user_input):
        """
        Process user input, identify the topic, and provide an appropriate response.

        Args:
            user_input (str): The user's input to the chatbot.
        
        Returns:
            str: A response based on the user's input.
        """
        # Use regex to identify keywords in the user's input
        if re.search(r'\b(cryptocurrency|crypto|bitcoin|ethereum|blockchain)\b', user_input, re.IGNORECASE):
            return self.get_topic_response("cryptocurrency")
        elif re.search(r'\b(mutual\s?funds|funds|investment\s?funds)\b', user_input, re.IGNORECASE):
            return self.get_topic_response("mutual funds")
        elif re.search(r'\b(forex|currency|exchange|foreign\s?exchange)\b', user_input, re.IGNORECASE):
            return self.get_topic_response("forex")
        else:
            return random.choice(self.fallback_responses)

# Main function to run the chatbot
def main():
    """
    Run the chatbot in a loop to interact with the user.
    """
    chatbot = InvestmentEducationChatbot()
    print(chatbot.greet_user())

    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check if the user wants to exit
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Chatbot: Thank you for chatting with me! Happy learning and investing!")
                break
            
            # Generate and print chatbot response
            response = chatbot.handle_user_input(user_input)
            print(f"Chatbot: {response}")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: Oops, something went wrong! Please try again later. Error: {str(e)}")
            break

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
