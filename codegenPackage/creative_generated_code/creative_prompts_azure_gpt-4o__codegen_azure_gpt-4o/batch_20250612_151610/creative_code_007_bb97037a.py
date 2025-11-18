"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Develop a Python script to analyze social media engagement metrics for campaigns, leveraging Cara Productions' strategies tailored to Kenya's digital landscape.
Generated: DETERMINISTIC_bb97037ae90723af
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import csv
import os
from datetime import datetime

# Define constants for file paths and settings
METRICS_FILE = "social_media_metrics.json"
OUTPUT_FILE = "campaign_analysis.csv"
SUPPORTED_PLATFORMS = ["Facebook", "Twitter", "Instagram"]
KENYA_TARGET_KEYWORDS = ["Kenya", "Nairobi", "Mombasa", "Africa"]

def load_metrics_file(file_path):
    """
    Load social media metrics JSON file.
    Args:
        file_path (str): Path to the metrics JSON file.
    Returns:
        dict: Parsed metrics data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file - {e}")
        return {}

def filter_metrics_for_kenya(metrics_data):
    """
    Filter metrics for campaigns targeting Kenya based on keywords.
    Args:
        metrics_data (dict): Raw metrics data.
    Returns:
        list: Filtered metrics specific to Kenya.
    """
    filtered_data = []
    for campaign in metrics_data.get("campaigns", []):
        if any(keyword in campaign.get("description", "") for keyword in KENYA_TARGET_KEYWORDS):
            filtered_data.append(campaign)
    return filtered_data

def analyze_engagement(filtered_data):
    """
    Analyze social media engagement metrics for campaigns.
    Args:
        filtered_data (list): Filtered campaign data.
    Returns:
        list: Processed engagement analysis results.
    """
    results = []
    for campaign in filtered_data:
        campaign_name = campaign.get("name")
        platform = campaign.get("platform")
        if platform not in SUPPORTED_PLATFORMS:
            continue  # Skip unsupported platforms

        engagement_rate = calculate_engagement_rate(
            campaign.get("likes", 0),
            campaign.get("comments", 0),
            campaign.get("shares", 0),
            campaign.get("views", 0)
        )
        results.append({
            "campaign_name": campaign_name,
            "platform": platform,
            "engagement_rate": engagement_rate,
            "analysis_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return results

def calculate_engagement_rate(likes, comments, shares, views):
    """
    Calculate engagement rate based on likes, comments, shares, and views.
    Args:
        likes (int): Number of likes.
        comments (int): Number of comments.
        shares (int): Number of shares.
        views (int): Number of views.
    Returns:
        float: Engagement rate percentage.
    """
    try:
        if views == 0:
            return 0.0  # Avoid division by zero
        return ((likes + comments + shares) / views) * 100
    except Exception as e:
        print(f"Error calculating engagement rate: {e}")
        return 0.0

def save_analysis_to_csv(output_file, analysis_results):
    """
    Save the analysis results to a CSV file.
    Args:
        output_file (str): Path to the output CSV file.
        analysis_results (list): Engagement analysis results.
    """
    try:
        with open(output_file, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["campaign_name", "platform", "engagement_rate", "analysis_time"])
            writer.writeheader()
            writer.writerows(analysis_results)
        print(f"Analysis results saved to '{output_file}'.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    """
    Main function to execute the social media engagement analysis pipeline.
    """
    print("Loading social media metrics...")
    metrics_data = load_metrics_file(METRICS_FILE)

    if not metrics_data:
        print("No metrics data found. Exiting program.")
        return

    print("Filtering campaigns targeting Kenya...")
    filtered_data = filter_metrics_for_kenya(metrics_data)

    print("Analyzing engagement metrics...")
    analysis_results = analyze_engagement(filtered_data)

    print("Saving results to CSV file...")
    save_analysis_to_csv(OUTPUT_FILE, analysis_results)

    print("Analysis complete.")

if __name__ == "__main__":
    main()
```
