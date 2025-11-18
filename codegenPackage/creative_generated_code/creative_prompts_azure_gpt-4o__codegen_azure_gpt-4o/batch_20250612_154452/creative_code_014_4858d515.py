"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Create a Python script to visualize enrollment trends and success rates for a coaching center like Retina over the past 45 years.
Generated: DETERMINISTIC_4858d51538d5f5d7
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import matplotlib.pyplot as plt
import os

def read_data(file_path):
    """
    Reads enrollment trends and success rates data from a CSV file.

    :param file_path: Path to the CSV file.
    :return: A tuple containing years, enrollment numbers, and success rates.
    """
    years = []
    enrollments = []
    success_rates = []
    
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ensure the required fields exist in each row
                try:
                    years.append(int(row['Year']))
                    enrollments.append(int(row['Enrollment']))
                    success_rates.append(float(row['SuccessRate']))
                except ValueError as e:
                    print(f"Skipping invalid data row: {row}. Error: {e}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    
    return years, enrollments, success_rates

def plot_trends(years, enrollments, success_rates):
    """
    Plots enrollment trends and success rates over time.

    :param years: List of years.
    :param enrollments: List of enrollment numbers.
    :param success_rates: List of success rates.
    """
    if not years or not enrollments or not success_rates:
        print("Error: No valid data available to plot.")
        return
    
    plt.figure(figsize=(10, 6))
    
    # Plot enrollment trends
    plt.subplot(2, 1, 1)
    plt.plot(years, enrollments, marker='o', label="Enrollment", color='blue')
    plt.title("Enrollment Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Enrollments")
    plt.grid(True)
    plt.legend()
    
    # Plot success rates trends
    plt.subplot(2, 1, 2)
    plt.plot(years, success_rates, marker='s', label="Success Rate", color='green')
    plt.title("Success Rates Over Time")
    plt.xlabel("Year")
    plt.ylabel("Success Rate (%)")
    plt.grid(True)
    plt.legend()
    
    # Adjust layout for readability
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the script.
    """
    # Adjust the path to point to your CSV file containing the data
    # Ensure the CSV file has columns: 'Year', 'Enrollment', 'SuccessRate'
    file_path = "enrollment_data.csv"
    
    print("Reading data from file...")
    years, enrollments, success_rates = read_data(file_path)
    
    print("Generating visualizations...")
    plot_trends(years, enrollments, success_rates)

if __name__ == "__main__":
    main()
```
