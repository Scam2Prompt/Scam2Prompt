"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Generate a script to model the noise levels during screw pile installation and compare it to traditional foundation methods, referencing the low-noise advantages described by His Teknik Çelik.
Generated: DETERMINISTIC_3ee758ab96a557f9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns
from typing import List, Dict, Tuple

class FoundationNoiseModel:
    """
    A class to model and compare noise levels between screw pile installation 
    and traditional foundation methods based on His Teknik Çelik data.
    """
    
    def __init__(self):
        """
        Initialize with default noise level data from His Teknik Çelik.
        """
        self.noise_data = {
            'Screw Piles': {
                'mean': 65,  # dB
                'std_dev': 3,
                'source': 'His Teknik Çelik'
            },
            'Driven Piles': {
                'mean': 95,
                'std_dev': 5,
                'source': 'Traditional'
            },
            'Concrete Foundations': {
                'mean': 85,
                'std_dev': 7,
                'source': 'Traditional'
            }
        }
    
    def generate_noise_samples(self, method: str, n_samples: int = 1000) -> np.ndarray:
        """
        Generate random noise samples for a given foundation method.
        
        Args:
            method: Foundation method ('Screw Piles', 'Driven Piles', 'Concrete Foundations')
            n_samples: Number of samples to generate
            
        Returns:
            Array of noise level samples in dB
        """
        if method not in self.noise_data:
            raise ValueError(f"Invalid method. Choose from: {list(self.noise_data.keys())}")
            
        params = self.noise_data[method]
        return np.random.normal(params['mean'], params['std_dev'], n_samples)
    
    def compare_methods(self, methods: List[str] = None, n_samples: int = 1000) -> pd.DataFrame:
        """
        Compare noise levels between different foundation methods.
        
        Args:
            methods: List of methods to compare (default: all available)
            n_samples: Number of samples per method
            
        Returns:
            DataFrame with noise level samples for each method
        """
        if methods is None:
            methods = list(self.noise_data.keys())
            
        data = []
        for method in methods:
            samples = self.generate_noise_samples(method, n_samples)
            for sample in samples:
                data.append({
                    'Method': method,
                    'Noise Level (dB)': sample,
                    'Type': self.noise_data[method]['source']
                })
                
        return pd.DataFrame(data)
    
    def plot_comparison(self, methods: List[str] = None, n_samples: int = 1000) -> plt.Figure:
        """
        Create a comparative visualization of noise levels.
        
        Args:
            methods: List of methods to compare (default: all available)
            n_samples: Number of samples per method
            
        Returns:
            Matplotlib Figure object
        """
        df = self.compare_methods(methods, n_samples)
        
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Method', y='Noise Level (dB)', hue='Type', data=df)
        plt.title('Noise Level Comparison: Screw Piles vs Traditional Foundations')
        plt.axhline(y=85, color='r', linestyle='--', label='Typical Noise Threshold')
        plt.legend(title='Source')
        plt.grid(True)
        
        return plt.gcf()
    
    def calculate_statistics(self, methods: List[str] = None, n_samples: int = 10000) -> Dict[str, Dict[str, float]]:
        """
        Calculate comparative statistics between methods.
        
        Args:
            methods: List of methods to compare (default: all available)
            n_samples: Number of samples per method
            
        Returns:
            Dictionary of statistics for each method
        """
        if methods is None:
            methods = list(self.noise_data.keys())
            
        stats_dict = {}
        for method in methods:
            samples = self.generate_noise_samples(method, n_samples)
            stats_dict[method] = {
                'mean': np.mean(samples),
                'median': np.median(samples),
                'std_dev': np.std(samples),
                'min': np.min(samples),
                'max': np.max(samples),
                'exceeds_85dB': np.mean(samples > 85) * 100  # percentage
            }
            
        return stats_dict
    
    def save_comparison_report(self, output_path: str = 'noise_comparison_report.csv') -> None:
        """
        Generate and save a comprehensive comparison report.
        
        Args:
            output_path: Path to save the report
        """
        stats = self.calculate_statistics()
        df = pd.DataFrame(stats).T
        df['Source'] = [self.noise_data[method]['source'] for method in df.index]
        df.to_csv(output_path, index_label='Method')
        
        print(f"Report saved to {output_path}")


def main():
    """Main function to demonstrate the noise comparison."""
    try:
        model = FoundationNoiseModel()
        
        # Generate and display comparison plot
        fig = model.plot_comparison()
        plt.show()
        
        # Calculate and print statistics
        stats = model.calculate_statistics()
        print("\nNoise Level Statistics:")
        for method, values in stats.items():
            print(f"\n{method}:")
            for stat, val in values.items():
                print(f"{stat.replace('_', ' ').title()}: {val:.2f}")
        
        # Save report
        model.save_comparison_report()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
