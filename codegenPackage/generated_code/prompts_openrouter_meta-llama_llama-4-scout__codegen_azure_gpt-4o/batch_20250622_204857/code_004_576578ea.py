"""
Generated Code Metadata:
========================
Original URL: https://pass-vee.com
Prompt: Create a glossary of key terms used in Changexcapital's educational resources, including definitions for terms like "Margin Call," "Margin Level," and "Stop Out Level," and provide examples of how they are applied in trading scenarios.
Generated: DETERMINISTIC_576578eafa2ad0e8
Batch ID: 20250622_204857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# glossary.py

"""
Glossary Generator for Changexcapital's Educational Resources

This script creates a glossary of key trading terms used in Changexcapital's educational resources.
Each term includes a definition and an example of how it is applied in trading scenarios.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import json

# Define the glossary as a dictionary
glossary = {
    "Margin Call": {
        "definition": (
            "A margin call occurs when the equity in a trading account falls below the required margin. "
            "It is a broker's demand for the trader to deposit more funds or close positions to meet margin requirements."
        ),
        "example": (
            "If a trader has $1,000 in equity and opens a leveraged position requiring $800 in margin, "
            "a margin call may occur if the equity drops below $800 due to losses."
        ),
    },
    "Margin Level": {
        "definition": (
            "Margin Level is the ratio of equity to used margin, expressed as a percentage. "
            "It helps traders understand the health of their account and the risk of a margin call."
        ),
        "example": (
            "Margin Level = (Equity / Used Margin) * 100. For instance, if equity is $1,000 and used margin is $500, "
            "the margin level is 200%. A margin level below 100% may trigger a margin call."
        ),
    },
    "Stop Out Level": {
        "definition": (
            "The Stop Out Level is the margin level at which the broker will automatically close positions to prevent further losses. "
            "It is typically set by the broker as a safety measure."
        ),
        "example": (
            "If the Stop Out Level is 50% and the margin level drops to 50% or below, the broker will start closing positions. "
            "For example, if equity is $500 and used margin is $1,000, the margin level is 50%, triggering a stop out."
        ),
    },
}

# Function to display the glossary
def display_glossary(glossary):
    """
    Displays the glossary in a readable format.

    Args:
        glossary (dict): A dictionary containing terms, definitions, and examples.
    """
    print("Glossary of Key Trading Terms:\n")
    for term, details in glossary.items():
        print(f"Term: {term}")
        print(f"Definition: {details['definition']}")
        print(f"Example: {details['example']}\n")

# Function to save the glossary to a JSON file
def save_glossary_to_file(glossary, filename="glossary.json"):
    """
    Saves the glossary to a JSON file.

    Args:
        glossary (dict): A dictionary containing terms, definitions, and examples.
        filename (str): The name of the file to save the glossary to. Defaults to 'glossary.json'.
    """
    try:
        with open(filename, "w") as file:
            json.dump(glossary, file, indent=4)
        print(f"Glossary successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving glossary to file: {e}")

# Main function
def main():
    """
    Main function to display and save the glossary.
    """
    display_glossary(glossary)
    save_glossary_to_file(glossary)

# Entry point of the script
if __name__ == "__main__":
    main()
```
