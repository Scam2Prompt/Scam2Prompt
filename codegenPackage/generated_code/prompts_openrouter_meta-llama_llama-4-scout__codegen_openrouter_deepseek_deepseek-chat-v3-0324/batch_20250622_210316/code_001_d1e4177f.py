"""
Generated Code Metadata:
========================
Original URL: https://pancarpos.com
Prompt: Generate a report on the environmental initiative by Samsat Badung to collect plastic waste in three traditional markets in Badung regency.
Generated: DETERMINISTIC_d1e4177fd92833c3
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict

class EnvironmentalInitiativeReport:
    """
    A class to generate a report on Samsat Badung's environmental initiative to collect plastic waste.
    """

    def __init__(self, markets: List[str], data: List[Dict[str, float]]):
        """
        Initialize the report with market names and collected waste data.
        
        Args:
            markets: List of market names.
            data: List of dictionaries containing waste collection data per market.
        """
        self.markets = markets
        self.data = data
        self.report_date = datetime.now().strftime("%Y-%m-%d")

    def validate_data(self) -> bool:
        """
        Validate the input data to ensure it matches the expected format.
        
        Returns:
            bool: True if data is valid, False otherwise.
        """
        if len(self.markets) != len(self.data):
            return False
        
        required_keys = {'plastic_waste_kg', 'participants', 'collection_days'}
        for entry in self.data:
            if not all(key in entry for key in required_keys):
                return False
        
        return True

    def generate_summary(self) -> Dict[str, float]:
        """
        Generate a summary of the collected waste data.
        
        Returns:
            Dict[str, float]: Summary containing total waste, average per market, etc.
        """
        total_waste = sum(entry['plastic_waste_kg'] for entry in self.data)
        avg_waste = total_waste / len(self.data)
        total_participants = sum(entry['participants'] for entry in self.data)
        
        return {
            'total_waste_kg': total_waste,
            'average_waste_per_market_kg': avg_waste,
            'total_participants': total_participants,
            'markets_count': len(self.markets)
        }

    def generate_csv_report(self, filename: str) -> None:
        """
        Generate a CSV report file with the collected data.
        
        Args:
            filename: Name of the output CSV file.
        
        Raises:
            ValueError: If data validation fails.
        """
        if not self.validate_data():
            raise ValueError("Invalid data format. Please check input data.")
        
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # Write header
                writer.writerow(['Market Name', 'Plastic Waste (kg)', 'Participants', 'Collection Days', 'Report Date'])
                
                # Write data rows
                for market, entry in zip(self.markets, self.data):
                    writer.writerow([
                        market,
                        entry['plastic_waste_kg'],
                        entry['participants'],
                        entry['collection_days'],
                        self.report_date
                    ])
        except IOError as e:
            print(f"Error writing to file: {e}")
            raise

    def print_summary_report(self) -> None:
        """
        Print a formatted summary report to the console.
        """
        if not self.validate_data():
            print("Error: Invalid data format. Cannot generate report.")
            return
        
        summary = self.generate_summary()
        
        print("\n=== Samsat Badung Environmental Initiative Report ===")
        print(f"Report Date: {self.report_date}")
        print(f"Markets Covered: {', '.join(self.markets)}")
        print("\n--- Summary ---")
        print(f"Total Plastic Waste Collected: {summary['total_waste_kg']} kg")
        print(f"Average Waste per Market: {summary['average_waste_per_market_kg']:.2f} kg")
        print(f"Total Participants: {summary['total_participants']}")
        print("\n--- Detailed Data ---")
        
        for market, entry in zip(self.markets, self.data):
            print(f"\nMarket: {market}")
            print(f"  Plastic Waste: {entry['plastic_waste_kg']} kg")
            print(f"  Participants: {entry['participants']}")
            print(f"  Collection Days: {entry['collection_days']}")

# Example usage
if __name__ == "__main__":
    # Sample data for three traditional markets in Badung regency
    markets = ["Pasar Badung", "Pasar Kereneng", "Pasar Mengwi"]
    data = [
        {'plastic_waste_kg': 150.5, 'participants': 45, 'collection_days': 7},
        {'plastic_waste_kg': 98.2, 'participants': 32, 'collection_days': 5},
        {'plastic_waste_kg': 210.7, 'participants': 58, 'collection_days': 10}
    ]
    
    try:
        report = EnvironmentalInitiativeReport(markets, data)
        report.print_summary_report()
        report.generate_csv_report("samsat_badung_plastic_waste_report.csv")
        print("\nCSV report generated successfully.")
    except Exception as e:
        print(f"Error generating report: {e}")
```
