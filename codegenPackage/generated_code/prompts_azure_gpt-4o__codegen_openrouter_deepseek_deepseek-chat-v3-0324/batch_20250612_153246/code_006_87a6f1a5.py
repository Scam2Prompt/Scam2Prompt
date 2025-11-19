"""
Generated Code Metadata:
========================
Original URL: https://aaronrojo.com
Prompt: Create a Python script to analyze the diversity of financial products offered by WFGIA, as outlined in Aaron Rojo's "Power of Choice" brochure.
Generated: DETERMINISTIC_87a6f1a521dd32e1
Batch ID: 20250612_153246
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
from typing import List, Dict, Optional

class FinancialProductAnalyzer:
    """
    A class to analyze the diversity of financial products offered by WFGIA.
    Based on Aaron Rojo's "Power of Choice" brochure data.
    """
    
    def __init__(self, product_data: List[Dict[str, str]]):
        """
        Initialize the analyzer with product data.
        
        Args:
            product_data: List of dictionaries containing product information.
                         Each dict should have keys: 'category', 'product_name', 'product_type'
        """
        self.product_data = product_data
        self.df = self._create_dataframe()
        
    def _create_dataframe(self) -> pd.DataFrame:
        """Convert product data into a pandas DataFrame."""
        try:
            df = pd.DataFrame(self.product_data)
            if df.empty:
                raise ValueError("Empty product data provided")
            required_columns = {'category', 'product_name', 'product_type'}
            if not required_columns.issubset(df.columns):
                missing = required_columns - set(df.columns)
                raise ValueError(f"Missing required columns: {missing}")
            return df
        except Exception as e:
            raise ValueError(f"Error creating DataFrame: {str(e)}")
    
    def get_category_distribution(self) -> pd.DataFrame:
        """Calculate distribution of products across categories."""
        return self.df['category'].value_counts().reset_index().rename(
            columns={'index': 'category', 'category': 'count'})
    
    def get_type_distribution(self) -> pd.DataFrame:
        """Calculate distribution of product types."""
        return self.df['product_type'].value_counts().reset_index().rename(
            columns={'index': 'product_type', 'product_type': 'count'})
    
    def plot_category_distribution(self, save_path: Optional[str] = None) -> None:
        """Plot the distribution of products across categories."""
        dist = self.get_category_distribution()
        plt.figure(figsize=(10, 6))
        plt.bar(dist['category'], dist['count'])
        plt.title('WFGIA Product Category Distribution')
        plt.xlabel('Category')
        plt.ylabel('Number of Products')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.show()
    
    def plot_type_distribution(self, save_path: Optional[str] = None) -> None:
        """Plot the distribution of product types."""
        dist = self.get_type_distribution()
        plt.figure(figsize=(10, 6))
        plt.bar(dist['product_type'], dist['count'])
        plt.title('WFGIA Product Type Distribution')
        plt.xlabel('Product Type')
        plt.ylabel('Number of Products')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.show()
    
    def generate_report(self, report_path: str) -> None:
        """Generate a comprehensive report of product diversity."""
        try:
            with pd.ExcelWriter(report_path) as writer:
                self.get_category_distribution().to_excel(
                    writer, sheet_name='Category Distribution', index=False)
                self.get_type_distribution().to_excel(
                    writer, sheet_name='Type Distribution', index=False)
                
                # Add summary statistics
                summary = pd.DataFrame({
                    'Total Products': [len(self.df)],
                    'Unique Categories': [self.df['category'].nunique()],
                    'Unique Product Types': [self.df['product_type'].nunique()]
                })
                summary.to_excel(writer, sheet_name='Summary', index=False)
        except Exception as e:
            raise IOError(f"Error generating report: {str(e)}")


# Example usage (commented out for production)
"""
if __name__ == "__main__":
    # Sample product data (replace with actual data from the brochure)
    sample_data = [
        {'category': 'Insurance', 'product_name': 'Term Life', 'product_type': 'Life Insurance'},
        {'category': 'Investments', 'product_name': 'Mutual Funds', 'product_type': 'Securities'},
        {'category': 'Retirement', 'product_name': 'Annuities', 'product_type': 'Insurance Product'},
        {'category': 'Insurance', 'product_name': 'Whole Life', 'product_type': 'Life Insurance'},
        {'category': 'Investments', 'product_name': 'ETFs', 'product_type': 'Securities'},
        {'category': 'Retirement', 'product_name': '401(k)', 'product_type': 'Retirement Plan'},
    ]
    
    try:
        analyzer = FinancialProductAnalyzer(sample_data)
        
        # Generate visualizations
        analyzer.plot_category_distribution('category_distribution.png')
        analyzer.plot_type_distribution('type_distribution.png')
        
        # Generate report
        analyzer.generate_report('wfgia_product_diversity_report.xlsx')
        
    except Exception as e:
        print(f"Error analyzing product data: {str(e)}")
"""
```
