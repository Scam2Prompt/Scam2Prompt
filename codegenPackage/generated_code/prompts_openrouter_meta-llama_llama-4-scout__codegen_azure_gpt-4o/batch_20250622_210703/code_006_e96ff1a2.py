"""
Generated Code Metadata:
========================
Original URL: https://armaalacak.com.tr
Prompt: What are the key performance indicators (KPIs) that Arma Alacak Yönetim A.Ş. uses to measure the success of its debt management services, and how are they tracked and reported?
Generated: DETERMINISTIC_e96ff1a21c89ccfd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import datetime
import json

class DebtManagementKPIs:
    """
    A class to represent and track the KPIs for Arma Alacak Yönetim A.Ş.'s debt management services.
    """

    def __init__(self):
        """
        Initialize the KPI tracking system with default values.
        """
        self.kpis = {
            "recovery_rate": 0.0,  # Percentage of recovered debt
            "average_resolution_time": 0.0,  # Average time to resolve a debt case (in days)
            "customer_satisfaction_score": 0.0,  # Customer satisfaction score (out of 10)
            "portfolio_growth_rate": 0.0,  # Growth rate of managed debt portfolio
            "compliance_rate": 0.0,  # Percentage of compliance with regulations
        }
        self.kpi_history = []  # List to store historical KPI data

    def update_kpi(self, kpi_name, value):
        """
        Update the value of a specific KPI.

        Args:
            kpi_name (str): The name of the KPI to update.
            value (float): The new value for the KPI.

        Raises:
            ValueError: If the KPI name is invalid or the value is negative.
        """
        if kpi_name not in self.kpis:
            raise ValueError(f"Invalid KPI name: {kpi_name}")
        if value < 0:
            raise ValueError("KPI value cannot be negative.")
        
        self.kpis[kpi_name] = value
        self._log_kpi_update(kpi_name, value)

    def _log_kpi_update(self, kpi_name, value):
        """
        Log the KPI update to the history.

        Args:
            kpi_name (str): The name of the KPI updated.
            value (float): The updated value of the KPI.
        """
        timestamp = datetime.datetime.now().isoformat()
        self.kpi_history.append({
            "timestamp": timestamp,
            "kpi_name": kpi_name,
            "value": value
        })

    def generate_report(self):
        """
        Generate a report of the current KPI values and historical updates.

        Returns:
            str: A JSON-formatted string containing the KPI report.
        """
        report = {
            "current_kpis": self.kpis,
            "kpi_history": self.kpi_history
        }
        return json.dumps(report, indent=4)

    def track_kpi(self, kpi_name):
        """
        Retrieve the historical data for a specific KPI.

        Args:
            kpi_name (str): The name of the KPI to track.

        Returns:
            list: A list of historical updates for the specified KPI.

        Raises:
            ValueError: If the KPI name is invalid.
        """
        if kpi_name not in self.kpis:
            raise ValueError(f"Invalid KPI name: {kpi_name}")
        
        return [entry for entry in self.kpi_history if entry["kpi_name"] == kpi_name]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the KPI tracking system
        kpi_tracker = DebtManagementKPIs()

        # Update KPIs
        kpi_tracker.update_kpi("recovery_rate", 85.5)
        kpi_tracker.update_kpi("average_resolution_time", 30.2)
        kpi_tracker.update_kpi("customer_satisfaction_score", 9.1)

        # Generate a report
        print("KPI Report:")
        print(kpi_tracker.generate_report())

        # Track a specific KPI
        print("\nTracking 'recovery_rate':")
        print(kpi_tracker.track_kpi("recovery_rate"))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
