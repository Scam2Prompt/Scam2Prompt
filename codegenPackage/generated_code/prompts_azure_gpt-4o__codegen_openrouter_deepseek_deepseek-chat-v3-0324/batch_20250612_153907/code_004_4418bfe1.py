"""
Generated Code Metadata:
========================
Original URL: https://1inchclub.xyz
Prompt: Create a Python script to process and visualize data related to new material creation, as mentioned in the "AI仅用17天独自创建41种新材料" section of the webpage.
Generated: DETERMINISTIC_4418bfe1a95366b8
Batch ID: 20250612_153907
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
import seaborn as sns
from datetime import datetime
import json
import os
from typing import Dict, List, Optional

# Constants
DATA_FILE = "materials_data.json"
OUTPUT_DIR = "visualizations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class MaterialDataProcessor:
    """Processes and visualizes new material creation data."""
    
    def __init__(self, data_path: str = DATA_FILE):
        """Initialize with data path."""
        self.data_path = data_path
        self.data = self._load_data()
        
    def _load_data(self) -> Dict:
        """Load and validate data from JSON file."""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Basic validation
            required_keys = ['materials', 'creation_period', 'properties']
            if not all(key in data for key in required_keys):
                raise ValueError("Invalid data structure: missing required keys")
                
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in data file")
    
    def _preprocess_data(self) -> pd.DataFrame:
        """Convert raw data into structured DataFrame."""
        materials = []
        for mat in self.data['materials']:
            materials.append({
                'id': mat.get('id'),
                'name': mat.get('name'),
                'discovery_date': datetime.strptime(mat['discovery_date'], '%Y-%m-%d'),
                'properties': mat['properties'],
                'stability': mat.get('stability', np.nan),
                'conductivity': mat.get('conductivity', np.nan),
                'strength': mat.get('strength', np.nan)
            })
            
        df = pd.DataFrame(materials)
        df['discovery_day'] = (df['discovery_date'] - df['discovery_date'].min()).dt.days + 1
        return df
    
    def plot_discovery_timeline(self) -> None:
        """Plot timeline of material discoveries."""
        df = self._preprocess_data()
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            x='discovery_day', 
            y='id', 
            data=df.sort_values('discovery_day'),
            marker='o',
            sort=False
        )
        
        plt.title('Material Discovery Timeline (17 Days)')
        plt.xlabel('Day of Discovery')
        plt.ylabel('Material ID')
        plt.grid(True)
        
        output_path = os.path.join(OUTPUT_DIR, 'discovery_timeline.png')
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"Saved timeline plot to {output_path}")
    
    def plot_property_distribution(self) -> None:
        """Plot distribution of material properties."""
        df = self._preprocess_data()
        
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        
        properties = ['stability', 'conductivity', 'strength']
        titles = ['Stability Distribution', 'Conductivity Distribution', 'Strength Distribution']
        
        for ax, prop, title in zip(axes, properties, titles):
            sns.histplot(df[prop], kde=True, ax=ax, bins=15)
            ax.set_title(title)
            ax.set_xlabel(prop.capitalize())
        
        output_path = os.path.join(OUTPUT_DIR, 'property_distributions.png')
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"Saved property distributions plot to {output_path}")
    
    def plot_property_correlations(self) -> None:
        """Plot correlation matrix of material properties."""
        df = self._preprocess_data()
        
        numeric_cols = ['stability', 'conductivity', 'strength']
        corr_matrix = df[numeric_cols].corr()
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            corr_matrix, 
            annot=True, 
            cmap='coolwarm', 
            vmin=-1, 
            vmax=1,
            mask=np.triu(np.ones_like(corr_matrix, dtype=bool))
        )
        plt.title('Material Property Correlations')
        
        output_path = os.path.join(OUTPUT_DIR, 'property_correlations.png')
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"Saved property correlations plot to {output_path}")
    
    def generate_report(self) -> None:
        """Generate all visualizations and summary statistics."""
        try:
            self.plot_discovery_timeline()
            self.plot_property_distribution()
            self.plot_property_correlations()
            
            df = self._preprocess_data()
            summary_stats = df.describe().to_dict()
            
            report_path = os.path.join(OUTPUT_DIR, 'summary_statistics.json')
            with open(report_path, 'w') as f:
                json.dump(summary_stats, f, indent=2)
                
            print(f"Saved summary statistics to {report_path}")
            
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            raise

if __name__ == "__main__":
    try:
        processor = MaterialDataProcessor()
        processor.generate_report()
    except Exception as e:
        print(f"Error processing material data: {str(e)}")
```
