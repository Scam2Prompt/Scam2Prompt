"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Write a script to compare anti-leak coatings for home improvement projects, and generate a report on the best pelapis anti bocor options.
Generated: DETERMINISTIC_317533a6f4e1ccb2
Batch ID: 20250612_150718
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
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class AntiLeakCoatingAnalyzer:
    """
    A class to analyze and compare anti-leak coatings for home improvement projects.
    Generates reports on the best pelapis anti bocor options.
    """
    
    def __init__(self, data_path: str = None):
        """
        Initialize the analyzer with optional data path.
        
        Args:
            data_path (str, optional): Path to CSV file containing coating data. 
                                      If None, uses sample data.
        """
        self.data = self._load_data(data_path)
        self.report_date = datetime.now().strftime("%Y-%m-%d")
        
    def _load_data(self, data_path: str) -> pd.DataFrame:
        """
        Load coating data from CSV or use sample data if no path provided.
        
        Args:
            data_path (str): Path to CSV file
            
        Returns:
            pd.DataFrame: Coating data
        """
        if data_path:
            try:
                return pd.read_csv(data_path)
            except FileNotFoundError:
                print(f"Warning: File {data_path} not found. Using sample data.")
        
        # Sample data structure
        sample_data = {
            'name': ['AquaSeal', 'DryGuard', 'WaterLock', 'PermaDry', 'SealMaster'],
            'type': ['Acrylic', 'Polyurethane', 'Silicone', 'Epoxy', 'Rubber'],
            'price_per_gallon': [45.99, 62.50, 78.25, 95.00, 52.75],
            'coverage_sqft_per_gallon': [350, 400, 300, 250, 450],
            'drying_time_hours': [4, 6, 2, 8, 3],
            'warranty_years': [5, 10, 7, 15, 8],
            'effectiveness_rating': [8.5, 9.2, 9.0, 9.5, 8.8],
            'ease_of_application': [9, 7, 8, 6, 9],
            'environmental_impact': [8, 6, 9, 5, 7]
        }
        return pd.DataFrame(sample_data)
    
    def calculate_cost_per_sqft(self) -> pd.DataFrame:
        """
        Calculate cost per square foot for each coating.
        
        Returns:
            pd.DataFrame: Original dataframe with added cost_per_sqft column
        """
        df = self.data.copy()
        df['cost_per_sqft'] = df['price_per_gallon'] / df['coverage_sqft_per_gallon']
        return df
    
    def calculate_composite_score(self, weights: Dict[str, float] = None) -> pd.DataFrame:
        """
        Calculate a composite score for each coating based on weighted factors.
        
        Args:
            weights (Dict[str, float], optional): Dictionary of weights for each factor.
                Default: {
                    'effectiveness': 0.4,
                    'cost': 0.3,
                    'drying_time': 0.1,
                    'ease': 0.1,
                    'environment': 0.1
                }
                
        Returns:
            pd.DataFrame: Original dataframe with added composite_score column
        """
        if weights is None:
            weights = {
                'effectiveness': 0.4,
                'cost': 0.3,
                'drying_time': 0.1,
                'ease': 0.1,
                'environment': 0.1
            }
            
        df = self.calculate_cost_per_sqft()
        
        # Normalize factors (higher is better)
        df['norm_effectiveness'] = df['effectiveness_rating'] / 10
        df['norm_cost'] = 1 - (df['cost_per_sqft'] / df['cost_per_sqft'].max())
        df['norm_drying'] = 1 - (df['drying_time_hours'] / df['drying_time_hours'].max())
        df['norm_ease'] = df['ease_of_application'] / 10
        df['norm_environment'] = df['environmental_impact'] / 10
        
        # Calculate composite score
        df['composite_score'] = (
            df['norm_effectiveness'] * weights['effectiveness'] +
            df['norm_cost'] * weights['cost'] +
            df['norm_drying'] * weights['drying_time'] +
            df['norm_ease'] * weights['ease'] +
            df['norm_environment'] * weights['environment']
        )
        
        return df
    
    def generate_ranking(self, weights: Dict[str, float] = None) -> pd.DataFrame:
        """
        Generate ranked list of coatings based on composite score.
        
        Args:
            weights (Dict[str, float], optional): Weights for composite score calculation
            
        Returns:
            pd.DataFrame: Sorted dataframe with rankings
        """
        df = self.calculate_composite_score(weights)
        df = df.sort_values('composite_score', ascending=False)
        df['rank'] = range(1, len(df) + 1)
        return df
    
    def generate_report(self, output_path: str = None, weights: Dict[str, float] = None) -> str:
        """
        Generate a comprehensive report on anti-leak coatings.
        
        Args:
            output_path (str, optional): Path to save HTML report. If None, returns as string.
            weights (Dict[str, float], optional): Weights for composite score calculation
            
        Returns:
            str: HTML report if output_path is None
        """
        ranked_df = self.generate_ranking(weights)
        
        # Create visualizations
        plt.figure(figsize=(10, 6))
        sns.barplot(x='composite_score', y='name', data=ranked_df, palette='viridis')
        plt.title('Anti-Leak Coating Composite Scores')
        plt.xlabel('Composite Score')
        plt.ylabel('Coating Name')
        plot_html = self._fig_to_html(plt)
        plt.close()
        
        # Create report HTML
        report_html = f"""
        <html>
            <head>
                <title>Anti-Leak Coating Analysis Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1 {{ color: #2c3e50; }}
                    h2 {{ color: #3498db; }}
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                    th {{ background-color: #f2f2f2; }}
                    tr:nth-child(even) {{ background-color: #f9f9f9; }}
                    .plot {{ margin: 20px 0; }}
                </style>
            </head>
            <body>
                <h1>Anti-Leak Coating Analysis Report</h1>
                <p>Generated on: {self.report_date}</p>
                
                <h2>Top Recommendations</h2>
                {ranked_df[['rank', 'name', 'type', 'composite_score']].head(3).to_html(index=False)}
                
                <h2>Performance Comparison</h2>
                <div class="plot">{plot_html}</div>
                
                <h2>Detailed Comparison</h2>
                {ranked_df.to_html(index=False)}
                
                <h2>Key Metrics</h2>
                <table>
                    <tr><th>Metric</th><th>Best Coating</th><th>Value</th></tr>
                    <tr><td>Highest Effectiveness</td><td>{ranked_df.iloc[0]['name']}</td><td>{ranked_df.iloc[0]['effectiveness_rating']}/10</td></tr>
                    <tr><td>Lowest Cost per sqft</td><td>{ranked_df.loc[ranked_df['cost_per_sqft'].idxmin()]['name']}</td><td>${ranked_df['cost_per_sqft'].min():.4f}</td></tr>
                    <tr><td>Fastest Drying</td><td>{ranked_df.loc[ranked_df['drying_time_hours'].idxmin()]['name']}</td><td>{ranked_df['drying_time_hours'].min()} hours</td></tr>
                    <tr><td>Longest Warranty</td><td>{ranked_df.loc[ranked_df['warranty_years'].idxmax()]['name']}</td><td>{ranked_df['warranty_years'].max()} years</td></tr>
                </table>
            </body>
        </html>
        """
        
        if output_path:
            try:
                with open(output_path, 'w') as f:
                    f.write(report_html)
                return f"Report saved to {output_path}"
            except IOError as e:
                return f"Error saving report
