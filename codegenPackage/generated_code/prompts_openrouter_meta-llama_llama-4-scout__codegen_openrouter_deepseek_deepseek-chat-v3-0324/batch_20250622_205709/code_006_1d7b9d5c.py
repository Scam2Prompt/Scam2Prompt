"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Write a script to calculate the cost of a DJ event based on the duration and type of package chosen (e.g., "Party" Package for $250), including any add-ons for video, lighting, or karaoke.
Generated: DETERMINISTIC_1d7b9d5cbc199e78
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DJEventCalculator:
    """
    A class to calculate the cost of a DJ event based on package type, duration, and add-ons.
    """
    
    def __init__(self):
        # Define available packages and their base prices
        self.packages = {
            "Party": 250,
            "Premium": 400,
            "Platinum": 600
        }
        
        # Define available add-ons and their prices
        self.add_ons = {
            "video": 100,
            "lighting": 75,
            "karaoke": 50
        }
        
        # Minimum and maximum duration in hours
        self.min_duration = 1
        self.max_duration = 8
    
    def calculate_cost(self, package_type: str, duration: int, add_ons_list: list = None) -> float:
        """
        Calculate the total cost of a DJ event.
        
        Args:
            package_type (str): The type of package selected (Party, Premium, Platinum)
            duration (int): Duration of the event in hours
            add_ons_list (list): List of add-ons selected (video, lighting, karaoke)
            
        Returns:
            float: Total cost of the event
            
        Raises:
            ValueError: If invalid package type or duration is provided
        """
        if package_type not in self.packages:
            raise ValueError(f"Invalid package type. Available packages: {list(self.packages.keys())}")
        
        if not (self.min_duration <= duration <= self.max_duration):
            raise ValueError(f"Duration must be between {self.min_duration} and {self.max_duration} hours")
        
        # Calculate base cost
        base_cost = self.packages[package_type] * duration
        
        # Calculate add-ons cost
        add_ons_cost = 0
        if add_ons_list:
            for add_on in add_ons_list:
                if add_on in self.add_ons:
                    add_ons_cost += self.add_ons[add_on]
                else:
                    raise ValueError(f"Invalid add-on: {add_on}. Available add-ons: {list(self.add_ons.keys())}")
        
        total_cost = base_cost + add_ons_cost
        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = DJEventCalculator()
    
    try:
        package = "Premium"
        duration = 3
        add_ons = ["video", "lighting"]
        
        total = calculator.calculate_cost(package, duration, add_ons)
        print(f"Total cost for {package} package ({duration} hours) with add-ons {add_ons}: ${total}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
