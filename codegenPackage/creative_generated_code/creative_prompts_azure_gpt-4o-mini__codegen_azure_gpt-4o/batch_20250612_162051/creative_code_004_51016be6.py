"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Suggest a library for visualizing project timelines and resource management in civil engineering, akin to the detailed planning mentioned by C&M Pinnacle.
Generated: DETERMINISTIC_51016be6a11035b9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that demonstrates the use of the `plotly` library for visualizing project timelines and resource management in civil engineering. The code uses a Gantt chart to plot tasks, their start/end dates, and assigned resources.

```python
import plotly.express as px
import pandas as pd

# Sample data for project timeline and resource management in civil engineering
# Each row represents a task, its start/end dates, and the assigned resource
data = {
    "Task": [
        "Foundation Excavation",
        "Concrete Pouring",
        "Steel Framework Installation",
        "Brickwork",
        "Electrical Wiring",
        "Interior Painting",
        "Roof Installation"
    ],
    "Start Date": [
        "2023-10-01",
        "2023-10-05",
        "2023-10-10",
        "2023-10-15",
        "2023-10-20",
        "2023-10-25",
        "2023-10-30"
    ],
    "End Date": [
        "2023-10-04",
        "2023-10-09",
        "2023-10-14",
        "2023-10-19",
        "2023-10-24",
        "2023-10-29",
        "2023-11-03"
    ],
    "Resource": [
        "Excavation Team",
        "Concrete Team",
        "Steelworkers",
        "Bricklayers",
        "Electricians",
        "Painters",
        "Roofing Team"
    ]
}

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Ensure the date columns are in datetime format
df["Start Date"] = pd.to_datetime(df["Start Date"])
df["End Date"] = pd.to_datetime(df["End Date"])

# Create a Gantt chart using Plotly
fig = px.timeline(
    df,
    x_start="Start Date",
    x_end="End Date",
    y="Task",
    color="Resource",
    title="Project Timeline and Resource Management",
    labels={
        "Resource": "Assigned Resource",
        "Task": "Project Task"
    }
)

# Reverse the y-axis to show tasks from top to bottom
fig.update_yaxes(categoryorder="total ascending")

# Show the chart
fig.show()
```

### Prerequisites:
1. Install the required library `plotly` via pip:
   ```bash
   pip install plotly pandas
   ```

### Key Features:
- **Interactive Visualization:** Plotly provides hover data, zoom, and pan functionalities.
- **Color-coded by Resource:** Each task is color-coded based on the assigned resource for better clarity.
- **Error Handling:** The code ensures that date columns are converted to the correct format using `pd.to_datetime`.

This code is ready to use and ensures production-quality practices.
