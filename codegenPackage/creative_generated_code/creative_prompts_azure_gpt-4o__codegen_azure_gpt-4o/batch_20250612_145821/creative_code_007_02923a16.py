"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur-nft-marketplace.org
Prompt: Write code to analyze slot game performance and identify "gacor" slots based on historical payout data, similar to the slot analysis described on PAIZA99.
Generated: DETERMINISTIC_02923a16358bed1f
Batch ID: 20250612_145821
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

class SlotGameAnalyzer:
    """
    A class to analyze slot game performance and identify "gacor" slots
    based on historical payout data.

    Attributes:
        data (pd.DataFrame): Historical payout data containing
                             'slot_name', 'spin_date', 'payout', 'bet_amount'.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the SlotGameAnalyzer with historical payout data.

        Args:
            data (pd.DataFrame): Historical payout data.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocesses the input data by checking for required columns,
        removing invalid entries, and converting date strings to datetime objects.
        """
        required_columns = {'slot_name', 'spin_date', 'payout', 'bet_amount'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Missing required columns. Expected: {required_columns}")

        # Ensure no NaN values and valid data types
        self.data = self.data.dropna()
        self.data = self.data[self.data['payout'] >= 0]
        self.data = self.data[self.data['bet_amount'] > 0]

        # Convert spin_date to datetime
        self.data['spin_date'] = pd.to_datetime(self.data['spin_date'])

    def calculate_rtp(self):
        """
        Calculates the Return to Player (RTP) ratio for each slot game.

        Returns:
            pd.DataFrame: A DataFrame containing slot names and their RTP.
        """
        # Group data by slot_name and calculate RTP
        grouped = self.data.groupby('slot_name').agg(
            total_payout=('payout', 'sum'),
            total_bet=('bet_amount', 'sum')
        )
        grouped['rtp'] = grouped['total_payout'] / grouped['total_bet']
        return grouped.reset_index()

    def identify_gacor_slots(self, rtp_threshold: float = 1.0):
        """
        Identifies "gacor" slots based on the RTP threshold.

        Args:
            rtp_threshold (float): The RTP threshold to classify a slot as "gacor".

        Returns:
            pd.DataFrame: A DataFrame containing only the "gacor" slots.
        """
        rtp_data = self.calculate_rtp()
        # Filter slots with RTP >= rtp_threshold
        gacor_slots = rtp_data[rtp_data['rtp'] >= rtp_threshold]
        return gacor_slots

    def analyze_daily_performance(self):
        """
        Analyzes slot game performance on a daily basis.

        Returns:
            pd.DataFrame: A DataFrame with daily RTP for each slot.
        """
        # Calculate daily RTP per slot
        daily_data = self.data.groupby(['slot_name', self.data['spin_date'].dt.date]).agg(
            total_payout=('payout', 'sum'),
            total_bet=('bet_amount', 'sum')
        )
        daily_data['daily_rtp'] = daily_data['total_payout'] / daily_data['total_bet']
        return daily_data.reset_index()

# Example usage
if __name__ == "__main__":
    try:
        # Sample historical payout data
        sample_data = pd.DataFrame({
            'slot_name': ['Slot A', 'Slot B', 'Slot A', 'Slot C', 'Slot B'],
            'spin_date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
            'payout': [100, 200, 150, 50, 300],
            'bet_amount': [50, 100, 75, 25, 150]
        })

        # Initialize the analyzer
        analyzer = SlotGameAnalyzer(sample_data)

        # Preprocess the data
        analyzer.preprocess_data()

        # Identify "gacor" slots
        gacor_slots = analyzer.identify_gacor_slots(rtp_threshold=1.0)
        print("Gacor Slots:")
        print(gacor_slots)

        # Analyze daily performance
        daily_performance = analyzer.analyze_daily_performance()
        print("\nDaily Performance:")
        print(daily_performance)

    except Exception as e:
        print(f"An error occurred: {e}")
```
