"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://envisiontradezone.com
Prompt: Write code to generate trading alerts based on the professional charts and trading conditions outlined by Envisiontradezone.
Generated: DETERMINISTIC_bc7367b575c12541
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging to record alerts
logging.basicConfig(
    filename='trading_alerts.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TradingAlerts:
    """
    A class to generate trading alerts based on market conditions.
    """

    def __init__(self, chart_data, conditions):
        """
        Initialize TradingAlerts instance.

        :param chart_data: List of dictionaries containing chart data (price, indicators, time).
        :param conditions: Dictionary of trading conditions for alerts.
        """
        self.chart_data = chart_data
        self.conditions = conditions

    def check_conditions(self, data_point):
        """
        Evaluate trading conditions for a given data point.

        :param data_point: A dictionary of price and indicator values.
        :return: List of triggered alerts.
        """
        triggered_alerts = []
        for condition_name, condition_func in self.conditions.items():
            try:
                # Condition functions return True if condition is met
                if condition_func(data_point):
                    triggered_alerts.append(condition_name)
            except Exception as e:
                # Log error in condition evaluation and continue
                logging.error(f"Error evaluating condition '{condition_name}': {str(e)}")
        return triggered_alerts

    def generate_alerts(self):
        """
        Generate alerts based on chart data and conditions.

        :return: List of alerts generated.
        """
        alerts = []
        for data_point in self.chart_data:
            triggered_alerts = self.check_conditions(data_point)
            for alert in triggered_alerts:
                alert_message = f"Alert triggered: {alert} at {data_point['timestamp']}"
                # Log the alert for auditing purposes
                logging.info(alert_message)
                alerts.append(alert_message)
        return alerts


# --- Example Usage ---

if __name__ == "__main__":
    # Define example chart data (normally fetched dynamically from APIs or databases)
    chart_data = [
        {"timestamp": datetime.now(), "price": 100, "rsi": 70, "moving_avg": 95},
        {"timestamp": datetime.now(), "price": 80, "rsi": 30, "moving_avg": 85},
    ]

    # Define example trading conditions as functions
    conditions = {
        "Overbought (RSI > 65)": lambda dp: dp["rsi"] > 65,  # RSI greater than 65 triggers overbought alert
        "Oversold (RSI < 35)": lambda dp: dp["rsi"] < 35,    # RSI less than 35 triggers oversold alert
        "Price above moving average": lambda dp: dp["price"] > dp["moving_avg"],  # Price is above MA
        "Price below moving average": lambda dp: dp["price"] < dp["moving_avg"],  # Price is below MA
    }

    # Create TradingAlerts instance
    trading_alerts = TradingAlerts(chart_data, conditions)

    # Generate and print alerts
    alerts = trading_alerts.generate_alerts()
    for alert in alerts:
        print(alert)
```
