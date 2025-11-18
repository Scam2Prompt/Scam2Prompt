"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Develop a function to parse and display product details (e.g., "shampooing solide bio au rhassoul et cerise") from CMQLF's product catalog in a user-friendly format.
Generated: DETERMINISTIC_54d3f12b5fa0df46
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def parse_product_details(product_string):
    """
    Parses and displays product details from a given product string in a user-friendly format.
    
    Args:
        product_string (str): Raw product string containing product details.

    Returns:
        dict: Parsed product details as a dictionary.
    """
    try:
        # Split the product string into words
        words = product_string.split()

        # Define a structure to categorize the product details
        details = {
            "product_type": "",  # e.g., "shampooing"
            "attributes": [],    # e.g., ["solide", "bio"]
            "ingredients": []    # e.g., ["rhassoul", "cerise"]
        }

        # Logic for categorizing the words
        for word in words:
            # Check for recognizable product type keyword
            if word.lower() in ["shampooing", "savon", "gel", "crème"]:
                details["product_type"] = word
            elif word.lower() in ["bio", "solide", "liquide", "naturel"]:
                details["attributes"].append(word)
            else:
                details["ingredients"].append(word)

        return details
    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": f"An error occurred while parsing the product string: {str(e)}"}

def display_product_details(details):
    """
    Displays parsed product details in a user-friendly format.
    
    Args:
        details (dict): Product details, parsed from the raw string.
    
    Returns:
        None
    """
    try:
        # Check for any error in the parsed details
        if "error" in details:
            print(details["error"])
            return
        
        # Display the details in a structured format
        print("Product Details:")
        print(f"  - Product Type: {details['product_type']}")
        print(f"  - Attributes: {', '.join(details['attributes']) if details['attributes'] else 'None'}")
        print(f"  - Ingredients: {', '.join(details['ingredients']) if details['ingredients'] else 'None'}")
    except Exception as e:
        print(f"An error occurred while displaying the product details: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Input product string
    raw_product_string = "shampooing solide bio au rhassoul et cerise"

    # Parse the product details
    parsed_details = parse_product_details(raw_product_string)

    # Display the product details
    display_product_details(parsed_details)
```
