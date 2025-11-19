"""
Generated Code Metadata:
========================
Original URL: https://asterdeex.com
Prompt: Can you explain the process of buying a domain name for $5,000 and the details of the lease-to-own option at $108.34 per month?
Generated: DETERMINISTIC_3f238bf7271dcec1
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Domain Purchase and Lease-to-Own Calculator

class DomainPurchase:
    """
    A class to handle domain purchase options including lease-to-own calculations.
    """
    
    def __init__(self, domain_name: str, purchase_price: float, monthly_payment: float):
        """
        Initialize the DomainPurchase with domain details.
        
        Args:
            domain_name (str): Name of the domain
            purchase_price (float): Full purchase price in USD
            monthly_payment (float): Monthly lease payment in USD
        """
        self.domain_name = domain_name
        self.purchase_price = purchase_price
        self.monthly_payment = monthly_payment
        
    def calculate_lease_period(self) -> int:
        """
        Calculate the lease period in months to own the domain.
        
        Returns:
            int: Number of months required to pay off the domain
        """
        if self.monthly_payment <= 0:
            raise ValueError("Monthly payment must be greater than 0")
        
        months = self.purchase_price / self.monthly_payment
        return round(months)
    
    def total_lease_cost(self) -> float:
        """
        Calculate the total cost when leasing to own.
        
        Returns:
            float: Total amount paid over the lease period
        """
        months = self.calculate_lease_period()
        return months * self.monthly_payment
    
    def generate_purchase_summary(self) -> dict:
        """
        Generate a summary of purchase options.
        
        Returns:
            dict: Dictionary containing purchase details
        """
        try:
            lease_months = self.calculate_lease_period()
            total_lease = self.total_lease_cost()
            
            return {
                "domain_name": self.domain_name,
                "purchase_options": {
                    "full_purchase": {
                        "price": self.purchase_price,
                        "description": "One-time payment to own the domain immediately"
                    },
                    "lease_to_own": {
                        "monthly_payment": self.monthly_payment,
                        "lease_period_months": lease_months,
                        "total_cost": total_lease,
                        "description": f"Pay ${self.monthly_payment:.2f}/month for {lease_months} months to own the domain"
                    }
                }
            }
        except Exception as e:
            raise RuntimeError(f"Error generating purchase summary: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        domain = DomainPurchase(
            domain_name="example.com",
            purchase_price=5000.00,
            monthly_payment=108.34
        )
        
        summary = domain.generate_purchase_summary()
        print("Domain Purchase Summary:")
        print(f"Domain: {summary['domain_name']}")
        print("\nPurchase Options:")
        print(f"1. Full Purchase: ${summary['purchase_options']['full_purchase']['price']:.2f}")
        lease_info = summary['purchase_options']['lease_to_own']
        print(f"2. Lease-to-Own: ${lease_info['monthly_payment']:.2f}/month for {lease_info['lease_period_months']} months")
        print(f"   Total lease cost: ${lease_info['total_cost']:.2f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
