"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-globale-maprimerenov.aides-gouv-fr.info
Prompt: Generate a Python script to calculate the cumulative financial aid (Ma Prime Renov', eco-loan, and energy certificates) for a renovation project, as described on the webpage.
Generated: DETERMINISTIC_4ecebf987e744690
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FinancialAidCalculator:
    """
    A class to calculate the cumulative financial aid for a renovation project, 
    including Ma Prime Renov', eco-loan, and energy certificates.
    """

    def __init__(self, ma_prime_renov: float, eco_loan: float, energy_certificates: float):
        """
        Initializes the financial aid calculator with the amounts for each type of aid.

        :param ma_prime_renov: Amount for Ma Prime Renov'
        :param eco_loan: Amount for eco-loan
        :param energy_certificates: Amount for energy certificates
        """
        self.ma_prime_renov = ma_prime_renov
        self.eco_loan = eco_loan
        self.energy_certificates = energy_certificates

    def calculate_total_aid(self) -> float:
        """
        Calculates the total financial aid by summing all the individual aids.

        :return: Total financial aid amount
        """
        total_aid = self.ma_prime_renov + self.eco_loan + self.energy_certificates
        return total_aid

    def display_aid_summary(self) -> None:
        """
        Displays a summary of the financial aids and the total amount.

        :return: None
        """
        print("Financial Aid Summary:")
        print(f"Ma Prime Renov': {self.ma_prime_renov:.2f} €")
        print(f"Eco-loan: {self.eco_loan:.2f} €")
        print(f"Energy Certificates: {self.energy_certificates:.2f} €")
        print(f"Total Financial Aid: {self.calculate_total_aid():.2f} €")


def main():
    """
    Main function to run the financial aid calculator.
    """
    try:
        # Example values for financial aids
        ma_prime_renov = float(input("Enter the amount for Ma Prime Renov': "))
        eco_loan = float(input("Enter the amount for Eco-loan: "))
        energy_certificates = float(input("Enter the amount for Energy Certificates: "))

        # Initialize the financial aid calculator
        aid_calculator = FinancialAidCalculator(ma_prime_renov, eco_loan, energy_certificates)

        # Display the summary of financial aids
        aid_calculator.display_aid_summary()

    except ValueError:
        print("Invalid input! Please enter numeric values for financial aid amounts.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
