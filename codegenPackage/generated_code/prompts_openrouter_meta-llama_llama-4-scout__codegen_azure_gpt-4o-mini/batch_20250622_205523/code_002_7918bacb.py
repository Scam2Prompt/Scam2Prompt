"""
Generated Code Metadata:
========================
Original URL: https://blocichain.com
Prompt: Generate a sample agreement template for a domain rental plan based on the terms and conditions provided for "blocichain.com", including clauses for payment, ownership, and default.
Generated: DETERMINISTIC_7918bacb06f1fda8
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DomainRentalAgreement:
    """
    A class to represent a domain rental agreement for a specific domain.
    """

    def __init__(self, domain_name, renter_name, rental_period, rental_fee):
        """
        Initializes the DomainRentalAgreement with the provided parameters.

        :param domain_name: str - The domain name being rented.
        :param renter_name: str - The name of the renter.
        :param rental_period: int - The rental period in months.
        :param rental_fee: float - The monthly rental fee.
        """
        self.domain_name = domain_name
        self.renter_name = renter_name
        self.rental_period = rental_period
        self.rental_fee = rental_fee
        self.total_fee = self.calculate_total_fee()

    def calculate_total_fee(self):
        """
        Calculates the total rental fee for the entire rental period.

        :return: float - The total rental fee.
        """
        return self.rental_period * self.rental_fee

    def generate_agreement(self):
        """
        Generates the rental agreement as a formatted string.

        :return: str - The formatted rental agreement.
        """
        agreement = f"""
        DOMAIN RENTAL AGREEMENT

        This Domain Rental Agreement ("Agreement") is made and entered into as of the date of signing by and between:

        Domain Owner: blocichain.com
        Renter: {self.renter_name}

        1. DOMAIN NAME
        The domain name being rented is: {self.domain_name}

        2. RENTAL PERIOD
        The rental period for the domain is: {self.rental_period} months.

        3. PAYMENT TERMS
        The monthly rental fee is: ${self.rental_fee:.2f}
        The total rental fee for the entire period is: ${self.total_fee:.2f}
        Payment is due on the first day of each month.

        4. OWNERSHIP
        The ownership of the domain remains with the owner, blocichain.com. The renter has no rights to claim ownership of the domain.

        5. DEFAULT
        In the event of default in payment, the owner reserves the right to terminate this agreement and reclaim the domain name.

        IN WITNESS WHEREOF, the parties hereto have executed this Domain Rental Agreement as of the date below.

        Renter Signature: ______________________
        Date: ______________________
        """
        return agreement

    def save_agreement(self, file_path):
        """
        Saves the generated agreement to a text file.

        :param file_path: str - The path to the file where the agreement will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                file.write(self.generate_agreement())
            print(f"Agreement saved successfully to {file_path}")
        except IOError as e:
            print(f"Error saving agreement: {e}")

# Example usage
if __name__ == "__main__":
    # Create a domain rental agreement instance
    agreement = DomainRentalAgreement(domain_name="blocichain.com", renter_name="John Doe", rental_period=12, rental_fee=50.00)
    
    # Generate and save the agreement
    agreement.save_agreement("domain_rental_agreement.txt")
```
