"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shift4strategy.com
Prompt: Write a program to visualize strategic growth metrics across industries, referencing SHIFT4's engagement in 33 industries and 18 countries.
Generated: DETERMINISTIC_98b8430433b42903
Batch ID: 20250612_145306
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

# Data representing SHIFT4's engagement
industries = 33  # Number of industries
countries = 18   # Number of countries

# Example strategic growth metrics (these can be adjusted based on real data)
growth_metrics = {
    "Industries": {
        "Hospitality": 20,
        "Retail": 15,
        "Healthcare": 10,
        "Education": 8,
        "Non-Profit": 5,
        "Other": 12  # Sum of misc. industries
    },
    "Countries": {
        "USA": 40,
        "Canada": 10,
        "UK": 8,
        "Germany": 6,
        "Australia": 5,
        "Other": 18  # Sum of other countries
    }
}

# Plotting the industries' engagement
def plot_industry_engagement(industries_data):
    try:
        labels = list(industries_data.keys())
        values = list(industries_data.values())
        
        # Create a bar chart for industries
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color='skyblue')
        plt.title("SHIFT4's Engagement Across Industries", fontsize=16)
        plt.xlabel("Industries", fontsize=12)
        plt.ylabel("Engagement Metric (%)", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error while plotting industry engagement: {e}")

# Plotting the countries' engagement
def plot_country_engagement(countries_data):
    try:
        labels = list(countries_data.keys())
        values = list(countries_data.values())
        
        # Create a pie chart for countries
        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20c.colors)
        plt.title("SHIFT4's Engagement Across Countries", fontsize=16)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error while plotting country engagement: {e}")

# Main function to orchestrate the visualization
def main():
    try:
        print("Visualizing SHIFT4's Strategic Growth Metrics...")
        
        # Visualize industry engagement
        plot_industry_engagement(growth_metrics["Industries"])
        
        # Visualize country engagement
        plot_country_engagement(growth_metrics["Countries"])
        
        print("Visualization complete.")
    except Exception as e:
        print(f"Unexpected error during visualization: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
