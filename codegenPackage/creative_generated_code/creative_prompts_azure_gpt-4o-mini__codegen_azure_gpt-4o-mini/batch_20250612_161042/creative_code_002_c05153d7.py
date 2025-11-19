"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wikicat-coin.web.app
Prompt: What are the tokenomics of Wiki Cat, and how does the 2% transaction tax contribute to its ecosystem?
Generated: DETERMINISTIC_c05153d7358c6693
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    """
    A class to represent the tokenomics of the Wiki Cat cryptocurrency.

    Attributes
    ----------
    total_supply : float
        Total supply of the token
    transaction_tax_rate : float
        Transaction tax rate applied to every transaction
    tax_collected : float
        Total tax collected from transactions
    ecosystem_fund : float
        Total fund contributed to the ecosystem from the transaction tax

    Methods
    -------
    transaction(amount: float):
        Simulates a transaction and calculates the tax and ecosystem fund contribution.
    get_tax_collected() -> float:
        Returns the total tax collected.
    get_ecosystem_fund() -> float:
        Returns the total fund contributed to the ecosystem.
    """

    def __init__(self, total_supply: float, transaction_tax_rate: float):
        """
        Initializes the Tokenomics with total supply and transaction tax rate.

        Parameters
        ----------
        total_supply : float
            Total supply of the token
        transaction_tax_rate : float
            Transaction tax rate applied to every transaction
        """
        self.total_supply = total_supply
        self.transaction_tax_rate = transaction_tax_rate / 100  # Convert percentage to decimal
        self.tax_collected = 0.0
        self.ecosystem_fund = 0.0

    def transaction(self, amount: float) -> None:
        """
        Simulates a transaction and calculates the tax and ecosystem fund contribution.

        Parameters
        ----------
        amount : float
            The amount involved in the transaction

        Raises
        ------
        ValueError
            If the transaction amount is negative or exceeds total supply
        """
        if amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        if amount > self.total_supply:
            raise ValueError("Transaction amount exceeds total supply.")

        # Calculate tax
        tax = amount * self.transaction_tax_rate
        self.tax_collected += tax
        self.ecosystem_fund += tax * 0.5  # 50% of tax goes to the ecosystem fund
        print(f"Transaction of {amount} processed. Tax collected: {tax}")

    def get_tax_collected(self) -> float:
        """
        Returns the total tax collected.

        Returns
        -------
        float
            The total tax collected from transactions
        """
        return self.tax_collected

    def get_ecosystem_fund(self) -> float:
        """
        Returns the total fund contributed to the ecosystem.

        Returns
        -------
        float
            The total fund contributed to the ecosystem from the transaction tax
        """
        return self.ecosystem_fund


# Example usage
def main():
    try:
        # Create an instance of Tokenomics
        wiki_cat_tokenomics = Tokenomics(total_supply=1_000_000, transaction_tax_rate=2)

        # Simulate some transactions
        wiki_cat_tokenomics.transaction(1000)
        wiki_cat_tokenomics.transaction(500)
        
        # Output total tax collected and ecosystem fund
        print(f"Total tax collected: {wiki_cat_tokenomics.get_tax_collected()}")
        print(f"Total ecosystem fund: {wiki_cat_tokenomics.get_ecosystem_fund()}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
