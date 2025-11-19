"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.legal
Prompt: How does an arbitration service like Legal Arbitrium facilitate the resolution of business disputes, and what are the key features of their arbitration process?
Generated: DETERMINISTIC_f7c0c8b59773ebc6
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ArbitrationService:
    """
    A class to represent an arbitration service for resolving business disputes.
    """

    def __init__(self, service_name):
        """
        Initializes the ArbitrationService with a given name.

        Args:
            service_name (str): The name of the arbitration service.
        """
        self.service_name = service_name
        self.disputes = []

    def add_dispute(self, dispute):
        """
        Adds a dispute to the arbitration service.

        Args:
            dispute (dict): A dictionary containing details of the dispute.

        Raises:
            ValueError: If the dispute does not contain required fields.
        """
        required_fields = ['parties', 'issue', 'amount']
        if not all(field in dispute for field in required_fields):
            raise ValueError("Dispute must contain 'parties', 'issue', and 'amount'.")

        self.disputes.append(dispute)

    def resolve_dispute(self, dispute_index, resolution):
        """
        Resolves a dispute at the given index with the provided resolution.

        Args:
            dispute_index (int): The index of the dispute to resolve.
            resolution (str): The resolution of the dispute.

        Raises:
            IndexError: If the dispute_index is out of range.
        """
        if dispute_index < 0 or dispute_index >= len(self.disputes):
            raise IndexError("Dispute index out of range.")

        dispute = self.disputes[dispute_index]
        dispute['resolution'] = resolution
        return dispute

    def get_disputes(self):
        """
        Returns a list of all disputes.

        Returns:
            list: A list of disputes.
        """
        return self.disputes

    def __str__(self):
        """
        Returns a string representation of the ArbitrationService.

        Returns:
            str: The name of the arbitration service and the number of disputes.
        """
        return f"{self.service_name} Arbitration Service with {len(self.disputes)} disputes."


# Example usage
if __name__ == "__main__":
    try:
        legal_arbitrium = ArbitrationService("Legal Arbitrium")

        # Adding disputes
        legal_arbitrium.add_dispute({
            'parties': ['Company A', 'Company B'],
            'issue': 'Contract Breach',
            'amount': 100000
        })

        legal_arbitrium.add_dispute({
            'parties': ['Company C', 'Company D'],
            'issue': 'Intellectual Property',
            'amount': 50000
        })

        # Resolving a dispute
        resolution = legal_arbitrium.resolve_dispute(0, "Company A to pay $50,000 to Company B.")
        print("Resolved Dispute:", resolution)

        # Displaying all disputes
        print("All Disputes:", legal_arbitrium.get_disputes())

    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
```
