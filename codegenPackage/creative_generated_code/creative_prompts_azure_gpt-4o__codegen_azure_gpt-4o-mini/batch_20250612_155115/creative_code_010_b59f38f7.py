"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fund-x.link
Prompt: Write code to calculate the risk associated with leveraged trading based on the risk warning provided on FUND-X LTD's website. Include safeguards for high-risk scenarios.
Generated: DETERMINISTIC_b59f38f7e799de0c
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LeveragedTradingRiskCalculator:
    """
    A class to calculate the risk associated with leveraged trading.
    It includes methods to assess risk based on user input and
    provides safeguards for high-risk scenarios.
    """

    def __init__(self, leverage_ratio: float, account_balance: float):
        """
        Initializes the risk calculator with leverage ratio and account balance.

        :param leverage_ratio: The leverage ratio (e.g., 2 for 2x leverage).
        :param account_balance: The total account balance in currency units.
        """
        if leverage_ratio <= 1:
            raise ValueError("Leverage ratio must be greater than 1.")
        if account_balance <= 0:
            raise ValueError("Account balance must be a positive amount.")

        self.leverage_ratio = leverage_ratio
        self.account_balance = account_balance

    def calculate_max_trade_size(self) -> float:
        """
        Calculates the maximum trade size based on the leverage ratio.

        :return: Maximum trade size in currency units.
        """
        return self.account_balance * self.leverage_ratio

    def assess_risk(self, trade_size: float) -> str:
        """
        Assesses the risk level based on the chosen trade size.

        :param trade_size: The proposed trade size in currency units.
        :return: A risk assessment message.
        """
        if trade_size <= 0:
            raise ValueError("Trade size must be a positive amount.")

        max_trade_size = self.calculate_max_trade_size()
        risk_warning = self.get_risk_warning(trade_size, max_trade_size)

        return risk_warning

    def get_risk_warning(self, trade_size: float, max_trade_size: float) -> str:
        """
        Generates a risk warning based on the trade size compared to max trade size.

        :param trade_size: The proposed trade size.
        :param max_trade_size: The maximum allowable trade size.
        :return: Risk warning message.
        """
        if trade_size > max_trade_size:
            return "Warning: Trade size exceeds maximum allowable limits! Consider reducing your trade size."

        risk_percentage = (trade_size / self.account_balance) * 100

        if risk_percentage >= 50:
            return "High Risk: You're risking more than 50% of your account balance. Proceed with caution."
        elif risk_percentage >= 25:
            return "Moderate Risk: You're risking 25% to 50% of your account balance. Be aware of potential losses."
        else:
            return "Low Risk: You're risking less than 25% of your account balance. Trade cautiously."

# Example usage
def main():
    try:
        leverage = float(input("Enter leverage ratio (e.g., 2 for 2x): "))
        balance = float(input("Enter your account balance: "))
        
        calculator = LeveragedTradingRiskCalculator(leverage, balance)
        
        trade_size = float(input("Enter proposed trade size: "))
        risk_assessment = calculator.assess_risk(trade_size)
        
        print(risk_assessment)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
