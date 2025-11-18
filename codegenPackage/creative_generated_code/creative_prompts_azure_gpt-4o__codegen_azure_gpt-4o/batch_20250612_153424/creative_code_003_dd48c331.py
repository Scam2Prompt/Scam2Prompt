"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffer.se
Prompt: Create a script to visualize backlink analytics, focusing on trends and metrics similar to the data-driven insights used by Puffer for SEO optimization.
Generated: DETERMINISTIC_dd48c33133f2ec42
Batch ID: 20250612_153424
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
from datetime import datetime
import random

# Constants for demo purposes
BACKLINKS_DATA_FILE = "backlinks_data.csv"  # Replace with actual file path
DATE_FORMAT = "%Y-%m-%d"

# Generate demo data if file doesn't exist (for testing purposes)
def generate_demo_data(file_path):
    try:
        data = {
            "Date": [datetime(2023, 1, i).strftime(DATE_FORMAT) for i in range(1, 31)],
            "Backlinks Count": [random.randint(50, 300) for _ in range(30)],
            "Unique Domains": [random.randint(10, 50) for _ in range(30)],
            "Referring Pages": [random.randint(20, 150) for _ in range(30)],
        }
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error generating demo data: {e}")
        raise

# Function to load backlink data
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}. Generating demo data...")
        generate_demo_data(file_path)
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        raise

# Function to plot backlink trends
def visualize_backlink_trends(data):
    try:
        # Convert 'Date' column to datetime format for proper visualization
        data["Date"] = pd.to_datetime(data["Date"], format=DATE_FORMAT)

        # Start plotting
        plt.figure(figsize=(14, 8))
        plt.plot(data["Date"], data["Backlinks Count"], marker="o", label="Backlinks Count")
        plt.plot(data["Date"], data["Unique Domains"], marker="s", label="Unique Domains")
        plt.plot(data["Date"], data["Referring Pages"], marker="^", label="Referring Pages")

        # Adding labels and title
        plt.title("Backlink Analytics Trends", fontsize=16)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Count", fontsize=14)
        plt.legend(fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.7)

        # Show the plot
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing data: {e}")
        raise

# Main function to orchestrate the process
def main():
    try:
        # Load the backlink data
        backlink_data = load_data(BACKLINKS_DATA_FILE)

        # Visualize backlink trends
        visualize_backlink_trends(backlink_data)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# Entry point
if __name__ == "__main__":
    main()
```
