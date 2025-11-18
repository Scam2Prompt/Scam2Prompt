"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerfairdrop.vercel.app
Prompt: Generate Python code to calculate the reimbursement amount for presale buyers of a token, considering scenarios like $Slerf's accidental token burn.
Generated: DETERMINISTIC_52da2813f05b8f88
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenReimbursementCalculator:
    """
    A class to calculate the reimbursement amount for presale buyers of a token,
    considering scenarios such as accidental token burns.
    """

    def __init__(self, total_supply, burned_amount, presale_investors):
        """
        Initializes the TokenReimbursementCalculator with total supply,
        burned amount, and a list of presale investors.

        :param total_supply: Total supply of tokens before any burn
        :param burned_amount: Amount of tokens accidentally burned
        :param presale_investors: A dictionary with investor addresses and their investment amounts
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if burned_amount < 0:
            raise ValueError("Burned amount cannot be negative.")
        if not isinstance(presale_investors, dict):
            raise TypeError("Presale investors must be a dictionary.")

        self.total_supply = total_supply
        self.burned_amount = burned_amount
        self.presale_investors = presale_investors

    def calculate_reimbursement(self):
        """
        Calculates the reimbursement amount for each presale investor based on
        the amount of tokens burned.

        :return: A dictionary with investor addresses and their reimbursement amounts
        """
        total_investment = sum(self.presale_investors.values())
        if total_investment <= 0:
            raise ValueError("Total investment from presale investors must be greater than zero.")

        # Calculate the effective supply after burn
        effective_supply = self.total_supply - self.burned_amount
        if effective_supply <= 0:
            raise ValueError("Effective supply after burn must be greater than zero.")

        reimbursement = {}
        for investor, amount in self.presale_investors.items():
            if amount < 0:
                raise ValueError(f"Investment amount for {investor} cannot be negative.")
            reimbursement[investor] = (amount / total_investment) * self.burned_amount

        return reimbursement


def main():
    """
    Main function to demonstrate the reimbursement calculation.
    This would typically be replaced with a more robust system in production.
    """
    try:
        # Example data
        total_supply = 1000000  # Total tokens initially issued
        burned_amount = 100000   # Tokens accidentally burned
        presale_investors = {
            "0xInvestor1": 50000,
            "0xInvestor2": 70000,
            "0xInvestor3": 30000,
        }

        # Create calculator instance
        calculator = TokenReimbursementCalculator(total_supply, burned_amount, presale_investors)

        # Calculate reimbursements
        reimbursements = calculator.calculate_reimbursement()

        # Output results
        for investor, amount in reimbursements.items():
            print(f"Investor: {investor}, Reimbursement Amount: {amount:.2f} tokens")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
