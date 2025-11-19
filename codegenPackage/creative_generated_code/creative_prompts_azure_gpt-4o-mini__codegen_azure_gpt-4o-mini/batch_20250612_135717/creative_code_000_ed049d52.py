"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://complyaml.com
Prompt: Generate a code snippet for an interactive training module that helps staff understand AML (FIC) obligations.
Generated: DETERMINISTIC_ed049d527735fdca
Batch ID: 20250612_135717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class AMLTrainingModule:
    """
    A class to represent an interactive training module for Anti-Money Laundering (AML) obligations.
    """

    def __init__(self):
        """
        Initializes the training module with a list of training topics.
        """
        self.topics = [
            "Introduction to AML",
            "Understanding Money Laundering",
            "AML Regulations and Compliance",
            "FIC Obligations",
            "Reporting Suspicious Transactions",
            "Case Studies and Examples"
        ]
        self.current_topic_index = 0

    def display_topic(self):
        """
        Displays the current training topic.
        """
        try:
            print(f"\nCurrent Topic: {self.topics[self.current_topic_index]}\n")
        except IndexError as e:
            print("Error: Unable to display topic. Index out of range.")
            print(f"Details: {e}")
            self.exit_module()

    def next_topic(self):
        """
        Advances to the next training topic, if available.
        """
        if self.current_topic_index < len(self.topics) - 1:
            self.current_topic_index += 1
            self.display_topic()
        else:
            print("You have completed all topics. Thank you for participating!")
            self.exit_module()

    def previous_topic(self):
        """
        Goes back to the previous training topic, if available.
        """
        if self.current_topic_index > 0:
            self.current_topic_index -= 1
            self.display_topic()
        else:
            print("You are already at the first topic.")
        
    def exit_module(self):
        """
        Exits the training module gracefully.
        """
        print("Exiting the AML Training Module. Thank you!")
        sys.exit()

    def start_training(self):
        """
        Starts the interactive training session.
        """
        print("Welcome to the AML Training Module!")
        self.display_topic()

        while True:
            user_input = input("Enter 'n' for next topic, 'p' for previous topic, or 'e' to exit: ").strip().lower()
            if user_input == 'n':
                self.next_topic()
            elif user_input == 'p':
                self.previous_topic()
            elif user_input == 'e':
                self.exit_module()
            else:
                print("Invalid input. Please enter 'n', 'p', or 'e'.")

if __name__ == "__main__":
    try:
        module = AMLTrainingModule()
        module.start_training()
    except Exception as e:
        print("An unexpected error occurred in the AML Training Module.")
        print(f"Details: {e}")
        sys.exit(1)
```
