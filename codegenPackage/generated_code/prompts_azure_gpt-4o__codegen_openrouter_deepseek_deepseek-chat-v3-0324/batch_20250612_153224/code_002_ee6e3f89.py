"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Generate a script to compare the horsepower and excavation depth of Yanmar mini excavators (e.g., ViO12, ViO17, ViO25, ViO35, SV100) and display the results in a tabular format.
Generated: DETERMINISTIC_ee6e3f89f077454c
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

def compare_yanmar_excavators():
    """
    Compares horsepower and excavation depth of Yanmar mini excavators.
    Displays results in a tabular format using pandas DataFrame.
    """
    
    # Data for Yanmar mini excavators (model: [horsepower (HP), excavation depth (m)])
    excavator_data = {
        'ViO12': [12.4, 2.3],
        'ViO17': [17.9, 2.7],
        'ViO25': [24.8, 3.2],
        'ViO35': [35.0, 3.8],
        'SV100': [74.3, 5.8]
    }
    
    try:
        # Create DataFrame from the data
        df = pd.DataFrame.from_dict(excavator_data, 
                                   orient='index',
                                   columns=['Horsepower (HP)', 'Excavation Depth (m)'])
        
        # Sort by horsepower (ascending)
        df.sort_values(by='Horsepower (HP)', inplace=True)
        
        # Display the comparison table
        print("Yanmar Mini Excavators Comparison:")
        print("=" * 40)
        print(df.to_string())
        print("\nNote: Specifications may vary by region and configuration.")
        
    except Exception as e:
        print(f"An error occurred while generating the comparison: {str(e)}")

if __name__ == "__main__":
    compare_yanmar_excavators()
```
