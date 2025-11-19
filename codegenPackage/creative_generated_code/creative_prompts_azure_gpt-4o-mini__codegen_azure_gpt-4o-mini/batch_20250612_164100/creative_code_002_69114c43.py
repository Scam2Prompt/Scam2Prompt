"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groovesup.pages.dev
Prompt: Generate a function that calculates the earnings for fans based on their music reviews and streaming activities in the GrooveUP ecosystem.
Generated: DETERMINISTIC_69114c43d440a0cf
Batch ID: 20250612_164100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GrooveUPEarningsCalculator:
    def __init__(self, review_earning_rate: float, streaming_earning_rate: float):
        """
        Initializes the earnings calculator with the specified rates.
        
        :param review_earning_rate: The earnings per review submitted by the fan
        :param streaming_earning_rate: The earnings per stream by the fan
        """
        self.review_earning_rate = review_earning_rate
        self.streaming_earning_rate = streaming_earning_rate

    def calculate_earnings(self, num_reviews: int, num_streams: int) -> float:
        """
        Calculates the total earnings based on the number of reviews and streams.

        :param num_reviews: The number of music reviews submitted by the fan
        :param num_streams: The number of music streams by the fan
        :return: Total earnings calculated from reviews and streams
        :raises ValueError: If the number of reviews or streams is negative
        """
        if num_reviews < 0 or num_streams < 0:
            raise ValueError("Number of reviews and streams must be non-negative.")

        # Calculate earnings from reviews and streams
        earnings_from_reviews = num_reviews * self.review_earning_rate
        earnings_from_streams = num_streams * self.streaming_earning_rate

        # Total earnings
        total_earnings = earnings_from_reviews + earnings_from_streams

        return total_earnings


def main():
    """
    Main function to demonstrate the earnings calculation for a fan.
    """
    # Define earning rates (example values)
    review_rate = 0.5  # $0.50 per review
    streaming_rate = 0.01  # $0.01 per stream

    # Create an instance of the earnings calculator
    calculator = GrooveUPEarningsCalculator(review_earning_rate=review_rate, streaming_earning_rate=streaming_rate)

    # Example input for earnings calculation
    num_reviews = 10  # Example: fan wrote 10 reviews
    num_streams = 200  # Example: fan streamed 200 songs

    try:
        # Calculate earnings
        earnings = calculator.calculate_earnings(num_reviews, num_streams)
        print(f"Total earnings for the fan: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error calculating earnings: {e}")


if __name__ == "__main__":
    main()
```
