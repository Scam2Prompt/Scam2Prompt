"""
Generated Code Metadata:
========================
Original URL: https://fesit.cl
Prompt: Develop a script using Python to simulate the impact of proposed Chilean tax reforms on different income groups, incorporating FESIT's principles of equity and justice.
Generated: DETERMINISTIC_98764f266b7c7436
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

class TaxReformSimulator:
    """
    Simulates the impact of Chilean tax reforms on different income groups,
    incorporating FESIT's principles of equity and justice.
    """
    
    def __init__(self):
        self.income_groups = {
            'low': (0, 500000),        # CLP monthly
            'middle': (500001, 2000000),
            'high': (2000001, 10000000),
            'very_high': (10000001, float('inf'))
        }
        
        # Current tax brackets (2023)
        self.current_tax_rates = {
            'low': 0.0,
            'middle': 0.08,
            'high': 0.135,
            'very_high': 0.23
        }
        
        # Proposed tax brackets (reform)
        self.proposed_tax_rates = {
            'low': 0.0,
            'middle': 0.10,
            'high': 0.18,
            'very_high': 0.30
        }
        
        # Social benefits (CLP monthly)
        self.social_benefits = {
            'low': 150000,
            'middle': 50000,
            'high': 0,
            'very_high': 0
        }
        
        # Population distribution (percentage)
        self.population_distribution = {
            'low': 0.40,
            'middle': 0.45,
            'high': 0.12,
            'very_high': 0.03
        }
    
    def calculate_tax(self, income: float, rates: Dict[str, float]) -> float:
        """
        Calculate tax based on income and tax rates.
        
        Args:
            income: Monthly income in CLP
            rates: Tax rates dictionary
            
        Returns:
            Calculated tax amount
        """
        for group, (min_income, max_income) in self.income_groups.items():
            if min_income <= income <= max_income:
                return income * rates[group]
        return 0.0
    
    def calculate_net_income(self, income: float, rates: Dict[str, float]) -> float:
        """
        Calculate net income after tax and benefits.
        
        Args:
            income: Monthly income in CLP
            rates: Tax rates dictionary
            
        Returns:
            Net income after tax and benefits
        """
        tax = self.calculate_tax(income, rates)
        for group, (min_income, max_income) in self.income_groups.items():
            if min_income <= income <= max_income:
                benefit = self.social_benefits[group]
                return income - tax + benefit
        return income - tax
    
    def generate_sample_population(self, size: int = 10000) -> pd.DataFrame:
        """
        Generate a sample population with incomes distributed according to Chilean statistics.
        
        Args:
            size: Number of individuals in the sample
            
        Returns:
            DataFrame with income data
        """
        np.random.seed(42)
        
        # Generate incomes based on distribution
        groups = []
        incomes = []
        
        for group, dist in self.population_distribution.items():
            n = int(size * dist)
            min_inc, max_inc = self.income_groups[group]
            
            # Generate log-normal distribution for more realistic income distribution
            if group == 'very_high':
                # Wider range for very high incomes
                incomes.extend(np.random.lognormal(mean=np.log(max_inc/2), sigma=1.0, size=n))
            else:
                incomes.extend(np.random.uniform(min_inc, max_inc, size=n))
            
            groups.extend([group] * n)
        
        # Create DataFrame
        df = pd.DataFrame({
            'income_group': groups,
            'monthly_income': incomes
        })
        
        # Ensure no negative incomes
        df['monthly_income'] = df['monthly_income'].clip(lower=0)
        
        return df
    
    def simulate_reform_impact(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Simulate the impact of tax reform on a population.
        
        Args:
            df: DataFrame with income data
            
        Returns:
            DataFrame with simulation results
        """
        results = df.copy()
        
        # Calculate current scenario
        results['current_tax'] = results['monthly_income'].apply(
            lambda x: self.calculate_tax(x, self.current_tax_rates)
        )
        results['current_net'] = results['monthly_income'].apply(
            lambda x: self.calculate_net_income(x, self.current_tax_rates)
        )
        
        # Calculate proposed scenario
        results['proposed_tax'] = results['monthly_income'].apply(
            lambda x: self.calculate_tax(x, self.proposed_tax_rates)
        )
        results['proposed_net'] = results['monthly_income'].apply(
            lambda x: self.calculate_net_income(x, self.proposed_tax_rates)
        )
        
        # Calculate differences
        results['tax_change'] = results['proposed_tax'] - results['current_tax']
        results['net_change'] = results['proposed_net'] - results['current_net']
        results['percent_change'] = (results['net_change'] / results['current_net']) * 100
        
        return results
    
    def analyze_by_group(self, results: pd.DataFrame) -> pd.DataFrame:
        """
        Aggregate results by income group.
        
        Args:
            results: DataFrame with simulation results
            
        Returns:
            Aggregated results by income group
        """
        analysis = results.groupby('income_group').agg({
            'monthly_income': 'mean',
            'current_tax': 'mean',
            'current_net': 'mean',
            'proposed_tax': 'mean',
            'proposed_net': 'mean',
            'tax_change': 'mean',
            'net_change': 'mean',
            'percent_change': 'mean'
        }).reset_index()
        
        # Add population percentage
        analysis['population_percentage'] = analysis['income_group'].map(self.population_distribution)
        
        return analysis
    
    def calculate_gini(self, incomes: List[float]) -> float:
        """
        Calculate Gini coefficient for income distribution.
        
        Args:
            incomes: List of incomes
            
        Returns:
            Gini coefficient (0-1)
        """
        sorted_incomes = np.sort(incomes)
        n = len(sorted_incomes)
        index = np.arange(1, n + 1)
        
        # Calculate Gini coefficient
        gini = (np.sum((2 * index - n - 1) * sorted_incomes)) / (n * np.sum(sorted_incomes))
        return gini
    
    def calculate_equity_metrics(self, results: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate equity metrics for current and proposed scenarios.
        
        Args:
            results: DataFrame with simulation results
            
        Returns:
            Dictionary with equity metrics
        """
        metrics = {}
        
        # Current scenario metrics
        current_gini = self.calculate_gini(results['current_net'].values)
        current_tax_revenue = results['current_tax'].sum()
        
        # Proposed scenario metrics
        proposed_gini = self.calculate_gini(results['proposed_net'].values)
        proposed_tax_revenue = results['proposed_tax'].sum()
        
        metrics['current_gini'] = current_gini
        metrics['proposed_gini'] = proposed_gini
        metrics['gini_change'] = proposed_gini - current_gini
        metrics['current_tax_revenue'] = current_tax_revenue
        metrics['proposed_tax_revenue'] = proposed_tax_revenue
        metrics['revenue_change'] = proposed_tax_revenue - current_tax_revenue
        metrics['revenue_change_percent'] = (
            (proposed_tax_revenue - current_tax_revenue) / current_tax_revenue * 100
        )
        
        return metrics
    
    def visualize_results(self, analysis: pd.DataFrame, metrics: Dict[str, float]):
        """
        Visualize the simulation results.
        
        Args:
            analysis: Aggregated results by income group
            metrics: Equity metrics dictionary
        """
        plt.style.use('seaborn')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Net income comparison
        analysis.plot(
            x='income_group',
            y=['current_net', 'proposed_net'],
            kind='bar',
            ax=axes[0, 0],
            title='Average Net Income by Group'
        )
        axes[0, 0].set_ylabel('CLP')
        
        # Tax change
        analysis.plot(
            x='income_group',
            y='tax_change',
            kind='bar',
            ax=axes[0, 1],
            title='Average Tax Change by Group',
            color='red'
        )
        axes[0, 1
