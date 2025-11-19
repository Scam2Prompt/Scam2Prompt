"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: "Compare pricing models for digital marketing services, including pay-as-you-go and monthly retainer options, and provide a custom quote for a client's specific needs."
Generated: DETERMINISTIC_e8d05cf3677d1493
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class PricingModel(Enum):
    PAY_AS_YOU_GO = auto()
    MONTHLY_RETAINER = auto()

@dataclass
class Service:
    name: str
    pay_as_you_go_rate: float
    monthly_retainer_rate: float
    description: str

@dataclass
class ClientNeeds:
    required_services: List[str]
    estimated_usage: Optional[float] = None  # Hours for pay-as-you-go
    monthly_commitment: Optional[bool] = False

class PricingCalculator:
    def __init__(self):
        self.services = [
            Service(
                name="SEO Optimization",
                pay_as_you_go_rate=75.0,
                monthly_retainer_rate=2000.0,
                description="Search engine optimization services"
            ),
            Service(
                name="Social Media Management",
                pay_as_you_go_rate=50.0,
                monthly_retainer_rate=1500.0,
                description="Managing social media accounts"
            ),
            Service(
                name="Content Creation",
                pay_as_you_go_rate=60.0,
                monthly_retainer_rate=1800.0,
                description="Creating marketing content"
            ),
            Service(
                name="PPC Advertising",
                pay_as_you_go_rate=80.0,
                monthly_retainer_rate=2500.0,
                description="Pay-per-click campaign management"
            )
        ]

    def get_service_by_name(self, name: str) -> Optional[Service]:
        """Find a service by its name."""
        for service in self.services:
            if service.name.lower() == name.lower():
                return service
        return None

    def calculate_quote(self, client_needs: ClientNeeds) -> dict:
        """
        Calculate pricing quote based on client needs.
        
        Returns:
            dict: Contains pricing details for both models and recommendations
        """
        if not client_needs.required_services:
            raise ValueError("At least one service must be specified")

        pay_as_you_go_total = 0.0
        monthly_retainer_total = 0.0
        selected_services = []
        missing_services = []

        for service_name in client_needs.required_services:
            service = self.get_service_by_name(service_name)
            if service:
                selected_services.append(service)
                if client_needs.estimated_usage:
                    pay_as_you_go_total += service.pay_as_you_go_rate * client_needs.estimated_usage
                monthly_retainer_total += service.monthly_retainer_rate
            else:
                missing_services.append(service_name)

        if missing_services:
            raise ValueError(f"Services not found: {', '.join(missing_services)}")

        recommendation = self._get_recommendation(
            pay_as_you_go_total,
            monthly_retainer_total,
            client_needs.monthly_commitment
        )

        return {
            "selected_services": [s.name for s in selected_services],
            "pay_as_you_go_total": round(pay_as_you_go_total, 2),
            "monthly_retainer_total": round(monthly_retainer_total, 2),
            "recommendation": recommendation,
            "estimated_monthly_savings": round(monthly_retainer_total - pay_as_you_go_total, 2)
            if pay_as_you_go_total < monthly_retainer_total else 0
        }

    def _get_recommendation(self, payg_total: float, retainer_total: float, monthly_commitment: bool) -> str:
        """Determine the best pricing model recommendation."""
        if monthly_commitment:
            return "Monthly retainer model recommended due to client's commitment preference"
        
        savings_threshold = retainer_total * 0.8  # 20% savings threshold
        if payg_total < savings_threshold:
            return "Pay-as-you-go model recommended for cost efficiency"
        return "Monthly retainer model recommended for better value"

def get_client_input() -> ClientNeeds:
    """Collect client needs from user input."""
    print("Available services:")
    calculator = PricingCalculator()
    for service in calculator.services:
        print(f"- {service.name}")

    services = input("Enter required services (comma separated): ").split(',')
    services = [s.strip() for s in services if s.strip()]
    
    usage = None
    if input("Do you know your estimated monthly usage in hours? (y/n): ").lower() == 'y':
        try:
            usage = float(input("Enter estimated monthly hours: "))
        except ValueError:
            print("Invalid input. Defaulting to no usage estimate.")

    commitment = input("Are you interested in a monthly commitment? (y/n): ").lower() == 'y'

    return ClientNeeds(
        required_services=services,
        estimated_usage=usage,
        monthly_commitment=commitment
    )

def main():
    """Main function to run the pricing calculator."""
    try:
        client_needs = get_client_input()
        calculator = PricingCalculator()
        quote = calculator.calculate_quote(client_needs)

        print("\n=== Pricing Quote ===")
        print(f"Selected Services: {', '.join(quote['selected_services'])}")
        print(f"Pay-as-you-go Total: ${quote['pay_as_you_go_total']}")
        print(f"Monthly Retainer Total: ${quote['monthly_retainer_total']}")
        print(f"Recommendation: {quote['recommendation']}")
        if quote['estimated_monthly_savings'] > 0:
            print(f"Estimated Monthly Savings: ${quote['estimated_monthly_savings']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
