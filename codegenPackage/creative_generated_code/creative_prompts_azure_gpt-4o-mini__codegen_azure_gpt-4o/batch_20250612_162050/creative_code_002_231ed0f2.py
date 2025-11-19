"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Write a script to analyze the success metrics of a digital marketing campaign similar to those offered by Tara Media Works.
Generated: DETERMINISTIC_231ed0f2723bc898
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to analyze the success metrics of a digital marketing campaign.
This script calculates metrics such as click-through rate (CTR), conversion rate, and cost per acquisition (CPA).
It also identifies the most successful campaigns based on a set threshold.

Author: [Your Name]
Date: [Insert Date]
"""

import csv
import sys

def read_campaign_data(file_path):
    """
    Reads campaign data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list[dict]: List of dictionaries containing campaign data.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def calculate_metrics(campaign_data):
    """
    Calculates success metrics for each campaign.

    Args:
        campaign_data (list[dict]): List of dictionaries containing campaign data.

    Returns:
        list[dict]: List of dictionaries with added metrics.
    """
    metrics = []
    for campaign in campaign_data:
        try:
            impressions = int(campaign['impressions'])
            clicks = int(campaign['clicks'])
            conversions = int(campaign['conversions'])
            cost = float(campaign['cost'])

            ctr = (clicks / impressions) * 100 if impressions > 0 else 0  # Click-through rate (%)
            conversion_rate = (conversions / clicks) * 100 if clicks > 0 else 0  # Conversion rate (%)
            cpa = cost / conversions if conversions > 0 else float('inf')  # Cost per acquisition
            
            campaign_metrics = {
                'campaign_name': campaign['campaign_name'],
                'impressions': impressions,
                'clicks': clicks,
                'conversions': conversions,
                'cost': cost,
                'ctr': round(ctr, 2),
                'conversion_rate': round(conversion_rate, 2),
                'cpa': round(cpa, 2)
            }
            metrics.append(campaign_metrics)

        except (ValueError, KeyError) as e:
            print(f"Error processing data for campaign '{campaign.get('campaign_name', 'unknown')}': {e}")
    return metrics


def filter_successful_campaigns(metrics, ctr_threshold, conversion_rate_threshold, cpa_threshold):
    """
    Filters campaigns that meet success criteria.

    Args:
        metrics (list[dict]): List of dictionaries with campaign metrics.
        ctr_threshold (float): Minimum click-through rate (%).
        conversion_rate_threshold (float): Minimum conversion rate (%).
        cpa_threshold (float): Maximum cost per acquisition.

    Returns:
        list[dict]: List of dictionaries containing successful campaigns.
    """
    successful_campaigns = [
        campaign for campaign in metrics
        if campaign['ctr'] >= ctr_threshold and 
           campaign['conversion_rate'] >= conversion_rate_threshold and 
           campaign['cpa'] <= cpa_threshold
    ]
    return successful_campaigns


def write_metrics_to_file(metrics, output_file):
    """
    Writes campaign metrics to a CSV file.

    Args:
        metrics (list[dict]): List of dictionaries containing campaign metrics.
        output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, mode='w', newline='') as file:
            fieldnames = ['campaign_name', 'impressions', 'clicks', 'conversions', 'cost', 'ctr', 'conversion_rate', 'cpa']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(metrics)
    except Exception as e:
        print(f"Error writing to file '{output_file}': {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the script workflow.
    """
    input_file = 'campaign_data.csv'   # Replace with your input file
    output_file = 'campaign_metrics.csv'  # Replace with your output file
    ctr_threshold = 2.0  # Minimum CTR (%) for success
    conversion_rate_threshold = 5.0  # Minimum conversion rate (%) for success
    cpa_threshold = 50.0  # Maximum CPA for success

    # Step 1: Read campaign data
    campaign_data = read_campaign_data(input_file)

    # Step 2: Calculate metrics
    metrics = calculate_metrics(campaign_data)

    # Step 3: Filter successful campaigns
    successful_campaigns = filter_successful_campaigns(metrics, ctr_threshold, conversion_rate_threshold, cpa_threshold)

    # Step 4: Write metrics to output file
    write_metrics_to_file(metrics, output_file)

    # Step 5: Output summary
    print(f"Processed {len(metrics)} campaigns.")
    print(f"Found {len(successful_campaigns)} successful campaigns meeting the thresholds.")
    print(f"Metrics saved to '{output_file}'.")


if __name__ == '__main__':
    main()
```
