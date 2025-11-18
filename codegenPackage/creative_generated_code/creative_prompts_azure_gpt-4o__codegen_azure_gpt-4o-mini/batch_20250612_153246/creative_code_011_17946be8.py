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
import json
import os

class Visitor:
    """Class to represent a visitor with entry and exit times."""
    
    def __init__(self, name):
        self.name = name
        self.entry_time = None
        self.exit_time = None

    def check_in(self):
        """Records the entry time of the visitor."""
        self.entry_time = datetime.datetime.now()
    
    def check_out(self):
        """Records the exit time of the visitor."""
        self.exit_time = datetime.datetime.now()

    def __repr__(self):
        return f"{self.name}: Entry - {self.entry_time}, Exit - {self.exit_time}"

class VisitorTracker:
    """Class for tracking visitors and generating daily reports."""
    
    def __init__(self):
        self.visitors = []

    def check_in_visitor(self, name):
        """Checks a visitor in by name."""
        visitor = Visitor(name)
        visitor.check_in()
        self.visitors.append(visitor)
        print(f"{name} checked in at {visitor.entry_time}")

    def check_out_visitor(self, name):
        """Checks a visitor out by name."""
        for visitor in self.visitors:
            if visitor.name == name and visitor.exit_time is None:
                visitor.check_out()
                print(f"{name} checked out at {visitor.exit_time}")
                return
        print(f"No active check-in found for {name}.")

    def generate_report(self):
        """Generates a daily report of visitors."""
        report = []
        date_today = datetime.datetime.now().date()
        for visitor in self.visitors:
            if visitor.entry_time and visitor.entry_time.date() == date_today:
                report.append({
                    "name": visitor.name,
                    "entry_time": visitor.entry_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "exit_time": visitor.exit_time.strftime("%Y-%m-%d %H:%M:%S") if visitor.exit_time else "Still Inside"
                })
        
        report_filename = f"visitor_report_{date_today}.json"
        with open(report_filename, 'w') as report_file:
            json.dump(report, report_file, indent=4)
        
        print(f"Report generated: {report_filename}")

def main():
    """Main function to run the visitor tracking program."""
    tracker = VisitorTracker()
    
    while True:
        print("\nVisitor Tracker Menu:")
        print("1. Check in Visitor")
        print("2. Check out Visitor")
        print("3. Generate Daily Report")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter visitor name: ")
            tracker.check_in_visitor(name)
        
        elif choice == '2':
            name = input("Enter visitor name: ")
            tracker.check_out_visitor(name)
        
        elif choice == '3':
            tracker.generate_report()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

Make sure to run this script in an environment where you have permissions to create files, as it generates a daily report in JSON format.
