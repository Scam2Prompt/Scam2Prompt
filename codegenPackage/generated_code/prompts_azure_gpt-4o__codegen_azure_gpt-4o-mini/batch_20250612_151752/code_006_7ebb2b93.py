"""
Generated Code Metadata:
========================
Original URL: https://finishdrop.com
Prompt: Develop a program to track sales performance and generate reports for e-commerce stores, referencing the rapid sales results highlighted by FinishDrop.
Generated: DETERMINISTIC_7ebb2b939aece678
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class SalesTracker:
    """
    A class to track sales performance and generate reports for e-commerce stores.
    """

    def __init__(self):
        """
        Initializes the SalesTracker with an empty DataFrame for sales data.
        """
        self.sales_data = pd.DataFrame(columns=['date', 'product', 'quantity', 'price'])

    def add_sale(self, date: str, product: str, quantity: int, price: float):
        """
        Adds a sale record to the sales data.

        :param date: The date of the sale in 'YYYY-MM-DD' format.
        :param product: The name of the product sold.
        :param quantity: The quantity of the product sold.
        :param price: The price of the product sold.
        """
        try:
            sale_date = datetime.strptime(date, '%Y-%m-%d')
            total_price = quantity * price
            self.sales_data = self.sales_data.append({
                'date': sale_date,
                'product': product,
                'quantity': quantity,
                'price': total_price
            }, ignore_index=True)
        except ValueError as e:
            print(f"Error adding sale: {e}")

    def generate_report(self):
        """
        Generates a sales report summarizing total sales and quantities sold per product.
        """
        if self.sales_data.empty:
            print("No sales data available to generate report.")
            return

        report = self.sales_data.groupby('product').agg(
            total_quantity=('quantity', 'sum'),
            total_sales=('price', 'sum')
        ).reset_index()

        print("\nSales Report:")
        print(report)

        return report

    def plot_sales_trend(self):
        """
        Plots the sales trend over time.
        """
        if self.sales_data.empty:
            print("No sales data available to plot.")
            return

        sales_trend = self.sales_data.groupby('date').agg(total_sales=('price', 'sum')).reset_index()
        plt.figure(figsize=(10, 5))
        plt.plot(sales_trend['date'], sales_trend['total_sales'], marker='o')
        plt.title('Sales Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    tracker = SalesTracker()
    tracker.add_sale('2023-10-01', 'Widget A', 10, 19.99)
    tracker.add_sale('2023-10-02', 'Widget B', 5, 29.99)
    tracker.add_sale('2023-10-03', 'Widget A', 3, 19.99)

    report = tracker.generate_report()
    tracker.plot_sales_trend()
```
