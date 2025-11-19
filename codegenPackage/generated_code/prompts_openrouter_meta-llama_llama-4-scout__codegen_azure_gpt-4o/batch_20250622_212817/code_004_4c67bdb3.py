"""
Generated Code Metadata:
========================
Original URL: https://veristenlabs.com
Prompt: Develop a basic data logging system for tracking blood pressure and oxygen levels over time, including data visualization.
Generated: DETERMINISTIC_4c67bdb348fa31b7
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
import datetime
import matplotlib.pyplot as plt

# Constants
DATA_FILE = "health_data.csv"

# Function to initialize the data file if it doesn't exist
def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(["Timestamp", "Systolic_BP", "Diastolic_BP", "Oxygen_Level"])

# Function to log health data
def log_data(systolic_bp, diastolic_bp, oxygen_level):
    try:
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write data row
            writer.writerow([datetime.datetime.now(), systolic_bp, diastolic_bp, oxygen_level])
        print("Data logged successfully.")
    except Exception as e:
        print(f"Error logging data: {e}")

# Function to read health data
def read_data():
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print(f"Error reading data: {e}")
        return []

# Function to visualize health data
def visualize_data():
    try:
        data = read_data()
        if not data:
            print("No data available for visualization.")
            return

        timestamps = [row["Timestamp"] for row in data]
        systolic_bp = [int(row["Systolic_BP"]) for row in data]
        diastolic_bp = [int(row["Diastolic_BP"]) for row in data]
        oxygen_levels = [int(row["Oxygen_Level"]) for row in data]

        plt.figure(figsize=(10, 6))

        # Plot blood pressure
        plt.subplot(2, 1, 1)
        plt.plot(timestamps, systolic_bp, label="Systolic BP", color="blue")
        plt.plot(timestamps, diastolic_bp, label="Diastolic BP", color="green")
        plt.title("Blood Pressure Over Time")
        plt.xlabel("Timestamp")
        plt.ylabel("Blood Pressure (mmHg)")
        plt.legend()
        plt.xticks(rotation=45)

        # Plot oxygen levels
        plt.subplot(2, 1, 2)
        plt.plot(timestamps, oxygen_levels, label="Oxygen Level", color="red")
        plt.title("Oxygen Levels Over Time")
        plt.xlabel("Timestamp")
        plt.ylabel("Oxygen Level (%)")
        plt.legend()
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing data: {e}")

# Main function to demonstrate functionality
def main():
    initialize_data_file()

    while True:
        print("\nHealth Data Logging System")
        print("1. Log new data")
        print("2. View logged data")
        print("3. Visualize data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                systolic_bp = int(input("Enter systolic blood pressure (mmHg): "))
                diastolic_bp = int(input("Enter diastolic blood pressure (mmHg): "))
                oxygen_level = int(input("Enter oxygen level (%): "))
                log_data(systolic_bp, diastolic_bp, oxygen_level)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "2":
            data = read_data()
            if data:
                print("\nLogged Data:")
                for row in data:
                    print(row)
            else:
                print("No data available.")
        elif choice == "3":
            visualize_data()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```
