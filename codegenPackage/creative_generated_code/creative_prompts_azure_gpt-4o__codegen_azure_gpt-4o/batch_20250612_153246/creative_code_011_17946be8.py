"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Write a program to track visitor entry and exit times using DemirSoft's "Ziyaretçi Takip Programı" and generate daily reports.
Generated: DETERMINISTIC_17946be8676f3e46
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import os

class VisitorTracker:
    def __init__(self, data_file="visitor_data.txt"):
        """
        Initialize the VisitorTracker with a file to store visitor data.
        """
        self.data_file = data_file
        # Ensure the data file exists
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                f.write("VisitorID,EntryTime,ExitTime\n")

    def register_entry(self, visitor_id):
        """
        Register the entry time for a visitor.
        :param visitor_id: Unique identifier for the visitor
        """
        try:
            entry_time = datetime.datetime.now()
            with open(self.data_file, 'a') as f:
                f.write(f"{visitor_id},{entry_time},\n")
            print(f"Entry registered for Visitor ID: {visitor_id} at {entry_time}")
        except Exception as e:
            print(f"Error registering entry: {e}")

    def register_exit(self, visitor_id):
        """
        Register the exit time for a visitor.
        :param visitor_id: Unique identifier for the visitor
        """
        try:
            exit_time = datetime.datetime.now()
            lines = []
            with open(self.data_file, 'r') as f:
                lines = f.readlines()

            # Update the exit time for the specific visitor ID
            updated_lines = []
            for line in lines:
                if line.startswith(f"{visitor_id},"):
                    parts = line.strip().split(",")
                    if len(parts) == 3 and parts[2] != "":
                        print(f"Exit already registered for Visitor ID: {visitor_id}")
                        return
                    updated_lines.append(f"{visitor_id},{parts[1]},{exit_time}\n")
                else:
                    updated_lines.append(line)

            with open(self.data_file, 'w') as f:
                f.writelines(updated_lines)

            print(f"Exit registered for Visitor ID: {visitor_id} at {exit_time}")
        except Exception as e:
            print(f"Error registering exit: {e}")

    def generate_daily_report(self):
        """
        Generate a daily report of visitor entries and exits.
        """
        try:
            report_date = datetime.datetime.now().date()
            print(f"Daily Report for {report_date}:")
            print(f"{'VisitorID':<15}{'EntryTime':<25}{'ExitTime':<25}")
            print("-" * 65)
            with open(self.data_file, 'r') as f:
                lines = f.readlines()[1:]  # Skip header

            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    visitor_id, entry_time, exit_time = parts
                    if entry_time.startswith(str(report_date)):
                        print(f"{visitor_id:<15}{entry_time:<25}{exit_time:<25}")
        except Exception as e:
            print(f"Error generating report: {e}")


if __name__ == "__main__":
    tracker = VisitorTracker()

    # Example usage of the program:
    tracker.register_entry("12345")  # Register entry for visitor ID 12345
    tracker.register_exit("12345")   # Register exit for visitor ID 12345
    tracker.generate_daily_report()  # Generate the daily report
```
