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
import sys

# Define battery types and their use cases
BATTERY_TYPES = {
    "AGM": ["Marine", "Automotive", "Solar"],
    "Gel": ["Marine", "Solar"],
    "Lithium": ["Automotive", "Solar"]
}

def get_battery_type_for_use_case(use_case):
    """
    Function to get suitable battery types for a given use case.
    
    Parameters:
        use_case (str): The use case (e.g., Marine, Automotive, Solar).

    Returns:
        list: A list of battery types suitable for the specified use case.
    """
    if not isinstance(use_case, str) or not use_case:
        raise ValueError("Use case must be a non-empty string.")
    
    # Filter battery types that match the use case
    suitable_batteries = [
        battery for battery, use_cases in BATTERY_TYPES.items() if use_case in use_cases
    ]
    
    return suitable_batteries


def main():
    """
    Main function to interact with the user and automate battery selection.
    """
    print("Welcome to Battery Selector!")
    print("Available use cases: Marine, Automotive, Solar")
    print("Available battery types: AGM, Gel, Lithium")
    
    try:
        # Get user input for use case
        use_case = input("Enter the use case for the battery (e.g., Marine, Automotive, Solar): ").strip()
        
        # Validate user input
        if not use_case:
            raise ValueError("Use case cannot be empty.")
        
        # Fetch suitable battery types
        suitable_batteries = get_battery_type_for_use_case(use_case)
        
        if suitable_batteries:
            print(f"Suitable battery types for '{use_case}': {', '.join(suitable_batteries)}")
        else:
            print(f"No suitable battery types found for '{use_case}'. Please check your input.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    finally:
        print("Thank you for using Battery Selector. Goodbye!")
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user. Exiting...")
        sys.exit(0)
```
