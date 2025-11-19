"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: "Generate a comparison table of QS150, QS200, and QS250 pumps, including their specifications and applications."
Generated: DETERMINISTIC_641dc77874bbab2f
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List

def generate_pump_comparison_table() -> pd.DataFrame:
    """
    Generates a comparison table of QS150, QS200, and QS250 pumps with specifications and applications.
    
    Returns:
        pd.DataFrame: A DataFrame containing the comparison data.
    """
    # Define pump specifications and applications
    pump_data: Dict[str, Dict[str, str]] = {
        "QS150": {
            "Flow Rate (m³/h)": "50",
            "Head (m)": "150",
            "Power (kW)": "15",
            "Efficiency (%)": "75",
            "Max Pressure (bar)": "10",
            "Inlet Size (mm)": "100",
            "Outlet Size (mm)": "80",
            "Applications": "Industrial water supply, irrigation, firefighting"
        },
        "QS200": {
            "Flow Rate (m³/h)": "80",
            "Head (m)": "200",
            "Power (kW)": "22",
            "Efficiency (%)": "78",
            "Max Pressure (bar)": "12",
            "Inlet Size (mm)": "125",
            "Outlet Size (mm)": "100",
            "Applications": "High-pressure water supply, mining, large-scale irrigation"
        },
        "QS250": {
            "Flow Rate (m³/h)": "120",
            "Head (m)": "250",
            "Power (kW)": "30",
            "Efficiency (%)": "80",
            "Max Pressure (bar)": "15",
            "Inlet Size (mm)": "150",
            "Outlet Size (mm)": "125",
            "Applications": "Heavy-duty industrial, oil & gas, large-scale water transfer"
        }
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(pump_data, orient='index')

    # Ensure columns are ordered consistently
    column_order: List[str] = [
        "Flow Rate (m³/h)",
        "Head (m)",
        "Power (kW)",
        "Efficiency (%)",
        "Max Pressure (bar)",
        "Inlet Size (mm)",
        "Outlet Size (mm)",
        "Applications"
    ]
    df = df[column_order]

    return df

if __name__ == "__main__":
    try:
        # Generate and display the comparison table
        comparison_table = generate_pump_comparison_table()
        print("Pump Comparison Table:")
        print(comparison_table)
    except Exception as e:
        print(f"An error occurred while generating the comparison table: {e}")
```
