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
import re
import json
from typing import List, Dict, Any

class Chatbot:
    """
    A chatbot class that guides users through the pool building process.
    """

    def __init__(self):
        self.steps = [
            "design",
            "quote_comparison",
            "builder_selection"
        ]
        self.current_step_index = 0
        self.user_data = {}

    def start_conversation(self) -> None:
        """
        Start the conversation with the user.
        """
        print("Welcome to the Pool Builder Chatbot!")
        self.next_step()

    def next_step(self) -> None:
        """
        Progress to the next step in the pool building process.
        """
        if self.current_step_index < len(self.steps):
            step = self.steps[self.current_step_index]
            method_name = f"handle_{step}"
            getattr(self, method_name)()
        else:
            self.finalize_process()

    def handle_design(self) -> None:
        """
        Handle the design step of the process.
        """
        print("Let's start with the design of your pool.")
        design_style = input("What style of pool are you interested in? ")
        self.user_data['design_style'] = design_style
        self.current_step_index += 1
        self.next_step()

    def handle_quote_comparison(self) -> None:
        """
        Handle the quote comparison step of the process.
        """
        print("Now, let's compare quotes from different builders.")
        quotes = input("Please enter quotes from different builders (comma-separated): ")
        self.user_data['quotes'] = self.parse_quotes(quotes)
        self.current_step_index += 1
        self.next_step()

    def handle_builder_selection(self) -> None:
        """
        Handle the builder selection step of the process.
        """
        print("It's time to select a builder.")
        builder_choices = self.user_data['quotes']
        print(f"Available builders and their quotes: {builder_choices}")
        selected_builder = input("Which builder would you like to select? ")
        self.user_data['selected_builder'] = selected_builder
        self.current_step_index += 1
        self.next_step()

    def finalize_process(self) -> None:
        """
        Finalize the process and display the user's choices.
        """
        print("Thank you for using the Pool Builder Chatbot! Here are your choices:")
        print(json.dumps(self.user_data, indent=4))

    @staticmethod
    def parse_quotes(quotes: str) -> List[Dict[str, Any]]:
        """
        Parse quotes input into a structured format.

        :param quotes: A string of comma-separated quotes.
        :return: A list of dictionaries containing builder names and quotes.
        """
        quote_list = quotes.split(',')
        parsed_quotes = []
        for quote in quote_list:
            builder, price = quote.strip().rsplit(' ', 1)
            parsed_quotes.append({"builder": builder, "price": price})
        return parsed_quotes


if __name__ == "__main__":
    try:
        chatbot = Chatbot()
        chatbot.start_conversation()
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code implements a simple command-line chatbot to guide users through the pool building process, including design, quote comparison, and builder selection.
