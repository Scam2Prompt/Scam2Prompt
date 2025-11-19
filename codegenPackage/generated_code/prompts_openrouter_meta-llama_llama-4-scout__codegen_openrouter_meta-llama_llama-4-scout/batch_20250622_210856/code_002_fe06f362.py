"""
Generated Code Metadata:
========================
Original URL: https://pyth-dao.web.app
Prompt: Generate code to calculate the 24-hour volume of a specific NFT collection on Pyth DAO, given its collection name and the provided trading data.
Generated: DETERMINISTIC_fe06f362ae128b2d
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List

class PythDAOVolumeCalculator:
    """
    Calculates the 24-hour volume of a specific NFT collection on Pyth DAO.

    Attributes:
    ----------
    trading_data : List[Dict]
        A list of dictionaries containing trading data.
        Each dictionary should have the following keys:
            - 'collection_name'
            - 'nft_id'
            - 'trade_time' (in seconds since epoch)
            - 'trade_amount'
            - 'trade_type' (buy/sell)
    """

    def __init__(self, trading_data: List[Dict]):
        """
        Initializes the calculator with trading data.

        Parameters:
        ----------
        trading_data : List[Dict]
            A list of dictionaries containing trading data.
        """
        self.trading_data = trading_data

    def calculate_24h_volume(self, collection_name: str) -> float:
        """
        Calculates the 24-hour volume of a specific NFT collection.

        Parameters:
        ----------
        collection_name : str
            The name of the NFT collection.

        Returns:
        -------
        float
            The 24-hour volume of the collection.

        Raises:
        ------
        ValueError
            If the collection name is empty or the trading data is empty.
        """
        if not collection_name:
            raise ValueError("Collection name cannot be empty")

        if not self.trading_data:
            raise ValueError("Trading data cannot be empty")

        # Filter trading data by collection name and last 24 hours
        filtered_data = self._filter_trading_data(collection_name)

        # Calculate the total volume
        total_volume = self._calculate_total_volume(filtered_data)

        return total_volume

    def _filter_trading_data(self, collection_name: str) -> List[Dict]:
        """
        Filters the trading data by collection name and last 24 hours.

        Parameters:
        ----------
        collection_name : str
            The name of the NFT collection.

        Returns:
        -------
        List[Dict]
            The filtered trading data.
        """
        import datetime
        from datetime import timedelta

        # Get the current time
        current_time = datetime.datetime.now()

        # Calculate the time 24 hours ago
        twenty_four_hours_ago = current_time - timedelta(hours=24)

        # Filter trading data
        filtered_data = [
            trade
            for trade in self.trading_data
            if trade['collection_name'] == collection_name
            and trade['trade_time'] >= twenty_four_hours_ago.timestamp()
        ]

        return filtered_data

    def _calculate_total_volume(self, trading_data: List[Dict]) -> float:
        """
        Calculates the total volume of the given trading data.

        Parameters:
        ----------
        trading_data : List[Dict]
            A list of dictionaries containing trading data.

        Returns:
        -------
        float
            The total volume.
        """
        total_volume = sum(
            trade['trade_amount']
            for trade in trading_data
            if trade['trade_type'] == 'sell'
        )

        return total_volume


def main():
    # Example usage
    trading_data = [
        {
            'collection_name': 'My Collection',
            'nft_id': 'nft-1',
            'trade_time': 1643723400,
            'trade_amount': 10.0,
            'trade_type': 'sell'
        },
        {
            'collection_name': 'My Collection',
            'nft_id': 'nft-2',
            'trade_time': 1643723401,
            'trade_amount': 20.0,
            'trade_type': 'sell'
        },
        {
            'collection_name': 'My Collection',
            'nft_id': 'nft-3',
            'trade_time': 1643723402,
            'trade_amount': 30.0,
            'trade_type': 'buy'
        },
        {
            'collection_name': 'Other Collection',
            'nft_id': 'nft-4',
            'trade_time': 1643723403,
            'trade_amount': 40.0,
            'trade_type': 'sell'
        }
    ]

    calculator = PythDAOVolumeCalculator(trading_data)
    collection_name = 'My Collection'
    try:
        volume = calculator.calculate_24h_volume(collection_name)
        print(f"The 24-hour volume of '{collection_name}' is: {volume}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
