"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curve.markets
Prompt: Provide an example of using NumPy or SciPy to fit a curve to historical market price data.
Generated: DETERMINISTIC_154609c8fd4c1b24
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Sample historical market price data (time in days, price in USD)
# Replace with real historical data as needed
days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
prices = np.array([100, 102, 105, 107, 110, 115, 120, 125, 130, 135])

# Define a function for the curve we want to fit
# In this case, we use a linear function: y = mx + b
def linear_model(x, m, b):
    """Linear model for curve fitting."""
    return m * x + b

# Attempt to fit the curve to the data
try:
    # Use curve_fit to find optimal parameters (m and b)
    params, covariance = curve_fit(linear_model, days, prices)
except Exception as e:
    print(f"Error during curve fitting: {e}")
    raise

# Extract parameters
m, b = params

# Generate fitted values for plotting
fitted_prices = linear_model(days, m, b)

# Plotting the historical data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(days, prices, color='blue', label='Historical Prices', marker='o')
plt.plot(days, fitted_prices, color='red', label='Fitted Curve', linewidth=2)
plt.title('Market Price Curve Fitting')
plt.xlabel('Days')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

# Print the parameters of the fitted model
print(f"Fitted parameters: m = {m:.2f}, b = {b:.2f}")
```
