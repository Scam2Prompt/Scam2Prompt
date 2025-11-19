"""
Generated Code Metadata:
========================
Original URL: https://alphapremiertrd.com
Prompt: "Develop an affiliate system with commission rates that can be integrated with a trading platform, providing a feature similar to Alpha Premier Trade's 10% commission system."
Generated: DETERMINISTIC_5de0745838936b3a
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# affiliate_system.py

class Affiliate:
    """
    Represents an affiliate in the system.
    Each affiliate has a unique ID, name, and commission rate.
    """
    
    def __init__(self, affiliate_id: str, name: str, commission_rate: float):
        self.affiliate_id = affiliate_id
        self.name = name
        self.commission_rate = commission_rate

    def calculate_commission(self, sale_amount: float) -> float:
        """
        Calculate the commission for a given sale amount.
        
        :param sale_amount: The total sale amount.
        :return: The calculated commission.
        """
        if sale_amount < 0:
            raise ValueError("Sale amount must be non-negative.")
        return sale_amount * self.commission_rate


class TradingPlatform:
    """
    Represents a trading platform that integrates with the affiliate system.
    It allows for tracking sales and calculating commissions for affiliates.
    """
    
    def __init__(self):
        self.affiliates = {}
        self.sales = []

    def add_affiliate(self, affiliate: Affiliate):
        """
        Add a new affiliate to the platform.
        
        :param affiliate: An instance of Affiliate.
        """
        if affiliate.affiliate_id in self.affiliates:
            raise ValueError("Affiliate with this ID already exists.")
        self.affiliates[affiliate.affiliate_id] = affiliate

    def record_sale(self, affiliate_id: str, sale_amount: float):
        """
        Record a sale made through an affiliate.
        
        :param affiliate_id: The ID of the affiliate.
        :param sale_amount: The total sale amount.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError("Affiliate not found.")
        if sale_amount < 0:
            raise ValueError("Sale amount must be non-negative.")
        
        self.sales.append((affiliate_id, sale_amount))

    def calculate_affiliate_commissions(self) -> dict:
        """
        Calculate total commissions for all affiliates based on recorded sales.
        
        :return: A dictionary with affiliate IDs as keys and total commissions as values.
        """
        commissions = {affiliate_id: 0.0 for affiliate_id in self.affiliates}
        
        for affiliate_id, sale_amount in self.sales:
            commission = self.affiliates[affiliate_id].calculate_commission(sale_amount)
            commissions[affiliate_id] += commission
        
        return commissions


# Example usage
if __name__ == "__main__":
    try:
        # Create a trading platform instance
        trading_platform = TradingPlatform()

        # Create affiliates with a 10% commission rate
        affiliate1 = Affiliate("A001", "John Doe", 0.10)
        affiliate2 = Affiliate("A002", "Jane Smith", 0.10)

        # Add affiliates to the platform
        trading_platform.add_affiliate(affiliate1)
        trading_platform.add_affiliate(affiliate2)

        # Record some sales
        trading_platform.record_sale("A001", 1000.0)  # John Doe makes a sale of $1000
        trading_platform.record_sale("A002", 500.0)   # Jane Smith makes a sale of $500

        # Calculate and print commissions
        commissions = trading_platform.calculate_affiliate_commissions()
        for affiliate_id, commission in commissions.items():
            print(f"Affiliate ID: {affiliate_id}, Total Commission: ${commission:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
