"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Create a program to track the first delegation date for all delegators in the BitsCrunch Network and calculate the duration of their participation.
Generated: DETERMINISTIC_28c13e1e4d228bbe
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
import csv

class DelegatorTracker:
    """
    A class to track delegators' first delegation date and calculate their participation duration.
    """

    def __init__(self):
        """Initialize an empty dictionary to store delegators' data."""
        self.delegators = {}

    def add_delegation(self, delegator_id, delegation_date):
        """
        Add a delegation entry for a delegator.
        
        Parameters:
            delegator_id (str): Unique identifier for the delegator.
            delegation_date (str): Delegation date in 'YYYY-MM-DD' format.
        """
        try:
            # Validate date format
            delegation_date_obj = datetime.strptime(delegation_date, '%Y-%m-%d')
            
            if delegator_id not in self.delegators:
                # Store the first delegation date
                self.delegators[delegator_id] = delegation_date_obj
                print(f"Delegation recorded for {delegator_id} on {delegation_date}")
            else:
                print(f"Delegator {delegator_id} already has a recorded date: {self.delegators[delegator_id].strftime('%Y-%m-%d')}")
        except ValueError:
            print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def calculate_participation_duration(self, delegator_id):
        """
        Calculate the duration of participation for a delegator.
        
        Parameters:
            delegator_id (str): Unique identifier for the delegator.
        
        Returns:
            int: Number of days of participation.
        """
        try:
            if delegator_id in self.delegators:
                first_delegation_date = self.delegators[delegator_id]
                current_date = datetime.now()
                duration = (current_date - first_delegation_date).days
                return duration
            else:
                print(f"Error: Delegator {delegator_id} not found.")
                return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def save_to_csv(self, file_name):
        """
        Save the delegator data to a CSV file.
        
        Parameters:
            file_name (str): Name of the CSV file to save the data.
        """
        try:
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Delegator ID', 'First Delegation Date', 'Participation Duration (Days)'])
                
                for delegator_id, first_date in self.delegators.items():
                    duration = self.calculate_participation_duration(delegator_id)
                    writer.writerow([delegator_id, first_date.strftime('%Y-%m-%d'), duration])
                
            print(f"Data successfully saved to {file_name}")
        except IOError:
            print("Error: Unable to write to file.")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Example usage
if __name__ == "__main__":
    tracker = DelegatorTracker()
    
    # Adding some delegations
    tracker.add_delegation("delegator1", "2023-01-15")
    tracker.add_delegation("delegator2", "2023-03-01")
    tracker.add_delegation("delegator1", "2023-04-01")  # Should print a warning about existing record

    # Calculating participation durations
    print("Delegator1 Participation Duration:", tracker.calculate_participation_duration("delegator1"), "days")
    print("Delegator2 Participation Duration:", tracker.calculate_participation_duration("delegator2"), "days")
    print("Delegator3 Participation Duration:", tracker.calculate_participation_duration("delegator3"))  # Should print an error

    # Saving data to a CSV file
    tracker.save_to_csv("delegators_data.csv")
```
