"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolz.uk
Prompt: Develop a chatbot that guides users through the pool building process, including design, quote comparison, and builder selection, based on the EasyBuild methodology described on Poolz.
Generated: DETERMINISTIC_e0e4cf600d94236d
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PoolBuildingChatbot:
    """
    A chatbot to guide users through the pool building process using the EasyBuild methodology.
    Includes design selection, quote comparison, and builder selection.
    """

    def __init__(self):
        self.pool_designs = ["Rectangular", "Freeform", "Infinity", "Lap Pool", "Plunge Pool"]
        self.builder_quotes = {
            "Builder A": 25000,
            "Builder B": 27000,
            "Builder C": 23000,
            "Builder D": 28000
        }
        self.selected_design = None
        self.selected_builder = None

    def greet_user(self):
        """
        Greets the user and explains the chatbot's purpose.
        """
        print("Welcome to the Pool Building Chatbot!")
        print("I will guide you through the EasyBuild methodology.")
        print("Let's help you design your dream pool, compare quotes, and choose a builder.")

    def choose_pool_design(self):
        """
        Allows the user to select a pool design from the available options.
        """
        print("\nAvailable Pool Designs:")
        for i, design in enumerate(self.pool_designs, start=1):
            print(f"{i}. {design}")
        
        try:
            choice = int(input("\nSelect the number corresponding to your preferred design: "))
            if choice < 1 or choice > len(self.pool_designs):
                raise ValueError("Invalid choice. Please select a valid design number.")
            self.selected_design = self.pool_designs[choice - 1]
            print(f"You selected: {self.selected_design}")
        except ValueError as ve:
            print(f"Error: {ve}. Let's try again.")
            self.choose_pool_design()

    def compare_quotes(self):
        """
        Displays builder quotes for comparison and allows the user to select a builder.
        """
        print("\nBuilder Quotes:")
        for builder, quote in self.builder_quotes.items():
            print(f"{builder}: ${quote}")
        
        try:
            builder_name = input("\nEnter the name of the builder you'd like to select: ").strip()
            if builder_name not in self.builder_quotes:
                raise ValueError("Invalid builder name. Please select a valid builder.")
            self.selected_builder = builder_name
            print(f"You selected: {self.selected_builder} with a quote of ${self.builder_quotes[builder_name]}")
        except ValueError as ve:
            print(f"Error: {ve}. Let's try again.")
            self.compare_quotes()

    def summarize_choices(self):
        """
        Summarizes the user's choices at the end of the process.
        """
        print("\nSummary of Your Choices:")
        print(f"Pool Design: {self.selected_design}")
        print(f"Builder: {self.selected_builder} with a quote of ${self.builder_quotes[self.selected_builder]}")
        print("Thank you for using the Pool Building Chatbot!")

    def run(self):
        """
        Executes the chatbot workflow in sequence.
        """
        self.greet_user()
        self.choose_pool_design()
        self.compare_quotes()
        self.summarize_choices()


# Entry point for the chatbot execution
if __name__ == "__main__":
    try:
        chatbot = PoolBuildingChatbot()
        chatbot.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
