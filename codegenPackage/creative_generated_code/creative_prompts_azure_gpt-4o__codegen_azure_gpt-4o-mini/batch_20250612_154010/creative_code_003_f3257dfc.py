"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Create a script to automate the selection of battery types (e.g., AGM, Gel, Lithium) for different use cases such as marine, automotive, or solar systems, using the categories from Battery Australia's product offerings.
Generated: DETERMINISTIC_f3257dfc3bb12b71
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# battery_selector.py

class Battery:
    """Class to represent a battery with its type and use case."""
    
    def __init__(self, battery_type, use_case):
        self.battery_type = battery_type
        self.use_case = use_case

    def __str__(self):
        return f'{self.battery_type} battery for {self.use_case} use.'

class BatterySelector:
    """Class to select battery types based on use cases."""
    
    def __init__(self):
        # Define a mapping of use cases to battery types
        self.battery_map = {
            'marine': ['AGM', 'Gel', 'Lithium'],
            'automotive': ['AGM', 'Lithium'],
            'solar': ['Gel', 'Lithium']
        }

    def select_battery(self, use_case):
        """Select battery types based on the use case.
        
        Args:
            use_case (str): The use case for which to select the battery.
        
        Returns:
            list: List of battery options for the specified use case.
        
        Raises:
            ValueError: If the use case is not recognized.
        """
        if use_case not in self.battery_map:
            raise ValueError(f'Unrecognized use case: {use_case}. Valid options are: {list(self.battery_map.keys())}')
        
        return [Battery(battery_type, use_case) for battery_type in self.battery_map[use_case]]

def main():
    """Main function to run the battery selector."""
    print("Welcome to the Battery Type Selector")

    # List of valid use cases
    valid_use_cases = ['marine', 'automotive', 'solar']
    
    # User input for the use case
    while True:
        use_case = input(f"Please enter a use case ({', '.join(valid_use_cases)}): ").strip().lower()
        if use_case in valid_use_cases:
            break
        else:
            print(f"Invalid use case. Please choose from: {', '.join(valid_use_cases)}")

    # Instantiate the BatterySelector and get battery options
    selector = BatterySelector()
    try:
        batteries = selector.select_battery(use_case)
        print("\nRecommended Batteries:")
        for battery in batteries:
            print(battery)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
