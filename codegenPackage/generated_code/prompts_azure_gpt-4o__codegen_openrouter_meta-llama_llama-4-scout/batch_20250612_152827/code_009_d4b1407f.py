"""
Generated Code Metadata:
========================
Original URL: https://origineth.us
Prompt: Develop a tool to calculate the benefits of Crédit Agricole's "Livret Engagé Sociétaire" savings account based on its unique features.
Generated: DETERMINISTIC_d4b1407f21715a35
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# livret_engagé_sociétaire_calculator.py

class LivretEngageSociataire:
    """
    Calculates the benefits of Crédit Agricole's "Livret Engagé Sociétaire" savings account.
    """

    def __init__(self, initial_deposit, monthly_deposit, interest_rate, 
                 state_tax_rate, solidarity_wealth_tax_rate, years):
        """
        Initializes the LivretEngageSociataire calculator.

        Args:
            initial_deposit (float): Initial deposit amount.
            monthly_deposit (float): Monthly deposit amount.
            interest_rate (float): Annual interest rate (in decimal form, e.g., 2% = 0.02).
            state_tax_rate (float): State tax rate (in decimal form, e.g., 10% = 0.10).
            solidarity_wealth_tax_rate (float): Solidarity wealth tax rate (in decimal form).
            years (int): Number of years to calculate benefits for.
        """
        self.initial_deposit = initial_deposit
        self.monthly_deposit = monthly_deposit
        self.interest_rate = interest_rate
        self.state_tax_rate = state_tax_rate
        self.solidarity_wealth_tax_rate = solidarity_wealth_tax_rate
        self.years = years

    def calculate_benefits(self):
        """
        Calculates the benefits of the Livret Engagé Sociétaire savings account.

        Returns:
            dict: A dictionary containing the total amount, interest earned, 
                  state tax, solidarity wealth tax, and net benefits.
        """
        try:
            # Calculate total amount
            total_amount = self.initial_deposit
            interest_earned = 0
            for _ in range(self.years * 12):
                total_amount += self.monthly_deposit
                interest_earned += total_amount * (self.interest_rate / 12)
                total_amount += interest_earned / 12

            # Calculate taxes
            state_tax = interest_earned * self.state_tax_rate
            solidarity_wealth_tax = interest_earned * self.solidarity_wealth_tax_rate

            # Calculate net benefits
            net_benefits = interest_earned - state_tax - solidarity_wealth_tax

            return {
                "total_amount": round(total_amount, 2),
                "interest_earned": round(interest_earned, 2),
                "state_tax": round(state_tax, 2),
                "solidarity_wealth_tax": round(solidarity_wealth_tax, 2),
                "net_benefits": round(net_benefits, 2)
            }

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    # Example usage
    calculator = LivretEngageSociataire(
        initial_deposit=1000,
        monthly_deposit=500,
        interest_rate=0.02,
        state_tax_rate=0.10,
        solidarity_wealth_tax_rate=0.05,
        years=5
    )

    benefits = calculator.calculate_benefits()
    if benefits:
        print("Benefits of Livret Engagé Sociétaire:")
        for key, value in benefits.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")


if __name__ == "__main__":
    main()
```
