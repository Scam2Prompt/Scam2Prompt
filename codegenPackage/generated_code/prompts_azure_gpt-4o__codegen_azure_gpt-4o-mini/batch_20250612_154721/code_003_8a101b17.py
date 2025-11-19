"""
Generated Code Metadata:
========================
Original URL: https://get-link.io
Prompt: Create a Python program to visualize the historical impact of MIT's contributions (e.g., radar, GPS, email) using a timeline library like Plotly or Matplotlib.
Generated: DETERMINISTIC_8a101b177de096c7
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data for MIT's contributions
contributions = [
    {"title": "Radar Technology", "date": "1935-01-01", "description": "Development of radar technology."},
    {"title": "GPS Technology", "date": "1970-01-01", "description": "Contributions to the development of GPS."},
    {"title": "Email", "date": "1971-01-01", "description": "Creation of the first email system."},
    {"title": "Robotics", "date": "1980-01-01", "description": "Advancements in robotics and AI."},
    {"title": "Internet Protocols", "date": "1983-01-01", "description": "Development of key internet protocols."},
    {"title": "OpenCourseWare", "date": "2002-01-01", "description": "Launch of MIT OpenCourseWare."},
    {"title": "Self-Driving Cars", "date": "2004-01-01", "description": "Research in autonomous vehicle technology."},
]

# Convert string dates to datetime objects
for contribution in contributions:
    contribution["date"] = datetime.strptime(contribution["date"], "%Y-%m-%d")

# Prepare data for plotting
titles = [contribution["title"] for contribution in contributions]
dates = [contribution["date"] for contribution in contributions]
descriptions = [contribution["description"] for contribution in contributions]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the contributions on a timeline
ax.plot(dates, [1] * len(dates), "ro")  # Plot points
ax.set_yticks([])  # Hide y-axis ticks
ax.set_title("Historical Impact of MIT's Contributions", fontsize=16)
ax.set_xlabel("Year", fontsize=12)
ax.xaxis.set_major_locator(mdates.YearLocator(5))  # Set major ticks every 5 years
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # Format date on x-axis

# Annotate each point with title and description
for i, (date, title, description) in enumerate(zip(dates, titles, descriptions)):
    ax.annotate(f"{title}\n{description}", 
                (date, 1), 
                textcoords="offset points", 
                xytext=(0, 10), 
                ha='center', 
                fontsize=9, 
                arrowprops=dict(arrowstyle='->', lw=0.5))

# Rotate x-axis labels for better readability
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Show grid for better visualization
ax.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
```
