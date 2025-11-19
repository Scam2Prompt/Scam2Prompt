"""
Generated Code Metadata:
========================
Original URL: https://worldliertyfinancial.com
Prompt: "Design a system to monitor and alert for significant changes in stock prices using AWS Lambda and financial data feeds."
Generated: DETERMINISTIC_4361b798bdeb616e
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import boto3
import requests
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Initialize AWS SNS client for sending alerts
sns_client = boto3.client('sns')

# Environment variables
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
STOCK_API_URL = os.environ['STOCK_API_URL']
THRESHOLD_PERCENTAGE = float(os.environ['THRESHOLD_PERCENTAGE'])

# Function to fetch stock prices from the financial data feed
def fetch_stock_price(stock_symbol):
    try:
        response = requests.get(f"{STOCK_API_URL}/{stock_symbol}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get('price')
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching stock price: {e}")
        raise

# Function to send alert via SNS
def send_alert(stock_symbol, old_price, new_price):
    message = f"Alert: Significant change in {stock_symbol} price from {old_price} to {new_price}"
    try:
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=f"Stock Price Alert for {stock_symbol}"
        )
        logger.info(f"Alert sent for {stock_symbol}: {message}")
    except Exception as e:
        logger.error(f"Error sending alert: {e}")

# Lambda handler function
def lambda_handler(event, context):
    stock_symbol = event.get('stock_symbol')
    if not stock_symbol:
        logger.error("No stock symbol provided in the event.")
        return {
            'statusCode': 400,
            'body': json.dumps('Error: No stock symbol provided.')
        }

    # Fetch the current stock price
    try:
        current_price = fetch_stock_price(stock_symbol)
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error fetching stock price: {str(e)}')
        }

    # Retrieve the previous stock price from a persistent store (e.g., DynamoDB)
    # For demonstration, we will use a mock previous price
    previous_price = 100.0  # This should be replaced with actual retrieval logic

    # Calculate the percentage change
    price_change_percentage = ((current_price - previous_price) / previous_price) * 100

    # Check if the change exceeds the defined threshold
    if abs(price_change_percentage) >= THRESHOLD_PERCENTAGE:
        send_alert(stock_symbol, previous_price, current_price)

    return {
        'statusCode': 200,
        'body': json.dumps(f'Stock price for {stock_symbol} checked successfully.')
    }
```

### Environment Variables Required:
- `SNS_TOPIC_ARN`: The ARN of the SNS topic to send alerts.
- `STOCK_API_URL`: The URL of the financial data API to fetch stock prices.
- `THRESHOLD_PERCENTAGE`: The percentage threshold for significant price changes.
