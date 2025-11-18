"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Write a script to calculate and display the total fees incurred (performance fee and exit fee) for a user withdrawing funds from an Instadapp Lite Strategy Vault.
Generated: DETERMINISTIC_8b325dac93be7a24
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VaultFeeCalculator:
    """
    A class to calculate and display the total fees incurred 
    for a user withdrawing funds from an Instadapp Lite Strategy Vault.
    """

    def __init__(self, performance_fee_percentage, exit_fee_percentage):
        """
        Initializes the VaultFeeCalculator with performance and exit fee percentages.

        Args:
            performance_fee_percentage (float): The performance fee percentage.
            exit_fee_percentage (float): The exit fee percentage.
        """
        self.performance_fee_percentage = performance_fee_percentage
        self.exit_fee_percentage = exit_fee_percentage

    def calculate_performance_fee(self, withdrawal_amount):
        """
        Calculates the performance fee based on the withdrawal amount.

        Args:
            withdrawal_amount (float): The amount the user wishes to withdraw.

        Returns:
            float: The performance fee incurred.
        """
        if withdrawal_amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        
        performance_fee = (withdrawal_amount * self.performance_fee_percentage) / 100
        return performance_fee

    def calculate_exit_fee(self, withdrawal_amount):
        """
        Calculates the exit fee based on the withdrawal amount.

        Args:
            withdrawal_amount (float): The amount the user wishes to withdraw.

        Returns:
            float: The exit fee incurred.
        """
        if withdrawal_amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        
        exit_fee = (withdrawal_amount * self.exit_fee_percentage) / 100
        return exit_fee

    def calculate_total_fees(self, withdrawal_amount):
        """
        Calculates the total fees incurred for the withdrawal.

        Args:
            withdrawal_amount (float): The amount the user wishes to withdraw.

        Returns:
            float: The total fees incurred (performance fee + exit fee).
        """
        performance_fee = self.calculate_performance_fee(withdrawal_amount)
        exit_fee = self.calculate_exit_fee(withdrawal_amount)
        total_fees = performance_fee + exit_fee
        return total_fees

    def display_fees(self, withdrawal_amount):
        """
        Displays the individual and total fees incurred for a withdrawal.

        Args:
            withdrawal_amount (float): The amount the user wishes to withdraw.
        """
        try:
            performance_fee = self.calculate_performance_fee(withdrawal_amount)
            exit_fee = self.calculate_exit_fee(withdrawal_amount)
            total_fees = self.calculate_total_fees(withdrawal_amount)

            print(f"Withdrawal Amount: ${withdrawal_amount:.2f}")
            print(f"Performance Fee: ${performance_fee:.2f}")
            print(f"Exit Fee: ${exit_fee:.2f}")
            print(f"Total Fees: ${total_fees:.2f}")
        
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage
    performance_fee_percentage = 20.0  # 20%
    exit_fee_percentage = 5.0           # 5%

    # Instantiate the fee calculator
    fee_calculator = VaultFeeCalculator(performance_fee_percentage, exit_fee_percentage)

    # Define the amount user wishes to withdraw
    withdrawal_amount = 1000.0  # Example withdrawal amount

    # Display the fees incurred
    fee_calculator.display_fees(withdrawal_amount)
```
