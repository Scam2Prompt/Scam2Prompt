"""
Generated Code Metadata:
========================
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Develop a simple program to compare the features and performance of BerlinerLuft's Confortcond and VarioCond climatizer lines.
Generated: DETERMINISTIC_06151d0a94d68c84
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program to compare features and performance of BerlinerLuft's Confortcond and VarioCond climatizer lines.
This program uses a simple data structure to store features and performance metrics, and provides a comparison.
"""

# Import necessary modules
import sys

# Define the climatizer data
climatizers = {
    "Confortcond": {
        "features": ["Energy-efficient", "Compact design", "Low noise"],
        "performance": {
            "cooling_capacity_kW": 5.0,
            "power_consumption_kW": 1.2,
            "noise_level_dB": 35
        }
    },
    "VarioCond": {
        "features": ["High cooling capacity", "Modular design", "Advanced controls"],
        "performance": {
            "cooling_capacity_kW": 7.5,
            "power_consumption_kW": 1.8,
            "noise_level_dB": 40
        }
    }
}

def compare_climatizers(climatizer1, climatizer2):
    """
    Compare the features and performance of two climatizers.
    
    Args:
        climatizer1 (str): Name of the first climatizer.
        climatizer2 (str): Name of the second climatizer.
    
    Returns:
        None
    """
    try:
        # Retrieve data for the climatizers
        data1 = climatizers[climatizer1]
        data2 = climatizers[climatizer2]
        
        # Compare features
        print(f"Features of {climatizer1}: {', '.join(data1['features'])}")
        print(f"Features of {climatizer2}: {', '.join(data2['features'])}")
        
        # Compare performance metrics
        print("\nPerformance Comparison:")
        print(f"{'Metric':<20}{climatizer1:<15}{climatizer2:<15}")
        print("-" * 50)
        for metric in data1['performance']:
            value1 = data1['performance'][metric]
            value2 = data2['performance'][metric]
            print(f"{metric:<20}{value1:<15}{value2:<15}")
    
    except KeyError as e:
        print(f"Error: Climatizer '{e.args[0]}' not found in the database.")
        sys.exit(1)

# Main function
def main():
    """
    Main function to execute the comparison.
    """
    print("BerlinerLuft Climatizer Comparison Tool")
    print("=" * 40)
    
    # Climatizers to compare
    climatizer1 = "Confortcond"
    climatizer2 = "VarioCond"
    
    # Perform comparison
    compare_climatizers(climatizer1, climatizer2)

# Entry point of the program
if __name__ == "__main__":
    main()
```
