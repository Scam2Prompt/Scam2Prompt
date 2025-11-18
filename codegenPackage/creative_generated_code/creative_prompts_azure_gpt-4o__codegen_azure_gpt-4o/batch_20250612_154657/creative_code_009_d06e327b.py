"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starshot90.com
Prompt: Create a program that visualizes web analytics data to improve online business performance, as discussed in the "Web Analytics: Understanding and Utilizing Data" section of the Star Shot 90 website.
Generated: DETERMINISTIC_d06e327b226cb4a1
Batch ID: 20250612_154657
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
from collections import defaultdict


def read_csv(file_path):
    """
    Reads a CSV file and returns the data as a list of dictionaries.

    :param file_path: Path to the CSV file
    :return: List of dictionaries containing the data
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def process_data(data):
    """
    Processes web analytics data to calculate metrics like page views and bounce rates.

    :param data: List of dictionaries containing web analytics data
    :return: Dictionary with aggregated metrics
    """
    aggregated_data = defaultdict(lambda: {'page_views': 0, 'bounces': 0})

    for row in data:
        try:
            page = row['Page']
            page_views = int(row['PageViews'])
            bounces = int(row['Bounces'])

            aggregated_data[page]['page_views'] += page_views
            aggregated_data[page]['bounces'] += bounces
        except KeyError as e:
            print(f"Error: Missing key {e} in data row.")
        except ValueError as e:
            print(f"Error: Invalid value in data row - {e}")

    return aggregated_data


def visualize_data(aggregated_data):
    """
    Visualizes the web analytics data using bar charts.

    :param aggregated_data: Dictionary with aggregated metrics
    """
    pages = list(aggregated_data.keys())
    page_views = [metrics['page_views'] for metrics in aggregated_data.values()]
    bounces = [metrics['bounces'] for metrics in aggregated_data.values()]

    plt.figure(figsize=(10, 5))
    
    # Plotting page views
    plt.subplot(1, 2, 1)
    plt.bar(pages, page_views, color='blue')
    plt.title('Page Views Per Page')
    plt.xlabel('Page')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)

    # Plotting bounces
    plt.subplot(1, 2, 2)
    plt.bar(pages, bounces, color='red')
    plt.title('Bounces Per Page')
    plt.xlabel('Page')
    plt.ylabel('Bounces')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to read, process, and visualize web analytics data.
    """
    # Path to web analytics data CSV file
    file_path = 'web_analytics_data.csv'

    # Step 1: Read the data
    data = read_csv(file_path)

    if not data:
        print("No data available to process.")
        return

    # Step 2: Process the data
    aggregated_data = process_data(data)

    # Step 3: Visualize the data
    visualize_data(aggregated_data)


if __name__ == '__main__':
    main()
```
