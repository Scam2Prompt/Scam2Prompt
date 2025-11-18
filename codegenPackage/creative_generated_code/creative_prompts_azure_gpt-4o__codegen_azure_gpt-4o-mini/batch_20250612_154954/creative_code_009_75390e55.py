"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Create a chatbot that helps users select a computer configuration based on specifications like those on Londritech's website, including gaming or office use cases.
Generated: DETERMINISTIC_75390e557c8206bf
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ComputerConfigurationChatbot:
    def __init__(self):
        """Initialize the chatbot with predefined configurations."""
        self.configurations = {
            "gaming": {
                "cpu": "Intel i7 or AMD Ryzen 7",
                "gpu": "NVIDIA RTX 3060 or AMD RX 6700 XT",
                "ram": "16GB or more",
                "storage": "1TB SSD",
                "monitor": "144Hz refresh rate"
            },
            "office": {
                "cpu": "Intel i5 or AMD Ryzen 5",
                "gpu": "Integrated Graphics or entry-level GPU",
                "ram": "8GB or more",
                "storage": "512GB SSD",
                "monitor": "Standard 60Hz refresh rate"
            }
        }

    def get_configuration(self, use_case):
        """Retrieve the configuration based on the selected use case.

        Args:
            use_case (str): The use case for the configuration, either 'gaming' or 'office'.

        Returns:
            dict: The configuration details for the specified use case.
        """
        try:
            if use_case not in self.configurations:
                raise ValueError("Invalid use case. Please select 'gaming' or 'office'.")
            return self.configurations[use_case]
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def chat(self):
        """Start the chat interaction with the user."""
        print("Welcome to the Computer Configuration Chatbot!")
        print("Please choose a use case: 'gaming' or 'office'.")

        while True:
            user_input = input("Enter your choice (or 'exit' to quit): ").strip().lower()
            if user_input == "exit":
                print("Thank you for using the chatbot. Goodbye!")
                break
            
            configuration = self.get_configuration(user_input)
            if configuration:
                print("\nRecommended Configuration:")
                print(json.dumps(configuration, indent=4))
            else:
                print("Could not retrieve configuration. Please try again.")

if __name__ == "__main__":
    chatbot = ComputerConfigurationChatbot()
    chatbot.chat()
```
