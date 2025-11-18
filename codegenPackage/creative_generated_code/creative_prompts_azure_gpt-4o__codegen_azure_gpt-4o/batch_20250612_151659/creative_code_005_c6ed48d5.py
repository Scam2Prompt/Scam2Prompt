"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groundcell.uk.com
Prompt: Develop a script to compare the effectiveness of Groundcell's honeycomb design against other soil stabilization systems for protecting tree roots under driveways, referencing the product specifications.
Generated: DETERMINISTIC_c6ed48d57ab96f68
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
Script to compare the effectiveness of Groundcell's honeycomb design against other soil stabilization systems
for protecting tree roots under driveways. The comparison is based on a predefined product specification dataset.

Requirements:
- Product specifications should be loaded from a file/database (mocked as static data here for simplicity).
- Comparison metrics include compression strength, water permeability, and environmental impact.
- Generate a summary table showing the performance of each system.
"""

import pandas as pd


def load_product_data():
    """
    Load product specifications for different soil stabilization systems.
    In a production environment, this could be replaced by a database query or API call.
    
    Returns:
        pd.DataFrame: DataFrame containing product specifications.
    """
    data = [
        {"System": "Groundcell Honeycomb Design", "Compression Strength (MPa)": 45, "Water Permeability (%)": 85, "Environmental Impact (Score)": 90},
        {"System": "System A", "Compression Strength (MPa)": 40, "Water Permeability (%)": 80, "Environmental Impact (Score)": 70},
        {"System": "System B", "Compression Strength (MPa)": 35, "Water Permeability (%)": 75, "Environmental Impact (Score)": 65},
        {"System": "System C", "Compression Strength (MPa)": 30, "Water Permeability (%)": 70, "Environmental Impact (Score)": 60},
    ]
    return pd.DataFrame(data)


def validate_data(df):
    """
    Validate the product specification data to ensure it meets expectations.
    
    Args:
        df (pd.DataFrame): DataFrame containing product specifications.
    
    Raises:
        ValueError: If required columns are missing or data is invalid.
    """
    required_columns = ["System", "Compression Strength (MPa)", "Water Permeability (%)", "Environmental Impact (Score)"]
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")
    if df.isnull().values.any():
        raise ValueError("Data contains null values. Please ensure all fields are populated.")


def compare_systems(df):
    """
    Compare the effectiveness of the systems based on product specifications.
    
    Args:
        df (pd.DataFrame): DataFrame containing product specifications.
    
    Returns:
        pd.DataFrame: DataFrame containing a summary of the comparison, sorted by overall performance.
    """
    # Calculate overall performance score (weighted average of metrics)
    weights = {"Compression Strength (MPa)": 0.4, "Water Permeability (%)": 0.3, "Environmental Impact (Score)": 0.3}
    df["Overall Performance Score"] = (
        df["Compression Strength (MPa)"] * weights["Compression Strength (MPa)"] +
        df["Water Permeability (%)"] * weights["Water Permeability (%)"] +
        df["Environmental Impact (Score)"] * weights["Environmental Impact (Score)"]
    )

    # Sort systems by overall performance score (descending order)
    summary_df = df.sort_values(by="Overall Performance Score", ascending=False)
    return summary_df


def main():
    """
    Main function to execute the comparison and display the results.
    """
    try:
        # Load product specifications
        product_data = load_product_data()

        # Validate data integrity
        validate_data(product_data)

        # Perform comparison
        comparison_results = compare_systems(product_data)

        # Display results
        print("Comparison Results:")
        print(comparison_results)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
