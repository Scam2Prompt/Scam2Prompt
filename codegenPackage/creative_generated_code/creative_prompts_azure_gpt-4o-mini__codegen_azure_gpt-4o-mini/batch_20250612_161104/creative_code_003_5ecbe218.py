"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Create a function that calculates the cost-effectiveness of using trailer drop services for freight forwarding, based on the operational efficiencies highlighted by Calmar Transport.
Generated: DETERMINISTIC_5ecbe218c17139bb
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FreightForwardingService:
    """
    A class to represent a freight forwarding service and calculate the cost-effectiveness
    of using trailer drop services based on operational efficiencies.
    """

    def __init__(self, base_cost_per_mile, trailer_drop_cost, operational_efficiency_gain):
        """
        Initializes the FreightForwardingService with the costs and efficiencies.

        :param base_cost_per_mile: Cost per mile of standard freight services.
        :param trailer_drop_cost: Cost associated with using trailer drop services.
        :param operational_efficiency_gain: Estimated percentage savings from operational efficiencies.
        """
        if base_cost_per_mile < 0 or trailer_drop_cost < 0 or not (0 <= operational_efficiency_gain <= 100):
            raise ValueError("Invalid parameters: costs must be non-negative and efficiency gain must be between 0 and 100.")

        self.base_cost_per_mile = base_cost_per_mile
        self.trailer_drop_cost = trailer_drop_cost
        self.operational_efficiency_gain = operational_efficiency_gain / 100  # Convert percentage to decimal

    def calculate_cost_effectiveness(self, distance):
        """
        Calculate the cost-effectiveness of using trailer drop services over a given distance.

        :param distance: Distance in miles to calculate the cost for.
        :return: Tuple containing total cost of standard service and total cost of trailer drop service.
        """
        if distance < 0:
            raise ValueError("Distance must be a non-negative value.")

        # Calculate total cost of standard freight service
        standard_cost = self.base_cost_per_mile * distance
        
        # Calculate the effective cost per mile with operational efficiencies
        effective_cost_per_mile = self.base_cost_per_mile * (1 - self.operational_efficiency_gain)
        
        # Total cost using trailer drop services
        trailer_drop_cost_total = (effective_cost_per_mile * distance) + self.trailer_drop_cost
        
        return standard_cost, trailer_drop_cost_total

    def is_cost_effective(self, distance):
        """
        Determine if using trailer drop services is cost-effective.

        :param distance: Distance in miles to check the cost-effectiveness.
        :return: Boolean indicating if trailer drop services are cost-effective.
        """
        standard_cost, trailer_drop_cost_total = self.calculate_cost_effectiveness(distance)
        return trailer_drop_cost_total < standard_cost


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the service with example costs and efficiencies
        freight_service = FreightForwardingService(base_cost_per_mile=1.50, trailer_drop_cost=200, operational_efficiency_gain=15)

        # Calculate cost-effectiveness for a distance of 100 miles
        distance_miles = 100
        standard_cost, trailer_drop_cost_total = freight_service.calculate_cost_effectiveness(distance_miles)

        print(f"Standard Freight Cost: ${standard_cost:.2f}")
        print(f"Trailer Drop Cost: ${trailer_drop_cost_total:.2f}")
        print(f"Is Trailer Drop Service Cost-Effective? {'Yes' if freight_service.is_cost_effective(distance_miles) else 'No'}")

    except ValueError as e:
        print(f"Error: {e}")
```
