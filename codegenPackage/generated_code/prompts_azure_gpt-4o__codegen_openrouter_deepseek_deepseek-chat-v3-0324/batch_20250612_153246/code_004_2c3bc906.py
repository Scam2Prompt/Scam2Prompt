"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Create a script to compare the UV állóság (UV resistance) of different műanyag ablak (plastic window) profiles, such as Aluplast 70 Prémium and Rehau Euro Design 86.
Generated: DETERMINISTIC_2c3bc906835550f9
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

class UVResistanceComparator:
    """
    A class to compare UV resistance of different plastic window profiles.
    """
    
    def __init__(self):
        self.profiles = {}
        
    def add_profile(self, name, uv_resistance, color_stability, warranty_years):
        """
        Add a window profile with its UV resistance properties.
        
        Args:
            name (str): Name of the window profile
            uv_resistance (float): UV resistance rating (0-100)
            color_stability (str): Color stability rating (e.g., 'Excellent', 'Good')
            warranty_years (int): Warranty period in years
        """
        if not isinstance(uv_resistance, (int, float)) or uv_resistance < 0 or uv_resistance > 100:
            raise ValueError("UV resistance must be a number between 0 and 100")
            
        if not isinstance(warranty_years, int) or warranty_years < 0:
            raise ValueError("Warranty years must be a positive integer")
            
        self.profiles[name] = {
            'uv_resistance': uv_resistance,
            'color_stability': color_stability,
            'warranty_years': warranty_years
        }
    
    def compare_uv_resistance(self):
        """
        Compare UV resistance of all added profiles.
        
        Returns:
            DataFrame: Comparison table sorted by UV resistance
        """
        if not self.profiles:
            raise ValueError("No profiles added for comparison")
            
        df = pd.DataFrame.from_dict(self.profiles, orient='index')
        df = df.sort_values('uv_resistance', ascending=False)
        return df
    
    def plot_comparison(self):
        """
        Create a bar plot comparing UV resistance of profiles.
        """
        if not self.profiles:
            raise ValueError("No profiles added for comparison")
            
        df = self.compare_uv_resistance()
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(df.index, df['uv_resistance'], color='skyblue')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom')
        
        plt.title('UV Resistance Comparison of Window Profiles')
        plt.xlabel('Window Profile')
        plt.ylabel('UV Resistance Rating (0-100)')
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, 110)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    comparator = UVResistanceComparator()
    
    # Add sample profiles (replace with actual data)
    comparator.add_profile("Aluplast 70 Prémium", 85, "Excellent", 10)
    comparator.add_profile("Rehau Euro Design 86", 82, "Good", 8)
    comparator.add_profile("Veka Softline 82", 78, "Good", 7)
    
    # Compare and display results
    print("UV Resistance Comparison:")
    print(comparator.compare_uv_resistance())
    
    # Visualize comparison
    comparator.plot_comparison()
```
