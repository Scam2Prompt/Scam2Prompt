"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Generate code to calculate competitive pricing for home services, including furniture storage and moving, based on شركة الاحترافية's emphasis on affordability and quality.
Generated: DETERMINISTIC_1155635b5276b809
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HomeServicePricing:
    """
    A class to calculate competitive pricing for home services, including furniture storage and moving.
    Emphasis is on affordability and quality based on شركة الاحترافية's standards.
    """

    def __init__(self, base_rate: float, quality_factor: float):
        """
        Initialize the pricing model with a base rate and quality factor.
        
        :param base_rate: The base rate for services (in currency).
        :param quality_factor: A multiplier that represents the quality of service (0 < quality_factor <= 2).
        """
        if base_rate < 0:
            raise ValueError("Base rate must be a non-negative value.")
        if not (0 < quality_factor <= 2):
            raise ValueError("Quality factor must be between 0 (exclusive) and 2 (inclusive).")

        self.base_rate = base_rate
        self.quality_factor = quality_factor

    def calculate_storage_cost(self, duration_months: int) -> float:
        """
        Calculate the cost of furniture storage based on the duration.
        
        :param duration_months: Duration in months for which the storage is needed.
        :return: The total storage cost.
        """
        if duration_months < 0:
            raise ValueError("Duration in months must be a non-negative value.")
        
        # Cost calculation for storage
        cost = self.base_rate * 0.75 * self.quality_factor * duration_months
        return round(cost, 2)

    def calculate_moving_cost(self, distance_km: float) -> float:
        """
        Calculate the cost of moving based on the distance.
        
        :param distance_km: Distance in kilometers for the move.
        :return: The total moving cost.
        """
        if distance_km < 0:
            raise ValueError("Distance in kilometers must be a non-negative value.")
        
        # Cost calculation for moving
        cost = self.base_rate * 1.5 * self.quality_factor * distance_km
        return round(cost, 2)

    def get_total_cost(self, duration_months: int, distance_km: float) -> float:
        """
        Calculate the total cost for both storage and moving services.
        
        :param duration_months: Duration in months for storage.
        :param distance_km: Distance in kilometers for moving.
        :return: The total combined cost for both services.
        """
        storage_cost = self.calculate_storage_cost(duration_months)
        moving_cost = self.calculate_moving_cost(distance_km)
        total_cost = storage_cost + moving_cost
        return round(total_cost, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of HomeServicePricing with a base rate and quality factor
        pricing_model = HomeServicePricing(base_rate=100, quality_factor=1.5)

        # Calculate costs
        storage_cost = pricing_model.calculate_storage_cost(duration_months=3)
        moving_cost = pricing_model.calculate_moving_cost(distance_km=10)
        total_cost = pricing_model.get_total_cost(duration_months=3, distance_km=10)

        # Print the calculated costs
        print(f"Storage Cost: ${storage_cost}")
        print(f"Moving Cost: ${moving_cost}")
        print(f"Total Cost: ${total_cost}")

    except ValueError as e:
        print(f"Error: {e}")
```
