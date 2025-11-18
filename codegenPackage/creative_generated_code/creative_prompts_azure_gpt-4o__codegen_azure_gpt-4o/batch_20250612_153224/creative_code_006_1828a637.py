"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Develop an algorithm to estimate the risk reduction in fatalities when fire sprinklers are installed, using the 80% decrease statistic mentioned by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_1828a63754208300
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def estimate_risk_reduction(total_fatalities_without_sprinklers, sprinklers_effectiveness=0.80):
    """
    Estimate the reduction in fatalities when fire sprinklers are installed.

    Parameters:
        total_fatalities_without_sprinklers (int): The number of fatalities occurring in the absence of sprinklers.
        sprinklers_effectiveness (float): The effectiveness of sprinklers in reducing fatalities, default is 80% (0.80).

    Returns:
        dict: A dictionary containing the risk reduction estimate and the remaining fatalities.
    """
    try:
        # Validate input
        if total_fatalities_without_sprinklers < 0:
            raise ValueError("Total fatalities cannot be negative.")
        if not (0 <= sprinklers_effectiveness <= 1):
            raise ValueError("Sprinkler effectiveness must be between 0 and 1.")

        # Calculate reduction in fatalities
        fatalities_reduced = total_fatalities_without_sprinklers * sprinklers_effectiveness

        # Calculate remaining fatalities
        remaining_fatalities = total_fatalities_without_sprinklers - fatalities_reduced

        # Return results
        return {
            "fatalities_reduced": round(fatalities_reduced),
            "remaining_fatalities": round(remaining_fatalities)
        }

    except ValueError as ve:
        # Handle value errors (e.g., invalid inputs)
        return {"error": str(ve)}
    except Exception as e:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

if __name__ == "__main__":
    # Example usage
    try:
        # Get input from the user
        total_fatalities_without_sprinklers = int(input("Enter total fatalities without sprinklers: "))
        sprinklers_effectiveness = 0.80  # Default effectiveness (80%)

        # Estimate risk reduction
        result = estimate_risk_reduction(total_fatalities_without_sprinklers, sprinklers_effectiveness)

        # Output result
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Estimated reduction in fatalities: {result['fatalities_reduced']}")
            print(f"Remaining fatalities: {result['remaining_fatalities']}")

    except KeyboardInterrupt:
        print("\nOperation aborted by user.")
        sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a valid integer for total fatalities.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
