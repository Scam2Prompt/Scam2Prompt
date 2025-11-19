"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Create a Python program to compare the filtration efficiency of NF (Nano-Filtration) membranes versus RO membranes, using Econopure's product data for NF hollow membranes.
Generated: DETERMINISTIC_555299bfce6bd8bc
Batch ID: 20250612_154631
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
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MembraneComparison:
    """
    A class to compare filtration efficiency between NF and RO membranes using product data.
    """
    
    def __init__(self, nf_data_path: str, ro_data_path: str):
        """
        Initialize the MembraneComparison with paths to NF and RO membrane data.
        
        Args:
            nf_data_path (str): Path to NF membrane data CSV file.
            ro_data_path (str): Path to RO membrane data CSV file.
        """
        self.nf_data_path = nf_data_path
        self.ro_data_path = ro_data_path
        self.nf_data = None
        self.ro_data = None
        
    def load_data(self) -> None:
        """
        Load NF and RO membrane data from CSV files.
        
        Raises:
            FileNotFoundError: If data files are not found.
            ValueError: If data files are malformed.
        """
        try:
            self.nf_data = pd.read_csv(self.nf_data_path)
            self.ro_data = pd.read_csv(self.ro_data_path)
            logger.info("Data loaded successfully")
        except FileNotFoundError as e:
            logger.error(f"Data file not found: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise ValueError(f"Malformed data file: {e}")
    
    def validate_data(self) -> None:
        """
        Validate that required columns exist in the loaded data.
        
        Raises:
            ValueError: If required columns are missing.
        """
        required_columns = ['membrane_type', 'efficiency', 'pressure', 'flow_rate']
        
        for df, name in [(self.nf_data, 'NF'), (self.ro_data, 'RO')]:
            if df is None:
                raise ValueError(f"{name} data not loaded")
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                raise ValueError(f"{name} data missing required columns: {missing_cols}")
    
    def calculate_average_efficiency(self) -> Dict[str, float]:
        """
        Calculate average filtration efficiency for NF and RO membranes.
        
        Returns:
            Dict[str, float]: Dictionary with average efficiency for NF and RO membranes.
            
        Raises:
            ValueError: If data is not loaded or validated.
        """
        if self.nf_data is None or self.ro_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            nf_avg = self.nf_data['efficiency'].mean()
            ro_avg = self.ro_data['efficiency'].mean()
            
            logger.info(f"NF average efficiency: {nf_avg:.2f}%")
            logger.info(f"RO average efficiency: {ro_avg:.2f}%")
            
            return {
                'NF': nf_avg,
                'RO': ro_avg
            }
        except Exception as e:
            logger.error(f"Error calculating average efficiency: {e}")
            raise
    
    def plot_comparison(self, save_path: Optional[str] = None) -> None:
        """
        Plot a comparison of NF vs RO membrane efficiency.
        
        Args:
            save_path (Optional[str]): Path to save the plot. If None, plot is displayed.
        """
        try:
            avg_efficiency = self.calculate_average_efficiency()
            
            plt.figure(figsize=(10, 6))
            plt.bar(avg_efficiency.keys(), avg_efficiency.values(), color=['blue', 'green'])
            plt.title('Average Filtration Efficiency: NF vs RO Membranes')
            plt.xlabel('Membrane Type')
            plt.ylabel('Efficiency (%)')
            plt.ylim(0, 100)
            
            for i, v in enumerate(avg_efficiency.values()):
                plt.text(i, v + 2, f"{v:.2f}%", ha='center')
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                logger.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
        except Exception as e:
            logger.error(f"Error generating plot: {e}")
            raise
    
    def compare_at_pressure(self, pressure: float) -> Dict[str, float]:
        """
        Compare efficiency at a specific pressure level.
        
        Args:
            pressure (float): Pressure level to compare at.
            
        Returns:
            Dict[str, float]: Dictionary with efficiency at specified pressure for NF and RO.
        """
        try:
            nf_at_pressure = self.nf_data[self.nf_data['pressure'] == pressure]['efficiency'].mean()
            ro_at_pressure = self.ro_data[self.ro_data['pressure'] == pressure]['efficiency'].mean()
            
            return {
                'NF': nf_at_pressure,
                'RO': ro_at_pressure
            }
        except Exception as e:
            logger.error(f"Error comparing at pressure {pressure}: {e}")
            raise

def main():
    try:
        # Initialize with data paths (replace with actual paths)
        comparator = MembraneComparison(
            nf_data_path='econopure_nf_data.csv',
            ro_data_path='ro_membrane_data.csv'
        )
        
        # Load and validate data
        comparator.load_data()
        comparator.validate_data()
        
        # Perform comparisons
        avg_efficiency = comparator.calculate_average_efficiency()
        print("Average Efficiency Comparison:")
        print(f"NF Membranes: {avg_efficiency['NF']:.2f}%")
        print(f"RO Membranes: {avg_efficiency['RO']:.2f}%")
        
        # Compare at standard pressure (example: 10 bar)
        pressure_comparison = comparator.compare_at_pressure(10)
        print(f"\nEfficiency at 10 bar:")
        print(f"NF Membranes: {pressure_comparison['NF']:.2f}%")
        print(f"RO Membranes: {pressure_comparison['RO']:.2f}%")
        
        # Generate and save plot
        comparator.plot_comparison(save_path='membrane_comparison.png')
        
    except Exception as e:
        logger.error(f"Error in membrane comparison: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
```
