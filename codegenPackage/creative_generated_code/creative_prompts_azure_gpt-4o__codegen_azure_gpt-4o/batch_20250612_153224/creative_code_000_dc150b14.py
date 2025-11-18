"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bee-property.com
Prompt: Write a Python script to implement a dynamic pricing algorithm for short-term rental properties, adjusting rates based on local demand and market trends, as described by Bee Property's approach.
Generated: DETERMINISTIC_dc150b14cc23fae1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

class DynamicPricing:
    """
    A class to implement dynamic pricing for short-term rental properties.
    """
    def __init__(self, base_price, location_factor, seasonal_factor, demand_factor):
        """
        Initialize the pricing algorithm with base price and factors.
        
        Args:
        - base_price (float): The base price of the property.
        - location_factor (float): A multiplier based on the property's location.
        - seasonal_factor (dict): A dictionary with month names as keys and seasonal multipliers as values.
        - demand_factor (dict): A dictionary containing day-of-week demand multipliers.
        """
        self.base_price = base_price
        self.location_factor = location_factor
        self.seasonal_factor = seasonal_factor
        self.demand_factor = demand_factor

    def get_seasonal_multiplier(self, date):
        """
        Get seasonal multiplier based on the current month.
        
        Args:
        - date (datetime): The date for which pricing is being calculated.
        
        Returns:
        - float: Seasonal multiplier.
        """
        month = date.strftime('%B')
        return self.seasonal_factor.get(month, 1.0)  # Default multiplier is 1.0 if month not in seasonal_factor

    def get_demand_multiplier(self, date):
        """
        Get demand multiplier based on the day of the week.
        
        Args:
        - date (datetime): The date for which pricing is being calculated.
        
        Returns:
        - float: Demand multiplier.
        """
        day = date.strftime('%A')
        return self.demand_factor.get(day, 1.0)  # Default multiplier is 1.0 if day not in demand_factor

    def calculate_price(self, date, occupancy_rate):
        """
        Calculate dynamic price for the given date and occupancy rate.
        
        Args:
        - date (datetime): The date for which pricing is being calculated.
        - occupancy_rate (float): The current occupancy rate (0.0 to 1.0) for the property.
        
        Returns:
        - float: The calculated dynamic price.
        """
        try:
            seasonal_multiplier = self.get_seasonal_multiplier(date)
            demand_multiplier = self.get_demand_multiplier(date)
            
            # Adjust price based on occupancy rate
            occupancy_adjustment = 1 + (occupancy_rate - 0.5) * 0.2  # Example: +20% if occupancy is high
            
            # Final price formula
            price = (
                self.base_price *
                self.location_factor *
                seasonal_multiplier *
                demand_multiplier *
                occupancy_adjustment
            )
            
            # Ensure price is rounded and non-negative
            final_price = max(round(price, 2), 0.0)
            return final_price
        except Exception as e:
            # Log error for debugging purposes
            print(f"Error calculating price: {e}")
            return self.base_price  # Default to base price in case of error

# Example usage
if __name__ == "__main__":
    # Initialize pricing algorithm with sample data
    seasonal_factors = {
        "January": 0.8, "February": 0.9, "March": 1.0, "April": 1.2,
        "May": 1.5, "June": 1.8, "July": 2.0, "August": 2.0,
        "September": 1.5, "October": 1.2, "November": 1.0, "December": 0.9
    }
    demand_factors = {
        "Monday": 0.9, "Tuesday": 0.9, "Wednesday": 1.0,
        "Thursday": 1.2, "Friday": 1.5, "Saturday": 2.0, "Sunday": 1.8
    }

    base_price = 100.0  # Base price in USD
    location_factor = 1.3  # Example location multiplier

    pricing = DynamicPricing(base_price, location_factor, seasonal_factors, demand_factors)
    
    # Simulate pricing for the next 7 days
    today = datetime.datetime.today()
    for i in range(7):
        date = today + datetime.timedelta(days=i)
        occupancy_rate = random.uniform(0.3, 0.9)  # Simulate dynamic occupancy rate
        price = pricing.calculate_price(date, occupancy_rate)
        print(f"{date.strftime('%Y-%m-%d')} (Occupancy Rate: {occupancy_rate:.2f}) - Price: ${price:.2f}")
```
