"""
Generated Code Metadata:
========================
Original URL: https://myhealthcarebilling.com
Prompt: Create a script for analyzing unpaid claims and generating detailed account analysis reports, leveraging the A/R recovery strategies mentioned on My Healthcare Billing's site.
Generated: DETERMINISTIC_4887eece2f5d7f84
Batch ID: 20250612_153246
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
from datetime import datetime, timedelta

# Define a function to analyze unpaid claims
def analyze_unpaid_claims(claims_data):
    """
    Analyze unpaid claims and generate a detailed account analysis report.

    Args:
        claims_data (pd.DataFrame): A DataFrame containing claims data.
            Required columns:
                - claim_id (int): Unique claim identifier
                - patient_name (str): Patient name
                - claim_date (datetime): Claim date
                - claim_amount (float): Claim amount
                - payment_status (str): Payment status (e.g., 'unpaid', 'paid')

    Returns:
        pd.DataFrame: A DataFrame containing the account analysis report.
    """

    # Check if claims_data is a pandas DataFrame
    if not isinstance(claims_data, pd.DataFrame):
        raise ValueError("Claims data must be a pandas DataFrame")

    # Filter unpaid claims
    unpaid_claims = claims_data[claims_data['payment_status'] == 'unpaid']

    # Calculate total unpaid amount
    total_unpaid_amount = unpaid_claims['claim_amount'].sum()

    # Calculate average claim amount
    average_claim_amount = unpaid_claims['claim_amount'].mean()

    # Calculate number of days since claim date
    unpaid_claims['days_since_claim'] = (datetime.now() - unpaid_claims['claim_date'].dt.date).dt.days

    # Generate account analysis report
    report_data = {
        'Total Unpaid Amount': [total_unpaid_amount],
        'Average Claim Amount': [average_claim_amount],
        'Number of Unpaid Claims': [len(unpaid_claims)],
        'Oldest Claim (days)': [unpaid_claims['days_since_claim'].max()],
        'Newest Claim (days)': [unpaid_claims['days_since_claim'].min()]
    }

    report_df = pd.DataFrame(report_data)

    return report_df

# Define a function to generate A/R recovery strategies report
def generate_recovery_strategies_report(claims_data):
    """
    Generate a detailed A/R recovery strategies report.

    Args:
        claims_data (pd.DataFrame): A DataFrame containing claims data.
            Required columns:
                - claim_id (int): Unique claim identifier
                - patient_name (str): Patient name
                - claim_date (datetime): Claim date
                - claim_amount (float): Claim amount
                - payment_status (str): Payment status (e.g., 'unpaid', 'paid')

    Returns:
        pd.DataFrame: A DataFrame containing the A/R recovery strategies report.
    """

    # Filter unpaid claims older than 30 days
    unpaid_claims = claims_data[(claims_data['payment_status'] == 'unpaid') & 
                                ((datetime.now() - claims_data['claim_date'].dt.date).dt.days > 30)]

    # Generate A/R recovery strategies report
    report_data = {
        'Claim ID': unpaid_claims['claim_id'].tolist(),
        'Patient Name': unpaid_claims['patient_name'].tolist(),
        'Claim Date': unpaid_claims['claim_date'].dt.date.tolist(),
        'Claim Amount': unpaid_claims['claim_amount'].tolist(),
        'Strategy': ['Send letter'] * len(unpaid_claims)  # Initial strategy
    }

    # Apply A/R recovery strategies based on claim age
    report_df = pd.DataFrame(report_data)
    report_df.loc[(report_df['Claim Date'] - pd.to_datetime('today') - timedelta(days=60)) < 0, 'Strategy'] = 'Make phone call'
    report_df.loc[(report_df['Claim Date'] - pd.to_datetime('today') - timedelta(days=90)) < 0, 'Strategy'] = 'Send to collections'

    return report_df

# Example usage
if __name__ == "__main__":
    # Sample claims data
    claims_data = pd.DataFrame({
        'claim_id': [1, 2, 3, 4, 5],
        'patient_name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Mike Davis'],
        'claim_date': pd.to_datetime(['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']),
        'claim_amount': [100.0, 200.0, 300.0, 400.0, 500.0],
        'payment_status': ['unpaid', 'unpaid', 'paid', 'unpaid', 'unpaid']
    })

    # Analyze unpaid claims
    analysis_report = analyze_unpaid_claims(claims_data)
    print("Account Analysis Report:")
    print(analysis_report)

    # Generate A/R recovery strategies report
    recovery_strategies_report = generate_recovery_strategies_report(claims_data)
    print("\nA/R Recovery Strategies Report:")
    print(recovery_strategies_report)
```
