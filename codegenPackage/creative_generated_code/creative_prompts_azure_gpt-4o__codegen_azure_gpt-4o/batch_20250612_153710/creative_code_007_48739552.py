"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Generate code to visualize consulting project timelines using Python libraries like matplotlib or seaborn.
Generated: DETERMINISTIC_4873955226d9f564
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Sample data for consulting project timelines
data = [
    {"Project": "Project A", "Start Date": "2023-01-01", "End Date": "2023-03-15"},
    {"Project": "Project B", "Start Date": "2023-02-01", "End Date": "2023-05-30"},
    {"Project": "Project C", "Start Date": "2023-03-10", "End Date": "2023-06-01"},
    {"Project": "Project D", "Start Date": "2023-01-15", "End Date": "2023-04-01"}
]

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert start and end dates to datetime objects for plotting
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Generate the duration of each project
df['Duration'] = (df['End Date'] - df['Start Date']).dt.days

# Set up the figure and axis for the timeline plot
plt.figure(figsize=(10, 6))
plt.title("Consulting Project Timelines", fontsize=16)
plt.xlabel("Timeline", fontsize=12)
plt.ylabel("Projects", fontsize=12)

# Create the timeline visualization
for i, row in enumerate(df.itertuples()):
    # Plot each project's timeline as a horizontal bar
    plt.plot(
        [row._2, row._3],  # Start and End Dates
        [i, i],            # Y-position (Project Index)
        linewidth=6,
        label=row.Project
    )
    # Annotate project name next to the bar
    plt.text(row._3 + datetime.timedelta(days=2), i, row.Project, fontsize=9, verticalalignment='center')

# Adjust y-axis to display project names instead of numeric indices
plt.yticks(range(len(df)), df["Project"])

# Add grid for better readability
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
```
