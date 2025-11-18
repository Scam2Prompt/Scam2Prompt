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
import matplotlib.pyplot as plt
import numpy as np

# Sample data for visualization
# Assuming these metrics are collected over a series of months
months = ["January", "February", "March", "April", "May", "June"]
apartments_constructed = [10, 20, 30, 50, 40, 60]  # Number of apartments constructed
hours_worked = [200, 300, 400, 600, 500, 700]      # Total hours worked
jobs_generated = [5, 10, 15, 25, 20, 30]            # Jobs generated

# Error handling for data consistency
def validate_data(*args):
    """Ensure that all data lists have the same length."""
    length = len(args[0])
    for arg in args:
        if len(arg) != length:
            raise ValueError("All data lists must have the same length.")

# Validate the input data
validate_data(apartments_constructed, hours_worked, jobs_generated)

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

# Plot for Apartments Constructed
axs[0].bar(months, apartments_constructed, color='skyblue')
axs[0].set_title('Apartments Constructed')
axs[0].set_ylabel('Number of Apartments')
axs[0].grid(axis='y')

# Plot for Hours Worked
axs[1].bar(months, hours_worked, color='lightgreen')
axs[1].set_title('Hours Worked')
axs[1].set_ylabel('Total Hours')
axs[1].grid(axis='y')

# Plot for Jobs Generated
axs[2].bar(months, jobs_generated, color='salmon')
axs[2].set_title('Jobs Generated')
axs[2].set_ylabel('Number of Jobs')
axs[2].grid(axis='y')

# Set common x-label
axs[2].set_xlabel('Months')

# Adjust layout
plt.tight_layout()

# Save the figure if needed
plt.savefig('construction_project_progress.png')

# Show the plots
plt.show()
```
