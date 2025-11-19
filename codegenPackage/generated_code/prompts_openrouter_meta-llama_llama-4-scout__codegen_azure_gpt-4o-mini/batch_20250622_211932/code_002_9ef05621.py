"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Generate a Python script to calculate the total earnings for a donor based on the compensation structure of $100-$200 per donation at Orlando Plasma Centers.
Generated: DETERMINISTIC_9ef0562148b3b61c
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donor_earnings_calculator.py

def calculate_total_earnings(donations):
    """
    Calculate the total earnings for a donor based on the number of donations.
    
    Parameters:
    donations (int): The number of donations made by the donor.
    
    Returns:
    float: The total earnings calculated based on the compensation structure.
    
    Raises:
    ValueError: If the number of donations is negative.
    """
    if donations < 0:
        raise ValueError("The number of donations cannot be negative.")
    
    # Define the compensation structure
    min_compensation = 100
    max_compensation = 200
    
    # Calculate total earnings
    total_earnings = donations * ((min_compensation + max_compensation) / 2)
    
    return total_earnings

def main():
    """
    Main function to execute the earnings calculation.
    """
    try:
        # Input: Number of donations from the user
        donations = int(input("Enter the number of donations: "))
        
        # Calculate total earnings
        total_earnings = calculate_total_earnings(donations)
        
        # Output: Display the total earnings
        print(f"Total earnings for {donations} donations: ${total_earnings:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
