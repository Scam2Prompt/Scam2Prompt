"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Provide a script to analyze social media engagement data for platforms like Facebook, Instagram, and YouTube, aligning with IDEX Marketing's social media marketing strategies.
Generated: DETERMINISTIC_4e707466e20a4190
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SocialMediaEngagementAnalyzer:
    """A class for analyzing social media engagement data."""

    def __init__(self, data_file):
        """
        Initializes the analyzer with a data file.

        Args:
            data_file (str): Path to the CSV file containing engagement data.
        """
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """Loads data from the specified CSV file and performs initial validation."""
        try:
            self.data = pd.read_csv(self.data_file)
            self.validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {self.data_file} not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")

    def validate_data(self):
        """Validates the loaded data for required columns."""
        required_columns = ['Platform', 'Engagement', 'Date']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def summarize_engagement(self):
        """Summarizes engagement data by platform."""
        summary = self.data.groupby('Platform')['Engagement'].agg(['mean', 'sum', 'count']).reset_index()
        print("Engagement Summary by Platform:")
        print(summary)

    def plot_engagement_over_time(self):
        """Plots engagement trends over time for each platform."""
        plt.figure(figsize=(12, 6))
        for platform in self.data['Platform'].unique():
            platform_data = self.data[self.data['Platform'] == platform]
            plt.plot(platform_data['Date'], platform_data['Engagement'], marker='o', label=platform)

        plt.title('Social Media Engagement Over Time')
        plt.xlabel('Date')
        plt.ylabel('Engagement')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.grid()
        plt.show()

    def analyze_engagement(self):
        """Executes the engagement analysis including summary and visualization."""
        self.summarize_engagement()
        self.plot_engagement_over_time()

if __name__ == "__main__":
    # Path to the CSV file containing social media engagement data
    data_file_path = 'social_media_engagement.csv'  # Update with your actual file path
    analyzer = SocialMediaEngagementAnalyzer(data_file_path)

    # Perform the engagement analysis
    analyzer.analyze_engagement()
```

**Note:** Ensure that the CSV file `social_media_engagement.csv` contains the required columns: `Platform`, `Engagement`, and `Date` in a proper format for the analysis to work correctly.
