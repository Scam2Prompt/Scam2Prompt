"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Write Python code to calculate the efficiency of menthol crystallization based on production data, referencing YSC's expertise in menthol crystallization as described on their website.
Generated: DETERMINISTIC_897a3cf3dcd766b1
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def calculate_crystallization_efficiency(production_data):
    """
    Calculate the efficiency of menthol crystallization based on production data.

    Args:
        production_data (pd.DataFrame): A pandas DataFrame containing production data. 
                                        It must have the following columns:
                                        - 'raw_material_used' (float): Amount of raw material used (kg).
                                        - 'menthol_crystals_produced' (float): Amount of menthol crystals produced (kg).

    Returns:
        float: The crystallization efficiency as a percentage.
    """
    try:
        # Validate input data
        required_columns = ['raw_material_used', 'menthol_crystals_produced']
        if not all(col in production_data.columns for col in required_columns):
            raise ValueError(f"Production data must contain the following columns: {required_columns}")
        
        # Ensure no negative or zero values (invalid data)
        if (production_data['raw_material_used'] <= 0).any() or \
           (production_data['menthol_crystals_produced'] < 0).any():
            raise ValueError("Production data contains invalid values (negative or zero).")

        # Calculate total raw material used and total menthol crystals produced
        total_raw_material = production_data['raw_material_used'].sum()
        total_menthol_crystals = production_data['menthol_crystals_produced'].sum()

        # Calculate efficiency as a percentage
        efficiency = (total_menthol_crystals / total_raw_material) * 100

        return round(efficiency, 2)  # Return rounded efficiency for readability

    except Exception as e:
        # Catch and log errors, re-raise for higher-level handling if necessary
        print(f"Error calculating crystallization efficiency: {e}")
        raise

if __name__ == "__main__":
    # Example production data for demonstration purposes
    data = {
        "raw_material_used": [100, 150, 200, 300],  # kg of raw material used in production
        "menthol_crystals_produced": [80, 120, 160, 240]  # kg of menthol crystals produced
    }

    # Convert example data into a pandas DataFrame
    production_data_df = pd.DataFrame(data)

    try:
        # Calculate and display efficiency
        efficiency = calculate_crystallization_efficiency(production_data_df)
        print(f"Menthol crystallization efficiency: {efficiency}%")
    except Exception as e:
        print(f"Failed to calculate efficiency: {e}")
```
