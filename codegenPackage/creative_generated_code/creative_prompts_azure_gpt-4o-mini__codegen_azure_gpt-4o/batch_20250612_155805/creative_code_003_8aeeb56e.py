"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinescoin.com
Prompt: Develop a code snippet that simulates market research data collection for a new cooking oil brand, highlighting customer preferences and trends in the Mediterranean oil market.
Generated: DETERMINISTIC_8aeeb56e41cb6732
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import csv
from datetime import datetime

def simulate_market_research_data(output_file="market_research_data.csv"):
    """
    Simulates market research data collection for a new cooking oil brand targeting the Mediterranean oil market.
    Data includes customer preferences, age groups, and trends.
    """

    # Define possible values for research data
    customer_age_groups = ["18-25", "26-35", "36-45", "46-55", "56+"]
    oil_preferences = ["Olive Oil", "Sunflower Oil", "Canola Oil", "Avocado Oil", "Grapeseed Oil"]
    purchase_frequencies = ["Weekly", "Monthly", "Occasionally"]
    regions = ["Spain", "Italy", "Greece", "Turkey", "Morocco"]

    # Define number of simulated entries
    num_entries = 500  # Adjust the number for more or less data

    # Open CSV file for writing
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header row
            writer.writerow(["Timestamp", "Age Group", "Oil Preference", "Purchase Frequency", "Region", "Customer Satisfaction"])

            # Write simulated data rows
            for _ in range(num_entries):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Generate current timestamp
                age_group = random.choice(customer_age_groups)
                oil_preference = random.choice(oil_preferences)
                purchase_frequency = random.choice(purchase_frequencies)
                region = random.choice(regions)
                customer_satisfaction = random.randint(1, 10)  # Satisfaction scale: 1 (low) to 10 (high)

                # Write a single row of simulated data
                writer.writerow([timestamp, age_group, oil_preference, purchase_frequency, region, customer_satisfaction])

        print(f"Market research data successfully written to '{output_file}'.")

    # Handle file-related errors
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    # Run simulation and generate data
    simulate_market_research_data()
```
