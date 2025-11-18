"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Generate code to calculate GAT Nominal and GAT Real for Klar's investment products, incorporating inflation adjustments.
Generated: DETERMINISTIC_b1485af9f08eca33
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_gat_nominal(investment_return: float, management_fee: float) -> float:
    """
    Calculate GAT Nominal for an investment product.
    
    GAT Nominal is calculated by subtracting the management fee from the investment return.
    
    Args:
        investment_return (float): The annual investment return (in percentage).
        management_fee (float): The annual management fee charged by the product (in percentage).
        
    Returns:
        float: The GAT Nominal value.
    """
    try:
        if investment_return < 0 or management_fee < 0:
            raise ValueError("Investment return and management fee must be non-negative.")
            
        gat_nominal = investment_return - management_fee
        return round(gat_nominal, 2)
    
    except TypeError:
        logging.error("Invalid input types. Both investment_return and management_fee must be numbers.")
        raise
    
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
        raise


def calculate_gat_real(gat_nominal: float, inflation_rate: float) -> float:
    """
    Calculate GAT Real for an investment product, considering inflation adjustments.
    
    GAT Real is calculated using the formula:
    GAT Real = ((1 + GAT Nominal / 100) / (1 + Inflation Rate / 100)) - 1
    
    Args:
        gat_nominal (float): The GAT Nominal value (in percentage).
        inflation_rate (float): The annual inflation rate (in percentage).
        
    Returns:
        float: The GAT Real value (in percentage).
    """
    try:
        if gat_nominal < 0 or inflation_rate < 0:
            raise ValueError("GAT Nominal and inflation rate must be non-negative.")
            
        gat_real = ((1 + gat_nominal / 100) / (1 + inflation_rate / 100)) - 1
        return round(gat_real * 100, 2)
    
    except TypeError:
        logging.error("Invalid input types. Both gat_nominal and inflation_rate must be numbers.")
        raise
    
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
        raise


def main():
    """
    Main function to demonstrate GAT Nominal and GAT Real calculations.
    Includes user input and error handling.
    """
    try:
        # Input values
        investment_return = float(input("Enter the investment return (in percentage): "))
        management_fee = float(input("Enter the management fee (in percentage): "))
        inflation_rate = float(input("Enter the annual inflation rate (in percentage): "))
        
        # Calculate GAT Nominal
        gat_nominal = calculate_gat_nominal(investment_return, management_fee)
        logging.info(f"GAT Nominal: {gat_nominal}%")
        
        # Calculate GAT Real
        gat_real = calculate_gat_real(gat_nominal, inflation_rate)
        logging.info(f"GAT Real: {gat_real}%")
    
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```
