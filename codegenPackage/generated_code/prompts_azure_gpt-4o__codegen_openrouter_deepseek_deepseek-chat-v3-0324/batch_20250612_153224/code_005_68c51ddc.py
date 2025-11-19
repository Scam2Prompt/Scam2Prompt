"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Write code to simulate the flat-fee pricing model for computer repair services offered by Geeks On Repair, including a feature to calculate costs based on repair type.
Generated: DETERMINISTIC_68c51ddc2732049e
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
Geeks On Repair - Flat-Fee Pricing Model Simulator

This script simulates the flat-fee pricing model for computer repair services.
It calculates costs based on different repair types and handles various edge cases.
"""

class RepairService:
    """
    A class to represent the flat-fee pricing model for computer repair services.
    """
    
    def __init__(self):
        """
        Initialize the repair service with predefined pricing for different repair types.
        """
        self.repair_prices = {
            'virus_removal': 99.99,
            'hardware_repair': 149.99,
            'os_installation': 79.99,
            'data_recovery': 199.99,
            'screen_replacement': 129.99,
            'diagnostic': 49.99
        }
        self.tax_rate = 0.08  # 8% sales tax
    
    def calculate_cost(self, repair_type, is_member=False):
        """
        Calculate the total cost for a repair service including tax.
        
        Args:
            repair_type (str): Type of repair service requested
            is_member (bool): Whether customer is a member (eligible for discount)
        
        Returns:
            float: Total cost after tax (and discount if applicable)
        
        Raises:
            ValueError: If repair_type is not recognized
        """
        if repair_type not in self.repair_prices:
            raise ValueError(f"Invalid repair type: {repair_type}. Available types: {list(self.repair_prices.keys())}")
        
        base_price = self.repair_prices[repair_type]
        
        # Apply 10% discount for members
        if is_member:
            base_price *= 0.9
        
        total_cost = base_price * (1 + self.tax_rate)
        
        return round(total_cost, 2)
    
    def display_price_menu(self):
        """
        Display the available repair services and their base prices.
        """
        print("Geeks On Repair - Service Menu")
        print("-----------------------------")
        for service, price in self.repair_prices.items():
            print(f"{service.replace('_', ' ').title():<20} ${price:.2f}")
        print("\n* Members receive 10% discount on all services")
        print(f"* All services subject to {self.tax_rate*100:.0f}% sales tax\n")


def main():
    """
    Main function to run the repair service cost calculator.
    """
    service = RepairService()
    
    print("Welcome to Geeks On Repair Pricing Calculator")
    print("-------------------------------------------")
    
    while True:
        try:
            service.display_price_menu()
            
            # Get user input
            repair_type = input("Enter repair type (or 'quit' to exit): ").strip().lower()
            if repair_type == 'quit':
                break
                
            membership = input("Is the customer a member? (yes/no): ").strip().lower()
            is_member = membership in ['yes', 'y']
            
            # Calculate and display cost
            total_cost = service.calculate_cost(repair_type, is_member)
            print(f"\nTotal cost for {repair_type.replace('_', ' ')}: ${total_cost:.2f}\n")
            
        except ValueError as e:
            print(f"\nError: {e}\nPlease try again.\n")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}\n")
            break

if __name__ == "__main__":
    main()
```
