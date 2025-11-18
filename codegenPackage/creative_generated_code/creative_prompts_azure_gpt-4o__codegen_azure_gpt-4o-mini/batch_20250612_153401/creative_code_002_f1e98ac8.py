"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Create a SQL query to retrieve all products under "Masala & Spices" and "Dry Fruits & Nuts" categories with their prices and discounts, similar to the product organization on Trykart.
Generated: DETERMINISTIC_f1e98ac8d5d4d59c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all products under specified categories
-- with their prices and discounts from the 'products' table

SELECT 
    p.product_id,               -- Unique identifier for the product
    p.product_name,             -- Name of the product
    p.price,                    -- Price of the product
    p.discount,                 -- Discount applicable on the product
    c.category_name             -- Name of the category the product belongs to
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id  -- Joining products with their categories
WHERE 
    c.category_name IN ('Masala & Spices', 'Dry Fruits & Nuts')  -- Filtering for specified categories
ORDER BY 
    c.category_name, p.product_name;  -- Ordering results by category name and product name
```

**Note:** Ensure that the `products` and `categories` tables contain the appropriate fields (`product_id`, `product_name`, `price`, `discount`, `category_id`, `category_name`) for this query to execute successfully without errors.
