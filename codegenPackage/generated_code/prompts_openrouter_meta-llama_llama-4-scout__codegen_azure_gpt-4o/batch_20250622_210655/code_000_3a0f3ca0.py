"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Write a Python script to determine the compliance of a ceramic ware product with US FDA Proposition 65 regulations, considering the testing services offered by Northern Testhouse.
Generated: DETERMINISTIC_3a0f3ca002ff0c8e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to determine compliance of a ceramic ware product with US FDA Proposition 65 regulations.
This script simulates the process of checking compliance based on testing services offered by Northern Testhouse.
"""

import json

# Constants for compliance thresholds (example values, adjust as per actual regulations)
PROP65_THRESHOLD_LEAD = 0.1  # mg/L
PROP65_THRESHOLD_CADMIUM = 0.2  # mg/L

# Sample testing data (replace with actual data from Northern Testhouse)
TESTING_DATA = [
    {"product_id": 1, "product_name": "Ceramic Plate", "lead": 0.05, "cadmium": 0.1},
    {"product_id": 2, "product_name": "Ceramic Bowl", "lead": 0.15, "cadmium": 0.25},
    {"product_id": 3, "product_name": "Ceramic Mug", "lead": 0.08, "cadmium": 0.18},
]

def check_compliance(test_data):
    """
    Check compliance of a ceramic ware product with Proposition 65 regulations.

    Args:
        test_data (dict): A dictionary containing product testing data.

    Returns:
        dict: A dictionary with compliance status and details.
    """
    try:
        # Extract relevant data
        product_id = test_data.get("product_id")
        product_name = test_data.get("product_name")
        lead_content = test_data.get("lead")
        cadmium_content = test_data.get("cadmium")

        # Validate data
        if product_id is None or product_name is None or lead_content is None or cadmium_content is None:
            raise ValueError("Missing required testing data for product.")

        # Determine compliance
        lead_compliant = lead_content <= PROP65_THRESHOLD_LEAD
        cadmium_compliant = cadmium_content <= PROP65_THRESHOLD_CADMIUM
        overall_compliance = lead_compliant and cadmium_compliant

        # Prepare result
        compliance_status = {
            "product_id": product_id,
            "product_name": product_name,
            "lead_compliant": lead_compliant,
            "cadmium_compliant": cadmium_compliant,
            "overall_compliance": overall_compliance,
        }
        return compliance_status

    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}

def main():
    """
    Main function to process testing data and determine compliance for each product.
    """
    compliance_results = []

    for test_data in TESTING_DATA:
        result = check_compliance(test_data)
        compliance_results.append(result)

    # Output results
    print("Compliance Results:")
    print(json.dumps(compliance_results, indent=4))

if __name__ == "__main__":
    main()
```
