"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Write a script to analyze customer preferences for products like high-visibility gloves, fire-resistant gloves, and impact gloves, based on Rising Star International's product descriptions.
Generated: DETERMINISTIC_1abdc4c05a2482bf
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import re
from collections import defaultdict
from typing import Dict, List

# Define a function to preprocess product descriptions
def preprocess_description(description: str) -> str:
    """
    Preprocess product descriptions by converting to lowercase and removing special characters.

    Args:
    description (str): Product description.

    Returns:
    str: Preprocessed product description.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', description).lower()

# Define a function to extract keywords from product descriptions
def extract_keywords(description: str) -> List[str]:
    """
    Extract keywords from product descriptions.

    Args:
    description (str): Product description.

    Returns:
    List[str]: List of extracted keywords.
    """
    keywords = ["high-visibility", "fire-resistant", "impact", "glove", "gloves"]
    return [keyword for keyword in keywords if keyword in description]

# Define a function to analyze customer preferences
def analyze_preferences(products: Dict[str, str]) -> Dict[str, int]:
    """
    Analyze customer preferences for products.

    Args:
    products (Dict[str, str]): Dictionary of product names and descriptions.

    Returns:
    Dict[str, int]: Dictionary of product preferences with their frequencies.
    """
    preferences = defaultdict(int)
    for product, description in products.items():
        description = preprocess_description(description)
        keywords = extract_keywords(description)
        for keyword in keywords:
            preferences[keyword] += 1
    return dict(preferences)

# Define a function to get product information from a CSV file
def get_product_info(csv_file: str) -> Dict[str, str]:
    """
    Get product information from a CSV file.

    Args:
    csv_file (str): Path to the CSV file.

    Returns:
    Dict[str, str]: Dictionary of product names and descriptions.
    """
    try:
        df = pd.read_csv(csv_file)
        return df.set_index('Product Name')['Description'].to_dict()
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
        return {}
    except pd.errors.EmptyDataError:
        print("The file is empty. Please check the file contents.")
        return {}
    except pd.errors.ParserError:
        print("Error parsing the file. Please check the file format.")
        return {}

# Main function
def main():
    csv_file = 'products.csv'  # replace with your CSV file
    products = get_product_info(csv_file)
    preferences = analyze_preferences(products)
    print("Customer Preferences:")
    for preference, frequency in preferences.items():
        print(f"{preference}: {frequency}")

if __name__ == "__main__":
    main()
```
