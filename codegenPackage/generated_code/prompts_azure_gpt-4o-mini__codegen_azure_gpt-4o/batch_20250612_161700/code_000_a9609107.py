"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: Generate a Python script to evaluate water quality using parameters from well and municipal sources, as discussed by Provincial Water Solutions.
Generated: DETERMINISTIC_a96091073e1ad1d0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def evaluate_water_quality(data):
    """
    Evaluates water quality based on parameters from well and municipal sources.

    Parameters:
        data (pd.DataFrame): A DataFrame containing water quality parameters.
                             Expected columns: 'Source', 'pH', 'Turbidity', 'Hardness', 'Contaminants'

    Returns:
        pd.DataFrame: A DataFrame with an additional 'Quality' column indicating water quality status.
    """
    # Define acceptable ranges for water quality parameters
    acceptable_ranges = {
        'pH': (6.5, 8.5),  # WHO recommended pH range
        'Turbidity': (0, 5),  # NTU (Nephelometric Turbidity Units)
        'Hardness': (0, 300),  # mg/L as CaCO3
        'Contaminants': (0, 0.01)  # mg/L (e.g., heavy metals, pesticides)
    }

    def assess_quality(row):
        """
        Assess the quality of water for a single row based on defined ranges.

        Parameters:
            row (pd.Series): A row of water quality data.

        Returns:
            str: 'Good', 'Moderate', or 'Poor' based on water quality.
        """
        issues = 0

        # Check each parameter against acceptable ranges
        for param, (min_val, max_val) in acceptable_ranges.items():
            if not (min_val <= row[param] <= max_val):
                issues += 1

        # Determine quality based on the number of issues
        if issues == 0:
            return 'Good'
        elif issues == 1:
            return 'Moderate'
        else:
            return 'Poor'

    # Apply the assessment function to each row
    data['Quality'] = data.apply(assess_quality, axis=1)
    return data


def main():
    """
    Main function to load water quality data, evaluate it, and save the results.
    """
    try:
        # Load water quality data from a CSV file
        input_file = 'water_quality_data.csv'
        data = pd.read_csv(input_file)

        # Validate required columns
        required_columns = ['Source', 'pH', 'Turbidity', 'Hardness', 'Contaminants']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Input file must contain the following columns: {required_columns}")

        # Evaluate water quality
        results = evaluate_water_quality(data)

        # Save the results to a new CSV file
        output_file = 'water_quality_results.csv'
        results.to_csv(output_file, index=False)
        print(f"Water quality evaluation completed. Results saved to '{output_file}'.")

    except FileNotFoundError:
        print("Error: Input file not found. Please ensure the file exists and the path is correct.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
```
