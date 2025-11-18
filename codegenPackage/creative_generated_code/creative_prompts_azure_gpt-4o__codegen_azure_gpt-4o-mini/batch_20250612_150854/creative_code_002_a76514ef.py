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

class InvestmentChatbot:
    def __init__(self):
        """Initialize the chatbot with predefined topics and responses."""
        self.topics = {
            "cryptocurrencies": [
                "Cryptocurrencies are digital or virtual currencies that use cryptography for security.",
                "Bitcoin is the first and most well-known cryptocurrency, created in 2009.",
                "Blockchain is the technology that underlies most cryptocurrencies."
            ],
            "mutual funds": [
                "Mutual funds are investment programs funded by shareholders that trade in diversified holdings.",
                "They are managed by professional portfolio managers and can be a good way to diversify your investments.",
                "Investors can buy shares in a mutual fund, and the fund's returns are distributed among shareholders."
            ],
            "forex": [
                "Forex, or foreign exchange, is the market where currencies are traded.",
                "It is the largest financial market in the world, with a daily trading volume exceeding $6 trillion.",
                "Forex trading involves speculating on the price movements of currency pairs."
            ]
        }

    def greet_user(self):
        """Greet the user and introduce the chatbot's purpose."""
        greetings = [
            "Hello! I'm your investment education chatbot.",
            "Hi there! I can help you learn about cryptocurrencies, mutual funds, and forex."
        ]
        print(random.choice(greetings))

    def get_topic(self):
        """Prompt the user to choose an investment topic."""
        print("Which topic would you like to learn about? (cryptocurrencies, mutual funds, forex)")
        while True:
            choice = input("Please enter a topic: ").strip().lower()
            if choice in self.topics:
                return choice
            else:
                print("Invalid choice. Please select from the available topics.")

    def provide_info(self, topic):
        """Provide information about the selected topic."""
        info = random.choice(self.topics[topic])
        print(f"Here is some information about {topic}: {info}")

    def run(self):
        """Run the chatbot conversation with the user."""
        self.greet_user()
        try:
            while True:
                topic = self.get_topic()
                self.provide_info(topic)
                again = input("Would you like to learn about another topic? (yes/no): ").strip().lower()
                if again != 'yes':
                    print("Thank you for using the Investment Education Chatbot! Goodbye!")
                    break
        except KeyboardInterrupt:
            print("\nChatbot terminated by user.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chatbot = InvestmentChatbot()
    chatbot.run()
```
