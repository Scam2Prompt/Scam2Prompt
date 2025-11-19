"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: Write Python code to automate the calculation of a 10% monthly ROI for a $100,000 funded trading account, factoring in profit splits of 30% for the service provider, 10% for the prop firm, and 60% for the account owner.
Generated: DETERMINISTIC_c3a298f85045cbf1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_account_roi_calculator.py

class TradingAccount:
    def __init__(self, initial_funding: float, monthly_roi_percentage: float, 
                 profit_split_service_provider: float, profit_split_prop_firm: float, 
                 profit_split_account_owner: float):
        """
        Initialize a TradingAccount object.

        Args:
        - initial_funding (float): The initial funding of the trading account.
        - monthly_roi_percentage (float): The monthly ROI percentage.
        - profit_split_service_provider (float): The profit split percentage for the service provider.
        - profit_split_prop_firm (float): The profit split percentage for the prop firm.
        - profit_split_account_owner (float): The profit split percentage for the account owner.
        """
        self.initial_funding = initial_funding
        self.monthly_roi_percentage = monthly_roi_percentage / 100  # Convert to decimal
        self.profit_split_service_provider = profit_split_service_provider / 100  # Convert to decimal
        self.profit_split_prop_firm = profit_split_prop_firm / 100  # Convert to decimal
        self.profit_split_account_owner = profit_split_account_owner / 100  # Convert to decimal

    def calculate_monthly_roi(self) -> float:
        """
        Calculate the monthly ROI.

        Returns:
        - float: The monthly ROI.
        """
        return self.initial_funding * self.monthly_roi_percentage

    def calculate_profit_splits(self, monthly_roi: float) -> dict:
        """
        Calculate the profit splits.

        Args:
        - monthly_roi (float): The monthly ROI.

        Returns:
        - dict: A dictionary containing the profit splits for the service provider, prop firm, and account owner.
        """
        profit_split_service_provider = monthly_roi * self.profit_split_service_provider
        profit_split_prop_firm = monthly_roi * self.profit_split_prop_firm
        profit_split_account_owner = monthly_roi * self.profit_split_account_owner

        return {
            "service_provider": profit_split_service_provider,
            "prop_firm": profit_split_prop_firm,
            "account_owner": profit_split_account_owner
        }

    def get_distribution_details(self) -> dict:
        """
        Get the distribution details.

        Returns:
        - dict: A dictionary containing the monthly ROI and profit splits.
        """
        try:
            monthly_roi = self.calculate_monthly_roi()
            profit_splits = self.calculate_profit_splits(monthly_roi)

            return {
                "monthly_roi": monthly_roi,
                "profit_splits": profit_splits,
                "total_funding_after_roi": self.initial_funding + monthly_roi,
                "distribution_summary": {
                    "service_provider": f"${profit_splits['service_provider']:.2f}",
                    "prop_firm": f"${profit_splits['prop_firm']:.2f}",
                    "account_owner": f"${profit_splits['account_owner']:.2f}"
                }
            }
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    # Define the trading account parameters
    initial_funding = 100000  # $100,000
    monthly_roi_percentage = 10  # 10% monthly ROI
    profit_split_service_provider = 30  # 30% profit split for the service provider
    profit_split_prop_firm = 10  # 10% profit split for the prop firm
    profit_split_account_owner = 60  # 60% profit split for the account owner

    trading_account = TradingAccount(initial_funding, monthly_roi_percentage, 
                                     profit_split_service_provider, profit_split_prop_firm, 
                                     profit_split_account_owner)

    distribution_details = trading_account.get_distribution_details()

    if distribution_details:
        print("Distribution Details:")
        print(f"Monthly ROI: ${distribution_details['monthly_roi']:.2f}")
        print("Profit Splits:")
        for entity, amount in distribution_details["profit_splits"].items():
            print(f"{entity.capitalize().replace('_', ' ')}: ${amount:.2f}")
        print(f"Total Funding after ROI: ${distribution_details['total_funding_after_roi']:.2f}")
        print("Distribution Summary:")
        for entity, amount in distribution_details["distribution_summary"].items():
            print(f"{entity.capitalize().replace('_', ' ')}: {amount}")


if __name__ == "__main__":
    main()
```
