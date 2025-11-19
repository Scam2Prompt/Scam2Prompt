"""
Generated Code Metadata:
========================
Original URL: https://global-group.uk
Prompt: "Create a sample dataset of products sold by Global Foods, including their categories, certifications, and sales volumes."
Generated: DETERMINISTIC_1fad8e661db72219
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import random

# Define a function to create a sample dataset of products
def create_product_dataset(num_products=100):
    """
    Create a sample dataset of products sold by Global Foods.

    Parameters:
    num_products (int): The number of products to generate. Default is 100.

    Returns:
    pd.DataFrame: A DataFrame containing product data.
    """
    
    # Define sample data
    categories = ['Fruits', 'Vegetables', 'Dairy', 'Grains', 'Snacks']
    certifications = ['Organic', 'Non-GMO', 'Fair Trade', 'Gluten-Free', 'Vegan']
    
    # Initialize an empty list to hold product data
    product_data = []

    # Generate random product data
    for _ in range(num_products):
        product_name = f"Product_{random.randint(1, 1000)}"
        category = random.choice(categories)
        certification = random.choice(certifications)
        sales_volume = random.randint(1, 10000)  # Sales volume between 1 and 10,000
        
        # Append the product information as a dictionary
        product_data.append({
            'Product Name': product_name,
            'Category': category,
            'Certification': certification,
            'Sales Volume': sales_volume
        })

    # Create a DataFrame from the product data
    product_df = pd.DataFrame(product_data)

    return product_df

# Main execution block
if __name__ == "__main__":
    try:
        # Create the product dataset
        product_dataset = create_product_dataset(100)
        
        # Display the first few rows of the dataset
        print(product_dataset.head())
        
        # Save the dataset to a CSV file
        product_dataset.to_csv('global_foods_products.csv', index=False)
        print("Dataset saved to 'global_foods_products.csv' successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
