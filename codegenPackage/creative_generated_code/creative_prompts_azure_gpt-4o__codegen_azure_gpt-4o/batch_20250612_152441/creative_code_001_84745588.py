"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://investinmusk.com
Prompt: Generate a script to analyze the energy efficiency of Tesla's stationary battery energy storage devices for both home and grid-scale applications, as discussed on InvestInMusk.com.
Generated: DETERMINISTIC_84745588a8b4882c
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import logging
from typing import List, Dict

# Configure logging for debugging and error tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("battery_analysis.log"),
        logging.StreamHandler()
    ]
)

class BatteryDataAnalyzer:
    """
    Class for analyzing energy efficiency data of Tesla's stationary battery energy storage devices.
    """

    def __init__(self, csv_file: str):
        """
        Initializes the BatteryDataAnalyzer with the provided CSV file containing battery data.
        
        Args:
            csv_file (str): Path to the CSV file.
        """
        self.csv_file = csv_file
        self.data = []

    def load_data(self) -> None:
        """
        Loads battery data from the CSV file.
        
        The CSV file should have the following columns:
        - Device: Name of the battery device (e.g., Powerwall, Megapack).
        - Application: Application type (e.g., Home, Grid).
        - Efficiency (%): Energy efficiency as a percentage.
        - Capacity (kWh): Battery capacity in kilowatt-hours.
        """
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
                logging.info(f"Successfully loaded data from {self.csv_file}.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.csv_file}.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading the data: {e}")
            raise

    def calculate_average_efficiency(self, application: str) -> float:
        """
        Calculates the average energy efficiency for a given application type.
        
        Args:
            application (str): The application type (e.g., "Home" or "Grid").

        Returns:
            float: The average efficiency percentage for the specified application.
        """
        filtered_data = [
            float(row['Efficiency (%)'])
            for row in self.data
            if row['Application'].lower() == application.lower()
        ]
        
        if not filtered_data:
            logging.warning(f"No data found for application type: {application}.")
            return 0.0
        
        average_efficiency = sum(filtered_data) / len(filtered_data)
        logging.info(f"Calculated average efficiency for {application}: {average_efficiency:.2f}%")
        return average_efficiency

    def get_device_summary(self) -> Dict[str, Dict[str, float]]:
        """
        Generates a summary of average efficiency and total capacity for each device.

        Returns:
            Dict[str, Dict[str, float]]: A dictionary summarizing efficiency and capacity by device.
        """
        summary = {}
        for row in self.data:
            device = row['Device']
            efficiency = float(row['Efficiency (%)'])
            capacity = float(row['Capacity (kWh)'])
            
            if device not in summary:
                summary[device] = {'total_capacity': 0, 'efficiencies': []}
            
            summary[device]['total_capacity'] += capacity
            summary[device]['efficiencies'].append(efficiency)
        
        # Calculate average efficiency for each device
        for device, stats in summary.items():
            stats['average_efficiency'] = sum(stats['efficiencies']) / len(stats['efficiencies'])
            del stats['efficiencies']  # Remove efficiency list to clean up the summary
        
        logging.info("Generated device summary.")
        return summary

    def save_summary_to_csv(self, output_file: str) -> None:
        """
        Saves the device summary to a CSV file.

        Args:
            output_file (str): Path to the output CSV file.
        """
        summary = self.get_device_summary()
        
        try:
            with open(output_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Device', 'Average Efficiency (%)', 'Total Capacity (kWh)'])
                
                for device, stats in summary.items():
                    writer.writerow([
                        device,
                        f"{stats['average_efficiency']:.2f}",
                        f"{stats['total_capacity']:.2f}"
                    ])
            
            logging.info(f"Summary successfully saved to {output_file}.")
        except Exception as e:
            logging.error(f"An error occurred while saving the summary: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    input_csv = "tesla_battery_data.csv"  # Replace with the actual path to your CSV file
    output_csv = "battery_summary.csv"   # Replace with the desired output file path

    analyzer = BatteryDataAnalyzer(input_csv)

    try:
        # Load and process data
        analyzer.load_data()
        home_avg_efficiency = analyzer.calculate_average_efficiency("Home")
        grid_avg_efficiency = analyzer.calculate_average_efficiency("Grid")

        print(f"Average Home Efficiency: {home_avg_efficiency:.2f}%")
        print(f"Average Grid Efficiency: {grid_avg_efficiency:.2f}%")

        # Save summary to CSV
        analyzer.save_summary_to_csv(output_csv)
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")
```
