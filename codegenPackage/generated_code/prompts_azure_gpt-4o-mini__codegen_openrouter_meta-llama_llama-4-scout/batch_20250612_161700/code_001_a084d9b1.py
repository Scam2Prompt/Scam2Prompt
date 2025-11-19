"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script that simulates notarial expenses for property purchases, incorporating the specific calculations mentioned in the Inmobiliaria Capri's notarial expense simulator.
Generated: DETERMINISTIC_a084d9b1d5d85c31
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notarial_expenses_simulator.py

class NotarialExpensesSimulator:
    """
    Simulates notarial expenses for property purchases based on Inmobiliaria Capri's calculator.

    Attributes:
        purchase_price (float): The price of the property being purchased.
        notary_fees_rate (float): The rate for notary fees (default: 0.5%).
        registry_fees_rate (float): The rate for registry fees (default: 0.3%).
        transfer_tax_rate (float): The rate for transfer tax (default: 7.0%).
        vat_rate (float): The rate for VAT (default: 21.0%).
    """

    def __init__(self, purchase_price, notary_fees_rate=0.005, registry_fees_rate=0.003, transfer_tax_rate=0.07, vat_rate=0.21):
        """
        Initializes the simulator with the purchase price and default rates.

        Args:
            purchase_price (float): The price of the property being purchased.
            notary_fees_rate (float, optional): The rate for notary fees. Defaults to 0.005.
            registry_fees_rate (float, optional): The rate for registry fees. Defaults to 0.003.
            transfer_tax_rate (float, optional): The rate for transfer tax. Defaults to 0.07.
            vat_rate (float, optional): The rate for VAT. Defaults to 0.21.
        """
        self.purchase_price = purchase_price
        self.notary_fees_rate = notary_fees_rate
        self.registry_fees_rate = registry_fees_rate
        self.transfer_tax_rate = transfer_tax_rate
        self.vat_rate = vat_rate

    def calculate_notary_fees(self):
        """
        Calculates the notary fees.

        Returns:
            float: The notary fees.
        """
        return self.purchase_price * self.notary_fees_rate

    def calculate_registry_fees(self):
        """
        Calculates the registry fees.

        Returns:
            float: The registry fees.
        """
        return self.purchase_price * self.registry_fees_rate

    def calculate_transfer_tax(self):
        """
        Calculates the transfer tax.

        Returns:
            float: The transfer tax.
        """
        return self.purchase_price * self.transfer_tax_rate

    def calculate_vat(self):
        """
        Calculates the VAT.

        Returns:
            float: The VAT.
        """
        return self.purchase_price * self.vat_rate / 100

    def simulate_expenses(self):
        """
        Simulates the notarial expenses.

        Returns:
            dict: A dictionary containing the simulated expenses.
        """
        try:
            notary_fees = self.calculate_notary_fees()
            registry_fees = self.calculate_registry_fees()
            transfer_tax = self.calculate_transfer_tax()
            vat = self.calculate_vat()
            total_expenses = notary_fees + registry_fees + transfer_tax + vat

            return {
                "Notary Fees": round(notary_fees, 2),
                "Registry Fees": round(registry_fees, 2),
                "Transfer Tax": round(transfer_tax, 2),
                "VAT": round(vat, 2),
                "Total Expenses": round(total_expenses, 2)
            }
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    try:
        purchase_price = float(input("Enter the property purchase price: "))
        simulator = NotarialExpensesSimulator(purchase_price)
        expenses = simulator.simulate_expenses()

        if expenses:
            print("\nSimulated Notarial Expenses:")
            for expense, amount in expenses.items():
                print(f"{expense}: ${amount}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
```
