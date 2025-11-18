"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: Create a data visualization using Python to showcase the rise of giving in the Global South, referencing Emerging Gifts' analysis and trends.
Generated: DETERMINISTIC_9d5c8467140d7a6b
Batch ID: 20250612_152511
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
import seaborn as sns

# Define the main function to run the data visualization
def main():
    try:
        # Load the dataset
        # Replace 'emerging_gifts_analysis.csv' with the actual path to your dataset
        data = pd.read_csv('emerging_gifts_analysis.csv')

        # Ensure the dataset contains the expected columns
        required_columns = ['Year', 'GivingAmount', 'Region']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Filter data for Global South regions
        global_south = data[data['Region'].isin(['Africa', 'Latin America', 'Asia', 'Middle East'])]

        # Group the data by year and sum the giving amounts
        grouped_data = global_south.groupby('Year', as_index=False)['GivingAmount'].sum()

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=grouped_data, x='Year', y='GivingAmount', marker='o')

        # Adding titles and labels
        plt.title('Rise of Giving in the Global South', fontsize=16)
        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Total Giving Amount (in USD)', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid()

        # Show the plot
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
Make sure to replace `'emerging_gifts_analysis.csv'` with the actual path to your dataset file.
