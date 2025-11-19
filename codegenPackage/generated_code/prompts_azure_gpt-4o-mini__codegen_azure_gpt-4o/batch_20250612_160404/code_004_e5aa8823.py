"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Illustrate how to use a library to generate a scorecard report for evaluating business advocacy efforts, similar to the IACI Scorecard mentioned on their site.
Generated: DETERMINISTIC_e5aa88232788f2ed
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define a function to generate a scorecard report
def generate_scorecard(data, output_dir="reports", file_name="scorecard_report"):
    """
    Generates a scorecard report for evaluating business advocacy efforts.

    Parameters:
    - data (list of dict): A list of dictionaries containing advocacy metrics.
                           Each dictionary should have keys: 'Category', 'Score', 'MaxScore'.
    - output_dir (str): Directory where the report will be saved.
    - file_name (str): Name of the output file (without extension).

    Returns:
    - None: Saves the report as a CSV file and a bar chart image.
    """
    try:
        # Validate input data
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Data must be a list of dictionaries.")

        # Convert data to a DataFrame
        df = pd.DataFrame(data)

        # Validate required columns
        required_columns = {'Category', 'Score', 'MaxScore'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Data must contain the following columns: {required_columns}")

        # Calculate percentage scores
        df['Percentage'] = (df['Score'] / df['MaxScore']) * 100

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save the scorecard as a CSV file
        csv_path = os.path.join(output_dir, f"{file_name}.csv")
        df.to_csv(csv_path, index=False)
        print(f"Scorecard saved as CSV: {csv_path}")

        # Generate a bar chart for visualization
        plt.figure(figsize=(10, 6))
        plt.bar(df['Category'], df['Percentage'], color='skyblue')
        plt.xlabel('Category')
        plt.ylabel('Percentage Score')
        plt.title('Business Advocacy Scorecard')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Save the bar chart as an image
        chart_path = os.path.join(output_dir, f"{file_name}.png")
        plt.savefig(chart_path)
        plt.close()
        print(f"Scorecard visualization saved as image: {chart_path}")

    except Exception as e:
        print(f"An error occurred while generating the scorecard: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for business advocacy efforts
    sample_data = [
        {"Category": "Policy Engagement", "Score": 85, "MaxScore": 100},
        {"Category": "Community Outreach", "Score": 70, "MaxScore": 100},
        {"Category": "Sustainability Initiatives", "Score": 90, "MaxScore": 100},
        {"Category": "Economic Impact", "Score": 75, "MaxScore": 100},
    ]

    # Generate the scorecard report
    generate_scorecard(sample_data)
```
