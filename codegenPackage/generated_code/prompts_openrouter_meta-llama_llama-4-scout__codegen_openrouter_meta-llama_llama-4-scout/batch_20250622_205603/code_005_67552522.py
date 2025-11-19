"""
Generated Code Metadata:
========================
Original URL: https://p30mag.com
Prompt: "Design a sales funnel for an Instagram-based affiliate marketing campaign, utilizing collaborations with influencers and بلاگرها."
Generated: DETERMINISTIC_675525224f825261
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime
from typing import Dict, List

# Define a class for Influencer
class Influencer:
    def __init__(self, id: int, name: str, followers: int, niche: str):
        """
        Initialize an Influencer object.

        Args:
        id (int): Unique identifier for the influencer.
        name (str): Name of the influencer.
        followers (int): Number of followers the influencer has.
        niche (str): Niche or area of expertise for the influencer.
        """
        self.id = id
        self.name = name
        self.followers = followers
        self.niche = niche

# Define a class for Blogger
class Blogger:
    def __init__(self, id: int, name: str, followers: int, niche: str):
        """
        Initialize a Blogger object.

        Args:
        id (int): Unique identifier for the blogger.
        name (str): Name of the blogger.
        followers (int): Number of followers the blogger has.
        niche (str): Niche or area of expertise for the blogger.
        """
        self.id = id
        self.name = name
        self.followers = followers
        self.niche = niche

# Define a class for Product
class Product:
    def __init__(self, id: int, name: str, price: float, commission: float):
        """
        Initialize a Product object.

        Args:
        id (int): Unique identifier for the product.
        name (str): Name of the product.
        price (float): Price of the product.
        commission (float): Commission earned per sale of the product.
        """
        self.id = id
        self.name = name
        self.price = price
        self.commission = commission

# Define a class for SalesFunnel
class SalesFunnel:
    def __init__(self):
        """
        Initialize a SalesFunnel object.
        """
        self.influencers: List[Influencer] = []
        self.bloggers: List[Blogger] = []
        self.products: List[Product] = []
        self.sales: Dict[int, int] = {}  # product_id: sales_count

    def add_influencer(self, influencer: Influencer):
        """
        Add an influencer to the sales funnel.

        Args:
        influencer (Influencer): Influencer object to add.
        """
        self.influencers.append(influencer)

    def add_blogger(self, blogger: Blogger):
        """
        Add a blogger to the sales funnel.

        Args:
        blogger (Blogger): Blogger object to add.
        """
        self.bloggers.append(blogger)

    def add_product(self, product: Product):
        """
        Add a product to the sales funnel.

        Args:
        product (Product): Product object to add.
        """
        self.products.append(product)

    def track_sale(self, product_id: int):
        """
        Track a sale of a product.

        Args:
        product_id (int): ID of the product sold.
        """
        if product_id in self.sales:
            self.sales[product_id] += 1
        else:
            self.sales[product_id] = 1

    def get_influencer_performance(self) -> pd.DataFrame:
        """
        Get a report on influencer performance.

        Returns:
        pd.DataFrame: DataFrame with influencer performance metrics.
        """
        influencer_performance = []
        for influencer in self.influencers:
            sales_count = sum(self.sales.values())
            influencer_performance.append({
                'Influencer': influencer.name,
                'Followers': influencer.followers,
                'Sales': sales_count,
                'Conversion Rate': f'{sales_count / influencer.followers * 100:.2f}%'
            })
        return pd.DataFrame(influencer_performance)

    def get_blogger_performance(self) -> pd.DataFrame:
        """
        Get a report on blogger performance.

        Returns:
        pd.DataFrame: DataFrame with blogger performance metrics.
        """
        blogger_performance = []
        for blogger in self.bloggers:
            sales_count = sum(self.sales.values())
            blogger_performance.append({
                'Blogger': blogger.name,
                'Followers': blogger.followers,
                'Sales': sales_count,
                'Conversion Rate': f'{sales_count / blogger.followers * 100:.2f}%'
            })
        return pd.DataFrame(blogger_performance)

    def get_product_performance(self) -> pd.DataFrame:
        """
        Get a report on product performance.

        Returns:
        pd.DataFrame: DataFrame with product performance metrics.
        """
        product_performance = []
        for product in self.products:
            sales_count = self.sales.get(product.id, 0)
            product_performance.append({
                'Product': product.name,
                'Price': product.price,
                'Commission': product.commission,
                'Sales': sales_count,
                'Revenue': sales_count * product.price,
                'Commission Earned': sales_count * product.commission
            })
        return pd.DataFrame(product_performance)

# Example usage
if __name__ == '__main__':
    sales_funnel = SalesFunnel()

    # Create influencers
    influencer1 = Influencer(1, 'Influencer 1', 10000, 'Fashion')
    influencer2 = Influencer(2, 'Influencer 2', 5000, 'Beauty')

    # Create bloggers
    blogger1 = Blogger(1, 'Blogger 1', 20000, 'Lifestyle')
    blogger2 = Blogger(2, 'Blogger 2', 10000, 'Food')

    # Create products
    product1 = Product(1, 'Product 1', 100.0, 10.0)
    product2 = Product(2, 'Product 2', 50.0, 5.0)

    # Add influencers, bloggers, and products to the sales funnel
    sales_funnel.add_influencer(influencer1)
    sales_funnel.add_influencer(influencer2)
    sales_funnel.add_blogger(blogger1)
    sales_funnel.add_blogger(blogger2)
    sales_funnel.add_product(product1)
    sales_funnel.add_product(product2)

    # Track sales
    sales_funnel.track_sale(1)
    sales_funnel.track_sale(1)
    sales_funnel.track_sale(2)

    # Get performance reports
    influencer_performance = sales_funnel.get_influencer_performance()
    blogger_performance = sales_funnel.get_blogger_performance()
    product_performance = sales_funnel.get_product_performance()

    # Print performance reports
    print("Influencer Performance:")
    print(influencer_performance)
    print("\nBlogger Performance:")
    print(blogger_performance)
    print("\nProduct Performance:")
    print(product_performance)
```
