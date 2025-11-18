"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soneium-crypto-price20250217.pages.dev
Prompt: Create a program that calculates the risk factors for investing in Soneium based on parameters like liquidity, token distribution, and TVL composition.
Generated: DETERMINISTIC_413176fcf179637f
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Risk Factor Calculator for Soneium Investments

This program calculates risk factors for investing in Soneium based on three key parameters:
1. Liquidity
2. Token Distribution
3. Total Value Locked (TVL) Composition

The program assigns weights to each parameter, calculates a composite risk score, and categorizes
the investment risk level as Low, Medium, or High.

Author: Expert Programmer
Date: October 2023
"""

# Import necessary modules
import sys

def calculate_risk_factor(liquidity, token_distribution, tvl_composition):
    """
    Calculates the risk factor based on provided parameters.
    
    Parameters:
        liquidity (float): Measure of liquidity (0-100 scale, higher is better liquidity).
        token_distribution (float): Measure of token distribution fairness (0-100 scale, higher is better distribution).
        tvl_composition (float): Measure of TVL composition (0-100 scale, higher implies better composition).
    
    Returns:
        dict: Contains the calculated composite risk score and risk level.
    """
    # Validate inputs
    if not (0 <= liquidity <= 100):
        raise ValueError("Liquidity must be between 0 and 100.")
    if not (0 <= token_distribution <= 100):
        raise ValueError("Token distribution must be between 0 and 100.")
    if not (0 <= tvl_composition <= 100):
        raise ValueError("TVL composition must be between 0 and 100.")
    
    # Define weights for the parameters (adjustable based on domain knowledge)
    liquidity_weight = 0.4
    token_distribution_weight = 0.3
    tvl_composition_weight = 0.3
    
    # Calculate composite risk score (lower is better for risk)
    composite_score = (
        (100 - liquidity) * liquidity_weight +
        (100 - token_distribution) * token_distribution_weight +
        (100 - tvl_composition) * tvl_composition_weight
    )
    
    # Determine risk level based on composite score
    if composite_score <= 30:
        risk_level = "Low"
    elif 30 < composite_score <= 60:
        risk_level = "Medium"
    else:
        risk_level = "High"
    
    # Return results
    return {
        "composite_score": round(composite_score, 2),
        "risk_level": risk_level
    }


def main():
    """
    Entry point for the program. Accepts user input and calculates risk factors.
    """
    try:
        # Prompt user for inputs
        print("Welcome to the Soneium Risk Factor Calculator.")
        liquidity = float(input("Enter Liquidity (0-100 scale): "))
        token_distribution = float(input("Enter Token Distribution (0-100 scale): "))
        tvl_composition = float(input("Enter TVL Composition (0-100 scale): "))
        
        # Calculate risk factors
        result = calculate_risk_factor(liquidity, token_distribution, tvl_composition)
        
        # Display results
        print("\nRisk Factor Calculation Results:")
        print(f"Composite Risk Score: {result['composite_score']}")
        print(f"Risk Level: {result['risk_level']}")
        
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
