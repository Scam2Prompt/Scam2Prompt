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
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime

def load_crm_data(file_path):
    """
    Load CRM data from a file.

    Args:
        file_path (str): Path to the CRM data file.

    Returns:
        pd.DataFrame: Loaded CRM data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        # Attempt to load the CRM data from the file
        crm_data = pd.read_csv(file_path)
        return crm_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file '{file_path}' is malformed.")
        return None

def preprocess_crm_data(crm_data):
    """
    Preprocess the CRM data.

    Args:
        crm_data (pd.DataFrame): CRM data to preprocess.

    Returns:
        pd.DataFrame: Preprocessed CRM data.
    """
    # Ensure date columns are in datetime format
    crm_data['donation_date'] = pd.to_datetime(crm_data['donation_date'], errors='coerce')
    crm_data['last_interaction_date'] = pd.to_datetime(crm_data['last_interaction_date'], errors='coerce')

    # Handle missing values
    crm_data.fillna({'donor_name': 'Unknown', 'donation_amount': 0}, inplace=True)

    return crm_data

def calculate_donor_engagement(crm_data):
    """
    Calculate donor engagement metrics.

    Args:
        crm_data (pd.DataFrame): Preprocessed CRM data.

    Returns:
        dict: Donor engagement metrics.
    """
    # Calculate average donation amount
    avg_donation_amount = crm_data['donation_amount'].mean()

    # Calculate total donations
    total_donations = crm_data['donation_amount'].sum()

    # Calculate number of donors
    num_donors = crm_data['donor_name'].nunique()

    # Calculate most recent donation date
    most_recent_donation_date = crm_data['donation_date'].max()

    # Calculate average time since last interaction
    avg_time_since_last_interaction = (crm_data['last_interaction_date'].max() - crm_data['last_interaction_date']).mean()

    engagement_metrics = {
        'avg_donation_amount': avg_donation_amount,
        'total_donations': total_donations,
        'num_donors': num_donors,
        'most_recent_donation_date': most_recent_donation_date,
        'avg_time_since_last_interaction': avg_time_since_last_interaction
    }

    return engagement_metrics

def generate_report(crm_data):
    """
    Generate a report on donor engagement and donation trends.

    Args:
        crm_data (pd.DataFrame): Preprocessed CRM data.

    Returns:
        str: Report on donor engagement and donation trends.
    """
    engagement_metrics = calculate_donor_engagement(crm_data)

    report = "Donor Engagement and Donation Trends Report\n"
    report += "-----------------------------------------\n"
    report += f"Average Donation Amount: ${engagement_metrics['avg_donation_amount']:.2f}\n"
    report += f"Total Donations: ${engagement_metrics['total_donations']:.2f}\n"
    report += f"Number of Donors: {engagement_metrics['num_donors']}\n"
    report += f"Most Recent Donation Date: {engagement_metrics['most_recent_donation_date'].strftime('%Y-%m-%d')}\n"
    report += f"Average Time Since Last Interaction: {engagement_metrics['avg_time_since_last_interaction']}\n"

    # Donation trends
    crm_data['donation_year'] = crm_data['donation_date'].dt.year
    yearly_donations = crm_data.groupby('donation_year')['donation_amount'].sum().reset_index()
    report += "\nDonation Trends by Year\n"
    report += "------------------------\n"
    for index, row in yearly_donations.iterrows():
        report += f"{row['donation_year']}: ${row['donation_amount']:.2f}\n"

    return report

def main():
    file_path = 'CRM_f_data.csv'  # Replace with actual file path
    crm_data = load_crm_data(file_path)

    if crm_data is not None:
        crm_data = preprocess_crm_data(crm_data)
        report = generate_report(crm_data)
        print(report)

if __name__ == "__main__":
    main()
```
