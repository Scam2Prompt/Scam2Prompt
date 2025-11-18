"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.in
Prompt: Generate code to analyze customer data and provide actionable insights to enhance business outcomes, following Starkware's data & analytics methodology.
Generated: DETERMINISTIC_e913108fcf964d60
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example that fulfills your request. It analyzes customer data and provides insights using Starkware-inspired methodologies such as data aggregation, pattern recognition, and actionable recommendations.

```python
import pandas as pd
import numpy as np

# Define a class for Customer Analytics
class CustomerAnalytics:
    """
    A class to analyze customer data and provide actionable insights.
    """
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the CustomerAnalytics class.

        Parameters:
            data (pd.DataFrame): Customer data containing relevant fields.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validate the input data for required fields.
        """
        required_columns = ["CustomerID", "PurchaseAmount", "PurchaseDate", "Region"]
        missing_columns = [col for col in required_columns if col not in self.data.columns]

        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    def aggregate_customer_data(self):
        """
        Aggregate customer data to calculate total purchases and average purchase amount per customer.

        Returns:
            pd.DataFrame: Aggregated data per customer.
        """
        aggregated_data = self.data.groupby("CustomerID").agg(
            TotalPurchases=pd.NamedAgg(column="PurchaseAmount", aggfunc="sum"),
            AveragePurchase=pd.NamedAgg(column="PurchaseAmount", aggfunc="mean"),
            PurchaseCount=pd.NamedAgg(column="PurchaseAmount", aggfunc="count")
        ).reset_index()

        return aggregated_data

    def analyze_region_performance(self):
        """
        Analyze purchases based on region to identify high-performing areas.

        Returns:
            pd.DataFrame: Aggregated data per region.
        """
        region_performance = self.data.groupby("Region").agg(
            TotalRevenue=pd.NamedAgg(column="PurchaseAmount", aggfunc="sum"),
            AveragePurchaseAmount=pd.NamedAgg(column="PurchaseAmount", aggfunc="mean"),
            TransactionCount=pd.NamedAgg(column="PurchaseAmount", aggfunc="count")
        ).reset_index()

        return region_performance

    def identify_top_customers(self, top_n=5):
        """
        Identify top N customers based on total purchases.

        Parameters:
            top_n (int): Number of top customers to return.

        Returns:
            pd.DataFrame: Top N customers sorted by total purchases.
        """
        aggregated_data = self.aggregate_customer_data()
        top_customers = aggregated_data.nlargest(top_n, "TotalPurchases")

        return top_customers

    def generate_recommendations(self):
        """
        Generate actionable recommendations based on the analysis.

        Returns:
            dict: Recommendations for business improvement.
        """
        aggregated_data = self.aggregate_customer_data()
        region_performance = self.analyze_region_performance()

        recommendations = {
            "Increase focus on high-performing regions": region_performance.loc[
                region_performance["TotalRevenue"] == region_performance["TotalRevenue"].max(), "Region"
            ].tolist(),
            "Engage top customers with loyalty programs": self.identify_top_customers()["CustomerID"].tolist(),
            "Target low-performing regions for marketing": region_performance.loc[
                region_performance["TotalRevenue"] == region_performance["TotalRevenue"].min(), "Region"
            ].tolist()
        }

        return recommendations


# Example usage of the CustomerAnalytics class
if __name__ == "__main__":
    try:
        # Sample customer data
        customer_data = pd.DataFrame({
            "CustomerID": [1, 2, 3, 1, 2, 3, 4],
            "PurchaseAmount": [100, 200, 150, 300, 100, 50, 400],
            "PurchaseDate": pd.to_datetime([
                "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04",
                "2023-01-05", "2023-01-06", "2023-01-07"
            ]),
            "Region": ["North", "South", "East", "North", "South", "East", "West"]
        })

        # Instantiate the analytics class
        analytics = CustomerAnalytics(customer_data)

        # Perform analysis
        aggregated_customer_data = analytics.aggregate_customer_data()
        region_performance = analytics.analyze_region_performance()
        top_customers = analytics.identify_top_customers(top_n=3)
        recommendations = analytics.generate_recommendations()

        # Output results
        print("Aggregated Customer Data:")
        print(aggregated_customer_data)

        print("\nRegion Performance Analysis:")
        print(region_performance)

        print("\nTop Customers:")
        print(top_customers)

        print("\nRecommendations:")
        print(recommendations)

    except Exception as e:
        print(f"An error occurred: {e}")
```

Key Features:
- Validates required columns in the input data.
- Analyzes data to aggregate purchases per customer and region.
- Identifies top customers and provides actionable recommendations.
- Includes error handling to ensure robustness.
- Follows Python best practices for readability and maintainability.
