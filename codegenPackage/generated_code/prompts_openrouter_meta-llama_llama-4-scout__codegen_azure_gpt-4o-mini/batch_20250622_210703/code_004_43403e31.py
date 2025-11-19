"""
Generated Code Metadata:
========================
Original URL: https://myhealthcarebilling.com
Prompt: "Create a function to calculate the clean claim ratio and net collection rate for a medical billing company."
Generated: DETERMINISTIC_43403e317627f418
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MedicalBillingMetrics:
    """
    A class to calculate key metrics for a medical billing company.
    """

    def __init__(self, total_clean_claims: float, total_claims: float, total_collections: float, total_billed: float):
        """
        Initializes the MedicalBillingMetrics with the required parameters.

        :param total_clean_claims: Total number of clean claims submitted.
        :param total_claims: Total number of claims submitted.
        :param total_collections: Total amount collected from claims.
        :param total_billed: Total amount billed to patients and insurers.
        """
        self.total_clean_claims = total_clean_claims
        self.total_claims = total_claims
        self.total_collections = total_collections
        self.total_billed = total_billed

    def calculate_clean_claim_ratio(self) -> float:
        """
        Calculates the clean claim ratio.

        :return: Clean claim ratio as a float.
        :raises ValueError: If total_claims is zero to avoid division by zero.
        """
        if self.total_claims == 0:
            raise ValueError("Total claims cannot be zero for clean claim ratio calculation.")
        
        clean_claim_ratio = self.total_clean_claims / self.total_claims
        return clean_claim_ratio

    def calculate_net_collection_rate(self) -> float:
        """
        Calculates the net collection rate.

        :return: Net collection rate as a float.
        :raises ValueError: If total_billed is zero to avoid division by zero.
        """
        if self.total_billed == 0:
            raise ValueError("Total billed amount cannot be zero for net collection rate calculation.")
        
        net_collection_rate = self.total_collections / self.total_billed
        return net_collection_rate

# Example usage:
if __name__ == "__main__":
    try:
        metrics = MedicalBillingMetrics(total_clean_claims=800, total_claims=1000, total_collections=60000, total_billed=75000)
        clean_claim_ratio = metrics.calculate_clean_claim_ratio()
        net_collection_rate = metrics.calculate_net_collection_rate()

        print(f"Clean Claim Ratio: {clean_claim_ratio:.2%}")
        print(f"Net Collection Rate: {net_collection_rate:.2%}")
    except ValueError as e:
        print(f"Error: {e}")
```
