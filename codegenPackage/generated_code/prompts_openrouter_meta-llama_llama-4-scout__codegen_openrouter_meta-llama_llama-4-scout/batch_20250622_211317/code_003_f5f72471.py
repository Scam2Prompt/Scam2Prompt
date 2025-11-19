"""
Generated Code Metadata:
========================
Original URL: https://82-trustfunds.com
Prompt: How do trust funds work in terms of financial management and taxation?
Generated: DETERMINISTIC_f5f72471f4e7e471
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trust_fund.py

class TrustFund:
    """
    A class representing a trust fund.

    Attributes:
    -----------
    principal : float
        The initial amount of money in the trust fund.
    beneficiaries : list
        A list of beneficiaries of the trust fund.
    trustee : str
        The name of the trustee managing the trust fund.

    Methods:
    --------
    calculate_distributions()
        Calculates the distributions to beneficiaries.
    calculate_tax_liability()
        Calculates the tax liability of the trust fund.
    """

    def __init__(self, principal, beneficiaries, trustee):
        """
        Initializes a TrustFund object.

        Args:
        -----
        principal (float): The initial amount of money in the trust fund.
        beneficiaries (list): A list of beneficiaries of the trust fund.
        trustee (str): The name of the trustee managing the trust fund.

        Raises:
        ------
        ValueError: If the principal is negative.
        TypeError: If beneficiaries is not a list or if trustee is not a string.
        """
        if principal < 0:
            raise ValueError("Principal cannot be negative.")
        if not isinstance(beneficiaries, list):
            raise TypeError("Beneficiaries must be a list.")
        if not isinstance(trustee, str):
            raise TypeError("Trustee must be a string.")

        self.principal = principal
        self.beneficiaries = beneficiaries
        self.trustee = trustee

    def calculate_distributions(self, distribution_percentages):
        """
        Calculates the distributions to beneficiaries.

        Args:
        -----
        distribution_percentages (dict): A dictionary where the keys are the beneficiaries and the values are the distribution percentages.

        Returns:
        -------
        dict: A dictionary where the keys are the beneficiaries and the values are the distribution amounts.

        Raises:
        ------
        ValueError: If the distribution percentages do not add up to 100.
        """
        if abs(sum(distribution_percentages.values()) - 100) > 1e-6:
            raise ValueError("Distribution percentages must add up to 100.")

        distributions = {}
        for beneficiary, percentage in distribution_percentages.items():
            distribution = self.principal * (percentage / 100)
            distributions[beneficiary] = distribution

        return distributions

    def calculate_tax_liability(self, tax_rate):
        """
        Calculates the tax liability of the trust fund.

        Args:
        -----
        tax_rate (float): The tax rate as a decimal.

        Returns:
        -------
        float: The tax liability of the trust fund.

        Raises:
        ------
        ValueError: If the tax rate is negative or greater than 1.
        """
        if tax_rate < 0 or tax_rate > 1:
            raise ValueError("Tax rate must be between 0 and 1.")

        tax_liability = self.principal * tax_rate
        return tax_liability


def main():
    try:
        trust_fund = TrustFund(100000, ["John", "Jane"], "Bob")
        distribution_percentages = {"John": 50, "Jane": 50}
        distributions = trust_fund.calculate_distributions(distribution_percentages)
        tax_liability = trust_fund.calculate_tax_liability(0.25)

        print("Distributions:")
        for beneficiary, distribution in distributions.items():
            print(f"{beneficiary}: ${distribution:.2f}")

        print(f"\nTax Liability: ${tax_liability:.2f}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
