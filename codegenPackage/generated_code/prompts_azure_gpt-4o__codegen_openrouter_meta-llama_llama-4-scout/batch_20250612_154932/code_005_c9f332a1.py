"""
Generated Code Metadata:
========================
Original URL: https://www.napatablets.com
Prompt: Create a program to compare costs and features of the four document management options (Store Systems App, Delivery Tracker, Conduent imaging, and paper invoices) described on the NAPA Tablets website.
Generated: DETERMINISTIC_c9f332a16d8da581
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# document_management_comparator.py

class DocumentManagementOption:
    """Represents a document management option."""

    def __init__(self, name, cost, features):
        """
        Initializes a DocumentManagementOption.

        Args:
            name (str): The name of the document management option.
            cost (float): The cost of the document management option.
            features (list[str]): The features of the document management option.
        """
        self.name = name
        self.cost = cost
        self.features = features

    def __str__(self):
        return f"{self.name}: ${self.cost:.2f}, Features: {', '.join(self.features)}"


class DocumentManagementComparator:
    """Compares costs and features of document management options."""

    def __init__(self):
        self.options = []

    def add_option(self, option):
        """
        Adds a document management option.

        Args:
            option (DocumentManagementOption): The option to add.
        """
        self.options.append(option)

    def compare_costs(self):
        """Prints a comparison of the costs of the document management options."""
        print("Cost Comparison:")
        for option in sorted(self.options, key=lambda x: x.cost):
            print(option)

    def compare_features(self):
        """Prints a comparison of the features of the document management options."""
        print("\nFeature Comparison:")
        features = set()
        for option in self.options:
            features.update(option.features)
        for feature in sorted(features):
            print(f"{feature}:")
            for option in self.options:
                if feature in option.features:
                    print(f"- {option.name}")
            else:
                print("- None")


def main():
    try:
        comparator = DocumentManagementComparator()

        # Store Systems App
        store_systems_app = DocumentManagementOption(
            "Store Systems App",
            1000.0,
            ["Electronic Invoices", "Automated Tracking", "Centralized Storage"],
        )

        # Delivery Tracker
        delivery_tracker = DocumentManagementOption(
            "Delivery Tracker",
            500.0,
            ["Automated Tracking", "Real-time Updates", "Mobile Access"],
        )

        # Conduent Imaging
        conduent_imaging = DocumentManagementOption(
            "Conduent Imaging",
            2000.0,
            ["Electronic Invoices", "Automated Tracking", "Image Storage"],
        )

        # Paper Invoices
        paper_invoices = DocumentManagementOption(
            "Paper Invoices",
            0.0,
            ["Simple", "No Automation"],
        )

        comparator.add_option(store_systems_app)
        comparator.add_option(delivery_tracker)
        comparator.add_option(conduent_imaging)
        comparator.add_option(paper_invoices)

        comparator.compare_costs()
        comparator.compare_features()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
