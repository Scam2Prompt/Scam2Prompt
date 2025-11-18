"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Write a script to generate a fee structure report for MBBS and MD/MS courses at MIMSR Medical College, based on the "Fees Last 5 Years" section.
Generated: DETERMINISTIC_e08a6960d471a47e
Batch ID: 20250612_153225
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

class FeeStructureReport:
    def __init__(self, data):
        """
        Initialize the FeeStructureReport with the given data.
        
        :param data: A DataFrame containing fee data for MBBS and MD/MS courses.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validate the input data to ensure it contains the necessary columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['Year', 'MBBS_Fee', 'MD_MS_Fee']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f'Missing required column: {column}')

    def generate_report(self):
        """
        Generate a fee structure report for the MBBS and MD/MS courses.
        This includes printing the fee data and plotting it.
        """
        # Print the fee structure data
        print("Fee Structure Report for MIMSR Medical College:")
        print(self.data)

        # Plotting the fee structure
        self.plot_fee_structure()

    def plot_fee_structure(self):
        """
        Create a bar plot for the fee structure over the years.
        """
        plt.figure(figsize=(10, 6))

        # Bar widths
        bar_width = 0.35

        # Calculate positions for bars
        r1 = range(len(self.data))
        r2 = [x + bar_width for x in r1]

        # Plotting the bars
        plt.bar(r1, self.data['MBBS_Fee'], color='blue', width=bar_width, edgecolor='grey', label='MBBS Fee')
        plt.bar(r2, self.data['MD_MS_Fee'], color='orange', width=bar_width, edgecolor='grey', label='MD/MS Fee')

        # Adding labels and title
        plt.xlabel('Years', fontweight='bold')
        plt.xticks([r + bar_width / 2 for r in range(len(self.data))], self.data['Year'])
        plt.ylabel('Fee Amount (INR)', fontweight='bold')
        plt.title('Fee Structure Over the Last 5 Years')
        plt.legend()
        plt.tight_layout()

        # Show the plot
        plt.show()

if __name__ == "__main__":
    # Example data for the last 5 years
    fee_data = {
        'Year': ['2019', '2020', '2021', '2022', '2023'],
        'MBBS_Fee': [150000, 160000, 170000, 180000, 190000],
        'MD_MS_Fee': [200000, 210000, 220000, 230000, 240000]
    }

    # Create a DataFrame
    fee_df = pd.DataFrame(fee_data)

    try:
        # Generate the fee structure report
        report = FeeStructureReport(fee_df)
        report.generate_report()
    except ValueError as e:
        print(f"Error generating report: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
