"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axos-management.com
Prompt: Create a script to track influencer campaign performance and establish long-term brand partnerships, following the methodology described by Axos Management.
Generated: DETERMINISTIC_c24865ceb38a562d
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import datetime
from typing import List, Dict

class InfluencerCampaignTracker:
    """
    A class to track influencer campaign performance and establish long-term brand partnerships.
    """

    def __init__(self, campaign_data_file: str, performance_metrics_file: str):
        """
        Initialize the tracker with paths to campaign data and performance metrics.
        
        Args:
            campaign_data_file (str): Path to the campaign data CSV file.
            performance_metrics_file (str): Path to the performance metrics JSON file.
        """
        self.campaign_data_file = campaign_data_file
        self.performance_metrics_file = performance_metrics_file

    def load_campaign_data(self) -> List[Dict]:
        """
        Load campaign data from a CSV file.

        Returns:
            List[Dict]: List of campaign data dictionaries.
        """
        try:
            with open(self.campaign_data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            print(f"Error: File '{self.campaign_data_file}' not found.")
            return []
        except Exception as e:
            print(f"Error: Failed to load campaign data. {e}")
            return []

    def load_performance_metrics(self) -> Dict:
        """
        Load performance metrics from a JSON file.

        Returns:
            Dict: Dictionary containing performance metrics.
        """
        try:
            with open(self.performance_metrics_file, mode='r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.performance_metrics_file}' not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to parse performance metrics JSON file.")
            return {}
        except Exception as e:
            print(f"Error: Failed to load performance metrics. {e}")
            return {}

    def evaluate_influencers(self, campaign_data: List[Dict], performance_metrics: Dict) -> List[Dict]:
        """
        Evaluate influencers based on campaign data and performance metrics.

        Args:
            campaign_data (List[Dict]): List of campaign data dictionaries.
            performance_metrics (Dict): Dictionary containing performance metrics.

        Returns:
            List[Dict]: List of evaluated influencers with performance scores.
        """
        evaluated_influencers = []
        for campaign in campaign_data:
            influencer_name = campaign.get('Influencer')
            engagement_rate = float(campaign.get('EngagementRate', 0))
            conversion_rate = float(campaign.get('ConversionRate', 0))
            audience_quality_score = performance_metrics.get(influencer_name, {}).get('AudienceQualityScore', 0)

            # Calculate a performance score based on the methodology
            performance_score = (engagement_rate * 0.4) + (conversion_rate * 0.4) + (audience_quality_score * 0.2)

            evaluated_influencers.append({
                'Influencer': influencer_name,
                'PerformanceScore': performance_score,
                'EngagementRate': engagement_rate,
                'ConversionRate': conversion_rate,
                'AudienceQualityScore': audience_quality_score
            })

        return evaluated_influencers

    def suggest_long_term_partnerships(self, evaluated_influencers: List[Dict], threshold: float = 75.0) -> List[Dict]:
        """
        Suggest long-term partnerships based on performance scores.

        Args:
            evaluated_influencers (List[Dict]): List of evaluated influencers with performance scores.
            threshold (float): Score threshold for long-term partnerships.

        Returns:
            List[Dict]: List of influencers suitable for long-term partnerships.
        """
        return [influencer for influencer in evaluated_influencers if influencer['PerformanceScore'] >= threshold]

    def save_suggestions_to_csv(self, suggestions: List[Dict], output_file: str):
        """
        Save suggested influencers for long-term partnerships to a CSV file.

        Args:
            suggestions (List[Dict]): List of influencers suitable for long-term partnerships.
            output_file (str): Path to the output CSV file.
        """
        try:
            with open(output_file, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=suggestions[0].keys())
                writer.writeheader()
                writer.writerows(suggestions)
                print(f"Suggestions successfully saved to '{output_file}'.")
        except Exception as e:
            print(f"Error: Failed to save suggestions to CSV file. {e}")

def main():
    """
    Main function to orchestrate the influencer campaign tracking process.
    """
    # File paths (replace with actual file paths)
    campaign_data_file = 'campaign_data.csv'
    performance_metrics_file = 'performance_metrics.json'
    output_file = 'suggested_partnerships.csv'

    # Initialize the tracker
    tracker = InfluencerCampaignTracker(campaign_data_file, performance_metrics_file)

    # Load data
    campaign_data = tracker.load_campaign_data()
    performance_metrics = tracker.load_performance_metrics()

    if not campaign_data or not performance_metrics:
        print("Error: Missing or invalid input data. Exiting.")
        return

    # Evaluate influencers
    evaluated_influencers = tracker.evaluate_influencers(campaign_data, performance_metrics)

    # Suggest long-term partnerships
    suggestions = tracker.suggest_long_term_partnerships(evaluated_influencers)

    # Save suggestions to CSV
    if suggestions:
        tracker.save_suggestions_to_csv(suggestions, output_file)
    else:
        print("No influencers meet the criteria for long-term partnerships.")

if __name__ == "__main__":
    main()
```
