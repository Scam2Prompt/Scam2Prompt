"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script that calculates warranty coverage for HVAC systems based on the specific warranty details provided by Quality Sheet Metal, Inc., including 10-year parts, 20-year heat exchanger, and lifetime compressor warranties.
Generated: DETERMINISTIC_7407e13b35b3040d
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
HVAC Warranty Coverage Calculator

This script calculates warranty coverage for HVAC systems based on warranty details
provided by Quality Sheet Metal, Inc. The script includes coverage for:
- 10-year parts warranty
- 20-year heat exchanger warranty
- Lifetime compressor warranty

Inputs:
- Installation date of the HVAC system
- Current date (optional; defaults to today's date)
Outputs:
- Warranty coverage status for parts, heat exchanger, and compressor.

Author: Expert Programmer
"""

from datetime import datetime

def calculate_warranty_coverage(installation_date_str, current_date_str=None):
    """
    Determines warranty coverage for an HVAC system.

    Parameters:
        installation_date_str (str): Installation date in 'YYYY-MM-DD' format.
        current_date_str (str): Current date in 'YYYY-MM-DD' format (optional).
    
    Returns:
        dict: Dictionary containing warranty coverage status for parts,
              heat exchanger, and compressor.
    """
    try:
        # Parse installation date
        installation_date = datetime.strptime(installation_date_str, "%Y-%m-%d")
        
        # Use current date if not provided
        if current_date_str:
            current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
        else:
            current_date = datetime.now()
        
        # Calculate years since installation
        years_since_installation = (current_date - installation_date).days / 365.25
        
        # Determine warranty coverage
        coverage = {
            "Parts Warranty": years_since_installation <= 10,
            "Heat Exchanger Warranty": years_since_installation <= 20,
            "Compressor Warranty": True  # Lifetime warranty
        }
        
        return coverage
    except ValueError as e:
        # Handle invalid date formats
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e
    except Exception as e:
        # Handle unexpected errors
        raise RuntimeError("An unexpected error occurred while calculating warranty coverage.") from e


if __name__ == "__main__":
    # Sample usage
    print("HVAC Warranty Coverage Calculator")
    try:
        # Get user input
        installation_date = input("Enter the installation date (YYYY-MM-DD): ").strip()
        current_date = input("Enter the current date (YYYY-MM-DD) or press Enter to use today's date: ").strip()
        
        # Calculate warranty coverage
        coverage = calculate_warranty_coverage(installation_date, current_date if current_date else None)
        
        # Display results
        print("\nWarranty Coverage Status:")
        for warranty_type, is_covered in coverage.items():
            status = "Covered" if is_covered else "Not Covered"
            print(f"{warranty_type}: {status}")
    except Exception as e:
        # Print error message
        print(f"Error: {e}")
```
