"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creocollective.io
Prompt: Develop a program to analyze ROI metrics from marketing campaigns, inspired by Creo Collective's case studies like "Record ROI: Coreview."
Generated: DETERMINISTIC_fcd1bf79c55c2f04
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import statistics

def read_campaign_data(file_path):
    """
    Reads marketing campaign data from a CSV file.
    :param file_path: Path to the CSV file
    :return: List of dictionaries containing campaign data
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def calculate_roi_metrics(campaign_data):
    """
    Calculates ROI metrics from campaign data.
    :param campaign_data: List of dictionaries containing campaign data
    :return: Dictionary with calculated metrics
    """
    try:
        rois = []
        for campaign in campaign_data:
            try:
                # Extracting required fields and converting strings to floats
                investment = float(campaign['Investment'])
                revenue = float(campaign['Revenue'])
                
                # ROI = (Revenue - Investment) / Investment * 100
                roi = ((revenue - investment) / investment) * 100
                rois.append(roi)
            except ValueError:
                print(f"Error: Invalid data format in campaign: {campaign}")
                continue

        # Calculate metrics
        metrics = {
            'average_roi': statistics.mean(rois) if rois else 0,
            'min_roi': min(rois) if rois else 0,
            'max_roi': max(rois) if rois else 0
        }
        return metrics
    except Exception as e:
        print(f"Error calculating ROI metrics: {e}")
        return {}

def display_metrics(metrics):
    """
    Displays calculated ROI metrics.
    :param metrics: Dictionary containing ROI metrics
    """
    print("\nMarketing Campaign ROI Metrics:")
    print(f"Average ROI: {metrics.get('average_roi', 0):.2f}%")
    print(f"Minimum ROI: {metrics.get('min_roi', 0):.2f}%")
    print(f"Maximum ROI: {metrics.get('max_roi', 0):.2f}%")

def main():
    """
    Main function to execute the program flow.
    """
    # Input CSV file path
    file_path = input("Enter the path to the campaign data CSV file: ").strip()

    # Step 1: Read campaign data
    campaign_data = read_campaign_data(file_path)

    if not campaign_data:
        print("No data to process. Exiting program.")
        return

    # Step 2: Calculate ROI metrics
    metrics = calculate_roi_metrics(campaign_data)

    # Step 3: Display metrics
    display_metrics(metrics)

if __name__ == "__main__":
    main()
```

### Expected CSV File Format
The CSV file should have the following headers:
- `Campaign Name` (string)
- `Investment` (numeric, e.g., 1000.00)
- `Revenue` (numeric, e.g., 1500.00)
