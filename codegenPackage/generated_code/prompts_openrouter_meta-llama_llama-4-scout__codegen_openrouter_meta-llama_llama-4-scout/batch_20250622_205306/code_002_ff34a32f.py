"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Recommend a suitable Niobium Oxide Capacitor for an automotive application, considering factors such as temperature range, ESR, and CV, based on the KYOCERA AVX product catalog.
Generated: DETERMINISTIC_ff34a32ff647186f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

# Define the KYOCERA AVX Niobium Oxide Capacitor product catalog
niobium_oxide_capacitors = {
    "part_number": ["NOJ", "NOC", "NOS"],
    "temperature_range": [-55, 125],
    "ESR": [0.1, 0.2, 0.5],
    "CV": [10, 22, 47]
}

# Create a DataFrame from the catalog
catalog_df = pd.DataFrame({
    "Part Number": ["NOJ106M", "NOC226M", "NOS476M"],
    "Temperature Range (°C)": [-55, -55, -55],
    "Max Temperature (°C)": [125, 125, 125],
    "ESR (Ω)": [0.1, 0.2, 0.5],
    "CV (μF*V)": [10, 22, 47]
})

def recommend_capacitor(application_temperature_range, max_ESR, min_CV):
    """
    Recommend a suitable Niobium Oxide Capacitor based on the application requirements.

    Parameters:
    application_temperature_range (list): [min_temperature, max_temperature]
    max_ESR (float): Maximum Equivalent Series Resistance
    min_CV (float): Minimum Capacitance-Voltage product

    Returns:
    recommended_capacitor (dict): Recommended capacitor details
    """
    try:
        # Filter capacitors based on temperature range
        temperature_filtered_df = catalog_df[
            (catalog_df["Temperature Range (°C)"] <= application_temperature_range[0]) &
            (catalog_df["Max Temperature (°C)"] >= application_temperature_range[1])
        ]

        # Filter capacitors based on ESR and CV
        recommended_capacitors = temperature_filtered_df[
            (temperature_filtered_df["ESR (Ω)"] <= max_ESR) &
            (temperature_filtered_df["CV (μF*V)"] >= min_CV)
        ]

        if recommended_capacitors.empty:
            return None

        # Select the capacitor with the highest CV
        recommended_capacitor = recommended_capacitors.loc[recommended_capacitors["CV (μF*V)"].idxmax()]

        return recommended_capacitor.to_dict()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
application_temperature_range = [-40, 100]
max_ESR = 0.3
min_CV = 20

recommended_capacitor = recommend_capacitor(application_temperature_range, max_ESR, min_CV)

if recommended_capacitor:
    print("Recommended Capacitor:")
    for key, value in recommended_capacitor.items():
        print(f"{key}: {value}")
else:
    print("No suitable capacitor found.")
```
