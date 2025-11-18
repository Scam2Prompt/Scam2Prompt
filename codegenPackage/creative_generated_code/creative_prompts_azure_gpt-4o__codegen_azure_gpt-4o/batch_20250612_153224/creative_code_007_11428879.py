"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Write a script to generate reports on cyberharassment awareness campaigns, similar to those conducted by Sophia Loisirs & Vie, including data visualization using Matplotlib or Seaborn.
Generated: DETERMINISTIC_11428879c8ad82c7
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
import seaborn as sns

# Function to generate a report on cyberharassment awareness campaigns
def generate_report(data_file):
    """
    Generates a report on cyberharassment awareness campaigns.

    Args:
        data_file (str): Path to the CSV file containing campaign data.

    Returns:
        None: Generates visualizations and summaries.
    """
    try:
        # Load the campaign data from a CSV file
        campaign_data = pd.read_csv(data_file)

        # Validate required columns exist
        required_columns = ['Campaign Name', 'Participants', 'Budget', 'Feedback Score']
        for column in required_columns:
            if column not in campaign_data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Summary statistics
        print("==== Campaign Summary Statistics ====")
        print(campaign_data.describe())

        # Visualization: Participants per campaign
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Campaign Name', y='Participants', data=campaign_data, palette='Blues_d')
        plt.title('Number of Participants per Campaign')
        plt.xlabel('Campaign Name')
        plt.ylabel('Number of Participants')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('participants_per_campaign.png')  # Save the plot
        plt.show()

        # Visualization: Budget per campaign
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Campaign Name', y='Budget', data=campaign_data, palette='Greens_d')
        plt.title('Budget per Campaign')
        plt.xlabel('Campaign Name')
        plt.ylabel('Budget (in USD)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('budget_per_campaign.png')  # Save the plot
        plt.show()

        # Visualization: Feedback scores distribution
        plt.figure(figsize=(8, 5))
        sns.histplot(campaign_data['Feedback Score'], kde=True, color='purple', bins=10)
        plt.title('Feedback Scores Distribution')
        plt.xlabel('Feedback Score')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig('feedback_scores_distribution.png')  # Save the plot
        plt.show()

        # Generate a CSV report summarizing findings
        summary_report = campaign_data.groupby('Campaign Name').agg({
            'Participants': 'sum',
            'Budget': 'sum',
            'Feedback Score': 'mean'
        }).reset_index()
        summary_report.rename(columns={
            'Participants': 'Total Participants',
            'Budget': 'Total Budget',
            'Feedback Score': 'Average Feedback Score'
        }, inplace=True)
        summary_report.to_csv('campaign_summary_report.csv', index=False)
        print("Summary report saved as 'campaign_summary_report.csv'.")

    except FileNotFoundError:
        print(f"Error: File '{data_file}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main function to execute the report generation
if __name__ == "__main__":
    # Example usage: Replace 'campaign_data.csv' with the actual file path
    data_file_path = 'campaign_data.csv'
    generate_report(data_file_path)
```
