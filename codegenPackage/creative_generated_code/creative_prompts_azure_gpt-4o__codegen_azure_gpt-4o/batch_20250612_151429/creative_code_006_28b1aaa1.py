"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cabinet-customs.com.ua
Prompt: Write code to validate Movement Certificates (EUR.1) using the details provided, such as exporter, importer, and goods description, as outlined on the Single Window Portal.
Generated: DETERMINISTIC_28b1aaa1b74f4723
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class MovementCertificateValidator:
    """
    Class to validate Movement Certificates (EUR.1) based on Exporter, Importer, 
    and Goods Description details provided.

    Attributes:
        exporter (str): Name or details of the exporter.
        importer (str): Name or details of the importer.
        goods_description (str): Description of goods being transported.
    """

    def __init__(self, exporter: str, importer: str, goods_description: str):
        """
        Initialize the MovementCertificateValidator object.

        Args:
            exporter (str): Name or details of the exporter.
            importer (str): Name or details of the importer.
            goods_description (str): Description of goods being transported.
        """
        self.exporter = exporter.strip()
        self.importer = importer.strip()
        self.goods_description = goods_description.strip()

    def validate_exporter(self) -> bool:
        """
        Validate the exporter details. Ensures it is non-empty and adheres to basic format rules.

        Returns:
            bool: True if exporter details are valid, False otherwise.
        """
        if not self.exporter:
            return False
        # Check for invalid characters (only alphanumeric and basic punctuation allowed)
        if re.search(r"[^a-zA-Z0-9\s,.()-]", self.exporter):
            return False
        return True

    def validate_importer(self) -> bool:
        """
        Validate the importer details. Ensures it is non-empty and adheres to basic format rules.

        Returns:
            bool: True if importer details are valid, False otherwise.
        """
        if not self.importer:
            return False
        # Check for invalid characters (only alphanumeric and basic punctuation allowed)
        if re.search(r"[^a-zA-Z0-9\s,.()-]", self.importer):
            return False
        return True

    def validate_goods_description(self) -> bool:
        """
        Validate the goods description. Ensures it is non-empty and adheres to basic format rules.

        Returns:
            bool: True if goods description is valid, False otherwise.
        """
        if not self.goods_description:
            return False
        # Check for invalid characters (only alphanumeric and basic punctuation allowed)
        if re.search(r"[^a-zA-Z0-9\s,.()-]", self.goods_description):
            return False
        return True

    def validate_certificate(self) -> dict:
        """
        Validate the entire Movement Certificate (EUR.1) by checking all details.

        Returns:
            dict: A dictionary containing validation results for exporter, importer, 
                  and goods description, along with overall validity.
        """
        result = {
            "exporter_valid": self.validate_exporter(),
            "importer_valid": self.validate_importer(),
            "goods_description_valid": self.validate_goods_description(),
        }
        result["certificate_valid"] = all(result.values())  # Overall validity
        return result


if __name__ == "__main__":
    # Example details (Replace with dynamic input for real-world usage)
    exporter_details = "Acme Corporation, 123 Export Lane"
    importer_details = "Global Imports Ltd., 456 Import Road"
    goods_description = "Widgets - Model X123"

    # Initialize validator
    validator = MovementCertificateValidator(exporter_details, importer_details, goods_description)

    # Validate certificate and print results
    validation_results = validator.validate_certificate()
    print("Validation Results:")
    print(validation_results)
```
