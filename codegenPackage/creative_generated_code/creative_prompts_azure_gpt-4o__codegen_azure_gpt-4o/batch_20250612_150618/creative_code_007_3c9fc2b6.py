"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiosell.com
Prompt: Create a SQL query to store and retrieve product data from Jiosell, focusing on "Books & Music" categories from Flipkart and Amazon.
Generated: DETERMINISTIC_3c9fc2b6212a6a9e
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store product data from Flipkart and Amazon
CREATE TABLE ProductData (
    product_id SERIAL PRIMARY KEY,               -- Unique identifier for the product
    product_name VARCHAR(255) NOT NULL,         -- Name of the product
    category VARCHAR(100) NOT NULL,             -- Category of the product
    subcategory VARCHAR(100) NOT NULL,          -- Subcategory (specific to "Books & Music")
    price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    source VARCHAR(50) NOT NULL,                -- Source platform (Flipkart or Amazon)
    availability_status VARCHAR(50) NOT NULL,  -- Product availability status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the record was created
);

-- Insert sample data for "Books & Music" category from Flipkart and Amazon
INSERT INTO ProductData (product_name, category, subcategory, price, source, availability_status)
VALUES 
('The Great Gatsby', 'Books & Music', 'Books', 299.99, 'Flipkart', 'In Stock'),
('Thriller Album', 'Books & Music', 'Music', 499.99, 'Amazon', 'In Stock'),
('Meditations', 'Books & Music', 'Books', 199.99, 'Flipkart', 'Out of Stock'),
('Classical Piano Collection', 'Books & Music', 'Music', 399.99, 'Amazon', 'In Stock');

-- Query to retrieve data from "Books & Music" category across Flipkart and Amazon
SELECT 
    product_id, 
    product_name, 
    category, 
    subcategory, 
    price, 
    source, 
    availability_status, 
    created_at
FROM 
    ProductData
WHERE 
    category = 'Books & Music'
ORDER BY 
    source, subcategory, price; -- Data sorted by source, subcategory, and price for better readability

-- Note: Ensure proper indexing on columns like source and category for optimized query performance.
```
