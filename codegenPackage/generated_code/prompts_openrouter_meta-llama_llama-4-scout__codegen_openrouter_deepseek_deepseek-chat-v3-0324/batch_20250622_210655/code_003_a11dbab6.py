"""
Generated Code Metadata:
========================
Original URL: https://rav4.expert
Prompt: Generate a Python code snippet to track and analyze Toyota RAV4 maintenance schedules using libraries like pandas and matplotlib.
Generated: DETERMINISTIC_a11dbab6461efdd7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('maintenance_tracker.log'), logging.StreamHandler()]
)

class MaintenanceTracker:
    """
    A class to track and analyze Toyota RAV4 maintenance schedules.
    """
    
    def __init__(self):
        """
        Initialize the maintenance tracker with an empty DataFrame.
        """
        self.maintenance_data = pd.DataFrame(columns=[
            'Date',
            'Mileage',
            'Service',
            'Cost',
            'Notes'
        ])
        logging.info("Maintenance tracker initialized")
    
    def add_service(self, date, mileage, service, cost=0.0, notes=''):
        """
        Add a new service record to the maintenance tracker.
        
        Args:
            date (str): Date of service in YYYY-MM-DD format
            mileage (int): Vehicle mileage at time of service
            service (str): Description of service performed
            cost (float): Cost of service (default 0.0)
            notes (str): Additional notes about service (default '')
        """
        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')
            
            new_record = {
                'Date': date,
                'Mileage': mileage,
                'Service': service,
                'Cost': cost,
                'Notes': notes
            }
            
            self.maintenance_data = pd.concat(
                [self.maintenance_data, pd.DataFrame([new_record])],
                ignore_index=True
            )
            logging.info(f"Added service record: {service} on {date}")
        except ValueError as e:
            logging.error(f"Invalid date format: {e}. Use YYYY-MM-DD.")
        except Exception as e:
            logging.error(f"Error adding service record: {e}")
    
    def get_maintenance_history(self):
        """
        Return the complete maintenance history.
        
        Returns:
            pandas.DataFrame: Maintenance records
        """
        return self.maintenance_data
    
    def plot_mileage_over_time(self):
        """
        Plot mileage over time to visualize service intervals.
        """
        try:
            if self.maintenance_data.empty:
                logging.warning("No maintenance data to plot")
                return
            
            # Convert date strings to datetime objects
            self.maintenance_data['Date'] = pd.to_datetime(self.maintenance_data['Date'])
            
            plt.figure(figsize=(10, 6))
            plt.plot(
                self.maintenance_data['Date'],
                self.maintenance_data['Mileage'],
                marker='o',
                linestyle='-'
            )
            
            plt.title('Toyota RAV4 Mileage Over Time')
            plt.xlabel('Date')
            plt.ylabel('Mileage')
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Save and show plot
            plt.savefig('mileage_over_time.png')
            plt.show()
            logging.info("Generated mileage over time plot")
        except Exception as e:
            logging.error(f"Error generating mileage plot: {e}")
    
    def calculate_service_costs(self):
        """
        Calculate and return total and average service costs.
        
        Returns:
            dict: Dictionary with total_cost and average_cost
        """
        try:
            if self.maintenance_data.empty:
                return {'total_cost': 0, 'average_cost': 0}
            
            total = self.maintenance_data['Cost'].sum()
            average = self.maintenance_data['Cost'].mean()
            
            logging.info(f"Calculated service costs: Total=${total:.2f}, Average=${average:.2f}")
            return {
                'total_cost': total,
                'average_cost': average
            }
        except Exception as e:
            logging.error(f"Error calculating service costs: {e}")
            return {'total_cost': 0, 'average_cost': 0}
    
    def save_to_csv(self, filename='rav4_maintenance.csv'):
        """
        Save maintenance data to a CSV file.
        
        Args:
            filename (str): Name of the output file (default 'rav4_maintenance.csv')
        """
        try:
            self.maintenance_data.to_csv(filename, index=False)
            logging.info(f"Saved maintenance data to {filename}")
        except Exception as e:
            logging.error(f"Error saving to CSV: {e}")
    
    def load_from_csv(self, filename='rav4_maintenance.csv'):
        """
        Load maintenance data from a CSV file.
        
        Args:
            filename (str): Name of the input file (default 'rav4_maintenance.csv')
        """
        try:
            self.maintenance_data = pd.read_csv(filename)
            logging.info(f"Loaded maintenance data from {filename}")
        except FileNotFoundError:
            logging.error(f"File not found: {filename}")
        except Exception as e:
            logging.error(f"Error loading CSV: {e}")


# Example usage
if __name__ == "__main__":
    tracker = MaintenanceTracker()
    
    # Add some sample maintenance records
    tracker.add_service('2023-01-15', 5000, 'Oil Change', 49.99, 'Synthetic oil')
    tracker.add_service('2023-04-20', 10000, 'Tire Rotation', 29.99)
    tracker.add_service('2023-07-10', 15000, 'Oil Change', 52.50, 'Synthetic oil')
    tracker.add_service('2023-10-05', 20000, 'Brake Inspection', 0.0, 'Free service')
    
    # Generate reports
    print(tracker.get_maintenance_history())
    tracker.plot_mileage_over_time()
    costs = tracker.calculate_service_costs()
    print(f"Total Maintenance Costs: ${costs['total_cost']:.2f}")
    
    # Save data
    tracker.save_to_csv()
```
