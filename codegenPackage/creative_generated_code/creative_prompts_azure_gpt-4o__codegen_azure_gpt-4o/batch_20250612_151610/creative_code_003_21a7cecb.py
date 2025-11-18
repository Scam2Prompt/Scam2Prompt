"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Create a script to calculate optimal packaging configurations for fruit export, taking into account Osku's emphasis on protecting fruit condition during transit.
Generated: DETERMINISTIC_21a7cecb6295d73f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for calculating optimal packaging configurations for fruit export.
The script ensures the optimal number of fruits per package while prioritizing fruit protection during transit.
"""

import math

class PackagingOptimizer:
    def __init__(self, fruit_type, fruit_weight, max_package_weight, max_package_volume, fruit_volume):
        """
        Initialize PackagingOptimizer with parameters.

        :param fruit_type: Type of fruit (e.g., "apple", "orange")
        :param fruit_weight: Weight of one fruit (in grams)
        :param max_package_weight: Maximum allowable package weight (in grams)
        :param max_package_volume: Maximum allowable package volume (in cubic centimeters)
        :param fruit_volume: Volume of one fruit (in cubic centimeters)
        """
        self.fruit_type = fruit_type
        self.fruit_weight = fruit_weight
        self.max_package_weight = max_package_weight
        self.max_package_volume = max_package_volume
        self.fruit_volume = fruit_volume

    def calculate_optimal_config(self):
        """
        Calculate the optimal number of fruits per package based on weight and volume constraints.

        :return: Dictionary containing the optimal configuration details.
        """
        try:
            # Calculate maximum fruits by weight constraint
            max_by_weight = self.max_package_weight // self.fruit_weight
            
            # Calculate maximum fruits by volume constraint
            max_by_volume = self.max_package_volume // self.fruit_volume
            
            # Optimal number of fruits per package (smallest of the two constraints)
            optimal_count = min(max_by_weight, max_by_volume)
            
            # Calculate total weight and volume of optimal package
            total_weight = optimal_count * self.fruit_weight
            total_volume = optimal_count * self.fruit_volume
            
            return {
                "fruit_type": self.fruit_type,
                "optimal_fruit_count": optimal_count,
                "total_weight": total_weight,
                "total_volume": total_volume,
                "max_package_weight": self.max_package_weight,
                "max_package_volume": self.max_package_volume
            }
        except Exception as e:
            # Handle unexpected errors
            print(f"Error calculating optimal configuration: {e}")
            return None

def main():
    """
    Main function to run the PackagingOptimizer script.
    """
    try:
        # Input parameters
        fruit_type = "apple"
        fruit_weight = 150  # in grams
        max_package_weight = 5000  # in grams
        max_package_volume = 20000  # in cubic centimeters
        fruit_volume = 500  # in cubic centimeters
        
        # Create PackagingOptimizer instance
        optimizer = PackagingOptimizer(fruit_type, fruit_weight, max_package_weight, max_package_volume, fruit_volume)
        
        # Calculate optimal packaging configuration
        result = optimizer.calculate_optimal_config()
        
        # Display the result
        if result:
            print("Optimal Packaging Configuration:")
            for key, value in result.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Failed to calculate optimal packaging configuration.")
    except Exception as e:
        # Handle unexpected errors in the main function
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
```
