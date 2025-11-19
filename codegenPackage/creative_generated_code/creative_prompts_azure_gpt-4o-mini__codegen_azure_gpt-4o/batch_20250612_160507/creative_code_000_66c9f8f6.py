"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Write a Python script that utilizes the principles of land acquisition and development as outlined by Carolina Capital to evaluate potential real estate investments.
Generated: DETERMINISTIC_66c9f8f6cd036fa9
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to evaluate potential real estate investments using principles of land 
acquisition and development inspired by Carolina Capital. 

This script takes input on various property parameters, calculates profitability,
and provides a recommendation based on a threshold for investment viability. 
"""

import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def evaluate_investment(property_price, development_cost, estimated_resale_value, roi_threshold=0.15):
    """
    Evaluate a real estate investment given the property price, development costs,
    and estimated resale value.

    Args:
        property_price (float): The acquisition cost of the property.
        development_cost (float): The total cost of development/upgrades for the property.
        estimated_resale_value (float): The estimated price at which the property can be sold after development.
        roi_threshold (float): The minimum return on investment (ROI) required for a viable investment. Default is 15%.

    Returns:
        dict: A dictionary containing ROI, net profit, and investment recommendation.
    """
    try:
        # Calculate total costs
        total_cost = property_price + development_cost

        # Calculate net profit
        net_profit = estimated_resale_value - total_cost

        # Calculate ROI (Return on Investment)
        roi = net_profit / total_cost

        # Determine investment recommendation
        recommendation = "Viable Investment" if roi >= roi_threshold else "Not Recommended"

        # Return results
        return {
            "Total Cost": total_cost,
            "Net Profit": net_profit,
            "ROI": roi,
            "Recommendation": recommendation
        }

    except Exception as e:
        logging.error(f"Error while evaluating investment: {e}")
        return None


def main():
    """
    Main function to interact with the user and evaluate investment opportunities.
    """

    logging.info("Welcome to the Real Estate Investment Evaluator!")
    
    try:
        # Gather user inputs
        property_price = float(input("Enter the property acquisition cost ($): "))
        development_cost = float(input("Enter the development cost ($): "))
        estimated_resale_value = float(input("Enter the estimated resale value ($): "))
        roi_threshold = float(input("Enter the ROI threshold (default is 0.15 for 15%): ") or 0.15)

        # Evaluate investment
        investment_result = evaluate_investment(
            property_price,
            development_cost,
            estimated_resale_value,
            roi_threshold
        )

        if investment_result:
            # Display results
            logging.info("Investment Evaluation Complete:")
            for key, value in investment_result.items():
                logging.info(f"{key}: {value}")
        else:
            logging.error("Failed to evaluate investment.")

    except ValueError:
        logging.error("Invalid input! Please enter numeric values.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
