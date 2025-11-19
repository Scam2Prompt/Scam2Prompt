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

**Stock Price Monitor using AWS Lambda and Financial Data Feeds**
===========================================================

### **dependencies**

* `aws-lambda`
* `yfinance` for retrieving financial data

### **Code**
```python
import boto3
import json
import logging
import os
from datetime import datetime, timedelta
import yfinance as yf

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define constants
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
STOCK_SYMBOLS = os.environ['STOCK_SYMBOLS'].split(',')

# Define a function to retrieve stock data
def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period='1d')
        return data
    except Exception as e:
        logger.error(f"Error retrieving stock data for {symbol}: {str(e)}")
        return None

# Define a function to calculate significant changes
def calculate_significant_changes(data, threshold=0.05):
    if data is None:
        return None
    significant_changes = []
    for symbol in STOCK_SYMBOLS:
        stock_data = data[symbol]
        if stock_data is not None:
            current_price = stock_data.iloc[-1]['Close']
            previous_price = stock_data.iloc[0]['Close']
            change = (current_price - previous_price) / previous_price
            if abs(change) > threshold:
                significant_changes.append({
                    'symbol': symbol,
                    'current_price': current_price,
                    'previous_price': previous_price,
                    'change': change
                })
    return significant_changes

# Define the Lambda function handler
def lambda_handler(event, context):
    try:
        # Retrieve stock data
        stock_data = {}
        for symbol in STOCK_SYMBOLS:
            stock_data[symbol] = get_stock_data(symbol)

        # Calculate significant changes
        significant_changes = calculate_significant_changes(stock_data)

        # Publish to SNS topic if significant changes detected
        if significant_changes:
            sns = boto3.client('sns')
            message = {
                'significant_changes': significant_changes
            }
            response = sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=json.dumps(message)
            )
            logger.info(f"Published to SNS topic: {response['MessageId']}")

        return {
            'statusCode': 200,
            'statusMessage': 'OK'
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'statusMessage': 'Internal Server Error'
        }

# Define a function to test the Lambda function
def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    print(response)

# Test the Lambda function (optional)
if __name__ == '__main__':
    test_lambda_handler()
```

### **Environment Variables**

* `SNS_TOPIC_ARN`: The ARN of the SNS topic to publish to
* `STOCK_SYMBOLS`: A comma-separated list of stock symbols to monitor (e.g. `AAPL,GOOG,MSFT`)

### **IAM Policy**

* `lambdaExecutionRole`:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSNSPublish",
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "${SNS_TOPIC_ARN}"
        },
        {
            "Sid": "AllowYFinance",
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```
