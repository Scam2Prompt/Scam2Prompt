"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curve.markets
Prompt: Generate code to visualize yield curves for bond markets using matplotlib or plotly.
Generated: DETERMINISTIC_a46dfe1495b4435d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

# Function to simulate yield curve data
def generate_yield_curve_data():
    """
    Generates sample yield curve data for visualization.

    Returns:
        maturities (list): List of bond maturities in years.
        yields (list): Corresponding yields in percent.
    """
    maturities = [1, 2, 3, 5, 7, 10, 20, 30]  # Common bond maturities in years
    yields = [3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.5]  # Sample yield data in percent
    return maturities, yields

# Function to visualize yield curve
def plot_yield_curve(maturities, yields):
    """
    Plots the yield curve using matplotlib.

    Args:
        maturities (list): List of bond maturities in years.
        yields (list): Corresponding yields in percent.
    """
    # Error handling: Check if data is valid
    if not maturities or not yields or len(maturities) != len(yields):
        raise ValueError("Maturities and yields must be non-empty and of the same length.")
    
    # Plotting the yield curve
    plt.figure(figsize=(10, 6))
    plt.plot(maturities, yields, marker='o', linestyle='-', color='blue', label='Yield Curve')
    
    # Adding labels and title
    plt.title("Yield Curve Visualization", fontsize=16)
    plt.xlabel("Maturity (Years)", fontsize=12)
    plt.ylabel("Yield (%)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    
    # Display the plot
    plt.show()

# Main execution block
if __name__ == "__main__":
    try:
        # Generate sample yield curve data
        maturities, yields = generate_yield_curve_data()
        
        # Plot the yield curve
        plot_yield_curve(maturities, yields)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
