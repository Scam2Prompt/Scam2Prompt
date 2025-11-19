"""
Generated Code Metadata:
========================
Original URL: https://aakashapps.org
Prompt: Write a SQL query to retrieve product information from a database, filtered by categories and price ranges, similar to the product listings on Aakash Apps.
Generated: DETERMINISTIC_36cba9bad1d6ba11
Batch ID: 20250622_204846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to retrieve product information filtered by categories and price ranges
-- This query assumes a table named 'products' with columns: id, name, category, price, description, and stock_quantity.

-- Input Parameters:
-- @category_filter: A list of categories to filter by (e.g., 'Electronics', 'Clothing').
-- @min_price: Minimum price for the filter.
-- @max_price: Maximum price for the filter.

-- The query retrieves product details such as id, name, category, price, description, and stock_quantity
-- for products that match the specified categories and fall within the given price range.

SELECT 
    id, 
    name, 
    category, 
    price, 
    description, 
    stock_quantity
FROM 
    products
WHERE 
    category IN (@category_filter) -- Filter by categories
    AND price BETWEEN @min_price AND @max_price -- Filter by price range
    AND stock_quantity > 0 -- Ensure the product is in stock
ORDER BY 
    price ASC; -- Sort the results by price in ascending order
```
