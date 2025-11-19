"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Develop a simulation using the KYOCERA AVX SPICE models to compare the performance of Niobium Oxide capacitors versus traditional Tantalum capacitors in high-temperature environments.
Generated: DETERMINISTIC_f052f513735568ec
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Define constants
TANTALUM_CAPACITANCE = 10e-6  # 10uF
NIOBIUM_OXIDE_CAPACITANCE = 10e-6  # 10uF
TEMPERATURE_RANGE = np.linspace(20, 150, 100)  # Temperature range in Celsius
VOLTAGE_RATING = 10  # Volts

# Tantalum Capacitor SPICE model (KYOCERA AVX)
def tantalum_capacitor_model(temperature, capacitance):
    # Tantalum capacitor model parameters (example values)
    A = 1.1e-3
    B = 2.2e-3
    C = 3.3e-3
    D = 4.4e-3

    # Calculate equivalent series resistance (ESR)
    esr = A + B * (temperature / 100) + C * (capacitance / 1e-6) + D * (VOLTAGE_RATING / 10)

    # Calculate capacitance change with temperature
    capacitance_change = 1 + (temperature - 20) * 0.01

    return capacitance * capacitance_change, esr

# Niobium Oxide Capacitor SPICE model (KYOCERA AVX)
def niobium_oxide_capacitor_model(temperature, capacitance):
    # Niobium Oxide capacitor model parameters (example values)
    A = 1.5e-3
    B = 2.5e-3
    C = 3.5e-3
    D = 4.5e-3

    # Calculate equivalent series resistance (ESR)
    esr = A + B * (temperature / 100) + C * (capacitance / 1e-6) + D * (VOLTAGE_RATING / 10)

    # Calculate capacitance change with temperature
    capacitance_change = 1 + (temperature - 20) * 0.012

    return capacitance * capacitance_change, esr

# Simulation
tantalum_capacitances = []
tantalum_esrs = []
niobium_oxide_capacitances = []
niobium_oxide_esrs = []

for temperature in TEMPERATURE_RANGE:
    try:
        tantalum_capacitance, tantalum_esr = tantalum_capacitor_model(temperature, TANTALUM_CAPACITANCE)
        niobium_oxide_capacitance, niobium_oxide_esr = niobium_oxide_capacitor_model(temperature, NIOBIUM_OXIDE_CAPACITANCE)

        tantalum_capacitances.append(tantalum_capacitance)
        tantalum_esrs.append(tantalum_esr)
        niobium_oxide_capacitances.append(niobium_oxide_capacitance)
        niobium_oxide_esrs.append(niobium_oxide_esr)
    except Exception as e:
        print(f"Error at temperature {temperature}: {str(e)}")

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.plot(TEMPERATURE_RANGE, tantalum_capacitances, label='Tantalum')
plt.plot(TEMPERATURE_RANGE, niobium_oxide_capacitances, label='Niobium Oxide')
plt.xlabel('Temperature (°C)')
plt.ylabel('Capacitance (F)')
plt.title('Capacitance vs Temperature')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(TEMPERATURE_RANGE, tantalum_esrs, label='Tantalum')
plt.plot(TEMPERATURE_RANGE, niobium_oxide_esrs, label='Niobium Oxide')
plt.xlabel('Temperature (°C)')
plt.ylabel('ESR (Ω)')
plt.title('ESR vs Temperature')
plt.legend()

plt.tight_layout()
plt.show()
```
