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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def generate_yield_curve_data(maturities, yields):
    """
    Generate a DataFrame with maturities and corresponding yields.

    Parameters:
    maturities (list): List of maturities in years.
    yields (list): List of yields corresponding to the maturities.

    Returns:
    pd.DataFrame: A DataFrame containing maturities and yields.
    """
    if len(maturities) != len(yields):
        raise ValueError("Maturities and yields lists must be the same length.")
    
    data = {'Maturity': maturities, 'Yield': yields}
    return pd.DataFrame(data)

def plot_yield_curve_matplotlib(data):
    """
    Plot yield curve using Matplotlib.
    
    Parameters:
    data (pd.DataFrame): DataFrame with maturities and yields.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['Maturity'], data['Yield'], marker='o')
    plt.title('Yield Curve')
    plt.xlabel('Maturity (Years)')
    plt.ylabel('Yield (%)')
    plt.grid()
    plt.axhline(0, color='black', lw=0.8, ls='--')
    plt.xlim(0, max(data['Maturity']) + 1)
    plt.ylim(min(data['Yield']) - 1, max(data['Yield']) + 1)
    plt.show()

def plot_yield_curve_plotly(data):
    """
    Plot yield curve using Plotly.
    
    Parameters:
    data (pd.DataFrame): DataFrame with maturities and yields.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Maturity'], y=data['Yield'],
                              mode='lines+markers',
                              name='Yield Curve'))
    
    fig.update_layout(title='Yield Curve',
                      xaxis_title='Maturity (Years)',
                      yaxis_title='Yield (%)',
                      yaxis=dict(showgrid=True),
                      xaxis=dict(showgrid=True))
    
    fig.show()

# Example usage
if __name__ == '__main__':
    # Sample maturities and yields
    maturities = [1, 2, 5, 10, 20, 30]
    yields = [1.5, 1.75, 2.5, 3.0, 3.5, 3.8]

    # Generate yield curve data
    try:
        yield_data = generate_yield_curve_data(maturities, yields)

        # Plot using Matplotlib
        plot_yield_curve_matplotlib(yield_data)

        # Plot using Plotly
        plot_yield_curve_plotly(yield_data)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
