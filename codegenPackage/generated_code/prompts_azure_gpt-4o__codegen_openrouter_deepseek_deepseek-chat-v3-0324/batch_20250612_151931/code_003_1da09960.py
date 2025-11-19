"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Create a program that calculates the load capacity for a parking lift system, using the range of 500 kg to 10 tons mentioned on OHC Lift's website.
Generated: DETERMINISTIC_1da099608db3dded
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ParkingLiftCapacityCalculator:
    """
    A class to calculate and validate the load capacity for a parking lift system.
    The valid range is between 500 kg and 10 tons (10000 kg).
    """
    
    MIN_CAPACITY_KG = 500
    MAX_CAPACITY_KG = 10000  # 10 tons
    
    @staticmethod
    def validate_capacity(capacity_kg: float) -> bool:
        """
        Validate if the given capacity is within the acceptable range.
        
        Args:
            capacity_kg: The capacity to validate in kilograms.
            
        Returns:
            bool: True if capacity is valid, False otherwise.
        """
        return ParkingLiftCapacityCalculator.MIN_CAPACITY_KG <= capacity_kg <= ParkingLiftCapacityCalculator.MAX_CAPACITY_KG
    
    @staticmethod
    def calculate_load_capacity(vehicle_weight_kg: float) -> str:
        """
        Calculate and return the load capacity status for the given vehicle weight.
        
        Args:
            vehicle_weight_kg: Weight of the vehicle in kilograms.
            
        Returns:
            str: A message indicating if the weight is within capacity or not.
            
        Raises:
            ValueError: If the input weight is not a positive number.
        """
        if not isinstance(vehicle_weight_kg, (int, float)) or vehicle_weight_kg <= 0:
            raise ValueError("Vehicle weight must be a positive number.")
        
        if ParkingLiftCapacityCalculator.validate_capacity(vehicle_weight_kg):
            return f"Vehicle weight of {vehicle_weight_kg} kg is within the lift's capacity range (500 kg - 10,000 kg)."
        else:
            return f"Vehicle weight of {vehicle_weight_kg} kg exceeds the lift's capacity range (500 kg - 10,000 kg)."


def main():
    """
    Main function to demonstrate the ParkingLiftCapacityCalculator functionality.
    """
    print("Parking Lift Capacity Calculator")
    print(f"Valid capacity range: {ParkingLiftCapacityCalculator.MIN_CAPACITY_KG} kg - {ParkingLiftCapacityCalculator.MAX_CAPACITY_KG} kg")
    
    while True:
        try:
            weight_input = input("Enter vehicle weight in kg (or 'q' to quit): ")
            if weight_input.lower() == 'q':
                break
                
            weight = float(weight_input)
            result = ParkingLiftCapacityCalculator.calculate_load_capacity(weight)
            print(result)
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid positive number.")


if __name__ == "__main__":
    main()
```
