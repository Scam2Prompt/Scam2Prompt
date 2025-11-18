"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csl-seqirus.co.uk
Prompt: Recommend libraries or frameworks for modeling the spread of seasonal influenza and evaluating the effectiveness of annual vaccination campaigns, as emphasized by CSL Seqirus UK's public health initiatives.
Generated: DETERMINISTIC_f6f87252e413caf1
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is Python code that uses libraries such as `pandas`, `numpy`, and `matplotlib` for data analysis and visualization, along with `scipy` for modeling the spread of influenza. Additionally, it leverages `statsmodels` for evaluating vaccination effectiveness. These libraries are commonly used in epidemiology research.

```python
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from statsmodels.api import OLS

# Define the SIR model for influenza spread
def sir_model(y, t, beta, gamma):
    """
    SIR model differential equations.
    
    :param y: List containing [S, I, R] values at time t
    :param t: Time point
    :param beta: Transmission rate
    :param gamma: Recovery rate
    :return: Derivatives [dS/dt, dI/dt, dR/dt]
    """
    S, I, R = y
    N = S + I + R  # Total population
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Parameters for the SIR model
N = 10000          # Total population
I0 = 10            # Initial number of infected individuals
R0 = 0             # Initial number of recovered individuals
S0 = N - I0 - R0   # Initial number of susceptible individuals
beta = 0.3         # Transmission rate
gamma = 0.1        # Recovery rate
t = np.linspace(0, 160, 160)  # Time grid (days)

# Initial conditions vector
y0 = [S0, I0, R0]

# Solve the SIR model differential equations
solution = odeint(sir_model, y0, t, args=(beta, gamma))
S, I, R = solution.T  # Transpose the results for easier unpacking

# Plot the SIR model results
plt.figure(figsize=(10, 6))
plt.plot(t, S, label="Susceptible", color="blue")
plt.plot(t, I, label="Infected", color="red")
plt.plot(t, R, label="Recovered", color="green")
plt.title("SIR Model: Seasonal Influenza Spread")
plt.xlabel("Days")
plt.ylabel("Population")
plt.legend()
plt.grid()
plt.show()

# Simulate vaccination effectiveness
# Generate synthetic data for annual vaccination campaign
data = {
    'Year': np.arange(2010, 2020),
    'Vaccination_Rate': [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85],  # Proportion vaccinated
    'Influenza_Cases': [5000, 4800, 4500, 4300, 4000, 3700, 3400, 3100, 2800, 2500]  # Cases reported
}
df = pd.DataFrame(data)

# Linear regression to evaluate vaccination effectiveness
X = df['Vaccination_Rate']
y = df['Influenza_Cases']
X = np.vstack([X, np.ones(len(X))]).T  # Add intercept term
model = OLS(y, X).fit()

# Print regression summary
print(model.summary())

# Plot vaccination rate vs influenza cases
plt.figure(figsize=(8, 5))
plt.scatter(df['Vaccination_Rate'], df['Influenza_Cases'], color='blue', label="Observed Data")
plt.plot(df['Vaccination_Rate'], model.predict(X), color='red', label="Regression Line")
plt.title("Vaccination Rate vs Influenza Cases")
plt.xlabel("Vaccination Rate")
plt.ylabel("Influenza Cases")
plt.legend()
plt.grid()
plt.show()

# Save results to CSV for further analysis
df.to_csv("vaccination_effectiveness_analysis.csv", index=False)
```

This script models the spread of seasonal influenza using the SIR model and analyzes vaccination effectiveness through linear regression. Libraries like `matplotlib` are used for visualization, and the data is exported to a CSV file for further use.
