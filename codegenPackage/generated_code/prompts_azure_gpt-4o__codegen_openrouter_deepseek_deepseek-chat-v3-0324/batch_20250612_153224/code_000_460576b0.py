"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Write a Python script to calculate the cost of consulting services for architectural projects, factoring in additional services beyond the initial agreement as described by TWM Associates.
Generated: DETERMINISTIC_460576b00c7d6969
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost of consulting services for architectural projects.
Factors in additional services beyond the initial agreement.
"""

class ConsultingCostCalculator:
    """
    A class to calculate the total cost of architectural consulting services,
    including base fees and additional services.
    """
    
    def __init__(self, base_fee: float, hourly_rate: float):
        """
        Initialize the calculator with base fee and hourly rate.
        
        Args:
            base_fee (float): The initial fixed fee for the project
            hourly_rate (float): The rate charged for additional services per hour
        """
        self.base_fee = base_fee
        self.hourly_rate = hourly_rate
        self.additional_services = []
    
    def add_service(self, service_name: str, hours: float):
        """
        Add an additional service to be factored into the total cost.
        
        Args:
            service_name (str): Name/description of the service
            hours (float): Number of hours required for this service
        """
        if hours <= 0:
            raise ValueError("Hours must be a positive number")
        self.additional_services.append({
            'name': service_name,
            'hours': hours
        })
    
    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost including base fee and additional services.
        
        Returns:
            float: The total calculated cost
        """
        additional_cost = sum(
            service['hours'] * self.hourly_rate 
            for service in self.additional_services
        )
        return self.base_fee + additional_cost
    
    def generate_invoice(self) -> str:
        """
        Generate a detailed invoice showing cost breakdown.
        
        Returns:
            str: Formatted invoice string
        """
        invoice_lines = [
            "TWM Associates - Architectural Consulting Invoice",
            "=" * 50,
            f"Base Fee: ${self.base_fee:.2f}",
            "\nAdditional Services:"
        ]
        
        for service in self.additional_services:
            cost = service['hours'] * self.hourly_rate
            invoice_lines.append(
                f"- {service['name']}: {service['hours']} hours @ ${self.hourly_rate}/hr = ${cost:.2f}"
            )
        
        total = self.calculate_total_cost()
        invoice_lines.extend([
            "\n" + "=" * 50,
            f"TOTAL DUE: ${total:.2f}",
            "=" * 50
        ])
        
        return "\n".join(invoice_lines)


def main():
    """Example usage of the ConsultingCostCalculator."""
    try:
        # Initialize calculator with base fee and hourly rate
        calculator = ConsultingCostCalculator(
            base_fee=5000.00,
            hourly_rate=150.00
        )
        
        # Add additional services
        calculator.add_service("Site Analysis", 8.5)
        calculator.add_service("3D Rendering", 12.0)
        calculator.add_service("Client Meetings", 5.0)
        
        # Generate and print invoice
        print(calculator.generate_invoice())
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
