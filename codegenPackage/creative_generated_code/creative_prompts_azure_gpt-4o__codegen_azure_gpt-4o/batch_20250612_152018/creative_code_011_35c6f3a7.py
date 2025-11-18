"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Develop a script to automate the generation of promotional gift sets, including items like notebooks, flash drives, and apparel, as described on the Merchandiso website.
Generated: DETERMINISTIC_35c6f3a79f87dfbe
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import logging
from typing import Dict, List

# Configure logging for debugging and error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define available promotional items
PROMOTIONAL_ITEMS = {
    "notebooks": ["Spiral Notebook", "Executive Notebook", "Pocket Notebook"],
    "flash_drives": ["8GB Flash Drive", "16GB Flash Drive", "32GB Flash Drive"],
    "apparel": ["T-Shirt", "Hoodie", "Baseball Cap"]
}

# Define constraints for the gift sets
MAX_ITEMS_PER_SET = 3
MIN_ITEMS_PER_SET = 1

def generate_gift_set(items: Dict[str, List[str]]) -> List[str]:
    """
    Generate a promotional gift set with a random selection of items.

    Args:
        items (Dict[str, List[str]]): Dictionary of item categories and their options.

    Returns:
        List[str]: A randomly generated gift set containing promotional items.
    """
    gift_set = []
    try:
        # Randomly determine how many items to include in the gift set
        num_items = random.randint(MIN_ITEMS_PER_SET, MAX_ITEMS_PER_SET)

        # Randomly select items for each category until the gift set is complete
        while len(gift_set) < num_items:
            category = random.choice(list(items.keys()))
            item = random.choice(items[category])
            if item not in gift_set:  # Ensure no duplicates in the gift set
                gift_set.append(item)
        return gift_set
    except Exception as e:
        logging.error(f"Error generating gift set: {e}")
        return ["Error occurred while generating gift set"]

def save_gift_set_to_file(gift_set: List[str], file_path: str) -> None:
    """
    Save the generated gift set to a JSON file.

    Args:
        gift_set (List[str]): List of promotional items in the gift set.
        file_path (str): Path to the file where the gift set should be saved.

    Returns:
        None
    """
    try:
        with open(file_path, 'w') as file:
            json.dump({"gift_set": gift_set}, file, indent=4)
        logging.info(f"Gift set successfully saved to {file_path}")
    except IOError as e:
        logging.error(f"Error saving gift set to file: {e}")

def main():
    """
    Main function to generate a promotional gift set and save it to a file.
    """
    logging.info("Starting gift set generation...")
    
    # Generate the gift set
    gift_set = generate_gift_set(PROMOTIONAL_ITEMS)
    
    # Display the generated gift set in the console
    logging.info(f"Generated gift set: {gift_set}")
    
    # Save the gift set to a JSON file
    save_gift_set_to_file(gift_set, "gift_set.json")
    
    logging.info("Gift set generation completed.")

if __name__ == "__main__":
    main()
```
