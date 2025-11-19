"""
Generated Code Metadata:
========================
Original URL: https://stuff-artgobblers.com
Prompt: "Design an affiliate marketing program for a digital marketing agency, including commission structures, tracking mechanisms, and promotional materials."
Generated: DETERMINISTIC_05839b349dfe496e
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Affiliate:
    """Represents an affiliate in the marketing program."""
    
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the affiliate
        self.name = name
        self.email = email
        self.commission_rate = 0.1  # Default commission rate of 10%
        self.sales = []  # List to track sales made by the affiliate

    def add_sale(self, sale_amount: float):
        """Records a sale made by the affiliate."""
        if sale_amount <= 0:
            raise ValueError("Sale amount must be greater than zero.")
        self.sales.append(sale_amount)

    def calculate_commission(self) -> float:
        """Calculates total commission earned by the affiliate."""
        total_sales = sum(self.sales)
        return total_sales * self.commission_rate


class AffiliateProgram:
    """Manages the affiliate marketing program."""
    
    def __init__(self):
        self.affiliates: Dict[str, Affiliate] = {}  # Dictionary to store affiliates

    def add_affiliate(self, name: str, email: str) -> Affiliate:
        """Adds a new affiliate to the program."""
        if email in self.affiliates:
            raise ValueError("Affiliate with this email already exists.")
        affiliate = Affiliate(name, email)
        self.affiliates[affiliate.id] = affiliate
        return affiliate

    def record_sale(self, affiliate_id: str, sale_amount: float):
        """Records a sale for a specific affiliate."""
        affiliate = self.affiliates.get(affiliate_id)
        if not affiliate:
            raise ValueError("Affiliate not found.")
        affiliate.add_sale(sale_amount)

    def get_affiliate_commission(self, affiliate_id: str) -> float:
        """Retrieves the total commission for a specific affiliate."""
        affiliate = self.affiliates.get(affiliate_id)
        if not affiliate:
            raise ValueError("Affiliate not found.")
        return affiliate.calculate_commission()

    def generate_promotional_materials(self, affiliate_id: str) -> str:
        """Generates promotional materials for the affiliate."""
        affiliate = self.affiliates.get(affiliate_id)
        if not affiliate:
            raise ValueError("Affiliate not found.")
        return f"Promotional materials for {affiliate.name}: [Link to product, Banners, etc.]"


# Example usage
if __name__ == "__main__":
    try:
        program = AffiliateProgram()
        
        # Adding affiliates
        affiliate1 = program.add_affiliate("John Doe", "john@example.com")
        affiliate2 = program.add_affiliate("Jane Smith", "jane@example.com")
        
        # Recording sales
        program.record_sale(affiliate1.id, 150.0)
        program.record_sale(affiliate1.id, 200.0)
        program.record_sale(affiliate2.id, 300.0)
        
        # Calculating commissions
        print(f"{affiliate1.name}'s commission: ${program.get_affiliate_commission(affiliate1.id):.2f}")
        print(f"{affiliate2.name}'s commission: ${program.get_affiliate_commission(affiliate2.id):.2f}")
        
        # Generating promotional materials
        print(program.generate_promotional_materials(affiliate1.id))
        
    except ValueError as e:
        print(f"Error: {e}")
```
