"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: "Generate a report using CRM.f data on donor engagement and donation trends for a foundation."
Generated: DETERMINISTIC_4b3ebac11b7289a9
Batch ID: 20250622_204809
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_donor_report(data_file, output_file):
    """
    Generates a report on donor engagement and donation trends.

    Parameters:
        data_file (str): Path to the CRM data file (CSV format).
        output_file (str): Path to save the generated report (PDF format).
    """
    try:
        # Load CRM data
        logging.info("Loading CRM data...")
        data = pd.read_csv(data_file)

        # Validate required columns
        required_columns = ['DonorID', 'DonationAmount', 'DonationDate', 'EngagementScore']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Missing required columns. Expected: {required_columns}")

        # Convert DonationDate to datetime
        logging.info("Processing data...")
        data['DonationDate'] = pd.to_datetime(data['DonationDate'])

        # Aggregate donation trends by year
        data['Year'] = data['DonationDate'].dt.year
        donation_trends = data.groupby('Year')['DonationAmount'].sum()

        # Calculate average engagement score
        avg_engagement = data['EngagementScore'].mean()

        # Generate plots
        logging.info("Generating plots...")
        plt.figure(figsize=(10, 6))

        # Donation trends plot
        plt.subplot(2, 1, 1)
        donation_trends.plot(kind='bar', color='skyblue')
        plt.title('Donation Trends by Year')
        plt.xlabel('Year')
        plt.ylabel('Total Donation Amount')

        # Engagement score distribution plot
        plt.subplot(2, 1, 2)
        data['EngagementScore'].plot(kind='hist', bins=20, color='lightgreen', edgecolor='black')
        plt.title('Engagement Score Distribution')
        plt.xlabel('Engagement Score')
        plt.ylabel('Frequency')

        plt.tight_layout()

        # Save report to PDF
        logging.info("Saving report...")
        plt.savefig(output_file)
        logging.info(f"Report saved successfully to {output_file}")

    except FileNotFoundError:
        logging.error(f"File not found: {data_file}")
    except ValueError as ve:
        logging.error(f"Data validation error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'crm_data.csv' and 'donor_report.pdf' with actual file paths
    generate_donor_report('crm_data.csv', 'donor_report.pdf')
```
