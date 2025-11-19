"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write a script to analyze and compare the performance of different car models, including the Chevrolet Cobalt SS/TC, based on specifications like horsepower, torque, and lap times.
Generated: DETERMINISTIC_36704ab2722aaf43
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

# Define the car specifications
car_data = [
    {"Model": "Chevrolet Cobalt SS/TC", "Horsepower": 260, "Torque": 260, "LapTime": 85.3},
    {"Model": "Ford Mustang GT", "Horsepower": 450, "Torque": 410, "LapTime": 82.5},
    {"Model": "Mazda MX-5 Miata", "Horsepower": 181, "Torque": 151, "LapTime": 90.2},
    {"Model": "Subaru WRX STI", "Horsepower": 310, "Torque": 290, "LapTime": 84.1},
    {"Model": "BMW M3", "Horsepower": 473, "Torque": 406, "LapTime": 81.7},
]

# Convert the car data into a pandas DataFrame
df = pd.DataFrame(car_data)

# Function to normalize data for comparison
def normalize_column(column):
    """
    Normalize a column to a scale of 0 to 1 for comparison purposes.
    """
    return (column - column.min()) / (column.max() - column.min())

# Normalize the specifications for comparison
df["NormalizedHorsepower"] = normalize_column(df["Horsepower"])
df["NormalizedTorque"] = normalize_column(df["Torque"])
df["NormalizedLapTime"] = normalize_column(df["LapTime"])

# Calculate a performance score based on normalized values
# Higher horsepower and torque are better, lower lap time is better
df["PerformanceScore"] = (
    df["NormalizedHorsepower"] * 0.4 +  # Weight: 40%
    df["NormalizedTorque"] * 0.3 +      # Weight: 30%
    (1 - df["NormalizedLapTime"]) * 0.3 # Weight: 30%, inverted lap time
)

# Sort cars by performance score in descending order
df_sorted = df.sort_values(by="PerformanceScore", ascending=False)

# Display the results
print("Car Performance Comparison:")
print(df_sorted[["Model", "Horsepower", "Torque", "LapTime", "PerformanceScore"]])

# Save the results to a CSV file
output_file = "car_performance_comparison.csv"
try:
    df_sorted.to_csv(output_file, index=False)
    print(f"\nResults saved to {output_file}")
except Exception as e:
    print(f"\nError saving results to file: {e}")
```
