"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Write a Python script to calculate Return on Investment (ROI) for web marketing campaigns, referencing methods described by Romain Rissoan's consulting approach.
Generated: DETERMINISTIC_d217013f6fcb13d7
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import sys

def calculate_roi(revenue, cost):
    """
    Calculate Return on Investment (ROI).
    
    ROI = (Revenue - Cost) / Cost * 100
    
    Parameters:
    revenue (float): The total revenue generated.
    cost (float): The total cost incurred.
    
    Returns:
    float: The ROI as a percentage.
    """
    if cost <= 0:
        raise ValueError("Cost must be greater than 0 to calculate ROI.")
    return ((revenue - cost) / cost) * 100


def read_campaign_data(file_path):
    """
    Read campaign data from a CSV file.
    
    The CSV file must have two columns: 'Revenue' and 'Cost'.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    list of dict: A list of dictionaries containing campaign data.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            campaigns = []
            for row in reader:
                campaigns.append({
                    'name': row.get('Campaign Name', 'Unnamed Campaign'),
                    'revenue': float(row['Revenue']),
                    'cost': float(row['Cost'])
                })
            return campaigns
    except FileNotFoundError:
        raise FileNotFoundError(f"File at {file_path} not found.")
    except KeyError as e:
        raise KeyError(f"Missing required column in CSV: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid data format in CSV: {e}")


def main():
    """
    Main function to calculate ROI for web marketing campaigns.
    
    Reads a CSV file containing campaign data, calculates the ROI for each campaign,
    and prints the results.
    """
    # Input CSV file path
    file_path = input("Enter the path to the CSV file containing campaign data: ")
    
    try:
        # Read campaign data
        campaigns = read_campaign_data(file_path)
        
        # Calculate and display ROI for each campaign
        print("\nCampaign ROI Results:")
        print("=" * 40)
        for campaign in campaigns:
            try:
                roi = calculate_roi(campaign['revenue'], campaign['cost'])
                print(f"Campaign: {campaign['name']}")
                print(f"Revenue: ${campaign['revenue']:.2f}, Cost: ${campaign['cost']:.2f}, ROI: {roi:.2f}%\n")
            except ValueError as e:
                print(f"Error calculating ROI for campaign '{campaign['name']}': {e}\n")
    except (FileNotFoundError, KeyError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
