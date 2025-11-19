"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydifferencebetween.com
Prompt: Write a code snippet that demonstrates how to analyze the performance analytics of marketing investments, as discussed in the article on My Difference Between.com.
Generated: DETERMINISTIC_19af61e2abe3aee2
Batch ID: 20250612_162945
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

class MarketingAnalytics:
    """
    A class to analyze and visualize performance analytics of marketing investments.

    Attributes:
        data (DataFrame): A pandas DataFrame containing marketing investment data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the MarketingAnalytics class with marketing data.

        Parameters:
            data (DataFrame): A pandas DataFrame containing 'Investment' and 'Return' columns.
        """
        # Ensure the DataFrame has the required columns
        if not all(col in data.columns for col in ['Investment', 'Return']):
            raise ValueError("DataFrame must contain 'Investment' and 'Return' columns.")

        self.data = data

    def calculate_roi(self) -> pd.Series:
        """
        Calculate the Return on Investment (ROI) for each marketing campaign.

        Returns:
            Series: A pandas Series containing the calculated ROI for each campaign.
        """
        try:
            # ROI calculation: (Return - Investment) / Investment
            roi = (self.data['Return'] - self.data['Investment']) / self.data['Investment']
            return roi
        except Exception as e:
            raise RuntimeError("Error calculating ROI: " + str(e))

    def visualize_performance(self):
        """
        Visualize the investment vs return and ROI using matplotlib.
        """
        try:
            roi = self.calculate_roi()

            # Create a figure and axis for the plots
            fig, ax = plt.subplots(2, 1, figsize=(10, 8))

            # Plot Investment vs Return
            ax[0].scatter(self.data['Investment'], self.data['Return'], color='blue')
            ax[0].set_title('Investment vs Return')
            ax[0].set_xlabel('Investment')
            ax[0].set_ylabel('Return')
            ax[0].grid()

            # Plot ROI
            ax[1].bar(self.data.index, roi, color='green')
            ax[1].set_title('Return on Investment (ROI)')
            ax[1].set_xlabel('Campaign Index')
            ax[1].set_ylabel('ROI')
            ax[1].grid()

            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError("Error during visualization: " + str(e))


# Example usage:
if __name__ == "__main__":
    # Sample data for marketing investments
    marketing_data = pd.DataFrame({
        'Investment': [1000, 2000, 1500, 3000, 2500],
        'Return': [1200, 2500, 1800, 4000, 3500]
    })

    try:
        # Initialize the MarketingAnalytics with sample data
        analytics = MarketingAnalytics(marketing_data)

        # Calculate ROI and print it
        roi = analytics.calculate_roi()
        print("ROI for each campaign:\n", roi)

        # Visualize the performance
        analytics.visualize_performance()

    except Exception as e:
        print("An error occurred:", str(e))
```
