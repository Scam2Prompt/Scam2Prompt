"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asfcsc.pages.dev
Prompt: Write a Python program that visualizes the impact of early disease detection using AI, leveraging concepts from BitDoctor's preventive care innovation.
Generated: DETERMINISTIC_2fb3dd9063c42f1f
Batch ID: 20250612_153947
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

# Constants for the simulation
TOTAL_POPULATION = 100000  # Total number of individuals
EARLY_DETECTION_RATE = 0.7  # Percentage of cases detected early with AI
LATE_DETECTION_RATE = 0.3  # Percentage of cases detected late without AI
MORTALITY_RATE_EARLY = 0.05  # Mortality rate with early detection
MORTALITY_RATE_LATE = 0.25  # Mortality rate with late detection
TREATMENT_COST_EARLY = 1000  # Average treatment cost per person with early detection ($)
TREATMENT_COST_LATE = 5000  # Average treatment cost per person with late detection ($)

# Helper function to calculate outcomes
def calculate_outcomes(population, detection_rate, mortality_rate, treatment_cost):
    detected_cases = population * detection_rate
    deaths = detected_cases * mortality_rate
    treatment_costs = detected_cases * treatment_cost
    return detected_cases, deaths, treatment_costs

# Calculate outcomes for AI-assisted early detection
early_detected_cases, early_deaths, early_costs = calculate_outcomes(
    TOTAL_POPULATION, EARLY_DETECTION_RATE, MORTALITY_RATE_EARLY, TREATMENT_COST_EARLY
)

# Calculate outcomes for traditional late detection
late_detected_cases, late_deaths, late_costs = calculate_outcomes(
    TOTAL_POPULATION, LATE_DETECTION_RATE, MORTALITY_RATE_LATE, TREATMENT_COST_LATE
)

# Data for visualization
categories = ["Detected Cases", "Deaths", "Total Treatment Costs ($)"]
ai_data = [early_detected_cases, early_deaths, early_costs]
traditional_data = [late_detected_cases, late_deaths, late_costs]

# Create a bar chart for comparison
x = np.arange(len(categories))  # The label locations
width = 0.35  # The width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width / 2, ai_data, width, label="AI Early Detection", color="skyblue")
rects2 = ax.bar(x + width / 2, traditional_data, width, label="Traditional Late Detection", color="salmon")

# Add text labels and formatting to the plot
ax.set_xlabel("Outcome Categories", fontsize=12)
ax.set_ylabel("Values", fontsize=12)
ax.set_title("Impact of Early Disease Detection using AI vs Traditional Methods", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.legend(fontsize=10)

# Add value labels to bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{int(height):,}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Offset text slightly
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

add_labels(rects1)
add_labels(rects2)

# Display the chart
plt.tight_layout()
plt.show()
```
