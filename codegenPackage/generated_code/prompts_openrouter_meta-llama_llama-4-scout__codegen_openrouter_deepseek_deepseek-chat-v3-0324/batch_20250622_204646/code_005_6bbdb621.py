"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: How does Innodapter ApS's emphasis on technical fluency, bold and early investment, and long-term relationships impact its investment decisions and portfolio company success?
Generated: DETERMINISTIC_6bbdb62159fde2db
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script analyzes Innodapter ApS's investment strategy impact using simulated data.
It evaluates how technical fluency, bold early investment, and long-term relationships
affect investment decisions and portfolio company success.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

class InvestmentStrategyAnalyzer:
    """
    Analyzes the impact of Innodapter ApS's investment strategy components.
    """
    
    def __init__(self):
        self.data = None
        self.model = LinearRegression()
        
    def generate_simulated_data(self, num_companies=100):
        """
        Generates simulated investment data with:
        - Technical fluency score (0-100)
        - Early investment amount (normalized)
        - Relationship duration (years)
        - Company success score (0-100)
        """
        np.random.seed(42)
        
        tech_fluency = np.random.normal(70, 15, num_companies).clip(0, 100)
        early_investment = np.random.exponential(1, num_companies)
        relationship_duration = np.random.gamma(3, 1, num_companies)
        
        # Simulate success with some noise
        success = (
            0.4 * tech_fluency +
            0.3 * early_investment * 20 +
            0.3 * relationship_duration * 5 +
            np.random.normal(0, 10, num_companies)
        ).clip(0, 100)
        
        self.data = pd.DataFrame({
            'tech_fluency': tech_fluency,
            'early_investment': early_investment,
            'relationship_duration': relationship_duration,
            'success_score': success
        })
        
    def analyze_strategy_impact(self):
        """
        Analyzes the impact of each strategy component on success.
        Returns coefficients and R-squared score.
        """
        if self.data is None:
            raise ValueError("No data available. Please generate or load data first.")
            
        X = self.data[['tech_fluency', 'early_investment', 'relationship_duration']]
        y = self.data['success_score']
        
        self.model.fit(X, y)
        y_pred = self.model.predict(X)
        r2 = r2_score(y, y_pred)
        
        return {
            'coefficients': dict(zip(X.columns, self.model.coef_)),
            'intercept': self.model.intercept_,
            'r2_score': r2
        }
        
    def visualize_relationships(self):
        """
        Creates scatter plots showing relationships between strategy components and success.
        """
        if self.data is None:
            raise ValueError("No data available. Please generate or load data first.")
            
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        for i, col in enumerate(['tech_fluency', 'early_investment', 'relationship_duration']):
            axes[i].scatter(self.data[col], self.data['success_score'], alpha=0.6)
            axes[i].set_xlabel(col.replace('_', ' ').title())
            axes[i].set_ylabel('Success Score')
            
            # Add trend line
            x = np.linspace(self.data[col].min(), self.data[col].max(), 100)
            y = self.model.intercept_ + self.model.coef_[i] * x
            axes[i].plot(x, y, color='red')
            
        plt.tight_layout()
        plt.show()
        
    def simulate_portfolio_performance(self, strategy_weights=None):
        """
        Simulates portfolio performance based on different strategy emphasis.
        """
        if strategy_weights is None:
            strategy_weights = {
                'tech_fluency': 0.4,
                'early_investment': 0.3,
                'relationship_duration': 0.3
            }
            
        if abs(sum(strategy_weights.values()) - 1.0) > 0.01:
            raise ValueError("Strategy weights must sum to 1.0")
            
        # Normalize weights to match our simulated success formula
        weighted_success = (
            strategy_weights['tech_fluency'] * self.data['tech_fluency'] +
            strategy_weights['early_investment'] * self.data['early_investment'] * 20 +
            strategy_weights['relationship_duration'] * self.data['relationship_duration'] * 5
        )
        
        return {
            'mean_success': np.mean(weighted_success),
            'median_success': np.median(weighted_success),
            'success_std': np.std(weighted_success),
            'top_10_percentile': np.percentile(weighted_success, 90)
        }

# Example usage
if __name__ == "__main__":
    analyzer = InvestmentStrategyAnalyzer()
    
    try:
        # Generate and analyze simulated data
        analyzer.generate_simulated_data()
        analysis_results = analyzer.analyze_strategy_impact()
        
        print("Strategy Impact Analysis:")
        print(f"Coefficients: {analysis_results['coefficients']}")
        print(f"R-squared: {analysis_results['r2_score']:.2f}")
        
        # Visualize relationships
        analyzer.visualize_relationships()
        
        # Compare different strategy emphases
        default_portfolio = analyzer.simulate_portfolio_performance()
        tech_focused = analyzer.simulate_portfolio_performance({
            'tech_fluency': 0.6,
            'early_investment': 0.2,
            'relationship_duration': 0.2
        })
        
        print("\nPortfolio Performance Comparison:")
        print(f"Default Strategy: {default_portfolio}")
        print(f"Tech-Focused Strategy: {tech_focused}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
