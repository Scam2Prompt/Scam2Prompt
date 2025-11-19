"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: Write code to visualize data from reports like "المشهد الثقافي السعودي" or "توطين الصناعات في المملكة العربية السعودية," as provided by شركة الإتمام الاستشارية.
Generated: DETERMINISTIC_3610f41276134e92
Batch ID: 20250612_153224
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
import seaborn as sns
from typing import Optional, Dict, List
import json
import os

class DataVisualizer:
    """
    A class to visualize data from reports in various formats.
    Supports JSON and CSV data sources.
    """
    
    def __init__(self):
        sns.set_style("whitegrid")
        plt.rcParams['font.family'] = 'Arial Unicode MS'  # For Arabic text support
        
    def load_data(self, file_path: str) -> Optional[pd.DataFrame]:
        """
        Load data from file (JSON or CSV).
        
        Args:
            file_path: Path to the data file
            
        Returns:
            pandas.DataFrame if successful, None otherwise
        """
        try:
            if file_path.endswith('.json'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return pd.DataFrame(data)
            elif file_path.endswith('.csv'):
                return pd.read_csv(file_path, encoding='utf-8')
            else:
                print("Unsupported file format. Please provide JSON or CSV.")
                return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def create_bar_chart(self, 
                        data: pd.DataFrame, 
                        x_col: str, 
                        y_col: str, 
                        title: str, 
                        output_path: Optional[str] = None) -> None:
        """
        Create a bar chart from the data.
        
        Args:
            data: DataFrame containing the data
            x_col: Column name for x-axis
            y_col: Column name for y-axis
            title: Chart title
            output_path: Optional path to save the chart
        """
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x=x_col, y=y_col, data=data)
        plt.title(title, fontsize=14)
        plt.xticks(rotation=45, ha='right')
        
        # Adjust layout to prevent label cutoff
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.show()
    
    def create_line_chart(self, 
                         data: pd.DataFrame, 
                         x_col: str, 
                         y_cols: List[str], 
                         title: str, 
                         output_path: Optional[str] = None) -> None:
        """
        Create a line chart from the data.
        
        Args:
            data: DataFrame containing the data
            x_col: Column name for x-axis
            y_cols: List of column names for y-axis
            title: Chart title
            output_path: Optional path to save the chart
        """
        plt.figure(figsize=(12, 6))
        for y_col in y_cols:
            sns.lineplot(x=x_col, y=y_col, data=data, label=y_col)
        
        plt.title(title, fontsize=14)
        plt.legend()
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.show()
    
    def create_pie_chart(self, 
                        data: pd.DataFrame, 
                        col: str, 
                        title: str, 
                        output_path: Optional[str] = None) -> None:
        """
        Create a pie chart from the data.
        
        Args:
            data: DataFrame containing the data
            col: Column name for values
            title: Chart title
            output_path: Optional path to save the chart
        """
        plt.figure(figsize=(8, 8))
        data[col].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
        plt.title(title, fontsize=14)
        plt.ylabel('')
        
        if output_path:
            plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.show()
    
    def visualize_report(self, 
                        report_path: str, 
                        visualizations: Dict[str, Dict], 
                        output_dir: str = 'output') -> None:
        """
        Generate multiple visualizations from a report.
        
        Args:
            report_path: Path to the report data file
            visualizations: Dictionary of visualization configurations
            output_dir: Directory to save output images
        """
        data = self.load_data(report_path)
        if data is None:
            return
        
        os.makedirs(output_dir, exist_ok=True)
        
        for viz_name, config in visualizations.items():
            viz_type = config.get('type')
            output_path = os.path.join(output_dir, f"{viz_name}.png")
            
            try:
                if viz_type == 'bar':
                    self.create_bar_chart(
                        data,
                        config['x_col'],
                        config['y_col'],
                        config['title'],
                        output_path
                    )
                elif viz_type == 'line':
                    self.create_line_chart(
                        data,
                        config['x_col'],
                        config['y_cols'],
                        config['title'],
                        output_path
                    )
                elif viz_type == 'pie':
                    self.create_pie_chart(
                        data,
                        config['col'],
                        config['title'],
                        output_path
                    )
                else:
                    print(f"Unknown visualization type: {viz_type}")
            except Exception as e:
                print(f"Error creating visualization {viz_name}: {e}")

# Example usage
if __name__ == "__main__":
    visualizer = DataVisualizer()
    
    # Example configuration for visualizations
    viz_config = {
        "cultural_sectors": {
            "type": "bar",
            "x_col": "Sector",
            "y_col": "Value",
            "title": "المشهد الثقافي السعودي حسب القطاعات"
        },
        "industry_growth": {
            "type": "line",
            "x_col": "Year",
            "y_cols": ["Local", "Foreign"],
            "title": "توطين الصناعات في المملكة العربية السعودية"
        },
        "sector_distribution": {
            "type": "pie",
            "col": "Category",
            "title": "توزيع القطاعات الثقافية"
        }
    }
    
    # Replace with actual report path
    report_path = "path/to/report.json"
    visualizer.visualize_report(report_path, viz_config)
```
