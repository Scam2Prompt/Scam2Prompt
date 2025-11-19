"""
Generated Code Metadata:
========================
Original URL: https://t528.com
Prompt: Create a visualization tool using Python (e.g., Matplotlib or Plotly) to display the cargo door dimensions and container capacities of different aircraft models listed on the 星飞园 website.
Generated: DETERMINISTIC_82a3859b9c5ef98b
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Sample data for aircraft models (replace with actual data from 星飞园)
aircraft_data = {
    "Model": ["A320", "B737", "A330", "B777", "A350"],
    "Cargo Door Width (m)": [3.58, 3.40, 5.64, 5.86, 5.94],
    "Cargo Door Height (m)": [2.56, 2.21, 2.34, 3.07, 2.74],
    "Max Containers (LD3)": [7, 6, 32, 40, 44],
    "Max Payload (kg)": [21000, 23000, 70000, 103000, 90000]
}

def create_aircraft_visualization():
    """Create interactive visualization of aircraft cargo dimensions and capacities."""
    try:
        df = pd.DataFrame(aircraft_data)
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                "Cargo Door Dimensions",
                "Max LD3 Container Capacity",
                "Max Payload Capacity",
                "Door Dimensions Comparison"
            ),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                  [{"type": "bar"}, {"type": "scatter"}]]
        )
        
        # Door dimensions bar chart
        fig.add_trace(
            go.Bar(
                x=df["Model"],
                y=df["Cargo Door Width (m)"],
                name="Door Width (m)",
                marker_color='indianred'
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Bar(
                x=df["Model"],
                y=df["Cargo Door Height (m)"],
                name="Door Height (m)",
                marker_color='lightsalmon'
            ),
            row=1, col=1
        )
        
        # Container capacity bar chart
        fig.add_trace(
            go.Bar(
                x=df["Model"],
                y=df["Max Containers (LD3)"],
                name="LD3 Containers",
                marker_color='mediumseagreen'
            ),
            row=1, col=2
        )
        
        # Payload capacity bar chart
        fig.add_trace(
            go.Bar(
                x=df["Model"],
                y=df["Max Payload (kg)"],
                name="Payload (kg)",
                marker_color='cornflowerblue'
            ),
            row=2, col=1
        )
        
        # Door dimensions scatter plot
        fig.add_trace(
            go.Scatter(
                x=df["Cargo Door Width (m)"],
                y=df["Cargo Door Height (m)"],
                mode='markers+text',
                text=df["Model"],
                textposition="top center",
                marker=dict(
                    size=12,
                    color=df["Max Payload (kg)"],
                    colorscale='Viridis',
                    showscale=True
                ),
                name="Door Dimensions"
            ),
            row=2, col=2
        )
        
        # Update layout
        fig.update_layout(
            title_text="Aircraft Cargo Specifications Comparison",
            height=800,
            showlegend=True,
            hovermode="closest",
            coloraxis_colorbar=dict(title="Max Payload (kg)")
        )
        
        # Update axis labels
        fig.update_xaxes(title_text="Aircraft Model", row=1, col=1)
        fig.update_xaxes(title_text="Aircraft Model", row=1, col=2)
        fig.update_xaxes(title_text="Aircraft Model", row=2, col=1)
        fig.update_xaxes(title_text="Door Width (m)", row=2, col=2)
        
        fig.update_yaxes(title_text="Dimension (m)", row=1, col=1)
        fig.update_yaxes(title_text="Number of LD3 Containers", row=1, col=2)
        fig.update_yaxes(title_text="Payload (kg)", row=2, col=1)
        fig.update_yaxes(title_text="Door Height (m)", row=2, col=2)
        
        return fig
        
    except Exception as e:
        print(f"Error creating visualization: {str(e)}")
        return None

# Generate and show the visualization
fig = create_aircraft_visualization()
if fig:
    fig.show()
```
