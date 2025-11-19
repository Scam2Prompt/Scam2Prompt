"""
Generated Code Metadata:
========================
Original URL: https://singularitydao-ailaunchpad.pages.dev
Prompt: Develop a tokenomics analysis tool for a cryptocurrency project like WSDM, including calculations for initial market cap, total supply, and vesting schedules.
Generated: DETERMINISTIC_9e222f38a16f294f
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_analysis_tool.py

import datetime

class Tokenomics:
    def __init__(self, total_supply, initial_circulating_supply, vesting_schedules):
        """
        Initialize the Tokenomics analysis tool.

        Args:
        - total_supply (float): The total supply of tokens.
        - initial_circulating_supply (float): The initial circulating supply of tokens.
        - vesting_schedules (list): A list of vesting schedules.
            Each schedule is a dictionary with the following keys:
            - 'amount': The amount of tokens to vest.
            - 'vesting_start': The start date of the vesting period.
            - 'vesting_end': The end date of the vesting period.
            - 'cliff': The cliff period in days.
        """
        self.total_supply = total_supply
        self.initial_circulating_supply = initial_circulating_supply
        self.vesting_schedules = vesting_schedules

    def calculate_initial_market_cap(self, token_price):
        """
        Calculate the initial market capitalization.

        Args:
        - token_price (float): The initial token price.

        Returns:
        - float: The initial market capitalization.
        """
        return self.initial_circulating_supply * token_price

    def calculate_vesting_schedule(self, current_date):
        """
        Calculate the vesting schedule.

        Args:
        - current_date (datetime.date): The current date.

        Returns:
        - dict: A dictionary with the following keys:
            - 'vested': The total amount of vested tokens.
            - 'unvested': The total amount of unvested tokens.
        """
        vested = 0
        unvested = 0

        for schedule in self.vesting_schedules:
            vesting_start = schedule['vesting_start']
            vesting_end = schedule['vesting_end']
            cliff = schedule['cliff']
            amount = schedule['amount']

            if current_date < vesting_start:
                unvested += amount
            elif current_date >= vesting_end:
                vested += amount
            else:
                vesting_period = (vesting_end - vesting_start).days
                elapsed_days = (current_date - vesting_start).days

                if elapsed_days <= cliff:
                    unvested += amount
                else:
                    vested_amount = (elapsed_days - cliff) / (vesting_period - cliff) * amount
                    vested += vested_amount
                    unvested += amount - vested_amount

        return {'vested': vested, 'unvested': unvested}

    def get_token_metrics(self, token_price, current_date):
        """
        Get token metrics.

        Args:
        - token_price (float): The current token price.
        - current_date (datetime.date): The current date.

        Returns:
        - dict: A dictionary with the following keys:
            - 'initial_market_cap': The initial market capitalization.
            - 'total_supply': The total supply of tokens.
            - 'initial_circulating_supply': The initial circulating supply of tokens.
            - 'vesting_schedule': The vesting schedule.
        """
        initial_market_cap = self.calculate_initial_market_cap(token_price)
        vesting_schedule = self.calculate_vesting_schedule(current_date)

        return {
            'initial_market_cap': initial_market_cap,
            'total_supply': self.total_supply,
            'initial_circulating_supply': self.initial_circulating_supply,
            'vesting_schedule': vesting_schedule
        }


def main():
    try:
        # Define tokenomics parameters
        total_supply = 1000000000  # 1 billion tokens
        initial_circulating_supply = 200000000  # 200 million tokens
        vesting_schedules = [
            {
                'amount': 300000000,  # 300 million tokens
                'vesting_start': datetime.date(2024, 1, 1),
                'vesting_end': datetime.date(2027, 1, 1),
                'cliff': 365  # 1 year cliff
            },
            {
                'amount': 50000000,  # 50 million tokens
                'vesting_start': datetime.date(2024, 6, 1),
                'vesting_end': datetime.date(2026, 6, 1),
                'cliff': 180  # 6 months cliff
            }
        ]

        token_price = 0.10  # $0.10 per token
        current_date = datetime.date(2025, 1, 1)

        tokenomics = Tokenomics(total_supply, initial_circulating_supply, vesting_schedules)
        token_metrics = tokenomics.get_token_metrics(token_price, current_date)

        print("Token Metrics:")
        print(f"Initial Market Cap: ${token_metrics['initial_market_cap']:,}")
        print(f"Total Supply: {token_metrics['total_supply']:,}")
        print(f"Initial Circulating Supply: {token_metrics['initial_circulating_supply']:,}")
        print("Vesting Schedule:")
        print(f"  Vested: {token_metrics['vesting_schedule']['vested']:,}")
        print(f"  Unvested: {token_metrics['vesting_schedule']['unvested']:,}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
