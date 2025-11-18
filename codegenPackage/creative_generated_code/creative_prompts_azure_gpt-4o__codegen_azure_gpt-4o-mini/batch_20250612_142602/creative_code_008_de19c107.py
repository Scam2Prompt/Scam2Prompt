"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-llama.github.io
Prompt: Generate code to display intuitive charts and graphs for DeFi protocol performance metrics using DeFiLlama data and Plotly.
Generated: DETERMINISTIC_de19c107ee05ec20
Batch ID: 20250612_142602
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Constants for DeFiLlama API endpoints
DEFI_LLAMA_URL = "https://api.llama.fi"

def fetch_defi_protocols():
    """
    Fetch the list of DeFi protocols and their respective performance metrics from DeFiLlama API.
    
    :return: DataFrame containing protocols and their performance metrics.
    """
    try:
        response = requests.get(f"{DEFI_LLAMA_URL}/protocols")
        response.raise_for_status()  # Raise an error for bad responses
        protocols_data = response.json()
        # Convert to DataFrame for easier manipulation
        return pd.DataFrame(protocols_data)
    except requests.RequestException as e:
        print(f"Error fetching DeFi protocols data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def plot_defi_performance(df):
    """
    Plot performance metrics of DeFi protocols using Plotly.
    
    :param df: DataFrame containing DeFi protocols data.
    """
    if df.empty:
        print("No data available to plot.")
        return

    # Select relevant columns for plotting
    df['TVL'] = df['tvlUsd']  # Total Value Locked in USD
    df['Name'] = df['name']
    
    # Create a bar chart for TVL of the top 10 protocols
    top_protocols = df.nlargest(10, 'TVL')
    fig = px.bar(top_protocols, x='Name', y='TVL', title='Top 10 DeFi Protocols by Total Value Locked (TVL)',
                 labels={'TVL': 'Total Value Locked (USD)', 'Name': 'DeFi Protocols'})
    
    fig.update_layout(xaxis_title='DeFi Protocol', yaxis_title='Total Value Locked (USD)')
    fig.show()  # Display the chart

def main():
    """
    Main function to execute the data fetching and plotting.
    """
    # Fetch data from DeFiLlama API
    protocols_df = fetch_defi_protocols()
    
    # Plot the performance metrics of the fetched protocols
    plot_defi_performance(protocols_df)

if __name__ == "__main__":
    main()
```
