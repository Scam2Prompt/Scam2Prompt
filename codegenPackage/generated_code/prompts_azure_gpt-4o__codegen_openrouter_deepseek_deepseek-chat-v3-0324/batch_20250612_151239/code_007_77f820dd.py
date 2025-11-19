"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Develop a Python script to simulate the impact of the Revolving Loan Scheme for sugarcane replantation on agricultural productivity, based on the loan details from the Development Bank of Mauritius.
Generated: DETERMINISTIC_77f820dd7f320470
Batch ID: 20250612_151239
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
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional

class SugarcaneLoanSimulator:
    """
    Simulates the impact of the Revolving Loan Scheme for sugarcane replantation on agricultural productivity.
    
    Attributes:
        loan_details (Dict): Dictionary containing loan parameters from Development Bank of Mauritius.
        productivity_data (pd.DataFrame): DataFrame containing historical productivity data.
    """
    
    def __init__(self, loan_details: Dict, productivity_data: pd.DataFrame):
        """
        Initializes the simulator with loan details and productivity data.
        
        Args:
            loan_details: Dictionary containing loan parameters.
            productivity_data: DataFrame with historical productivity data (columns: 'Year', 'Productivity').
        """
        self.loan_details = loan_details
        self.productivity_data = productivity_data
        
        # Validate input data
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validates the input data for required fields and types."""
        required_loan_fields = ['principal', 'interest_rate', 'term_years', 'replanting_cost_per_hectare']
        for field in required_loan_fields:
            if field not in self.loan_details:
                raise ValueError(f"Missing required loan field: {field}")
                
        if not isinstance(self.productivity_data, pd.DataFrame):
            raise TypeError("productivity_data must be a pandas DataFrame")
            
        required_data_columns = ['Year', 'Productivity']
        for col in required_data_columns:
            if col not in self.productivity_data.columns:
                raise ValueError(f"Missing required column in productivity_data: {col}")
    
    def calculate_loan_repayment(self) -> Dict[str, List[float]]:
        """
        Calculates the annual loan repayment schedule.
        
        Returns:
            Dictionary with 'year', 'principal_paid', 'interest_paid', 'remaining_balance'.
        """
        principal = self.loan_details['principal']
        rate = self.loan_details['interest_rate'] / 100
        term = self.loan_details['term_years']
        
        # Calculate annual payment using amortization formula
        annual_payment = principal * (rate * (1 + rate)**term) / ((1 + rate)**term - 1)
        
        schedule = {
            'year': [],
            'principal_paid': [],
            'interest_paid': [],
            'remaining_balance': []
        }
        
        remaining_balance = principal
        for year in range(1, term + 1):
            interest_paid = remaining_balance * rate
            principal_paid = annual_payment - interest_paid
            remaining_balance -= principal_paid
            
            schedule['year'].append(year)
            schedule['principal_paid'].append(principal_paid)
            schedule['interest_paid'].append(interest_paid)
            schedule['remaining_balance'].append(max(0, remaining_balance))
            
        return schedule
    
    def simulate_productivity_impact(self, replanted_area_hectares: float) -> pd.DataFrame:
        """
        Simulates the impact of replantation on productivity over time.
        
        Args:
            replanted_area_hectares: Area to be replanted in hectares.
            
        Returns:
            DataFrame with projected productivity including 'Year', 'Productivity', 'ProjectedProductivity'.
        """
        if replanted_area_hectares <= 0:
            raise ValueError("Replanted area must be positive")
            
        # Calculate maximum replantable area based on loan amount
        max_replantable = self.loan_details['principal'] / self.loan_details['replanting_cost_per_hectare']
        if replanted_area_hectares > max_replantable:
            raise ValueError(f"Requested area exceeds maximum replantable area of {max_replantable:.2f} hectares")
        
        # Get the last year from historical data
        last_year = self.productivity_data['Year'].max()
        last_productivity = self.productivity_data.loc[self.productivity_data['Year'] == last_year, 'Productivity'].values[0]
        
        # Create projection years
        projection_years = range(last_year + 1, last_year + self.loan_details['term_years'] + 1)
        
        # Calculate productivity improvement (assume 15% increase over loan term)
        improvement_factor = 0.15 * (replanted_area_hectares / max_replantable)
        yearly_improvement = improvement_factor / self.loan_details['term_years']
        
        # Generate projections
        projections = []
        current_productivity = last_productivity
        for year in projection_years:
            current_productivity *= (1 + yearly_improvement)
            projections.append({
                'Year': year,
                'Productivity': np.nan,
                'ProjectedProductivity': current_productivity
            })
            
        # Combine historical and projected data
        result = pd.concat([
            self.productivity_data.assign(ProjectedProductivity=np.nan),
            pd.DataFrame(projections)
        ], ignore_index=True)
        
        return result
    
    def calculate_roi(self, replanted_area_hectares: float, sugarcane_price_per_ton: float) -> Dict:
        """
        Calculates return on investment for the replantation.
        
        Args:
            replanted_area_hectares: Area to be replanted in hectares.
            sugarcane_price_per_ton: Current market price per ton of sugarcane.
            
        Returns:
            Dictionary with ROI metrics including 'total_cost', 'total_revenue', 'net_profit', 'roi_percentage'.
        """
        # Get loan repayment schedule
        repayment = self.calculate_loan_repayment()
        total_loan_cost = sum(repayment['principal_paid']) + sum(repayment['interest_paid'])
        
        # Get productivity projections
        projections = self.simulate_productivity_impact(replanted_area_hectares)
        last_historical = projections[projections['ProjectedProductivity'].isna()]['Productivity'].iloc[-1]
        avg_projected = projections[~projections['ProjectedProductivity'].isna()]['ProjectedProductivity'].mean()
        
        # Calculate additional production
        additional_production = (avg_projected - last_historical) * replanted_area_hectares
        additional_revenue = additional_production * sugarcane_price_per_ton * self.loan_details['term_years']
        
        # Calculate ROI
        net_profit = additional_revenue - total_loan_cost
        roi_percentage = (net_profit / total_loan_cost) * 100 if total_loan_cost > 0 else 0
        
        return {
            'total_cost': total_loan_cost,
            'total_revenue': additional_revenue,
            'net_profit': net_profit,
            'roi_percentage': roi_percentage
        }
    
    def generate_report(self, replanted_area_hectares: float, sugarcane_price_per_ton: float, output_file: Optional[str] = None) -> None:
        """
        Generates a comprehensive report with charts and tables.
        
        Args:
            replanted_area_hectares: Area to be replanted in hectares.
            sugarcane_price_per_ton: Current market price per ton of sugarcane.
            output_file: Optional path to save the report as HTML.
        """
        # Create figure with subplots
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Loan repayment schedule
        plt.subplot(2, 2, 1)
        repayment = self.calculate_loan_repayment()
        plt.plot(repayment['year'], repayment['principal_paid'], label='Principal')
        plt.plot(repayment['year'], repayment['interest_paid'], label='Interest')
        plt.title('Loan Repayment Schedule')
        plt.xlabel('Year')
        plt.ylabel('Amount (MUR)')
        plt.legend()
        plt.grid(True)
        
        # Plot 2: Productivity impact
        plt.subplot(2, 2, 2)
        projections = self.simulate_productivity_impact(replanted_area_hectares)
        plt.plot(projections['Year'], projections['Productivity'], 'b-', label='Historical')
        plt.plot(projections['Year'], projections['ProjectedProductivity'], 'r--', label='Projected')
        plt.title('Productivity Projection')
        plt.xlabel('Year')
        plt.ylabel('Tons per Hectare')
        plt.legend()
        plt.grid(True)
        
        # Plot 3: ROI components
        plt.subplot(2, 2, 3)
        roi_data = self.calculate_roi(replanted_area_hectares, sugarcane_price_per_ton)
        components = ['Total Cost', 'Additional Revenue', 'Net Profit']
        values = [roi_data['total_cost'], roi_data['total_revenue'], roi_data['net_profit']]
        plt.bar(components, values, color=['red', 'green', 'blue'])
        plt.title('Financial Overview')
        plt.ylabel('Amount (MUR)')
        plt.grid(True)
        
        # Plot 4: ROI percentage
        plt.subplot(2, 2, 4)
        plt.bar(['ROI'], [roi_data
