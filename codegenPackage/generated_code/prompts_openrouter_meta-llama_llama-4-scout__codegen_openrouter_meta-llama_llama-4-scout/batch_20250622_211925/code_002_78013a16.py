"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Generate a sample insurance policy document in Spanish for a homeowner's insurance plan in Torreón, Coahuila, Mexico, incorporating details like coverage for natural disasters and theft.
Generated: DETERMINISTIC_78013a1671c1fe2a
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import date

class InsurancePolicy:
    def __init__(self, policy_number, homeowner_name, address, city, state, country, 
                 policy_start_date, policy_end_date, premium):
        self.policy_number = policy_number
        self.homeowner_name = homeowner_name
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.policy_start_date = policy_start_date
        self.policy_end_date = policy_end_date
        self.premium = premium
        self.coverages = []

    def add_coverage(self, coverage):
        self.coverages.append(coverage)

    def generate_policy_document(self):
        document = f"Póliza de Seguro de Hogar\n"
        document += f"Número de Póliza: {self.policy_number}\n"
        document += f"Nombre del Propietario: {self.homeowner_name}\n"
        document += f"Dirección: {self.address}, {self.city}, {self.state}, {self.country}\n"
        document += f"Fecha de Inicio: {self.policy_start_date}\n"
        document += f"Fecha de Fin: {self.policy_end_date}\n"
        document += f"Prima: ${self.premium:.2f} MXN\n\n"

        document += "Coberturas:\n"
        for coverage in self.coverages:
            document += f"- {coverage['name']}: {coverage['description']}\n"

        return document


def main():
    try:
        policy_number = "HOM-001"
        homeowner_name = "Juan Pérez"
        address = "Calle 123"
        city = "Torreón"
        state = "Coahuila"
        country = "México"
        policy_start_date = date(2024, 9, 16)
        policy_end_date = date(2025, 9, 16)
        premium = 12000.00

        policy = InsurancePolicy(policy_number, homeowner_name, address, city, state, country, 
                                 policy_start_date, policy_end_date, premium)

        natural_disaster_coverage = {
            'name': 'Desastres Naturales',
            'description': 'Cubre daños causados por huracanes, inundaciones, terremotos y otros desastres naturales.'
        }

        theft_coverage = {
            'name': 'Robo',
            'description': 'Cubre el robo de bienes personales dentro de la propiedad asegurada.'
        }

        policy.add_coverage(natural_disaster_coverage)
        policy.add_coverage(theft_coverage)

        policy_document = policy.generate_policy_document()
        print(policy_document)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
