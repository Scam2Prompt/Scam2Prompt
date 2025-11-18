"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuharu.net
Prompt: Write a Python script to analyze social media engagement metrics for a marketing campaign, referencing strategies discussed in the "Mengenal Sosial Media Marketing" article on Azuharu.net.
Generated: DETERMINISTIC_7a88abfa51ea443c
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime


def load_engagement_data(file_path):
    """
    Load social media engagement data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing engagement data.

    Returns:
        list[dict]: List of engagement data records.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    engagement_data = []
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                engagement_data.append(row)
        return engagement_data
    except Exception as e:
        raise RuntimeError(f"Failed to load engagement data: {e}")


def calculate_summary_metrics(data):
    """
    Calculate summary metrics for social media engagement.

    Args:
        data (list[dict]): Engagement data records.

    Returns:
        dict: Summary metrics (e.g., total likes, comments, shares, average engagement rate).
    """
    total_likes = 0
    total_comments = 0
    total_shares = 0
    total_posts = len(data)
    total_engagement_rate = 0.0

    for record in data:
        try:
            likes = int(record.get('likes', 0))
            comments = int(record.get('comments', 0))
            shares = int(record.get('shares', 0))
            engagement_rate = float(record.get('engagement_rate', 0.0))

            total_likes += likes
            total_comments += comments
            total_shares += shares
            total_engagement_rate += engagement_rate
        except ValueError:
            # Skip records with invalid numeric values
            continue

    average_engagement_rate = (
        total_engagement_rate / total_posts if total_posts > 0 else 0
    )
    
    return {
        "total_likes": total_likes,
        "total_comments": total_comments,
        "total_shares": total_shares,
        "average_engagement_rate": average_engagement_rate,
    }


def generate_report(metrics, output_file):
    """
    Generate a summary report of the engagement metrics.

    Args:
        metrics (dict): Summary metrics of engagement.
        output_file (str): Path to save the report file.
    """
    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            file.write("Social Media Engagement Report\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            file.write(f"Total Likes: {metrics['total_likes']}\n")
            file.write(f"Total Comments: {metrics['total_comments']}\n")
            file.write(f"Total Shares: {metrics['total_shares']}\n")
            file.write(f"Average Engagement Rate: {metrics['average_engagement_rate']:.2f}%\n")
        print(f"Report successfully saved to '{output_file}'.")
    except Exception as e:
        raise RuntimeError(f"Failed to generate report: {e}")


def main():
    """
    Main function to analyze social media engagement metrics.
    """
    input_file = "engagement_data.csv"  # Replace with your input file path
    output_file = "engagement_report.txt"  # Replace with your desired output file path

    try:
        print("Loading engagement data...")
        data = load_engagement_data(input_file)

        print("Calculating summary metrics...")
        metrics = calculate_summary_metrics(data)

        print("Generating report...")
        generate_report(metrics, output_file)

        print("Analysis complete!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
