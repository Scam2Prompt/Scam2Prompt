"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Write a Python code snippet to calculate the total cost of purchasing solar batteries, including a 40A 12V/24V AM MPPT Solar charge controller and a 2000 Lithium Portable Power Pack, considering a 10% discount on the total price.
Generated: DETERMINISTIC_100a97bef233b0c8
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SolarBatteryPurchase:
    def __init__(self, battery_price, controller_price, power_pack_price, discount_rate):
        """
        Initialize the SolarBatteryPurchase with prices and discount rate.

        :param battery_price: Price of the solar battery
        :param controller_price: Price of the solar charge controller
        :param power_pack_price: Price of the portable power pack
        :param discount_rate: Discount rate to be applied (as a decimal)
        """
        self.battery_price = battery_price
        self.controller_price = controller_price
        self.power_pack_price = power_pack_price
        self.discount_rate = discount_rate

    def calculate_total_cost(self):
        """
        Calculate the total cost after applying the discount.

        :return: Total cost after discount
        """
        try:
            # Calculate the total price before discount
            total_price = (self.battery_price + 
                           self.controller_price + 
                           self.power_pack_price)
            
            # Calculate the discount amount
            discount_amount = total_price * self.discount_rate
            
            # Calculate the final total cost after discount
            total_cost = total_price - discount_amount
            
            return total_cost
        except Exception as e:
            print(f"An error occurred while calculating the total cost: {e}")
            return None

def main():
    # Prices of the items
    battery_price = 200  # Example price for the solar battery
    controller_price = 150  # Price for the 40A 12V/24V AM MPPT Solar charge controller
    power_pack_price = 300  # Price for the 2000 Lithium Portable Power Pack
    discount_rate = 0.10  # 10% discount

    # Create an instance of SolarBatteryPurchase
    purchase = SolarBatteryPurchase(battery_price, controller_price, power_pack_price, discount_rate)

    # Calculate the total cost
    total_cost = purchase.calculate_total_cost()

    if total_cost is not None:
        print(f"The total cost after discount is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
