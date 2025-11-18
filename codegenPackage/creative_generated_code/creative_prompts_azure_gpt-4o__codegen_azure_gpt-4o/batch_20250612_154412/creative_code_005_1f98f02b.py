"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invictacobrancas.com.br
Prompt: Provide code examples for implementing a debt conversion agent that tracks daily conversions and calculates engagement metrics, inspired by Invicta Cobranças' approach.
Generated: DETERMINISTIC_1f98f02b30d8567d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class DebtConversionAgent:
    """
    DebtConversionAgent tracks daily debt conversions and calculates engagement metrics.
    Inspired by Invicta Cobranças' approach.
    """
    def __init__(self):
        # Stores conversion data: {date: {"total_conversions": int, "amount_converted": float}}
        self.daily_conversions = {}
        # Logs for error tracking or data issues
        self.error_logs = []

    def record_conversion(self, amount):
        """
        Records a debt conversion for the current day.
        
        Args:
            amount (float): The amount converted in the transaction.
        """
        try:
            if amount <= 0:
                raise ValueError(f"Conversion amount must be positive. Provided: {amount}")
            
            today = datetime.date.today().isoformat()
            if today not in self.daily_conversions:
                self.daily_conversions[today] = {"total_conversions": 0, "amount_converted": 0.0}

            self.daily_conversions[today]["total_conversions"] += 1
            self.daily_conversions[today]["amount_converted"] += amount
        except Exception as e:
            error_message = f"Error recording conversion on {datetime.datetime.now().isoformat()}: {str(e)}"
            self.error_logs.append(error_message)

    def get_daily_metrics(self, date=None):
        """
        Retrieves conversion metrics for a specified date or for today if no date is provided.
        
        Args:
            date (str, optional): Date in ISO format (YYYY-MM-DD). Defaults to None (today).
            
        Returns:
            dict: Conversion metrics for the specified date.
        """
        try:
            if date is None:
                date = datetime.date.today().isoformat()
            
            if date not in self.daily_conversions:
                return {"date": date, "total_conversions": 0, "amount_converted": 0.0}
            
            return {"date": date, **self.daily_conversions[date]}
        except Exception as e:
            error_message = f"Error retrieving metrics on {datetime.datetime.now().isoformat()}: {str(e)}"
            self.error_logs.append(error_message)
            return {}

    def calculate_engagement_rate(self, date=None):
        """
        Calculates the engagement rate for a specified date or for today if no date is provided.
        Engagement rate is defined as the total_conversions * amount_converted.
        
        Args:
            date (str, optional): Date in ISO format (YYYY-MM-DD). Defaults to None (today).
            
        Returns:
            float: Engagement rate for the specified date.
        """
        try:
            metrics = self.get_daily_metrics(date)
            return metrics["total_conversions"] * metrics["amount_converted"]
        except Exception as e:
            error_message = f"Error calculating engagement rate on {datetime.datetime.now().isoformat()}: {str(e)}"
            self.error_logs.append(error_message)
            return 0.0

    def export_daily_data(self, date=None, file_path="daily_conversions.json"):
        """
        Exports conversion data for a specific date or for today if no date is provided to a JSON file.
        
        Args:
            date (str, optional): Date in ISO format (YYYY-MM-DD). Defaults to None (today).
            file_path (str, optional): Path to the output JSON file. Defaults to "daily_conversions.json".
        """
        try:
            metrics = self.get_daily_metrics(date)
            with open(file_path, "w") as json_file:
                json.dump(metrics, json_file, indent=4)
        except Exception as e:
            error_message = f"Error exporting data on {datetime.datetime.now().isoformat()}: {str(e)}"
            self.error_logs.append(error_message)

    def log_errors(self, file_path="error_logs.txt"):
        """
        Exports error logs to a text file for tracking and debugging purposes.
        
        Args:
            file_path (str, optional): Path to the output text file. Defaults to "error_logs.txt".
        """
        try:
            with open(file_path, "w") as log_file:
                for log_entry in self.error_logs:
                    log_file.write(log_entry + "\n")
        except Exception as e:
            print(f"Failed to log errors: {str(e)}")
            

# Example usage:
if __name__ == "__main__":
    agent = DebtConversionAgent()
    agent.record_conversion(150.50)
    agent.record_conversion(300.75)
    print(agent.get_daily_metrics())
    print("Engagement Rate:", agent.calculate_engagement_rate())
    agent.export_daily_data()
    agent.log_errors()
```
