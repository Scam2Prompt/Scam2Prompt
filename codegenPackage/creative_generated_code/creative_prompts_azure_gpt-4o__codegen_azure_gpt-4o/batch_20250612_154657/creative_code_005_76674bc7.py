"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Provide an example of using the Pandas library to analyze and visualize the price range of products listed under "Mesa Posta" on the Camicado website.
Generated: DETERMINISTIC_76674bc7992a970a
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch and prepare data from a website
def fetch_product_data():
    """
    Simulates fetching product data. In a real-world scenario, this would involve web scraping or API requests.
    Returns a DataFrame with product data.
    """
    # Example product data; in reality, this would be dynamically fetched from the website
    data = {
        "Product Name": [
            "Mesa Posta - Product 1", 
            "Mesa Posta - Product 2", 
            "Mesa Posta - Product 3", 
            "Mesa Posta - Product 4", 
            "Mesa Posta - Product 5"
        ],
        "Price (BRL)": [129.99, 89.90, 199.99, 149.00, 75.50]
    }
    return pd.DataFrame(data)

# Analyze price range
def analyze_price_range(df):
    """
    Analyzes the price range of products in the given DataFrame.
    Prints key statistics and visualizes the price distribution using a histogram.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing product data with a "Price (BRL)" column.
    """
    try:
        # Ensure the DataFrame has the necessary column
        if "Price (BRL)" not in df.columns:
            raise ValueError("DataFrame must contain a 'Price (BRL)' column.")

        # Descriptive statistics
        print("Price Range Analysis:")
        print(f"Minimum Price: BRL {df['Price (BRL)'].min():.2f}")
        print(f"Maximum Price: BRL {df['Price (BRL)'].max():.2f}")
        print(f"Average Price: BRL {df['Price (BRL)'].mean():.2f}")
        print(f"Median Price: BRL {df['Price (BRL)'].median():.2f}")
        print(f"Standard Deviation: BRL {df['Price (BRL)'].std():.2f}\n")

        # Visualization
        plt.figure(figsize=(8, 6))
        plt.hist(df["Price (BRL)"], bins=10, color='skyblue', edgecolor='black')
        plt.title("Price Distribution of Mesa Posta Products")
        plt.xlabel("Price (BRL)")
        plt.ylabel("Frequency")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function
def main():
    """
    Main entry point for the program. Fetches product data, analyzes it, and visualizes the price range.
    """
    # Fetch product data
    product_data = fetch_product_data()

    # Display the product data
    print("Product Data:")
    print(product_data, "\n")

    # Analyze the price range
    analyze_price_range(product_data)

if __name__ == "__main__":
    main()
```
