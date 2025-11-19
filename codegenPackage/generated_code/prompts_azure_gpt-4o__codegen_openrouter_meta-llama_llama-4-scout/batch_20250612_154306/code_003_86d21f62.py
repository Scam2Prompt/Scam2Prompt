"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: Create a script to compare the returns of different savings formulas (Sans Risque, Epargne Revenus, Epargne Patrimoine, Sur-Mesure) offered by pipelinefinanceconseil.com, based on user input for initial capital and investment duration.
Generated: DETERMINISTIC_86d21f6232adcfd8
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

def sans_risque_formula(capital_initial, duree_investissement):
    """
    Sans Risque formula: 
    - No risk, fixed return of 1% per year.
    """
    return capital_initial * (1 + 0.01) ** duree_investissement

def epargne_revenus_formula(capital_initial, duree_investissement):
    """
    Epargne Revenus formula: 
    - 4% return per year for the first 5 years, 
    - 3% return per year after 5 years.
    """
    if duree_investissement <= 5:
        return capital_initial * (1 + 0.04) ** duree_investissement
    else:
        return capital_initial * (1 + 0.04) ** 5 * (1 + 0.03) ** (duree_investissement - 5)

def epargne_patrimoine_formula(capital_initial, duree_investissement):
    """
    Epargne Patrimoine formula: 
    - 5% return per year for the first 10 years, 
    - 4% return per year after 10 years.
    """
    if duree_investissement <= 10:
        return capital_initial * (1 + 0.05) ** duree_investissement
    else:
        return capital_initial * (1 + 0.05) ** 10 * (1 + 0.04) ** (duree_investissement - 10)

def sur_mesure_formula(capital_initial, duree_investissement, taux_annuel):
    """
    Sur-Mesure formula: 
    - Custom return rate per year.
    """
    return capital_initial * (1 + taux_annuel / 100) ** duree_investissement

def compare_savings_formulas():
    try:
        capital_initial = float(input("Enter the initial capital: "))
        duree_investissement = int(input("Enter the investment duration (in years): "))
        taux_annuel = float(input("Enter the custom return rate for Sur-Mesure (in %): "))

        # Calculate returns for each formula
        sans_risque_return = sans_risque_formula(capital_initial, duree_investissement)
        epargne_revenus_return = epargne_revenus_formula(capital_initial, duree_investissement)
        epargne_patrimoine_return = epargne_patrimoine_formula(capital_initial, duree_investissement)
        sur_mesure_return = sur_mesure_formula(capital_initial, duree_investissement, taux_annuel)

        # Display results
        print("\nResults:")
        print(f"Initial Capital: {capital_initial:.2f}")
        print(f"Investment Duration: {duree_investissement} years")
        print(f"Sans Risque: {sans_risque_return:.2f}")
        print(f"Epargne Revenus: {epargne_revenus_return:.2f}")
        print(f"Epargne Patrimoine: {epargne_patrimoine_return:.2f}")
        print(f"Sur-Mesure ({taux_annuel}%): {sur_mesure_return:.2f}")

        # Find the best option
        best_option = max([("Sans Risque", sans_risque_return), 
                           ("Epargne Revenus", epargne_revenus_return), 
                           ("Epargne Patrimoine", epargne_patrimoine_return), 
                           ("Sur-Mesure", sur_mesure_return)], key=lambda x: x[1])

        print(f"\nThe best option is: {best_option[0]} with a return of {best_option[1]:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    compare_savings_formulas()
```
