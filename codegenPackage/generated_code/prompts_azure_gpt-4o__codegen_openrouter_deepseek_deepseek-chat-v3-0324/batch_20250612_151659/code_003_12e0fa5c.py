"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Develop an algorithm to estimate the cost of moving furniture based on شركة آل البيت's recommendations for budget planning and minimizing expenses.
Generated: DETERMINISTIC_12e0fa5c8d9875e1
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FurnitureMovingCostEstimator:
    """
    A class to estimate the cost of moving furniture based on شركة آل البيت's recommendations.
    The estimator considers factors like distance, volume, and additional services.
    """
    
    def __init__(self):
        # Base rates (in local currency)
        self.base_rate = 500  # Minimum charge
        self.per_km_rate = 50  # Rate per kilometer
        self.per_volume_rate = 100  # Rate per cubic meter
        self.packing_rate = 200  # Flat rate for packing service
        self.assembly_rate = 300  # Flat rate for assembly/disassembly
        
        # Discount thresholds
        self.distance_discount_threshold = 50  # km
        self.distance_discount_percent = 0.1  # 10%
        self.volume_discount_threshold = 10  # cubic meters
        self.volume_discount_percent = 0.15  # 15%
    
    def calculate_cost(self, distance_km: float, volume_m3: float, 
                      needs_packing: bool = False, needs_assembly: bool = False) -> float:
        """
        Calculate the total moving cost based on input parameters.
        
        Args:
            distance_km: Distance of the move in kilometers
            volume_m3: Total volume of furniture in cubic meters
            needs_packing: Whether packing service is required
            needs_assembly: Whether assembly/disassembly service is required
            
        Returns:
            float: Total estimated cost
            
        Raises:
            ValueError: If distance or volume are negative
        """
        if distance_km < 0 or volume_m3 < 0:
            raise ValueError("Distance and volume must be non-negative values")
        
        # Calculate distance cost with possible discount
        distance_cost = distance_km * self.per_km_rate
        if distance_km > self.distance_discount_threshold:
            distance_cost *= (1 - self.distance_discount_percent)
        
        # Calculate volume cost with possible discount
        volume_cost = volume_m3 * self.per_volume_rate
        if volume_m3 > self.volume_discount_threshold:
            volume_cost *= (1 - self.volume_discount_percent)
        
        # Calculate additional services
        additional_services = 0
        if needs_packing:
            additional_services += self.packing_rate
        if needs_assembly:
            additional_services += self.assembly_rate
        
        # Calculate total cost
        total_cost = self.base_rate + distance_cost + volume_cost + additional_services
        
        return total_cost
    
    def get_detailed_estimate(self, distance_km: float, volume_m3: float, 
                            needs_packing: bool = False, needs_assembly: bool = False) -> dict:
        """
        Get a detailed breakdown of the moving cost estimate.
        
        Args:
            Same as calculate_cost()
            
        Returns:
            dict: Detailed cost breakdown with components
            
        Raises:
            ValueError: If distance or volume are negative
        """
        total_cost = self.calculate_cost(distance_km, volume_m3, needs_packing, needs_assembly)
        
        breakdown = {
            'base_rate': self.base_rate,
            'distance_km': distance_km,
            'distance_cost': distance_km * self.per_km_rate,
            'distance_discount_applied': distance_km > self.distance_discount_threshold,
            'volume_m3': volume_m3,
            'volume_cost': volume_m3 * self.per_volume_rate,
            'volume_discount_applied': volume_m3 > self.volume_discount_threshold,
            'packing_service': needs_packing,
            'packing_cost': self.packing_rate if needs_packing else 0,
            'assembly_service': needs_assembly,
            'assembly_cost': self.assembly_rate if needs_assembly else 0,
            'total_cost': total_cost
        }
        
        return breakdown


# Example usage
if __name__ == "__main__":
    estimator = FurnitureMovingCostEstimator()
    
    try:
        # Sample move: 75km, 12m³, needs packing
        cost = estimator.calculate_cost(75, 12, needs_packing=True)
        print(f"Estimated moving cost: {cost:.2f}")
        
        # Get detailed breakdown
        details = estimator.get_detailed_estimate(75, 12, needs_packing=True)
        print("\nDetailed cost breakdown:")
        for key, value in details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
