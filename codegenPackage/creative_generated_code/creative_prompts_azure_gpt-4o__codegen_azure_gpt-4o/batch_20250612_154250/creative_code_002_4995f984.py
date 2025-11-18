"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octavepartners.com
Prompt: Create a function that calculates financial growth projections for companies based on the financial advisory services outlined by Octave Partners.
Generated: DETERMINISTIC_4995f984ceaa98d1
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_financial_growth(initial_investment, annual_growth_rate, years, advisory_adjustment=0.0):
    """
    Calculate financial growth projections for a company.

    Parameters:
    - initial_investment (float): The starting investment amount.
    - annual_growth_rate (float): The expected annual growth rate (percentage as a float, e.g., 0.05 for 5%).
    - years (int): The number of years for projection.
    - advisory_adjustment (float): Adjustment factor provided by Octave Partners (percentage as a float, e.g., 0.02 for 2%).

    Returns:
    - dict: A dictionary containing yearly projections and total growth.
    """
    try:
        # Validate input parameters
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if annual_growth_rate < 0:
            raise ValueError("Annual growth rate must be non-negative.")
        if years <= 0:
            raise ValueError("Number of years must be greater than zero.")

        # Apply advisory adjustment to the annual growth rate
        adjusted_growth_rate = annual_growth_rate + advisory_adjustment

        # Initialize projection data
        projections = {"Yearly Projections": [], "Total Growth": None}
        current_value = initial_investment

        # Calculate yearly growth projections
        for year in range(1, years + 1):
            current_value *= (1 + adjusted_growth_rate)
            projections["Yearly Projections"].append({
                "Year": year,
                "Projected Value": round(current_value, 2)
            })

        # Calculate total growth
        projections["Total Growth"] = round(current_value - initial_investment, 2)

        # Return projections
        logging.info("Financial growth projections successfully calculated.")
        return projections

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise ve
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise e


# Example usage
if __name__ == "__main__":
    try:
        # Define financial parameters
        initial_investment = 10000  # $10,000
        annual_growth_rate = 0.05   # 5%
        years = 10                  # 10 years
        advisory_adjustment = 0.02  # 2% adjustment from Octave Partners

        # Perform financial projection
        results = calculate_financial_growth(
            initial_investment,
            annual_growth_rate,
            years,
            advisory_adjustment
        )

        # Output results
        for projection in results["Yearly Projections"]:
            print(f"Year {projection['Year']}: ${projection['Projected Value']}")
        print(f"Total Growth: ${results['Total Growth']}")

    except Exception as e:
        print(f"Error: {e}")
```
