"""
Generated Code Metadata:
========================
Original URL: https://nlyedu.com
Prompt: Write a code snippet to parse and analyze home warranty company data, similar to the top 5 home warranty companies listed for 2025.
Generated: DETERMINISTIC_a8edcd5b7ad30965
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# home_warranty_analyzer.py

import pandas as pd
from typing import List, Dict

class HomeWarrantyCompany:
    """Represents a home warranty company."""

    def __init__(self, name: str, rating: float, coverage: str, price: float):
        """
        Initializes a HomeWarrantyCompany instance.

        Args:
        - name (str): The company name.
        - rating (float): The company rating (out of 5).
        - coverage (str): The company coverage details.
        - price (float): The company price.
        """
        self.name = name
        self.rating = rating
        self.coverage = coverage
        self.price = price

class HomeWarrantyAnalyzer:
    """Analyzes home warranty company data."""

    def __init__(self, data: List[Dict]):
        """
        Initializes a HomeWarrantyAnalyzer instance.

        Args:
        - data (List[Dict]): A list of dictionaries containing company data.
        """
        self.companies = []
        for company_data in data:
            try:
                company = HomeWarrantyCompany(
                    name=company_data['name'],
                    rating=company_data['rating'],
                    coverage=company_data['coverage'],
                    price=company_data['price']
                )
                self.companies.append(company)
            except KeyError as e:
                print(f"Invalid company data: {e}")

    def get_top_rated_companies(self, n: int = 5) -> List[HomeWarrantyCompany]:
        """
        Returns the top-rated home warranty companies.

        Args:
        - n (int): The number of top-rated companies to return (default: 5).

        Returns:
        - List[HomeWarrantyCompany]: A list of top-rated HomeWarrantyCompany instances.
        """
        return sorted(self.companies, key=lambda company: company.rating, reverse=True)[:n]

    def get_average_price(self) -> float:
        """
        Returns the average price of all home warranty companies.

        Returns:
        - float: The average price.
        """
        prices = [company.price for company in self.companies]
        return sum(prices) / len(prices) if prices else 0.0

def load_company_data(file_path: str) -> List[Dict]:
    """
    Loads home warranty company data from a CSV file.

    Args:
    - file_path (str): The path to the CSV file.

    Returns:
    - List[Dict]: A list of dictionaries containing company data.
    """
    try:
        data = pd.read_csv(file_path).to_dict(orient='records')
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return []
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {e}")
        return []

def main():
    # Example usage
    file_path = 'home_warranty_companies.csv'
    data = load_company_data(file_path)
    analyzer = HomeWarrantyAnalyzer(data)

    top_companies = analyzer.get_top_rated_companies()
    print("Top 5 Home Warranty Companies:")
    for i, company in enumerate(top_companies):
        print(f"{i+1}. {company.name} - Rating: {company.rating}, Price: ${company.price:.2f}")

    average_price = analyzer.get_average_price()
    print(f"\nAverage Price: ${average_price:.2f}")

if __name__ == '__main__':
    main()
```

Example CSV file (`home_warranty_companies.csv`):
```csv
name,rating,coverage,price
Company A,4.5,Comprehensive,1200.0
Company B,4.2,Basic,900.0
Company C,4.8,Premium,1500.0
Company D,4.1,Standard,1000.0
Company E,4.6,Elite,1300.0
```
