"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgiwindia.com
Prompt: Write a SQL query to store and retrieve information about Jai Gurudev Industries' sugar-boiled confectionery products, such as "Peanut Candy" and "Honey Lemon Mint Candy."
Generated: DETERMINISTIC_82dab87628d7d575
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store information about sugar-boiled confectionery products
CREATE TABLE ConfectioneryProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,               -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,                      -- Name of the confectionery product
    Description TEXT,                                       -- Optional description of the product
    Ingredients TEXT NOT NULL,                              -- List of ingredients used in the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),       -- Price of the product (non-negative)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,          -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Insert sample data into the table
INSERT INTO ConfectioneryProducts (ProductName, Description, Ingredients, Price)
VALUES 
('Peanut Candy', 'Delicious peanut-based candy, sugar-boiled to perfection.', 'Sugar, Peanuts', 1.99),
('Honey Lemon Mint Candy', 'Refreshing candy with honey, lemon, and mint flavors.', 'Sugar, Honey, Lemon, Mint', 2.49);

-- Retrieve all records from the table
SELECT 
    ProductID,
    ProductName,
    Description,
    Ingredients,
    Price,
    CreatedAt,
    UpdatedAt
FROM 
    ConfectioneryProducts
ORDER BY 
    ProductName;   -- Order by product name for better readability
```
