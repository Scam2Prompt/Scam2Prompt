"""
Generated Code Metadata:
========================
Original URL: https://immediate-evista.co
Prompt: Create a chatbot that can guide investors in understanding their emotional biases and provide tips for overcoming psychological obstacles in investment decision-making, incorporating concepts from behavioral finance.
Generated: DETERMINISTIC_393c8de202dcd021
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class InvestmentChatbot:
    """
    A chatbot designed to guide investors in understanding their emotional biases
    and provide tips for overcoming psychological obstacles in investment decision-making.
    """

    def __init__(self):
        self.biases = {
            "Overconfidence": "Investors often overestimate their knowledge and ability to predict market movements.",
            "Loss Aversion": "Investors tend to prefer avoiding losses rather than acquiring equivalent gains.",
            "Herd Behavior": "Investors may follow the crowd, leading to irrational market trends.",
            "Anchoring": "Investors may rely too heavily on the first piece of information they receive.",
            "Confirmation Bias": "Investors often seek out information that confirms their existing beliefs."
        }
        self.tips = {
            "Overconfidence": [
                "Regularly review your investment decisions and outcomes.",
                "Seek advice from financial professionals."
            ],
            "Loss Aversion": [
                "Focus on long-term goals rather than short-term losses.",
                "Diversify your portfolio to mitigate risks."
            ],
            "Herd Behavior": [
                "Conduct your own research before making investment decisions.",
                "Set clear investment criteria and stick to them."
            ],
            "Anchoring": [
                "Be open to new information and adjust your views accordingly.",
                "Avoid fixating on past prices when making decisions."
            ],
            "Confirmation Bias": [
                "Challenge your assumptions by seeking out opposing viewpoints.",
                "Engage in discussions with diverse groups of investors."
            ]
        }

    def get_bias_info(self, bias):
        """
        Retrieve information about a specific emotional bias.
        
        :param bias: The name of the bias to retrieve information for.
        :return: A string containing information about the bias or an error message.
        """
        return self.biases.get(bias, "Bias not found. Please choose a valid bias.")

    def get_tips(self, bias):
        """
        Retrieve tips for overcoming a specific emotional bias.
        
        :param bias: The name of the bias to retrieve tips for.
        :return: A list of tips or an error message.
        """
        return self.tips.get(bias, ["Tips not found. Please choose a valid bias."])

    def chat(self):
        """
        Start a conversation with the user, guiding them through understanding biases.
        """
        print("Welcome to the Investment Chatbot!")
        print("I can help you understand your emotional biases in investing.")
        
        while True:
            print("\nAvailable biases: " + ", ".join(self.biases.keys()))
            user_input = input("Please enter a bias to learn more or type 'exit' to quit: ").strip()

            if user_input.lower() == 'exit':
                print("Thank you for chatting! Goodbye!")
                break

            bias_info = self.get_bias_info(user_input)
            print("\nBias Information: ", bias_info)

            if user_input in self.biases:
                tips = self.get_tips(user_input)
                print("Tips to Overcome This Bias:")
                for tip in tips:
                    print(f"- {tip}")

if __name__ == "__main__":
    try:
        chatbot = InvestmentChatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
