"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: Write a Python script to design a digital-first fundraising program tailored for nonprofit organizations in emerging markets, incorporating strategies mentioned on Emerging Gifts' website.
Generated: DETERMINISTIC_aa1753e28a47766d
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FundraisingProgram:
    def __init__(self, organization_name: str):
        """
        Initialize the FundraisingProgram with the organization's name.

        :param organization_name: Name of the nonprofit organization
        """
        self.organization_name = organization_name
        self.strategies = []

    def add_strategy(self, strategy: str):
        """
        Add a fundraising strategy to the program.

        :param strategy: A description of the fundraising strategy
        """
        self.strategies.append(strategy)
        logging.info(f"Strategy added: {strategy}")

    def remove_strategy(self, strategy: str):
        """
        Remove a fundraising strategy from the program.

        :param strategy: A description of the fundraising strategy to remove
        """
        try:
            self.strategies.remove(strategy)
            logging.info(f"Strategy removed: {strategy}")
        except ValueError:
            logging.error(f"Strategy not found: {strategy}")

    def get_strategies(self) -> List[str]:
        """
        Get the list of fundraising strategies.

        :return: List of strategies
        """
        return self.strategies

    def save_to_file(self, filename: str):
        """
        Save the fundraising program details to a JSON file.

        :param filename: The name of the file to save the program details
        """
        try:
            with open(filename, 'w') as file:
                json.dump({
                    'organization_name': self.organization_name,
                    'strategies': self.strategies
                }, file, indent=4)
            logging.info(f"Fundraising program saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving to file {filename}: {e}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'FundraisingProgram':
        """
        Load a fundraising program from a JSON file.

        :param filename: The name of the file to load the program details from
        :return: An instance of FundraisingProgram
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                program = cls(data['organization_name'])
                program.strategies = data['strategies']
                logging.info(f"Fundraising program loaded from {filename}")
                return program
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading from file {filename}: {e}")
            return cls("Unknown Organization")  # Return a default instance on error

def main():
    # Example usage of the FundraisingProgram class
    program = FundraisingProgram("Emerging Gifts Nonprofit")

    # Adding strategies based on Emerging Gifts' recommendations
    program.add_strategy("Leverage social media for outreach and engagement.")
    program.add_strategy("Implement a recurring donation program.")
    program.add_strategy("Utilize email marketing for donor communication.")
    program.add_strategy("Create compelling storytelling content to connect with donors.")

    # Save the program to a file
    program.save_to_file("fundraising_program.json")

    # Load the program from a file
    loaded_program = FundraisingProgram.load_from_file("fundraising_program.json")
    logging.info(f"Loaded strategies: {loaded_program.get_strategies()}")

if __name__ == "__main__":
    main()
```
