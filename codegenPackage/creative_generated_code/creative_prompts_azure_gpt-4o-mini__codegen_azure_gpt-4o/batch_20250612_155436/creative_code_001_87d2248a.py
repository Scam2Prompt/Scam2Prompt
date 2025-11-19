"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rearb.pages.dev
Prompt: Can you provide a code snippet that demonstrates how to use the Rearb library for data manipulation?
Generated: DETERMINISTIC_87d2248a90b1ba73
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary modules from the Rearb library
from rearb import Rearb

# Define a dataset as an example for manipulation
data = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 35},
]

# Initialize Rearb for data manipulation
rearb = Rearb(data)

# Example: Apply a transformation to add a new field to each record
def add_is_adult(record):
    """
    Adds a new field 'is_adult' to the record based on age.
    """
    record["is_adult"] = record["age"] >= 18
    return record

try:
    # Transform the dataset
    transformed_data = rearb.transform(add_is_adult)

    # Filter the dataset to include only adults
    adults_only = transformed_data.filter(lambda record: record["is_adult"])

    # Sort the dataset by age in descending order
    sorted_data = adults_only.sort(key=lambda record: record["age"], reverse=True)

    # Output the final dataset
    print("Final sorted dataset of adults:")
    for record in sorted_data.get_data():
        print(record)

except Exception as e:
    # Handle any errors that occur during manipulation
    print(f"An error occurred: {e}")
```
