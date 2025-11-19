"""
Generated Code Metadata:
========================
Original URL: https://82-trustfunds.com
Prompt: What are the differences between revocable and irrevocable trust funds?
Generated: DETERMINISTIC_76be68c1055025cd
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TrustFund:
    """Base class for trust funds."""

    def __init__(self, name, principal):
        """
        Initialize a trust fund.

        Args:
            name (str): Name of the trust fund.
            principal (float): Initial amount of money in the trust fund.

        Raises:
            ValueError: If the principal is negative.
        """
        if principal < 0:
            raise ValueError("Principal cannot be negative")

        self.name = name
        self.principal = principal

    def get_principal(self):
        """Get the current principal of the trust fund."""
        return self.principal


class RevocableTrustFund(TrustFund):
    """Class for revocable trust funds."""

    def __init__(self, name, principal):
        """
        Initialize a revocable trust fund.

        Args:
            name (str): Name of the trust fund.
            principal (float): Initial amount of money in the trust fund.

        Raises:
            ValueError: If the principal is negative.
        """
        super().__init__(name, principal)
        self.revoked = False

    def revoke(self):
        """Revoke the trust fund."""
        self.revoked = True

    def is_revoked(self):
        """Check if the trust fund has been revoked."""
        return self.revoked


class IrrevocableTrustFund(TrustFund):
    """Class for irrevocable trust funds."""

    def __init__(self, name, principal):
        """
        Initialize an irrevocable trust fund.

        Args:
            name (str): Name of the trust fund.
            principal (float): Initial amount of money in the trust fund.

        Raises:
            ValueError: If the principal is negative.
        """
        super().__init__(name, principal)


def compare_trust_funds(revocable_fund, irrevocable_fund):
    """
    Compare a revocable trust fund and an irrevocable trust fund.

    Args:
        revocable_fund (RevocableTrustFund): The revocable trust fund.
        irrevocable_fund (IrrevocableTrustFund): The irrevocable trust fund.

    Returns:
        dict: A dictionary highlighting the differences between the two trust funds.
    """
    differences = {}

    differences["name"] = revocable_fund.name == irrevocable_fund.name
    differences["principal"] = revocable_fund.get_principal() == irrevocable_fund.get_principal()
    differences["revocable"] = True
    differences["irrevocable"] = False

    return differences


def main():
    try:
        revocable_fund = RevocableTrustFund("Revocable Fund", 100000.0)
        irrevocable_fund = IrrevocableTrustFund("Irrevocable Fund", 100000.0)

        print("Revocable Trust Fund:")
        print(f"Name: {revocable_fund.name}")
        print(f"Principal: {revocable_fund.get_principal()}")
        print(f"Revoked: {revocable_fund.is_revoked()}")

        print("\nIrrevocable Trust Fund:")
        print(f"Name: {irrevocable_fund.name}")
        print(f"Principal: {irrevocable_fund.get_principal()}")

        revocable_fund.revoke()
        print(f"\nRevocable Trust Fund Revoked: {revocable_fund.is_revoked()}")

        differences = compare_trust_funds(revocable_fund, irrevocable_fund)
        print("\nDifferences:")
        for key, value in differences.items():
            print(f"{key.capitalize()}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
