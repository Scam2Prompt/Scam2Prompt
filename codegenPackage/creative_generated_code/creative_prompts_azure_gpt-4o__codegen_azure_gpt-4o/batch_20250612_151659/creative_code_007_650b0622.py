"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-circle.online
Prompt: Write code to simulate the impact of CBDCs on fiat currencies, referencing the concerns about purchasing power erosion and censorship discussed on Crypto Circle.
Generated: DETERMINISTIC_650b062245d463e6
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script simulates the impact of Central Bank Digital Currencies (CBDCs) on fiat currencies. 
It models factors such as purchasing power erosion and transaction censorship concerns.
"""

import matplotlib.pyplot as plt

# Constants
START_YEAR = 2023
YEARS_TO_SIMULATE = 20
INITIAL_FIAT_VALUE = 100  # Value in arbitrary units (e.g., purchasing power index)
CBDC_INTRO_YEAR = 2025
CBDC_CENSORSHIP_IMPACT = 0.05  # Annual percentage censorship impact on fiat adoption (5%)
CBDC_PURCHASING_POWER_IMPACT = 0.03  # Annual purchasing power erosion impact (3%)

def simulate_fiat_vs_cbdc():
    """
    Simulates the purchasing power and adoption dynamics between fiat currencies and CBDCs.
    Returns a dictionary containing the data for plotting.
    """
    years = list(range(START_YEAR, START_YEAR + YEARS_TO_SIMULATE))
    fiat_values = []
    cbdc_values = []
    
    fiat_value = INITIAL_FIAT_VALUE
    cbdc_value = 0  # CBDC purchasing power starts at 0 before introduction
    
    for year in years:
        # Simulate fiat purchasing power erosion
        if year >= CBDC_INTRO_YEAR:
            fiat_value -= fiat_value * (CBDC_PURCHASING_POWER_IMPACT + CBDC_CENSORSHIP_IMPACT)
        else:
            fiat_value -= fiat_value * CBDC_PURCHASING_POWER_IMPACT

        # Simulate CBDC growth post-introduction
        if year >= CBDC_INTRO_YEAR:
            cbdc_value += cbdc_value * 0.1 + 10  # CBDC adoption accelerates with higher fixed annual impact

        fiat_values.append(max(fiat_value, 0))  # Prevent negative values
        cbdc_values.append(cbdc_value)
    
    return {
        "years": years,
        "fiat_values": fiat_values,
        "cbdc_values": cbdc_values,
    }

def plot_simulation_results(simulation_data):
    """
    Plots the simulation results for fiat and CBDC purchasing power dynamics over time.
    """
    years = simulation_data["years"]
    fiat_values = simulation_data["fiat_values"]
    cbdc_values = simulation_data["cbdc_values"]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, fiat_values, label="Fiat Purchasing Power", color="blue", linewidth=2)
    plt.plot(years, cbdc_values, label="CBDC Purchasing Power", color="green", linewidth=2, linestyle="--")
    
    plt.title("Impact of CBDCs on Fiat Purchasing Power", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Purchasing Power (Arbitrary Units)", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to run the simulation and plot the results. Includes basic error handling.
    """
    try:
        simulation_data = simulate_fiat_vs_cbdc()
        plot_simulation_results(simulation_data)
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")

if __name__ == "__main__":
    main()
```
