"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velodrome-financ.github.io
Prompt: Provide an example of how to use Velodrome Finance's customizable yield tokens to create a portfolio with multiple yield curves and durations.
Generated: DETERMINISTIC_00ed976839544dc6
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import velodrome_sdk  # Hypothetical Velodrome Finance SDK for Python
from velodrome_sdk.exceptions import VelodromeError

# Define constants for portfolio setup
API_KEY = "your_velodrome_api_key"  # Replace with your actual Velodrome API key
PORTFOLIO_NAME = "MyYieldPortfolio"
TOKENS = [
    {"symbol": "USDC", "amount": 1000, "duration": 30},  # 30 days
    {"symbol": "DAI", "amount": 2000, "duration": 90},  # 90 days
    {"symbol": "ETH", "amount": 1, "duration": 180},    # 180 days
]

# Initialize Velodrome SDK client
try:
    velodrome_client = velodrome_sdk.Client(api_key=API_KEY)
except VelodromeError as e:
    print(f"Failed to initialize Velodrome client: {e}")
    exit(1)

try:
    # Create a new portfolio
    portfolio = velodrome_client.create_portfolio(name=PORTFOLIO_NAME)
    print(f"Portfolio '{PORTFOLIO_NAME}' created successfully.")

    # Loop through tokens and add them to the portfolio with specific yield curves and durations
    for token in TOKENS:
        symbol = token["symbol"]
        amount = token["amount"]
        duration = token["duration"]

        # Convert token into a customizable yield token
        yield_token = portfolio.create_yield_token(
            symbol=symbol,
            amount=amount,
            duration_days=duration
        )
        print(f"Added {amount} {symbol} with a duration of {duration} days as yield token.")

    # Finalize the portfolio
    portfolio.finalize()
    print(f"Portfolio '{PORTFOLIO_NAME}' finalized and ready.")
except VelodromeError as e:
    print(f"An error occurred while creating the portfolio: {e}")
    exit(1)

# Fetch and display portfolio details
try:
    portfolio_details = portfolio.get_details()
    print(f"Portfolio Details: {portfolio_details}")
except VelodromeError as e:
    print(f"Failed to fetch portfolio details: {e}")
```
