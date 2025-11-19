"""
Generated Code Metadata:
========================
Original URL: https://lite-trades.org
Prompt: Write a program to track and visualize the growth of committed funds and supported countries, inspired by Lite Trade's statistics and facts section.
Generated: DETERMINISTIC_2984329637b7ebb8
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import matplotlib.pyplot as plt
from datetime import datetime
from typing import List, Dict, Optional

class FundTracker:
    """
    A class to track and visualize the growth of committed funds and supported countries.
    """
    
    def __init__(self, data_file: str = "fund_data.json"):
        """
        Initialize the FundTracker with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing the fund data.
        """
        self.data_file = data_file
        self.data = self._load_data()
        
    def _load_data(self) -> Dict:
        """
        Load data from the JSON file.
        
        Returns:
            Dict: The loaded data or an empty dictionary if file doesn't exist.
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"funds": [], "countries": []}
        except json.JSONDecodeError:
            print("Error: Invalid JSON data in file.")
            return {"funds": [], "countries": []}
    
    def _save_data(self) -> None:
        """
        Save data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_fund_entry(self, amount: float, date: Optional[str] = None) -> None:
        """
        Add a new fund entry.
        
        Args:
            amount (float): The committed fund amount.
            date (str, optional): Date in YYYY-MM-DD format. Defaults to current date.
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return
        
        self.data["funds"].append({
            "date": date,
            "amount": amount
        })
        self._save_data()
    
    def add_country_entry(self, country: str, date: Optional[str] = None) -> None:
        """
        Add a new supported country entry.
        
        Args:
            country (str): Name of the supported country.
            date (str, optional): Date in YYYY-MM-DD format. Defaults to current date.
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return
        
        self.data["countries"].append({
            "date": date,
            "country": country
        })
        self._save_data()
    
    def get_fund_growth(self) -> List[Dict]:
        """
        Get the chronological fund growth data.
        
        Returns:
            List[Dict]: List of fund entries sorted by date.
        """
        return sorted(self.data["funds"], key=lambda x: x["date"])
    
    def get_country_growth(self) -> List[Dict]:
        """
        Get the chronological country support growth data.
        
        Returns:
            List[Dict]: List of country entries sorted by date.
        """
        return sorted(self.data["countries"], key=lambda x: x["date"])
    
    def plot_growth(self) -> None:
        """
        Plot the growth of funds and supported countries over time.
        """
        fund_data = self.get_fund_growth()
        country_data = self.get_country_growth()
        
        if not fund_data and not country_data:
            print("No data available to plot.")
            return
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Plot funds
        if fund_data:
            dates = [entry["date"] for entry in fund_data]
            amounts = [entry["amount"] for entry in fund_data]
            cumulative = [sum(amounts[:i+1]) for i in range(len(amounts))]
            
            ax1.plot(dates, cumulative, marker='o', color='b')
            ax1.set_title('Committed Funds Growth')
            ax1.set_ylabel('Amount ($)')
            ax1.grid(True)
            plt.setp(ax1.get_xticklabels(), rotation=45)
        
        # Plot countries
        if country_data:
            dates = [entry["date"] for entry in country_data]
            countries = [entry["country"] for entry in country_data]
            unique_countries = []
            country_counts = []
            
            # Calculate cumulative unique countries
            seen = set()
            count = 0
            for entry in country_data:
                if entry["country"] not in seen:
                    seen.add(entry["country"])
                    count += 1
                unique_countries.append(entry["country"])
                country_counts.append(count)
            
            ax2.plot(dates, country_counts, marker='o', color='g')
            ax2.set_title('Supported Countries Growth')
            ax2.set_ylabel('Number of Countries')
            ax2.grid(True)
            plt.setp(ax2.get_xticklabels(), rotation=45)
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    tracker = FundTracker()
    
    # Add some sample data
    tracker.add_fund_entry(1000000, "2023-01-01")
    tracker.add_fund_entry(500000, "2023-02-15")
    tracker.add_fund_entry(750000, "2023-03-10")
    
    tracker.add_country_entry("USA", "2023-01-05")
    tracker.add_country_entry("Canada", "2023-02-20")
    tracker.add_country_entry("UK", "2023-03-15")
    tracker.add_country_entry("Germany", "2023-04-01")
    
    # Visualize the growth
    tracker.plot_growth()
```
