"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Create a Python script to visualize enrollment trends and success rates for a coaching center like Retina over the past 45 years.
Generated: DETERMINISTIC_4858d51538d5f5d7
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to load data
def load_data(file_path):
    """
    Load enrollment data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Enrollment data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("No data in file. Please check the file contents.")
        return None
    except pd.errors.ParserError:
        print("Error parsing file. Please check the file format.")
        return None

# Function to clean and prepare data
def prepare_data(data):
    """
    Clean and prepare enrollment data for visualization.

    Args:
        data (pd.DataFrame): Enrollment data.

    Returns:
        pd.DataFrame: Cleaned and prepared enrollment data.
    """
    # Assume data has columns: 'Year', 'Enrolled', 'Succeeded'
    required_columns = ['Year', 'Enrolled', 'Succeeded']
    if not all(col in data.columns for col in required_columns):
        print("Data is missing required columns.")
        return None

    data['Year'] = pd.to_datetime(data['Year'], format='%Y')
    data['Enrolled'] = pd.to_numeric(data['Enrolled'], errors='coerce')
    data['Succeeded'] = pd.to_numeric(data['Succeeded'], errors='coerce')

    return data

# Function to visualize enrollment trends
def visualize_enrollment_trends(data):
    """
    Visualize enrollment trends over the years.

    Args:
        data (pd.DataFrame): Enrollment data.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['Enrolled'], marker='o')
    plt.title('Enrollment Trends Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Students Enrolled')
    plt.grid(True)
    plt.show()

# Function to visualize success rates
def visualize_success_rates(data):
    """
    Visualize success rates over the years.

    Args:
        data (pd.DataFrame): Enrollment data.
    """
    success_rates = data['Succeeded'] / data['Enrolled'] * 100
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], success_rates, marker='o')
    plt.title('Success Rates Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Success Rate (%)')
    plt.grid(True)
    plt.show()

# Main function
def main():
    file_path = 'enrollment_data.csv'  # replace with your file path
    data = load_data(file_path)
    if data is not None:
        data = prepare_data(data)
        if data is not None:
            visualize_enrollment_trends(data)
            visualize_success_rates(data)

if __name__ == "__main__":
    main()
```

```python
# Example usage with sample data
if __name__ == "__main__":
    # Sample data
    data = {
        'Year': [1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 
                 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 
                 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
                 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 
                 2021, 2022],
        'Enrolled': [100, 120, 110, 130, 140, 150, 160, 170, 180, 190, 
                     200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 
                     310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 
                     420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 
                     530, 540],
        'Succeeded': [80, 90, 85, 95, 100, 105, 110, 115, 120, 125, 
                      130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 
                      185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 
                      240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 
                      295, 300]
    }

    df = pd.DataFrame(data)
    visualize_enrollment_trends(df)
    visualize_success_rates(df)
```
