"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a script to calculate the total cost of temporary registration for multiple individuals in Adygea, including adjustments for minors and duration of registration, as specified on the website.
Generated: DETERMINISTIC_4fc91acc974b986a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_registration_cost(age, duration):
    """
    Calculate the registration cost based on age and duration.
    
    Args:
        age (int): Age of the individual.
        duration (int): Duration of the registration in days.
    
    Returns:
        float: Total cost of registration.
    """
    try:
        # Base cost per day
        base_cost_per_day = 50.0  # Assume 50 rubles per day
        
        # Minors (under 18) receive a 50% discount
        discount_rate = 0.5 if age < 18 else 0.0
        
        # Calculate total cost
        total_cost = duration * base_cost_per_day * (1 - discount_rate)
        return total_cost
    except Exception as e:
        print(f"Error calculating registration cost: {e}")
        sys.exit(1)

def main():
    """
    Main function to calculate the total registration cost for multiple individuals.
    """
    try:
        print("Adygea Temporary Registration Cost Calculator")
        
        # Number of individuals
        num_individuals = int(input("Enter the number of individuals: "))
        if num_individuals <= 0:
            raise ValueError("Number of individuals must be greater than zero.")
        
        total_cost = 0.0
        
        for i in range(1, num_individuals + 1):
            print(f"\nIndividual {i}")
            
            # Input age
            age = int(input("Enter age: "))
            if age < 0:
                raise ValueError("Age must be a non-negative integer.")
            
            # Input duration of registration
            duration = int(input("Enter duration of registration (in days): "))
            if duration <= 0:
                raise ValueError("Duration must be greater than zero.")
            
            # Calculate cost for this individual
            individual_cost = calculate_registration_cost(age, duration)
            print(f"Cost for Individual {i}: {individual_cost:.2f} rubles")
            total_cost += individual_cost
        
        # Display total cost for all individuals
        print(f"\nTotal cost for {num_individuals} individuals: {total_cost:.2f} rubles")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
