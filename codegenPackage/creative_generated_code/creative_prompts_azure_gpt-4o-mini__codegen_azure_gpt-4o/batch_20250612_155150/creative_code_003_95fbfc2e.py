"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Generate a Python script that calculates the performance improvement after cleaning fuel injectors based on contamination levels.
Generated: DETERMINISTIC_95fbfc2e513f1f06
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_performance_improvement(contamination_level):
    """
    Calculate the performance improvement based on the contamination level.
    
    Parameters:
        contamination_level (float): The percentage of contamination in the fuel injectors (0-100).
        
    Returns:
        float: The estimated performance improvement percentage.
    """
    if not (0 <= contamination_level <= 100):
        raise ValueError("Contamination level must be between 0 and 100.")
    
    # Basic formula for improvement: higher contamination leads to higher improvement after cleaning.
    # Assume a linear relation: improvement = 0.8 * contamination level.
    improvement = 0.8 * contamination_level
    return improvement

def get_user_input():
    """
    Prompt the user for contamination level input.
    
    Returns:
        float: The validated contamination level entered by the user.
    """
    try:
        user_input = input("Enter the contamination level of the fuel injectors (0-100): ").strip()
        contamination_level = float(user_input)
        if not (0 <= contamination_level <= 100):
            raise ValueError
        return contamination_level
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100.", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to calculate and display performance improvement.
    """
    print("Fuel Injector Performance Improvement Calculator")
    
    try:
        # Get contamination level from user.
        contamination_level = get_user_input()
        
        # Calculate performance improvement.
        improvement = calculate_performance_improvement(contamination_level)
        
        # Display the result.
        print(f"Estimated performance improvement after cleaning: {improvement:.2f}%")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
