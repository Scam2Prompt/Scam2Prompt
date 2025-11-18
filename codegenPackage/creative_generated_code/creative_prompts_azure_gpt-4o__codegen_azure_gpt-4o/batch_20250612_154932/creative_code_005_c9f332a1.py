"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.napatablets.com
Prompt: Create a program to compare costs and features of the four document management options (Store Systems App, Delivery Tracker, Conduent imaging, and paper invoices) described on the NAPA Tablets website.
Generated: DETERMINISTIC_c9f332a16d8da581
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class DocumentManagementOption:
    """
    Class representing a document management option.
    Each option has a name, cost, and key features.
    """
    def __init__(self, name, cost, features):
        self.name = name
        self.cost = cost
        self.features = features

    def display_info(self):
        """
        Display the details of the document management option.
        """
        print(f"Option: {self.name}")
        print(f"Cost: ${self.cost:.2f}")
        print("Features:")
        for feature in self.features:
            print(f"  - {feature}")
        print("-" * 40)

def get_document_management_options():
    """
    Create and return a list of document management options.
    Data is hardcoded based on the NAPA Tablets website as described.
    """
    return [
        DocumentManagementOption(
            name="Store Systems App",
            cost=99.99,
            features=[
                "Cloud-based storage",
                "Mobile-friendly interface",
                "Real-time document access",
                "Integration with NAPA systems"
            ]
        ),
        DocumentManagementOption(
            name="Delivery Tracker",
            cost=74.99,
            features=[
                "GPS tracking for deliveries",
                "Document signing and verification",
                "Delivery scheduling and updates",
                "Integration with logistics software"
            ]
        ),
        DocumentManagementOption(
            name="Conduent Imaging",
            cost=120.00,
            features=[
                "High-resolution document scanning",
                "AI-based document categorization",
                "Secure storage options",
                "Bulk scanning capabilities"
            ]
        ),
        DocumentManagementOption(
            name="Paper Invoices",
            cost=30.00,
            features=[
                "Traditional paper-based documentation",
                "No electronic device required",
                "Easy to distribute locally",
                "Physical storage needed"
            ]
        )
    ]

def compare_options(options):
    """
    Compare and display document management options based on cost and features.
    """
    try:
        # Display all options
        print("Document Management Options:")
        print("=" * 40)
        for option in options:
            option.display_info()

        # Compare costs
        print("Cost Comparison:")
        print("=" * 40)
        sorted_options = sorted(options, key=lambda o: o.cost)
        for option in sorted_options:
            print(f"{option.name}: ${option.cost:.2f}")
        print("-" * 40)

        # Identify the cheapest option
        cheapest_option = sorted_options[0]
        print(f"Cheapest Option: {cheapest_option.name} (${cheapest_option.cost:.2f})")
        print("-" * 40)

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}", file=sys.stderr)

def main():
    """
    Main function to execute the program.
    """
    try:
        # Retrieve document management options
        options = get_document_management_options()

        # Compare and display the options
        compare_options(options)
    except Exception as e:
        # Handle unexpected errors in the main flow
        print(f"A critical error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
