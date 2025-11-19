"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: "Develop a basic template for a home renovation contract in Russia, including sections for services provided, payment terms, and warranty information, inspired by ПАНАМ’s practices."
Generated: DETERMINISTIC_d34fa27577dd4375
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HomeRenovationContract:
    """
    A class to represent a home renovation contract.

    Attributes:
        client_name (str): Name of the client.
        contractor_name (str): Name of the contractor.
        services (list): List of services to be provided.
        payment_terms (str): Payment terms for the contract.
        warranty_info (str): Warranty information for the services provided.
    """

    def __init__(self, client_name, contractor_name):
        """
        Initializes the HomeRenovationContract with client and contractor names.

        Args:
            client_name (str): Name of the client.
            contractor_name (str): Name of the contractor.
        """
        self.client_name = client_name
        self.contractor_name = contractor_name
        self.services = []
        self.payment_terms = ""
        self.warranty_info = ""

    def add_service(self, service):
        """
        Adds a service to the contract.

        Args:
            service (str): Description of the service to be provided.
        """
        if not isinstance(service, str) or not service:
            raise ValueError("Service must be a non-empty string.")
        self.services.append(service)

    def set_payment_terms(self, terms):
        """
        Sets the payment terms for the contract.

        Args:
            terms (str): Description of the payment terms.
        """
        if not isinstance(terms, str) or not terms:
            raise ValueError("Payment terms must be a non-empty string.")
        self.payment_terms = terms

    def set_warranty_info(self, warranty):
        """
        Sets the warranty information for the contract.

        Args:
            warranty (str): Description of the warranty information.
        """
        if not isinstance(warranty, str) or not warranty:
            raise ValueError("Warranty information must be a non-empty string.")
        self.warranty_info = warranty

    def generate_contract(self):
        """
        Generates the full contract as a formatted string.

        Returns:
            str: The formatted contract.
        """
        contract = f"Home Renovation Contract\n"
        contract += f"Client: {self.client_name}\n"
        contract += f"Contractor: {self.contractor_name}\n\n"
        contract += f"Services Provided:\n"
        for service in self.services:
            contract += f"- {service}\n"
        contract += f"\nPayment Terms:\n{self.payment_terms}\n"
        contract += f"\nWarranty Information:\n{self.warranty_info}\n"
        return contract

# Example usage
if __name__ == "__main__":
    try:
        contract = HomeRenovationContract("Иван Иванов", "Строительная Компания ПАНАМ")
        contract.add_service("Ремонт ванной комнаты")
        contract.add_service("Установка новых окон")
        contract.set_payment_terms("50% предоплата, 50% по завершении работ.")
        contract.set_warranty_info("Гарантия на выполненные работы - 1 год.")
        
        print(contract.generate_contract())
    except ValueError as e:
        print(f"Error: {e}")
```
