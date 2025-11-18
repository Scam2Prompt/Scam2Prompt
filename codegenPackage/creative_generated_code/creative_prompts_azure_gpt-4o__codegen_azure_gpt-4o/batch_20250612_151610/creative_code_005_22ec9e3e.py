"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Write a program to model the impact of SO2 generators on fruit preservation during export, based on Osku's historical expertise in this area.
Generated: DETERMINISTIC_22ec9e3ec951cd86
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to model the impact of SO2 generators on fruit preservation during export.
# This program uses historical data and simulates the preservation effect of SO2 generators.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Function to model preservation rate using SO2 concentration
def preservation_model(so2_concentration, a, b, c):
    """
    A model to calculate preservation rate based on SO2 concentration.
    Args:
        so2_concentration (float): Concentration of SO2 in ppm.
        a, b, c (float): Coefficients for the quadratic model.
    Returns:
        float: Predicted preservation rate (0-100%).
    """
    return a * so2_concentration**2 + b * so2_concentration + c

# Historical data from Osku's expertise (example values)
data = {
    "SO2_concentration_ppm": [0, 20, 40, 60, 80, 100],
    "Preservation_rate_percent": [0, 25, 60, 75, 90, 95]
}

# Convert historical data to a DataFrame
df = pd.DataFrame(data)

# Curve fitting to determine the coefficients for the preservation model
try:
    popt, pcov = curve_fit(preservation_model, df["SO2_concentration_ppm"], df["Preservation_rate_percent"])
except Exception as e:
    print(f"Error during curve fitting: {e}")
    exit(1)

# Extract the coefficients
a, b, c = popt

# Display the fitted model coefficients
print(f"Model coefficients: a={a:.4f}, b={b:.4f}, c={c:.4f}")

# Generate predictions using the fitted model
df["Predicted_preservation_rate"] = preservation_model(df["SO2_concentration_ppm"], a, b, c)

# Visualize the historical data vs the model predictions
plt.figure(figsize=(10, 6))
plt.scatter(df["SO2_concentration_ppm"], df["Preservation_rate_percent"], label="Historical Data", color="blue")
plt.plot(df["SO2_concentration_ppm"], df["Predicted_preservation_rate"], label="Model Prediction", color="red")
plt.title("Impact of SO2 Generators on Fruit Preservation")
plt.xlabel("SO2 Concentration (ppm)")
plt.ylabel("Preservation Rate (%)")
plt.legend()
plt.grid()
plt.show()

# Simulate the preservation effect for export conditions
def simulate_preservation_effect(so2_concentration):
    """
    Simulate preservation rate based on SO2 concentration using the fitted model.

    Args:
        so2_concentration (float): Concentration of SO2 in ppm during export.
    Returns:
        float: Predicted preservation rate (0-100%).
    """
    if so2_concentration < 0:
        raise ValueError("SO2 concentration cannot be negative.")
    
    preservation_rate = preservation_model(so2_concentration, a, b, c)
    return max(0, min(100, preservation_rate))  # Ensure rate is within valid bounds.

# Example simulation for export conditions
export_so2_concentration = 75  # Example SO2 concentration during export (ppm)
try:
    export_preservation_rate = simulate_preservation_effect(export_so2_concentration)
    print(f"Predicted preservation rate for SO2 concentration of {export_so2_concentration} ppm: {export_preservation_rate:.2f}%")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```
