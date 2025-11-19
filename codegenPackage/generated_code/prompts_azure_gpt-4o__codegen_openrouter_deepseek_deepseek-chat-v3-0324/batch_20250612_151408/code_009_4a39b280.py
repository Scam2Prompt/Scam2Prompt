"""
Generated Code Metadata:
========================
Original URL: https://iwslink.com
Prompt: Write code to implement a feature that educates users on safe product usage by providing immediate access to product-specific content, inspired by Interactive Warning Systems.
Generated: DETERMINISTIC_4a39b2808e135cea
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Optional

class ProductSafetyEducator:
    """
    A class to provide product-specific safety education content to users.
    """

    def __init__(self, safety_content_file: str = "safety_content.json"):
        """
        Initialize the ProductSafetyEducator with safety content.

        Args:
            safety_content_file: Path to JSON file containing safety content.
        """
        self.safety_content = self._load_safety_content(safety_content_file)

    def _load_safety_content(self, file_path: str) -> Dict:
        """
        Load safety content from a JSON file.

        Args:
            file_path: Path to the JSON file.

        Returns:
            Dictionary containing safety content.

        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Safety content file not found: {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in safety content file: {e}", e.doc, e.pos)

    def get_safety_content(self, product_id: str) -> Optional[Dict]:
        """
        Retrieve safety content for a specific product.

        Args:
            product_id: The ID of the product to get safety info for.

        Returns:
            Dictionary containing safety content for the product, or None if not found.
        """
        return self.safety_content.get(product_id)

    def display_safety_content(self, product_id: str) -> None:
        """
        Display safety content for a specific product.

        Args:
            product_id: The ID of the product to display safety info for.
        """
        content = self.get_safety_content(product_id)
        if content:
            print("\n=== PRODUCT SAFETY INFORMATION ===")
            print(f"Product: {content.get('name', 'Unknown Product')}")
            print(f"\nWarnings:")
            for warning in content.get('warnings', []):
                print(f"- {warning}")
            print(f"\nSafe Usage Instructions:")
            for instruction in content.get('instructions', []):
                print(f"- {instruction}")
            print("\nFor emergencies, contact:", content.get('emergency_contact', 'N/A'))
            print("===============================\n")
        else:
            print(f"No safety information found for product ID: {product_id}")


# Example usage
if __name__ == "__main__":
    try:
        educator = ProductSafetyEducator()
        
        # Example product IDs (would normally come from user input or system)
        test_products = ["prod_001", "prod_002", "invalid_id"]
        
        for product_id in test_products:
            educator.display_safety_content(product_id)
            
    except Exception as e:
        print(f"Error initializing safety educator: {e}")
```
