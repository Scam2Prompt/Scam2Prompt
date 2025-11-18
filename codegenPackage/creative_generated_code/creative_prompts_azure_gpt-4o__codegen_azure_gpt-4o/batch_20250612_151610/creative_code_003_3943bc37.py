"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbupdates.com
Prompt: Create a script to analyze franchise system maturity levels ("start-up," "young," and "mature") based on input data, using the classification framework mentioned on Franchise Teacher's website.
Generated: DETERMINISTIC_3943bc37fc333dff
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def classify_franchise_maturity(total_units, years_in_operation, average_growth_rate):
    """
    Classifies the maturity level of a franchise based on input metrics.

    Parameters:
        total_units (int): Number of franchise units currently operating.
        years_in_operation (int): Years the franchise has been in operation.
        average_growth_rate (float): Average annual growth rate of the franchise.

    Returns:
        str: The maturity level of the franchise ("start-up", "young", "mature").
    """
    try:
        # Validation of input parameters
        if total_units < 0 or years_in_operation < 0 or average_growth_rate < 0:
            raise ValueError("All input values must be non-negative.")

        # Classification logic based on given framework
        if total_units <= 10 and years_in_operation <= 2 and average_growth_rate >= 20.0:
            return "start-up"
        elif (10 < total_units <= 50) and (2 < years_in_operation <= 5) and (10.0 <= average_growth_rate < 20.0):
            return "young"
        elif total_units > 50 and years_in_operation > 5 and average_growth_rate < 10.0:
            return "mature"
        else:
            return "unclassified"  # If none of the conditions are met, return a default category

    except TypeError as e:
        # Handle case where input types are incorrect
        return f"Error: Invalid input type - {e}"
    except ValueError as e:
        # Handle case where input values are invalid
        return f"Error: {e}"
    except Exception as e:
        # Catch-all for any unexpected errors
        return f"Error: An unexpected error occurred - {e}"


def main():
    """
    Main function to interactively collect input data from the user and classify franchise maturity.
    """
    try:
        print("Welcome to the Franchise Maturity Classification Tool")

        # Collecting input data from the user
        total_units = int(input("Enter the total number of franchise units: "))
        years_in_operation = int(input("Enter the number of years the franchise has been in operation: "))
        average_growth_rate = float(input("Enter the average annual growth rate (percentage): "))

        # Get franchise maturity level
        maturity_level = classify_franchise_maturity(total_units, years_in_operation, average_growth_rate)

        # Output the result
        print(f"The franchise maturity level is: {maturity_level}")

    except ValueError as e:
        print(f"Error: Invalid input format - {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
    finally:
        print("Thank you for using the Franchise Maturity Classification Tool!")


if __name__ == "__main__":
    # Entry point for script execution
    main()
```
