"""
Generated Code Metadata:
========================
Original URL: https://refund-me.net
Prompt: Develop a chatbot using Python that guides users through the fraud recovery claim process, referencing steps like case assessment, bank submission, and escalation to the FOS.
Generated: DETERMINISTIC_5f064a6bb9bb3b95
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class FraudRecoveryChatbot:
    def __init__(self):
        self.steps = [
            "Step 1: Case Assessment",
            "Step 2: Bank Submission",
            "Step 3: Escalation to the Financial Ombudsman Service (FOS)"
        ]
        self.current_step = 0

    def start_chat(self):
        """Initiates the chat with the user."""
        print("Welcome to the Fraud Recovery Claim Chatbot!")
        self.next_step()

    def next_step(self):
        """Advances to the next step in the fraud recovery process."""
        if self.current_step < len(self.steps):
            print(self.steps[self.current_step])
            self.current_step += 1
            self.ask_for_input()
        else:
            print("You have completed the fraud recovery claim process.")
            self.end_chat()

    def ask_for_input(self):
        """Prompts the user for input to proceed to the next step."""
        user_input = input("Type 'next' to proceed to the next step or 'exit' to end the chat: ").strip().lower()
        if user_input == 'next':
            self.next_step()
        elif user_input == 'exit':
            self.end_chat()
        else:
            print("Invalid input. Please type 'next' or 'exit'.")
            self.ask_for_input()

    def end_chat(self):
        """Ends the chat session."""
        print("Thank you for using the Fraud Recovery Claim Chatbot. Goodbye!")
        sys.exit()

if __name__ == "__main__":
    try:
        chatbot = FraudRecoveryChatbot()
        chatbot.start_chat()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```
