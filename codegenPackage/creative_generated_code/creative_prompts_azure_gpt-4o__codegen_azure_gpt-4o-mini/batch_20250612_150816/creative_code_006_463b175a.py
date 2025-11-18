"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-halo.pages.dev
Prompt: Write a function to calculate total airdrop gains and paperhanded amounts, similar to the metrics provided by Halo's analytics.
Generated: DETERMINISTIC_463b175a92357c97
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirdropAnalytics:
    def __init__(self):
        """Initialize the AirdropAnalytics class."""
        self.airdrop_data = []

    def add_airdrop(self, amount: float, received: bool) -> None:
        """
        Add a new airdrop entry.

        :param amount: The amount of airdrop received.
        :param received: A boolean indicating whether the airdrop was received.
        """
        if amount < 0:
            raise ValueError("Airdrop amount cannot be negative.")
        self.airdrop_data.append({'amount': amount, 'received': received})

    def calculate_gains(self) -> float:
        """
        Calculate the total airdrop gains.

        :return: Total gains from received airdrops.
        """
        total_gains = sum(entry['amount'] for entry in self.airdrop_data if entry['received'])
        return total_gains

    def calculate_paperhands(self) -> float:
        """
        Calculate the total amount of airdrops not received, indicating paperhanded amounts.

        :return: Total amounts of paperhanded airdrops.
        """
        total_paperhands = sum(entry['amount'] for entry in self.airdrop_data if not entry['received'])
        return total_paperhands

    def report(self) -> dict:
        """
        Generate a report of total gains and paperhanded amounts.

        :return: A dictionary containing total gains and paperhands.
        """
        try:
            gains = self.calculate_gains()
            paperhands = self.calculate_paperhands()
            return {
                'total_gains': gains,
                'total_paperhands': paperhands,
            }
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")


# Example Usage
if __name__ == "__main__":
    analytics = AirdropAnalytics()
    analytics.add_airdrop(100.0, True)
    analytics.add_airdrop(50.0, False)
    analytics.add_airdrop(200.0, True)

    report = analytics.report()
    print(report)  # Output: {'total_gains': 300.0, 'total_paperhands': 50.0}
```
