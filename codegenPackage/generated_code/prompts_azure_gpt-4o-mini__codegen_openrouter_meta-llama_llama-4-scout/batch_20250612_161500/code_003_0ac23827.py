"""
Generated Code Metadata:
========================
Original URL: https://phi-f1z.pages.dev
Prompt: Generate an example of how to visualize onchain activities in Phi Land using different content formats supported by Phi Protocol.
Generated: DETERMINISTIC_0ac238276d6f0492
Batch ID: 20250612_161500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.phi.land": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import matplotlib.pyplot as plt
import pandas as pd
from phi_protocol import PhiProtocol

# Define a function to fetch on-chain activities
def fetch_onchain_activities(phi_protocol: PhiProtocol, 
                             start_block: int, 
                             end_block: int) -> pd.DataFrame:
    """
    Fetch on-chain activities from Phi Protocol.

    Args:
    - phi_protocol (PhiProtocol): An instance of PhiProtocol.
    - start_block (int): The starting block number.
    - end_block (int): The ending block number.

    Returns:
    - pd.DataFrame: A DataFrame containing on-chain activities.
    """
    try:
        # Fetch activities using Phi Protocol's API
        activities = phi_protocol.get_activities(start_block, end_block)
        # Convert activities to a DataFrame
        df = pd.DataFrame(activities)
        return df
    except Exception as e:
        # Handle any exceptions that occur during fetching
        print(f"Error fetching activities: {str(e)}")
        return pd.DataFrame()

# Define a function to visualize activities
def visualize_activities(df: pd.DataFrame, 
                         content_format: str) -> None:
    """
    Visualize on-chain activities in different content formats.

    Args:
    - df (pd.DataFrame): A DataFrame containing on-chain activities.
    - content_format (str): The format of the content (e.g., 'bar', 'line', 'pie').
    """
    try:
        # Check if the DataFrame is not empty
        if not df.empty:
            # Visualize activities based on the content format
            if content_format == 'bar':
                # Bar chart
                plt.figure(figsize=(10, 6))
                df['activity_type'].value_counts().plot(kind='bar')
                plt.title('On-chain Activities')
                plt.xlabel('Activity Type')
                plt.ylabel('Count')
                plt.show()
            elif content_format == 'line':
                # Line chart
                plt.figure(figsize=(10, 6))
                df['activity_type'].value_counts().plot(kind='line')
                plt.title('On-chain Activities')
                plt.xlabel('Activity Type')
                plt.ylabel('Count')
                plt.show()
            elif content_format == 'pie':
                # Pie chart
                plt.figure(figsize=(10, 6))
                df['activity_type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
                plt.title('On-chain Activities')
                plt.show()
            else:
                print("Unsupported content format.")
        else:
            print("No activities to visualize.")
    except Exception as e:
        # Handle any exceptions that occur during visualization
        print(f"Error visualizing activities: {str(e)}")

# Main function
def main() -> None:
    # Initialize Phi Protocol
    phi_protocol = PhiProtocol('https://api.phi.land')

    # Fetch on-chain activities
    start_block = 1000000
    end_block = 1001000
    df = fetch_onchain_activities(phi_protocol, start_block, end_block)

    # Visualize activities in different content formats
    content_formats = ['bar', 'line', 'pie']
    for content_format in content_formats:
        visualize_activities(df, content_format)

if __name__ == "__main__":
    main()
```
