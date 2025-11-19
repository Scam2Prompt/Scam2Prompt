"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Develop a simple chatbot that can provide basic troubleshooting guidance for common issues with white goods appliances, using the information available on the Ankara Beyaz Eşya Teknik Servisi website.
Generated: DETERMINISTIC_4c849bcfd53cd3e9
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Chatbot for troubleshooting white goods appliances
class ApplianceTroubleshootingChatbot:
    def __init__(self):
        # Initialize common issues and troubleshooting steps
        self.troubleshooting_guide = {
            "refrigerator": {
                "not cooling": "Check if the thermostat is set correctly. Ensure the vents are not blocked and clean the condenser coils.",
                "leaking water": "Inspect the drain pan for cracks and ensure the defrost drain is not clogged.",
            },
            "washing machine": {
                "not spinning": "Ensure the lid is closed properly. Check for unbalanced loads and inspect the drive belt.",
                "leaking water": "Check the hoses for cracks or loose connections. Inspect the door seal for damage.",
            },
            "dishwasher": {
                "not cleaning dishes": "Ensure the spray arms are not clogged. Use the correct detergent and check the water inlet valve.",
                "leaking water": "Inspect the door gasket for damage and ensure the dishwasher is level.",
            },
            "oven": {
                "not heating": "Check the heating element for damage. Ensure the temperature settings are correct.",
                "door won't close": "Inspect the hinges and door seal for obstructions or damage.",
            },
        }

    def greet_user(self):
        # Greet the user
        print("Hello! I'm your appliance troubleshooting assistant.")
        print("I can help you with common issues related to refrigerators, washing machines, dishwashers, and ovens.")
        print("Type 'exit' anytime to end the conversation.\n")

    def get_user_input(self):
        # Get input from the user
        return input("Please describe your appliance issue (e.g., 'refrigerator not cooling'): ").strip().lower()

    def provide_guidance(self, user_input):
        # Provide troubleshooting guidance based on user input
        for appliance, issues in self.troubleshooting_guide.items():
            if appliance in user_input:
                for issue, solution in issues.items():
                    if issue in user_input:
                        return f"Troubleshooting for {appliance} - {issue}: {solution}"
        return "I'm sorry, I couldn't find a solution for your issue. Please check the appliance manual or contact a technician."

    def run(self):
        # Main chatbot loop
        self.greet_user()
        while True:
            try:
                user_input = self.get_user_input()
                if user_input == "exit":
                    print("Thank you for using the troubleshooting assistant. Goodbye!")
                    break
                response = self.provide_guidance(user_input)
                print(response + "\n")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.\n")


# Entry point for the chatbot
if __name__ == "__main__":
    # Create an instance of the chatbot and start it
    chatbot = ApplianceTroubleshootingChatbot()
    chatbot.run()
```
