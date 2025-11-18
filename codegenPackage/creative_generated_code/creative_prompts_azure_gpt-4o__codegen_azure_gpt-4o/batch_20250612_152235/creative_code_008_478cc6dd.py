"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Write a program to generate performance reports for virtual receptionist services, including metrics like call handling efficiency and customer satisfaction, as mentioned in ProSync's ongoing support and reporting.
Generated: DETERMINISTIC_478cc6dd940a27a5
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics
from datetime import datetime

class VirtualReceptionistPerformanceReport:
    """
    Class to generate performance reports for virtual receptionist services.
    Includes metrics like call handling efficiency and customer satisfaction.
    """

    def __init__(self):
        self.call_data = []

    def add_call_record(self, call_id, duration_seconds, customer_satisfaction_rating):
        """
        Adds a record for a completed call.
        
        Args:
            call_id (str): Unique identifier for the call
            duration_seconds (int): Duration of the call in seconds
            customer_satisfaction_rating (float): Rating provided by the customer (0.0 to 5.0 scale)

        Raises:
            ValueError: If input values are invalid
        """
        if duration_seconds < 0:
            raise ValueError("Call duration cannot be negative")
        if not 0.0 <= customer_satisfaction_rating <= 5.0:
            raise ValueError("Customer satisfaction rating must be between 0.0 and 5.0")
        
        self.call_data.append({
            "call_id": call_id,
            "duration_seconds": duration_seconds,
            "customer_satisfaction_rating": customer_satisfaction_rating,
            "timestamp": datetime.now()
        })

    def generate_report(self):
        """
        Generates a performance report based on the call data.

        Returns:
            dict: A dictionary containing performance metrics (average call handling time, 
                  average customer satisfaction, and total calls handled)
        """
        if not self.call_data:
            return {
                "average_call_handling_time_seconds": 0,
                "average_customer_satisfaction_rating": 0,
                "total_calls_handled": 0,
            }

        # Extract metrics
        durations = [call["duration_seconds"] for call in self.call_data]
        satisfaction_ratings = [call["customer_satisfaction_rating"] for call in self.call_data]

        # Compute averages
        avg_duration = statistics.mean(durations)
        avg_satisfaction = statistics.mean(satisfaction_ratings)

        # Generate report
        report = {
            "average_call_handling_time_seconds": round(avg_duration, 2),
            "average_customer_satisfaction_rating": round(avg_satisfaction, 2),
            "total_calls_handled": len(self.call_data),
        }

        return report

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the report generator
        report_generator = VirtualReceptionistPerformanceReport()

        # Add call records
        report_generator.add_call_record("CALL001", 300, 4.5)
        report_generator.add_call_record("CALL002", 180, 4.0)
        report_generator.add_call_record("CALL003", 240, 5.0)

        # Generate and print the report
        report = report_generator.generate_report()
        print("Performance Report:")
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
