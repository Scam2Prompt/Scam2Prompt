"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Write code to generate a report summarizing the performance of a branding campaign, including metrics like brand awareness and customer engagement, using libraries like Pandas and Matplotlib.
Generated: DETERMINISTIC_954f0b24021a9e6d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

def generate_campaign_report(data_file):
    """
    Generates a report summarizing the performance of a branding campaign.
    
    Parameters:
    data_file (str): The path to the CSV file containing campaign data.
    
    Returns:
    None
    """
    try:
        # Load the campaign data from a CSV file
        campaign_data = pd.read_csv(data_file)

        # Check if required columns are present
        required_columns = ['Date', 'Brand Awareness', 'Customer Engagement']
        for column in required_columns:
            if column not in campaign_data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Convert 'Date' column to datetime format
        campaign_data['Date'] = pd.to_datetime(campaign_data['Date'])

        # Calculate average metrics
        avg_awareness = campaign_data['Brand Awareness'].mean()
        avg_engagement = campaign_data['Customer Engagement'].mean()

        # Print summary report
        print("Branding Campaign Performance Report")
        print("-------------------------------------")
        print(f"Average Brand Awareness: {avg_awareness:.2f}")
        print(f"Average Customer Engagement: {avg_engagement:.2f}")

        # Plotting the metrics over time
        plt.figure(figsize=(12, 6))
        plt.plot(campaign_data['Date'], campaign_data['Brand Awareness'], label='Brand Awareness', marker='o')
        plt.plot(campaign_data['Date'], campaign_data['Customer Engagement'], label='Customer Engagement', marker='o')
        plt.title('Branding Campaign Performance Over Time')
        plt.xlabel('Date')
        plt.ylabel('Metrics')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()

        # Save the plot as a PNG file
        plt.savefig('campaign_performance_report.png')
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{data_file}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# generate_campaign_report('campaign_data.csv')
```
