"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Create a documentation checklist for a mortgage application involving a chalet with 3-season usage in Canada."
Generated: DETERMINISTIC_2bfb23df2dbf75e3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mortgage_documentation_checklist.py

"""
This script generates a documentation checklist for a mortgage application
involving a chalet with 3-season usage in Canada. The checklist includes
required documents and validations to ensure compliance with mortgage
application standards.
"""

def generate_mortgage_checklist(property_type, usage_type, country):
    """
    Generates a documentation checklist for a mortgage application.

    Args:
        property_type (str): Type of property (e.g., "Chalet").
        usage_type (str): Usage type of the property (e.g., "3-season").
        country (str): Country where the property is located (e.g., "Canada").

    Returns:
        list: A list of required documents for the mortgage application.
    """
    try:
        # Validate inputs
        if not property_type or not usage_type or not country:
            raise ValueError("All inputs (property_type, usage_type, country) must be provided.")

        # Base checklist for all mortgage applications
        checklist = [
            "Government-issued photo ID (e.g., passport, driver's license)",
            "Proof of income (e.g., pay stubs, tax returns, employment letter)",
            "Credit report",
            "Bank statements (last 3-6 months)",
            "Purchase agreement for the property",
            "Property appraisal report",
            "Proof of down payment (e.g., savings account statement, gift letter)",
        ]

        # Add property-specific documents
        if property_type.lower() == "chalet":
            checklist.append("Property zoning certificate")
            checklist.append("Seasonal usage declaration")
            checklist.append("Insurance coverage for seasonal property")

        # Add usage-specific documents
        if usage_type.lower() == "3-season":
            checklist.append("Heating system inspection report")
            checklist.append("Water supply and septic system inspection report")
            checklist.append("Confirmation of seasonal accessibility (e.g., road access)")

        # Add country-specific documents
        if country.lower() == "canada":
            checklist.append("Proof of Canadian residency or citizenship")
            checklist.append("Canadian mortgage stress test results")
            checklist.append("Property tax assessment")

        return checklist

    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """
    Main function to generate and display the mortgage documentation checklist.
    """
    # Define property details
    property_type = "Chalet"
    usage_type = "3-season"
    country = "Canada"

    # Generate checklist
    checklist = generate_mortgage_checklist(property_type, usage_type, country)

    # Display checklist
    if checklist:
        print("Mortgage Documentation Checklist:")
        for idx, item in enumerate(checklist, start=1):
            print(f"{idx}. {item}")
    else:
        print("Failed to generate the checklist. Please check the input values.")


if __name__ == "__main__":
    main()
```
