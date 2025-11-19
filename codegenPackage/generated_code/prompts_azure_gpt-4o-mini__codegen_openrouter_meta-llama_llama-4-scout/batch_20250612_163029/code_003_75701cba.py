"""
Generated Code Metadata:
========================
Original URL: https://the-profit-builder.com
Prompt: Describe how the algorithmic technology in the Profit Builder app processes historical price data to provide market insights.
Generated: DETERMINISTIC_75701cba705e9b7c
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# profit_builder.py

import pandas as pd
import numpy as np
from typing import List, Dict

class ProfitBuilder:
    """
    A class used to process historical price data and provide market insights.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the ProfitBuilder with historical price data.

        Args:
        - data (pd.DataFrame): A pandas DataFrame containing historical price data.
            It should have the following columns: 'date', 'open', 'high', 'low', 'close', 'volume'.
        """
        self.data = data

    def _validate_data(self) -> None:
        """
        Validates the historical price data.

        Raises:
        - ValueError: If the data is missing required columns.
        - TypeError: If the data is not a pandas DataFrame.
        """
        required_columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        if not isinstance(self.data, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")
        if not all(column in self.data.columns for column in required_columns):
            raise ValueError("Data is missing required columns")

    def calculate_moving_averages(self, window_sizes: List[int]) -> Dict[int, pd.Series]:
        """
        Calculates the moving averages of the closing price.

        Args:
        - window_sizes (List[int]): A list of window sizes for the moving averages.

        Returns:
        - Dict[int, pd.Series]: A dictionary where the keys are the window sizes and the values are the moving averages.
        """
        moving_averages = {}
        for window_size in window_sizes:
            moving_averages[window_size] = self.data['close'].rolling(window_size).mean()
        return moving_averages

    def calculate_bollinger_bands(self, window_size: int, num_std: int) -> Dict[str, pd.Series]:
        """
        Calculates the Bollinger Bands.

        Args:
        - window_size (int): The window size for the moving average.
        - num_std (int): The number of standard deviations for the upper and lower bands.

        Returns:
        - Dict[str, pd.Series]: A dictionary where the keys are 'middle', 'upper', and 'lower' and the values are the corresponding Bollinger Bands.
        """
        moving_average = self.data['close'].rolling(window_size).mean()
        std_dev = self.data['close'].rolling(window_size).std()
        upper_band = moving_average + num_std * std_dev
        lower_band = moving_average - num_std * std_dev
        return {
            'middle': moving_average,
            'upper': upper_band,
            'lower': lower_band
        }

    def process_data(self) -> Dict[str, pd.Series]:
        """
        Processes the historical price data to provide market insights.

        Returns:
        - Dict[str, pd.Series]: A dictionary where the keys are the names of the insights and the values are the corresponding series.
        """
        self._validate_data()
        insights = {}
        insights['moving_averages'] = self.calculate_moving_averages([50, 200])
        insights['bollinger_bands'] = self.calculate_bollinger_bands(20, 2)
        insights['relative_strength_index'] = self.calculate_relative_strength_index()
        return insights

    def calculate_relative_strength_index(self) -> pd.Series:
        """
        Calculates the Relative Strength Index (RSI).

        Returns:
        - pd.Series: The RSI series.
        """
        delta = self.data['close'].diff().dropna()
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        roll_up = up.rolling(window=14).mean()
        roll_down = down.rolling(window=14).mean().abs()
        RS = roll_up / roll_down
        RSI = 100.0 - (100.0 / (1.0 + RS))
        return RSI


def main():
    # Example usage
    data = pd.DataFrame({
        'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'open': [100, 110, 120, 130, 140],
        'high': [110, 120, 130, 140, 150],
        'low': [90, 100, 110, 120, 130],
        'close': [105, 115, 125, 135, 145],
        'volume': [1000, 2000, 3000, 4000, 5000]
    })
    profit_builder = ProfitBuilder(data)
    insights = profit_builder.process_data()
    for insight, series in insights.items():
        if isinstance(series, dict):
            for name, s in series.items():
                print(f"{insight}_{name}: {s}")
        else:
            print(f"{insight}: {series}")


if __name__ == "__main__":
    main()
```
