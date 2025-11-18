"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trattar.blogspot.com
Prompt: Create a Python script to compare the mechanical properties of treated eucalyptus wood versus untreated native woods, as discussed on Trattar Madeiras' website.
Generated: DETERMINISTIC_516095e6529a8da3
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load mechanical properties data from a CSV file.
    
    :param file_path: Path to the CSV file containing the data.
    :return: A pandas DataFrame containing the loaded data.
    """
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        # Check if the required columns exist
        required_columns = {'Wood Type', 'Density (kg/m³)', 'Modulus of Elasticity (MPa)', 'Flexural Strength (MPa)'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"CSV file is missing required columns. Expected columns: {required_columns}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

def compare_wood_properties(data):
    """
    Compare the mechanical properties of treated eucalyptus wood versus untreated native woods.

    :param data: DataFrame containing mechanical properties of different woods.
    """
    # Filter entries for treated eucalyptus wood and untreated native woods
    treated_eucalyptus = data[data['Wood Type'] == 'Treated Eucalyptus']
    untreated_native_woods = data[data['Wood Type'] == 'Untreated Native Wood']

    if treated_eucalyptus.empty or untreated_native_woods.empty:
        print("Error: Missing data for one or both wood types.")
        return

    # Calculate mean properties for both wood types
    treated_means = treated_eucalyptus.mean(numeric_only=True)
    untreated_means = untreated_native_woods.mean(numeric_only=True)

    # Create a comparison DataFrame
    comparison = pd.DataFrame({
        'Property': ['Density (kg/m³)', 'Modulus of Elasticity (MPa)', 'Flexural Strength (MPa)'],
        'Treated Eucalyptus': [treated_means['Density (kg/m³)'], treated_means['Modulus of Elasticity (MPa)'], treated_means['Flexural Strength (MPa)']],
        'Untreated Native Wood': [untreated_means['Density (kg/m³)'], untreated_means['Modulus of Elasticity (MPa)'], untreated_means['Flexural Strength (MPa)']]
    })

    print("\nComparison of Mechanical Properties:")
    print(comparison)

    # Plot the comparison
    comparison.set_index('Property').plot(kind='bar', figsize=(10, 6))
    plt.title('Mechanical Properties Comparison: Treated Eucalyptus vs Untreated Native Wood')
    plt.ylabel('Value')
    plt.xlabel('Property')
    plt.xticks(rotation=45)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the wood properties comparison script.
    """
    # Path to the CSV file containing the data
    file_path = 'wood_properties.csv'  # Replace with the correct path to your CSV file

    try:
        # Load the data
        data = load_data(file_path)

        # Compare the mechanical properties
        compare_wood_properties(data)
    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
```
