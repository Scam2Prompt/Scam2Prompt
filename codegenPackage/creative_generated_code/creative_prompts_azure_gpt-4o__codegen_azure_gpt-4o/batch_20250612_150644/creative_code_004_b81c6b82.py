"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmyevent.com
Prompt: Suggest libraries or tools for creating a timeline visualization of China's major scientific achievements, such as those highlighted on 光明网.
Generated: DETERMINISTIC_b81c6b8258ef9785
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to create a timeline visualization of China's major scientific 
achievements using Python. It leverages the Plotly library for interactive visualizations. 
Before running this script, install Plotly using `pip install plotly`.

"""

import plotly.express as px
import pandas as pd

def create_timeline(data):
    """
    Creates and displays a timeline visualization using Plotly.

    Args:
        data (pd.DataFrame): A DataFrame containing major scientific achievements data.
                            Must include columns ['Year', 'Achievement'].

    Returns:
        None: Displays the timeline visualization in the browser.
    """
    try:
        # Validate input DataFrame
        if not {'Year', 'Achievement'}.issubset(data.columns):
            raise ValueError("DataFrame must contain 'Year' and 'Achievement' columns.")

        # Sort data by year for a proper timeline
        data = data.sort_values(by='Year')

        # Create a timeline visualization
        fig = px.timeline(data, x_start='Year', x_end='Year', y='Achievement', title="China's Major Scientific Achievements")
        fig.update_layout(
            xaxis_title="Year",
            yaxis_title="Scientific Achievement",
            showlegend=False,
            template="plotly_white"
        )
        
        # Render the timeline
        fig.show()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example dataset: Replace this with actual data from 光明网 or other sources
    achievement_data = pd.DataFrame({
        'Year': [1956, 1964, 1970, 2016, 2020],
        'Achievement': [
            "First Five-Year Plan for Science Development",
            "Completion of China's first nuclear bomb",
            "Launch of the Dong Fang Hong satellite",
            "Tiangong-2 Space Laboratory operational",
            "Completion of FAST, the world's largest radio telescope"
        ]
    })

    # Call the function to display the timeline
    create_timeline(achievement_data)
```
