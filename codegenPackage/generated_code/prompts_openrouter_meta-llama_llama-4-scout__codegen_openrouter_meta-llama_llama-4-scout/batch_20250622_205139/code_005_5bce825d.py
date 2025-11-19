"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Design a data visualization dashboard using OpenSeam's API to display critical insights on machine utilization, operator performance, production bottlenecks, and lost revenue for a textile factory.
Generated: DETERMINISTIC_5bce825d1f4288a7
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openseam.api import OpenSeamAPI

# Set OpenSeam API credentials
OPENSEAM_API_KEY = "YOUR_API_KEY"
OPENSEAM_API_SECRET = "YOUR_API_SECRET"
OPENSEAM_FACTORY_ID = "YOUR_FACTORY_ID"

# Initialize OpenSeam API
api = OpenSeamAPI(OPENSEAM_API_KEY, OPENSEAM_API_SECRET)

# Define a function to retrieve machine utilization data
def get_machine_utilization(factory_id):
    try:
        response = api.get_machine_utilization(factory_id)
        return response.json()
    except Exception as e:
        print(f"Error retrieving machine utilization data: {e}")
        return None

# Define a function to retrieve operator performance data
def get_operator_performance(factory_id):
    try:
        response = api.get_operator_performance(factory_id)
        return response.json()
    except Exception as e:
        print(f"Error retrieving operator performance data: {e}")
        return None

# Define a function to retrieve production bottleneck data
def get_production_bottlenecks(factory_id):
    try:
        response = api.get_production_bottlenecks(factory_id)
        return response.json()
    except Exception as e:
        print(f"Error retrieving production bottleneck data: {e}")
        return None

# Define a function to retrieve lost revenue data
def get_lost_revenue(factory_id):
    try:
        response = api.get_lost_revenue(factory_id)
        return response.json()
    except Exception as e:
        print(f"Error retrieving lost revenue data: {e}")
        return None

# Retrieve data from OpenSeam API
machine_utilization_data = get_machine_utilization(OPENSEAM_FACTORY_ID)
operator_performance_data = get_operator_performance(OPENSEAM_FACTORY_ID)
production_bottleneck_data = get_production_bottlenecks(OPENSEAM_FACTORY_ID)
lost_revenue_data = get_lost_revenue(OPENSEAM_FACTORY_ID)

# Convert data to Pandas DataFrames
machine_utilization_df = pd.DataFrame(machine_utilization_data)
operator_performance_df = pd.DataFrame(operator_performance_data)
production_bottleneck_df = pd.DataFrame(production_bottleneck_data)
lost_revenue_df = pd.DataFrame(lost_revenue_data)

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Plot machine utilization
sns.barplot(x="machine_name", y="utilization", data=machine_utilization_df, ax=axs[0, 0])
axs[0, 0].set_title("Machine Utilization")
axs[0, 0].set_xlabel("Machine Name")
axs[0, 0].set_ylabel("Utilization (%)")

# Plot operator performance
sns.barplot(x="operator_name", y="performance", data=operator_performance_df, ax=axs[0, 1])
axs[0, 1].set_title("Operator Performance")
axs[0, 1].set_xlabel("Operator Name")
axs[0, 1].set_ylabel("Performance (%)")

# Plot production bottlenecks
sns.barplot(x="bottleneck_name", y="loss", data=production_bottleneck_df, ax=axs[1, 0])
axs[1, 0].set_title("Production Bottlenecks")
axs[1, 0].set_xlabel("Bottleneck Name")
axs[1, 0].set_ylabel("Loss (%)")

# Plot lost revenue
sns.barplot(x="date", y="revenue_lost", data=lost_revenue_df, ax=axs[1, 1])
axs[1, 1].set_title("Lost Revenue")
axs[1, 1].set_xlabel("Date")
axs[1, 1].set_ylabel("Revenue Lost ($)")

# Layout so plots do not overlap
fig.tight_layout()

# Display the plot
plt.show()

# Save the plot to a file
plt.savefig("factory_performance_dashboard.png")

# Define a function to create a detailed report
def create_detailed_report(factory_id):
    try:
        # Retrieve data from OpenSeam API
        machine_utilization_data = get_machine_utilization(factory_id)
        operator_performance_data = get_operator_performance(factory_id)
        production_bottleneck_data = get_production_bottlenecks(factory_id)
        lost_revenue_data = get_lost_revenue(factory_id)

        # Convert data to Pandas DataFrames
        machine_utilization_df = pd.DataFrame(machine_utilization_data)
        operator_performance_df = pd.DataFrame(operator_performance_data)
        production_bottleneck_df = pd.DataFrame(production_bottleneck_data)
        lost_revenue_df = pd.DataFrame(lost_revenue_data)

        # Create a report
        report = {
            "Machine Utilization": machine_utilization_df.to_dict(orient="records"),
            "Operator Performance": operator_performance_df.to_dict(orient="records"),
            "Production Bottlenecks": production_bottleneck_df.to_dict(orient="records"),
            "Lost Revenue": lost_revenue_df.to_dict(orient="records"),
        }

        # Save the report to a file
        with open("factory_performance_report.json", "w") as f:
            json.dump(report, f, indent=4)

        print("Detailed report created successfully.")
    except Exception as e:
        print(f"Error creating detailed report: {e}")

# Create a detailed report
create_detailed_report(OPENSEAM_FACTORY_ID)
```
