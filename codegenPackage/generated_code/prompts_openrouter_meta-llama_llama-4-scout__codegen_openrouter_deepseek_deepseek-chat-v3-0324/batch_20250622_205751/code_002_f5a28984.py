"""
Generated Code Metadata:
========================
Original URL: https://humanxpert.com
Prompt: "Generate a denial management plan using Python and pandas library to reduce refusal and increase money recovery for a medical practice."
Generated: DETERMINISTIC_f5a2898462014147
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class DenialManagementPlan:
    """
    A class to manage and analyze claim denials for a medical practice.
    Helps identify patterns, root causes, and recovery strategies.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the DenialManagementPlan with data.
        
        Args:
            data_path (str): Path to the CSV file containing denial data.
                           Expected columns: ['claim_id', 'patient_id', 'service_date', 
                           'payer', 'denial_code', 'denial_reason', 'amount', 
                           'resubmitted', 'recovered_amount', 'status']
        """
        if data_path:
            self.df = pd.read_csv(data_path)
            self._clean_data()
        else:
            self.df = pd.DataFrame(columns=[
                'claim_id', 'patient_id', 'service_date', 'payer', 
                'denial_code', 'denial_reason', 'amount', 
                'resubmitted', 'recovered_amount', 'status'
            ])
    
    def _clean_data(self):
        """Clean and preprocess the denial data."""
        # Convert dates
        self.df['service_date'] = pd.to_datetime(self.df['service_date'])
        
        # Fill missing values
        self.df['recovered_amount'] = self.df['recovered_amount'].fillna(0)
        self.df['resubmitted'] = self.df['resubmitted'].fillna(False)
        
        # Calculate days since service
        self.df['days_since_service'] = (datetime.now() - self.df['service_date']).dt.days
    
    def add_denial_record(self, record):
        """
        Add a new denial record to the dataset.
        
        Args:
            record (dict): Dictionary containing denial record fields.
        """
        new_record = pd.DataFrame([record])
        self.df = pd.concat([self.df, new_record], ignore_index=True)
        self._clean_data()
    
    def analyze_denials(self):
        """
        Analyze denial patterns and generate insights.
        
        Returns:
            dict: Dictionary containing analysis results.
        """
        analysis = {}
        
        # Denial reasons breakdown
        analysis['denial_reasons'] = self.df['denial_reason'].value_counts().to_dict()
        
        # Payer-wise denials
        analysis['payer_denials'] = self.df['payer'].value_counts().to_dict()
        
        # Recovery rate
        total_amount = self.df['amount'].sum()
        recovered_amount = self.df['recovered_amount'].sum()
        analysis['recovery_rate'] = recovered_amount / total_amount if total_amount > 0 else 0
        
        # Resubmission success rate
        resubmitted = self.df[self.df['resubmitted']]
        analysis['resubmission_success'] = len(resubmitted[resubmitted['recovered_amount'] > 0]) / len(resubmitted) if len(resubmitted) > 0 else 0
        
        # Aging analysis
        aging_bins = [0, 30, 60, 90, 180, 365, np.inf]
        aging_labels = ['0-30', '31-60', '61-90', '91-180', '181-365', '365+']
        self.df['aging_bucket'] = pd.cut(self.df['days_since_service'], bins=aging_bins, labels=aging_labels)
        analysis['aging_analysis'] = self.df['aging_bucket'].value_counts().to_dict()
        
        return analysis
    
    def generate_recovery_strategy(self):
        """
        Generate prioritized recovery strategy based on analysis.
        
        Returns:
            pd.DataFrame: Prioritized claims for recovery efforts.
        """
        # Calculate recovery potential score
        self.df['recovery_score'] = (
            (self.df['amount'] - self.df['recovered_amount']) * 
            (1 - self.df['days_since_service'] / 365)  # Older claims get lower priority
        )
        
        # Prioritize claims
        prioritized = self.df.sort_values(
            by=['recovery_score', 'days_since_service'], 
            ascending=[False, True]
        )
        
        return prioritized[['claim_id', 'payer', 'denial_reason', 'amount', 
                           'recovered_amount', 'days_since_service', 'recovery_score']]
    
    def visualize_denials(self, analysis):
        """
        Create visualizations of denial patterns.
        
        Args:
            analysis (dict): Analysis results from analyze_denials()
        """
        plt.figure(figsize=(15, 10))
        
        # Denial reasons pie chart
        plt.subplot(2, 2, 1)
        pd.Series(analysis['denial_reasons']).plot.pie(autopct='%1.1f%%')
        plt.title('Denial Reasons Breakdown')
        
        # Payer-wise denials bar chart
        plt.subplot(2, 2, 2)
        pd.Series(analysis['payer_denials']).sort_values().plot.barh()
        plt.title('Denials by Payer')
        
        # Aging analysis
        plt.subplot(2, 2, 3)
        pd.Series(analysis['aging_analysis']).sort_index().plot.bar()
        plt.title('Denials by Age')
        plt.xlabel('Days Since Service')
        
        # Recovery rate
        plt.subplot(2, 2, 4)
        plt.bar(['Recovered', 'Unrecovered'], 
                [analysis['recovery_rate'], 1 - analysis['recovery_rate']])
        plt.title('Recovery Rate')
        
        plt.tight_layout()
        plt.show()
    
    def export_recovery_plan(self, filename):
        """
        Export the recovery plan to a CSV file.
        
        Args:
            filename (str): Path to save the recovery plan.
        """
        strategy = self.generate_recovery_strategy()
        strategy.to_csv(filename, index=False)
    
    def track_recovery(self, claim_id, recovered_amount, resubmitted=True):
        """
        Update recovery status for a claim.
        
        Args:
            claim_id (str): ID of the claim to update.
            recovered_amount (float): Amount recovered.
            resubmitted (bool): Whether the claim was resubmitted.
        """
        mask = self.df['claim_id'] == claim_id
        if mask.any():
            self.df.loc[mask, 'recovered_amount'] = recovered_amount
            self.df.loc[mask, 'resubmitted'] = resubmitted
            self.df.loc[mask, 'status'] = 'Recovered' if recovered_amount > 0 else 'Resubmitted'
        else:
            raise ValueError(f"Claim ID {claim_id} not found.")

# Example usage
if __name__ == "__main__":
    # Initialize with sample data
    dm = DenialManagementPlan("denials_data.csv")
    
    # Analyze denials
    analysis = dm.analyze_denials()
    print("Denial Analysis:")
    print(analysis)
    
    # Generate recovery strategy
    recovery_strategy = dm.generate_recovery_strategy()
    print("\nTop 5 Claims for Recovery:")
    print(recovery_strategy.head())
    
    # Visualize patterns
    dm.visualize_denials(analysis)
    
    # Export recovery plan
    dm.export_recovery_plan("recovery_plan.csv")
    
    # Track recovery for a claim
    try:
        dm.track_recovery("CLM12345", 500.00)
    except ValueError as e:
        print(f"Error: {e}")
```
