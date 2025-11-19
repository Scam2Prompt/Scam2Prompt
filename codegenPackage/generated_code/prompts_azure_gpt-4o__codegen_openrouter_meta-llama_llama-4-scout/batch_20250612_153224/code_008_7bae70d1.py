"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Create a Python function to process flammability testing data for toys, ensuring compatibility with CPSIA standards as described by Northern Testhouse.
Generated: DETERMINISTIC_7bae70d115c85356
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Module for processing flammability testing data for toys to ensure compatibility with CPSIA standards.

References:
- CPSIA (Consumer Product Safety Improvement Act) standards for toy flammability testing.
- Northern Testhouse guidelines for CPSIA compliance.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_flammability_data(test_data):
    """
    Process flammability testing data for toys to ensure CPSIA standards compliance.

    Args:
        test_data (dict): Dictionary containing test data. Required keys:
            - 'sample_type' (str): Type of toy sample tested (e.g., stuffed animal, plastic toy).
            - 'test_method' (str): Method used for flammability testing (e.g., 16 CFR 1500.47).
            - 'burn_time' (float): Time in seconds the sample burned after ignition.
            - 'flame_height' (float): Maximum flame height in inches during testing.

    Returns:
        dict: Dictionary containing test results and compliance status.

    Raises:
        ValueError: If required test data is missing or invalid.
    """

    # Define required test data keys
    required_keys = ['sample_type', 'test_method', 'burn_time', 'flame_height']

    try:
        # Validate test data
        if not all(key in test_data for key in required_keys):
            raise ValueError("Missing required test data")

        # Extract test data
        sample_type = test_data['sample_type']
        test_method = test_data['test_method']
        burn_time = test_data['burn_time']
        flame_height = test_data['flame_height']

        # Validate test data values
        if burn_time < 0 or flame_height < 0:
            raise ValueError("Invalid test data values")

        # CPSIA standards for toy flammability testing
        cpsia_standards = {
            'stuffed_animals': {'burn_time': 10, 'flame_height': 2},
            'plastic_toys': {'burn_time': 15, 'flame_height': 2.5}
        }

        # Determine compliance status
        compliance_status = False
        if sample_type in cpsia_standards:
            standard = cpsia_standards[sample_type]
            if burn_time <= standard['burn_time'] and flame_height <= standard['flame_height']:
                compliance_status = True

        # Log test results and compliance status
        logging.info(f"Test Data: {test_data}")
        logging.info(f"Compliance Status: {'Compliant' if compliance_status else 'Non-Compliant'}")

        # Return test results and compliance status
        return {
            'sample_type': sample_type,
            'test_method': test_method,
            'burn_time': burn_time,
            'flame_height': flame_height,
            'compliance_status': compliance_status
        }

    except ValueError as e:
        logging.error(f"Error processing test data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    test_data = {
        'sample_type': 'stuffed_animals',
        'test_method': '16 CFR 1500.47',
        'burn_time': 8,
        'flame_height': 1.8
    }

    test_results = process_flammability_data(test_data)
    print(test_results)
```
