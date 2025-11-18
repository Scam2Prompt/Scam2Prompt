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
class DocumentManagementOption:
    """
    Class to represent a document management option.
    """

    def __init__(self, name, cost, features):
        """
        Initialize a DocumentManagementOption instance.

        :param name: Name of the document management option.
        :param cost: Annual cost of the option.
        :param features: List of features provided by the option.
        """
        self.name = name
        self.cost = cost
        self.features = features

    def __str__(self):
        """
        String representation of the document management option.

        :return: A formatted string with the option details.
        """
        return f"{self.name} - Cost: ${self.cost:.2f}, Features: {', '.join(self.features)}"


def compare_options(options):
    """
    Compare document management options based on cost and features.

    :param options: List of DocumentManagementOption instances.
    :return: None
    """
    if not options:
        print("No options to compare.")
        return

    # Sorting options by cost
    options.sort(key=lambda x: x.cost)

    print("Comparing Document Management Options:\n")
    for option in options:
        print(option)


def main():
    """
    Main function to execute the document management comparison program.
    """
    try:
        # Defining document management options with their respective costs and features
        options = [
            DocumentManagementOption("Store Systems App", 1200, ["Secure storage", "Easy access", "Collaboration tools"]),
            DocumentManagementOption("Delivery Tracker", 800, ["Real-time tracking", "Notifications", "Reporting"]),
            DocumentManagementOption("Conduent Imaging", 1500, ["Image capture", "Data extraction", "Storage"]),
            DocumentManagementOption("Paper Invoices", 500, ["Tangible records", "Simple to use", "No technology needed"]),
        ]

        # Compare the options
        compare_options(options)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
