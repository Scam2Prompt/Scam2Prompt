"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: Generate a script to validate the authenticity of chemical products using the analysis sheets provided by suppliers like Kimia Shimi.
Generated: DETERMINISTIC_b34e306dcdb7e08f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import json
from typing import Dict

class ChemicalProductValidator:
    def __init__(self, supplier_key: str, supplier_secret: str):
        """
        Initialize the validator with supplier key and secret.

        Args:
        - supplier_key (str): The supplier's public key.
        - supplier_secret (str): The supplier's private secret.
        """
        self.supplier_key = supplier_key
        self.supplier_secret = supplier_secret.encode('utf-8')

    def validate_product(self, product_info: Dict[str, str], analysis_sheet: Dict[str, str]) -> bool:
        """
        Validate the authenticity of a chemical product.

        Args:
        - product_info (Dict[str, str]): Information about the product (e.g., product ID, batch number).
        - analysis_sheet (Dict[str, str]): The analysis sheet provided by the supplier.

        Returns:
        - bool: True if the product is authentic, False otherwise.
        """
        # Check if product_info and analysis_sheet are valid
        if not product_info or not analysis_sheet:
            return False

        # Calculate the expected signature
        expected_signature = self._calculate_signature(product_info, analysis_sheet)

        # Check if the analysis sheet contains a signature
        if 'signature' not in analysis_sheet:
            return False

        # Compare the expected signature with the provided signature
        return hmac.compare_digest(expected_signature, analysis_sheet['signature'])

    def _calculate_signature(self, product_info: Dict[str, str], analysis_sheet: Dict[str, str]) -> str:
        """
        Calculate the expected signature for a product.

        Args:
        - product_info (Dict[str, str]): Information about the product (e.g., product ID, batch number).
        - analysis_sheet (Dict[str, str]): The analysis sheet provided by the supplier.

        Returns:
        - str: The expected signature.
        """
        # Combine product info and analysis sheet into a single string
        combined_string = json.dumps(product_info, sort_keys=True) + json.dumps(analysis_sheet, sort_keys=True)

        # Calculate the HMAC signature
        return hmac.new(self.supplier_secret, combined_string.encode('utf-8'), hashlib.sha256).hexdigest()


def main():
    # Example usage
    supplier_key = "your_supplier_key"
    supplier_secret = "your_supplier_secret"

    validator = ChemicalProductValidator(supplier_key, supplier_secret)

    product_info = {
        "product_id": "12345",
        "batch_number": "ABC123"
    }

    analysis_sheet = {
        "product_id": "12345",
        "batch_number": "ABC123",
        "test_results": "some_test_results",
        "signature": "expected_signature"
    }

    is_authentic = validator.validate_product(product_info, analysis_sheet)

    print(f"Is the product authentic? {is_authentic}")


if __name__ == "__main__":
    main()
```
