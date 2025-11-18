"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://transactionfinder.in
Prompt: Create a chatbot using Python that educates users on scam types and provides guidance on recovering lost funds, following the strategies outlined on Transaction Finder.
Generated: DETERMINISTIC_bbee8670270538b5
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Chatbot:
    def __init__(self):
        self.scam_types = {
            "phishing": "Phishing scams involve tricking individuals into revealing sensitive information such as passwords or credit card numbers, often through fake emails or websites.",
            "tech_support": "Tech support scams typically involve scammers posing as technical support staff to gain remote access to your computer or to steal your personal information.",
            "investment": "Investment scams promise high returns with little risk, often involving Ponzi schemes or fake investment opportunities.",
            "romance": "Romance scams involve building a false relationship to persuade individuals to send money or personal information.",
            "lottery": "Lottery scams convince victims that they've won a lottery they never entered, requiring payment of fees to claim the prize."
        }
        self.recovery_steps = [
            "Contact your bank or credit card company immediately to report the fraud.",
            "File a report with your local law enforcement agency.",
            "Report the scam to the Federal Trade Commission (FTC) through their website.",
            "Change any compromised passwords and enable two-factor authentication where possible.",
            "Consult with a legal professional if you've lost a significant amount of money."
        ]

    def greet_user(self):
        return "Hello! I'm ScamBot, here to educate you on different types of scams and guide you on how to recover lost funds."

    def get_scam_info(self, scam_type):
        """Retrieve information about a specific scam type."""
        info = self.scam_types.get(scam_type.lower())
        if info:
            return info
        else:
            return "I'm sorry, I don't have information on that scam type. Please try another."

    def get_recovery_guidance(self):
        """Provide guidance on recovering lost funds."""
        return random.choice(self.recovery_steps)

    def main(self):
        """Main method to run the chatbot interaction."""
        print(self.greet_user())
        while True:
            user_input = input("\nWhat would you like to know? (type 'exit' to end) ").strip()
            if user_input.lower() == 'exit':
                print("Thank you for chatting! Stay safe!")
                break
            elif user_input.lower() in self.scam_types:
                print(self.get_scam_info(user_input))
            elif "recover" in user_input.lower():
                print(self.get_recovery_guidance())
            else:
                print("I'm not sure about that. Please ask about a specific scam type or how to recover lost funds.")
                
if __name__ == "__main__":
    try:
        chatbot = Chatbot()
        chatbot.main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
