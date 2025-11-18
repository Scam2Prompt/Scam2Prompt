"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Create a function to calculate the estimated yearly yield and net APY for a DeFi strategy using Instadapp Lite's Strategy Vaults. Include logic for fee deductions (20% performance fee and 0.05% exit fee).
Generated: DETERMINISTIC_b80d0b57c2a5ebdc
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DeFiYieldCalculator:
    """
    A class to calculate the estimated yearly yield and net Annual Percentage Yield (APY)
    for a DeFi strategy using Instadapp Lite's Strategy Vaults with fee deductions.
    """

    def __init__(self, initial_investment: float, estimated_yearly_yield: float, performance_fee_rate: float = 0.20, exit_fee_rate: float = 0.0005):
        """
        Initializes the calculator with the initial investment, estimated yearly yield,
        performance fee rate, and exit fee rate.
        
        :param initial_investment: The amount of money initially invested.
        :param estimated_yearly_yield: The estimated yearly yield as a decimal (e.g., 0.15 for 15%).
        :param performance_fee_rate: The rate of performance fee as a decimal (default is 20%).
        :param exit_fee_rate: The rate of exit fee as a decimal (default is 0.05%).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= estimated_yearly_yield <= 1):
            raise ValueError("Estimated yearly yield must be between 0 and 1.")

        self.initial_investment = initial_investment
        self.estimated_yearly_yield = estimated_yearly_yield
        self.performance_fee_rate = performance_fee_rate
        self.exit_fee_rate = exit_fee_rate

    def calculate_net_yield(self) -> float:
        """
        Calculates the net yield after deducting the performance fee.
        
        :return: The net yield after performance fee as a float.
        """
        gross_yield = self.initial_investment * self.estimated_yearly_yield
        performance_fee = gross_yield * self.performance_fee_rate
        net_yield = gross_yield - performance_fee
        return net_yield

    def calculate_net_apy(self) -> float:
        """
        Calculates the net APY after deducting both the performance fee and the exit fee.
        
        :return: The net APY as a decimal.
        """
        net_yield = self.calculate_net_yield()
        final_amount = self.initial_investment + net_yield
        exit_fee = final_amount * self.exit_fee_rate
        total_after_exit_fee = final_amount - exit_fee
        net_apy = (total_after_exit_fee - self.initial_investment) / self.initial_investment
        return net_apy

    def estimate_results(self):
        """
        Prints the estimated results including net yield and net APY.
        """
        try:
            net_yield = self.calculate_net_yield()
            net_apy = self.calculate_net_apy()
            print(f"Estimated Net Yield: ${net_yield:.2f}")
            print(f"Estimated Net APY: {net_apy * 100:.2f}%")
        except Exception as e:
            print(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        calculator = DeFiYieldCalculator(initial_investment=10000, estimated_yearly_yield=0.15)
        calculator.estimate_results()
    except ValueError as e:
        print(f"Input error: {e}")
```
