"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Write code to generate a report summarizing the performance of a branding campaign, including metrics like brand awareness and customer engagement, using libraries like Pandas and Matplotlib.
Generated: DETERMINISTIC_954f0b24021a9e6d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

def generate_branding_campaign_report(data_file, output_report_file, output_plot_file):
    """
    Generates a summary report and visualization of a branding campaign's performance.

    Parameters:
        data_file (str): Path to the CSV file containing campaign performance data.
        output_report_file (str): Path to save the summary report (as a text file).
        output_plot_file (str): Path to save the campaign performance plot (as an image file).
    
    Returns:
        None
    """
    try:
        # Load the campaign data from a CSV file
        campaign_data = pd.read_csv(data_file)
        
        # Ensure necessary columns exist
        required_columns = ['Brand Awareness', 'Customer Engagement', 'Date']
        for column in required_columns:
            if column not in campaign_data.columns:
                raise KeyError(f"Missing required column: {column}")
        
        # Data analysis: Calculate summary metrics
        brand_awareness_avg = campaign_data['Brand Awareness'].mean()
        customer_engagement_avg = campaign_data['Customer Engagement'].mean()
        
        brand_awareness_max = campaign_data['Brand Awareness'].max()
        customer_engagement_max = campaign_data['Customer Engagement'].max()
        
        brand_awareness_min = campaign_data['Brand Awareness'].min()
        customer_engagement_min = campaign_data['Customer Engagement'].min()
        
        # Generate summary report
        with open(output_report_file, 'w') as report_file:
            report_file.write("Branding Campaign Performance Report\n")
            report_file.write("===================================\n")
            report_file.write(f"Average Brand Awareness: {brand_awareness_avg:.2f}\n")
            report_file.write(f"Average Customer Engagement: {customer_engagement_avg:.2f}\n")
            report_file.write(f"Max Brand Awareness: {brand_awareness_max:.2f}\n")
            report_file.write(f"Max Customer Engagement: {customer_engagement_max:.2f}\n")
            report_file.write(f"Min Brand Awareness: {brand_awareness_min:.2f}\n")
            report_file.write(f"Min Customer Engagement: {customer_engagement_min:.2f}\n")
        
        # Data visualization: Plot Brand Awareness and Customer Engagement over time
        plt.figure(figsize=(10, 6))
        plt.plot(campaign_data['Date'], campaign_data['Brand Awareness'], label='Brand Awareness', marker='o')
        plt.plot(campaign_data['Date'], campaign_data['Customer Engagement'], label='Customer Engagement', marker='x')
        plt.title('Branding Campaign Performance Over Time')
        plt.xlabel('Date')
        plt.ylabel('Metrics')
        plt.legend()
        plt.grid(True)
        
        # Save the plot
        plt.savefig(output_plot_file)
        plt.close()

        print(f"Report saved to {output_report_file}")
        print(f"Plot saved to {output_plot_file}")
    
    except FileNotFoundError:
        print(f"Error: File not found - {data_file}")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    generate_branding_campaign_report(
        data_file='campaign_data.csv',
        output_report_file='branding_campaign_report.txt',
        output_plot_file='branding_campaign_plot.png'
    )
```
