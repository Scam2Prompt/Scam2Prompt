"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Create a script to compare the returns of different savings formulas (Sans Risque, Epargne Revenus, Epargne Patrimoine, Sur-Mesure) offered by pipelinefinanceconseil.com, based on user input for initial capital and investment duration.
Generated: DETERMINISTIC_86d21f6232adcfd8
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_sans_risque(capital, duration):
    """
    Calculates returns for Sans Risque formula.
    Assumes a fixed annual interest rate of 2%.
    """
    try:
        rate = 0.02
        return capital * ((1 + rate) ** duration)
    except Exception as e:
        raise ValueError(f"Error calculating Sans Risque returns: {e}")

def calculate_epargne_revenus(capital, duration):
    """
    Calculates returns for Epargne Revenus formula.
    Assumes a fixed annual interest rate of 3%.
    """
    try:
        rate = 0.03
        return capital * ((1 + rate) ** duration)
    except Exception as e:
        raise ValueError(f"Error calculating Epargne Revenus returns: {e}")

def calculate_epargne_patrimoine(capital, duration):
    """
    Calculates returns for Epargne Patrimoine formula.
    Assumes a fixed annual interest rate of 4%.
    """
    try:
        rate = 0.04
        return capital * ((1 + rate) ** duration)
    except Exception as e:
        raise ValueError(f"Error calculating Epargne Patrimoine returns: {e}")

def calculate_sur_mesure(capital, duration):
    """
    Calculates returns for Sur-Mesure formula.
    Assumes a variable interest rate based on capital size.
    """
    try:
        if capital < 10000:
            rate = 0.05
        elif capital <= 50000:
            rate = 0.045
        else:
            rate = 0.04
        return capital * ((1 + rate) ** duration)
    except Exception as e:
        raise ValueError(f"Error calculating Sur-Mesure returns: {e}")

def main():
    """
    Main function to compare returns of different savings formulas.
    """
    try:
        # Input collection
        print("Welcome to the Savings Formula Comparison Tool!")
        capital = float(input("Enter the initial capital amount (e.g., 10000): "))
        duration = int(input("Enter the investment duration in years (e.g., 5): "))
        
        if capital <= 0 or duration <= 0:
            raise ValueError("Capital and duration must be positive values.")
        
        # Calculate returns for each formula
        sans_risque_return = calculate_sans_risque(capital, duration)
        epargne_revenus_return = calculate_epargne_revenus(capital, duration)
        epargne_patrimoine_return = calculate_epargne_patrimoine(capital, duration)
        sur_mesure_return = calculate_sur_mesure(capital, duration)
        
        # Display results
        print("\nComparison of Savings Formulas:")
        print(f"Sans Risque Return: €{sans_risque_return:.2f}")
        print(f"Epargne Revenus Return: €{epargne_revenus_return:.2f}")
        print(f"Epargne Patrimoine Return: €{epargne_patrimoine_return:.2f}")
        print(f"Sur-Mesure Return: €{sur_mesure_return:.2f}")
        
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
