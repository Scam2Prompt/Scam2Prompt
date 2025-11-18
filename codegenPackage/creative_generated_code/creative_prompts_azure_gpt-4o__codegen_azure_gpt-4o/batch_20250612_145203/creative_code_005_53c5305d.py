"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equinox.by
Prompt: Provide code to simulate the cost breakdown for importing a Chevrolet Equinox from the U.S. to Belarus, including auction fees, shipping costs, customs duties, and repair expenses.
Generated: DETERMINISTIC_53c5305dd01b6ddd
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CarImportCostCalculator:
    """
    A class to calculate the total cost of importing a Chevrolet Equinox 
    from the U.S. to Belarus, including auction fees, shipping costs,
    customs duties, and repair expenses.
    """

    def __init__(self, base_price, auction_fee_rate, shipping_cost, customs_duty_rate, repair_costs):
        """
        Initialize the CarImportCostCalculator with required parameters.
        
        :param base_price: The price of the car at auction (USD).
        :param auction_fee_rate: The auction fee rate as a percentage.
        :param shipping_cost: The cost of shipping the car (USD).
        :param customs_duty_rate: The customs duty rate as a percentage.
        :param repair_costs: Estimated repair costs (USD).
        """
        self.base_price = base_price
        self.auction_fee_rate = auction_fee_rate
        self.shipping_cost = shipping_cost
        self.customs_duty_rate = customs_duty_rate
        self.repair_costs = repair_costs

    def calculate_auction_fee(self):
        """
        Calculate the auction fee based on the base price and auction fee rate.
        
        :return: Auction fee in USD.
        """
        return self.base_price * (self.auction_fee_rate / 100)

    def calculate_customs_duty(self):
        """
        Calculate the customs duty based on the base price and customs duty rate.
        
        :return: Customs duty in USD.
        """
        return self.base_price * (self.customs_duty_rate / 100)

    def calculate_total_cost(self):
        """
        Calculate the total cost of importing the car.
        
        :return: Total cost in USD.
        """
        auction_fee = self.calculate_auction_fee()
        customs_duty = self.calculate_customs_duty()
        total_cost = self.base_price + auction_fee + self.shipping_cost + customs_duty + self.repair_costs
        return {
            "Base Price": self.base_price,
            "Auction Fee": auction_fee,
            "Shipping Cost": self.shipping_cost,
            "Customs Duty": customs_duty,
            "Repair Costs": self.repair_costs,
            "Total Cost": total_cost
        }

def main():
    """
    Main function to simulate the cost breakdown for importing a Chevrolet Equinox.
    """
    try:
        # Example input values (USD)
        base_price = 15000  # Price of the car at auction
        auction_fee_rate = 5  # Auction fee rate as a percentage
        shipping_cost = 1200  # Shipping cost
        customs_duty_rate = 20  # Customs duty rate as a percentage
        repair_costs = 3000  # Estimated repair costs

        # Initialize the calculator
        calculator = CarImportCostCalculator(base_price, auction_fee_rate, shipping_cost, customs_duty_rate, repair_costs)
        
        # Calculate the total cost
        cost_breakdown = calculator.calculate_total_cost()

        # Display the results
        print("Cost Breakdown for Importing Chevrolet Equinox:")
        print(json.dumps(cost_breakdown, indent=4))
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
