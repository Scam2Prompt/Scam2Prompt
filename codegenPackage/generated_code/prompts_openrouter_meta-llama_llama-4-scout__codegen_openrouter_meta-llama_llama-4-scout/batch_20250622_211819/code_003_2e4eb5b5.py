"""
Generated Code Metadata:
========================
Original URL: https://jamcards.io
Prompt: "Generate a list of all traits mentioned for the 'Heart Full of Love' JamCards, including ARTIST, COLLECTIBLE, INSTRUMENT, MUSICIAN, VOCAL, and VOCALS."
Generated: DETERMINISTIC_2e4eb5b5b85189f3
Batch ID: 20250622_211819
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

def load_jamcards_data(file_path):
    """
    Load JamCards data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of JamCards data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"Error: File '{file_path}' not found.")
        raise e
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{file_path}'.")
        raise e

def extract_traits(jamcards_data, traits):
    """
    Extract specific traits from JamCards data.

    Args:
        jamcards_data (list): A list of JamCards data.
        traits (list): A list of traits to extract.

    Returns:
        dict: A dictionary with traits as keys and lists of values as values.
    """
    extracted_traits = {trait: [] for trait in traits}

    for card in jamcards_data:
        for trait in traits:
            if trait in card:
                extracted_traits[trait].append(card[trait])

    return extracted_traits

def main():
    file_path = 'jamcards_data.json'  # Replace with your file path
    traits = ['ARTIST', 'COLLECTIBLE', 'INSTRUMENT', 'MUSICIAN', 'VOCAL', 'VOCALS']

    try:
        jamcards_data = load_jamcards_data(file_path)
        extracted_traits = extract_traits(jamcards_data, traits)

        for trait, values in extracted_traits.items():
            print(f"**{trait}**")
            print(values)
            print()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
