"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate Python code for a quality control module that ensures compliance with cosmetic product standards, inspired by Fabricare Cosméticos' approach to quality management.
Generated: DETERMINISTIC_54a509fdc0438c01
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QualityControlError(Exception):
    """Custom exception for quality control failures."""
    pass

class CosmeticQualityControl:
    """
    A class to perform quality control checks for cosmetic products.
    Inspired by Fabricare Cosméticos' approach to quality management.
    """

    # Define thresholds for compliance standards (example values)
    STANDARDS = {
        'pH_range': (4.5, 7.0),  # Acceptable pH range
        'microbial_limit': 1000,  # Maximum allowable microbial count (CFU)
        'heavy_metal_limit': 10,  # Maximum allowable heavy metal content (ppm)
    }

    def __init__(self, product_name):
        """
        Initialize the QualityControl instance.

        Args:
            product_name (str): Name of the cosmetic product.
        """
        self.product_name = product_name

    def check_ph(self, ph_value):
        """
        Check if the pH value is within the acceptable range.

        Args:
            ph_value (float): pH value to check.

        Returns:
            bool: True if pH is compliant, False otherwise.

        Raises:
            QualityControlError: If pH value is out of range.
        """
        min_ph, max_ph = self.STANDARDS['pH_range']
        if not (min_ph <= ph_value <= max_ph):
            raise QualityControlError(f"pH value of {ph_value} is not within the acceptable range ({min_ph} - {max_ph}).")
        logging.info(f"pH value {ph_value} is compliant.")
        return True

    def check_microbial_count(self, microbial_count):
        """
        Check if the microbial count is below the maximum allowable limit.

        Args:
            microbial_count (int): Microbial count (CFU).

        Returns:
            bool: True if microbial count is compliant, False otherwise.

        Raises:
            QualityControlError: If microbial count exceeds the limit.
        """
        if microbial_count > self.STANDARDS['microbial_limit']:
            raise QualityControlError(f"Microbial count of {microbial_count} exceeds the allowable limit ({self.STANDARDS['microbial_limit']}).")
        logging.info(f"Microbial count {microbial_count} is compliant.")
        return True

    def check_heavy_metal_content(self, metal_content):
        """
        Check if the heavy metal content is below the maximum allowable limit.

        Args:
            metal_content (float): Heavy metal content (ppm).

        Returns:
            bool: True if heavy metal content is compliant, False otherwise.

        Raises:
            QualityControlError: If heavy metal content exceeds the limit.
        """
        if metal_content > self.STANDARDS['heavy_metal_limit']:
            raise QualityControlError(f"Heavy metal content of {metal_content} ppm exceeds the allowable limit ({self.STANDARDS['heavy_metal_limit']} ppm).")
        logging.info(f"Heavy metal content {metal_content} ppm is compliant.")
        return True

    def perform_quality_checks(self, ph_value, microbial_count, heavy_metal_content):
        """
        Perform all quality control checks.

        Args:
            ph_value (float): pH value of the product.
            microbial_count (int): Microbial count (CFU) of the product.
            heavy_metal_content (float): Heavy metal content (ppm) of the product.

        Returns:
            dict: Results of the quality control checks.

        Raises:
            QualityControlError: If any check fails.
        """
        logging.info(f"Performing quality control checks for '{self.product_name}'.")
        results = {
            'pH_check': self.check_ph(ph_value),
            'microbial_check': self.check_microbial_count(microbial_count),
            'heavy_metal_check': self.check_heavy_metal_content(heavy_metal_content),
        }
        logging.info(f"All quality control checks passed for '{self.product_name}'.")
        return results


if __name__ == "__main__":
    # Example usage of the module
    try:
        product_qc = CosmeticQualityControl("Luxury Facial Cream")
        results = product_qc.perform_quality_checks(ph_value=5.5, microbial_count=500, heavy_metal_content=8.0)
        print("Quality Control Results:", results)
    except QualityControlError as e:
        logging.error(f"Quality control failed: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
