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
    def __init__(self, exporter, importer, goods_description):
        self.exporter = exporter
        self.importer = importer
        self.goods_description = goods_description

    def is_valid_exporter(self):
        """
        Validate the exporter's name and details.
        The exporter name should not be empty and should follow basic formatting.
        """
        return bool(self.exporter) and isinstance(self.exporter, str) and len(self.exporter) > 0

    def is_valid_importer(self):
        """
        Validate the importer's name and details.
        The importer name should not be empty and should follow basic formatting.
        """
        return bool(self.importer) and isinstance(self.importer, str) and len(self.importer) > 0

    def is_valid_goods_description(self):
        """
        Validate the goods description.
        The description should not be empty and should follow basic formatting.
        """
        return bool(self.goods_description) and isinstance(self.goods_description, str) and len(self.goods_description) > 0

    def validate(self):
        """
        Validate the Movement Certificate (EUR.1).
        Checks the validity of the exporter, importer, and goods description.
        Returns a dictionary with validation results.
        """
        validation_results = {
            'exporter_valid': self.is_valid_exporter(),
            'importer_valid': self.is_valid_importer(),
            'goods_description_valid': self.is_valid_goods_description(),
            'all_valid': all([
                self.is_valid_exporter(),
                self.is_valid_importer(),
                self.is_valid_goods_description()
            ])
        }
        return validation_results

def main():
    # Sample details for a Movement Certificate
    exporter_name = "ABC Exports Ltd."
    importer_name = "XYZ Imports Inc."
    goods_desc = "Electronics goods - Laptops and Accessories"

    # Create a Movement Certificate Validator instance
    validator = MovementCertificateValidator(exporter_name, importer_name, goods_desc)

    # Validate the Movement Certificate
    validation_results = validator.validate()

    # Print the validation results
    print("Movement Certificate Validation Results:")
    for key, value in validation_results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
