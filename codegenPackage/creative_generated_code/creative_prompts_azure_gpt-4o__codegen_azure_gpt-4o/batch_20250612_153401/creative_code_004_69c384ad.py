"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Write a script to visualize the progress of construction projects using Python and a data visualization library (e.g., `Matplotlib` or `Plotly`), incorporating metrics like apartments constructed, hours worked, and jobs generated, inspired by INARO S.A.S.'s statistics.
Generated: DETERMINISTIC_69c384ad23a23e49
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import plotly.graph_objects as go

# Example data representing construction projects
# Replace this with actual data or integrate with a database
data = {
    'Project': ['Project A', 'Project B', 'Project C', 'Project D'],
    'Apartments Constructed': [120, 85, 45, 150],
    'Hours Worked': [3000, 2500, 1500, 4000],
    'Jobs Generated': [50, 40, 20, 70]
}

# Create a DataFrame for easier manipulation
df = pd.DataFrame(data)

# Error handling: Ensure data integrity
try:
    if df.isnull().values.any():
        raise ValueError("Data contains null values. Please check the input.")
except ValueError as e:
    print(e)
    exit(1)

# Initialize a Plotly figure
fig = go.Figure()

# Add a bar chart for Apartments Constructed
fig.add_trace(
    go.Bar(
        x=df['Project'],
        y=df['Apartments Constructed'],
        name='Apartments Constructed',
        marker=dict(color='blue')
    )
)

# Add a line chart for Hours Worked
fig.add_trace(
    go.Scatter(
        x=df['Project'],
        y=df['Hours Worked'],
        name='Hours Worked',
        mode='lines+markers',
        marker=dict(color='green')
    )
)

# Add a bar chart for Jobs Generated
fig.add_trace(
    go.Bar(
        x=df['Project'],
        y=df['Jobs Generated'],
        name='Jobs Generated',
        marker=dict(color='orange')
    )
)

# Update layout for better visualization
fig.update_layout(
    title='Construction Project Progress',
    xaxis_title='Project',
    yaxis_title='Metrics',
    barmode='group',  # Group bars for better comparison
    legend_title='Metrics',
    template='plotly_white'
)

# Error handling: Check if the figure has traces
if len(fig.data) == 0:
    print("Visualization failed. No data to display.")
    exit(1)

# Render the plot
fig.show()
```
