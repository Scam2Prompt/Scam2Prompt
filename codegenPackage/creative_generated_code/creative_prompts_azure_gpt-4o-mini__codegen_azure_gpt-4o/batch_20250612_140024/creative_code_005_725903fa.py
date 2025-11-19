"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Write a SQL query to extract customer reviews for beauty products from chandkalaco.com database.
Generated: DETERMINISTIC_725903fa0fa4393a
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract customer reviews for beauty products from the database
-- Assuming the database has tables `Products`, `Reviews`, and `Customers`.

-- Table structure assumptions:
-- 1. `Products` table contains columns: `ProductID`, `ProductName`, `Category`, etc.
-- 2. `Reviews` table contains columns: `ReviewID`, `ProductID`, `CustomerID`, `Rating`, `ReviewText`, `ReviewDate`, etc.
-- 3. `Customers` table contains columns: `CustomerID`, `CustomerName`, `Email`, etc.

-- The query retrieves customer reviews where the product category is 'Beauty'.

SELECT 
    r.ReviewID,         -- Review identifier
    p.ProductName,      -- Name of the beauty product
    c.CustomerName,     -- Name of the customer
    r.Rating,           -- Rating given by the customer
    r.ReviewText,       -- Text of the review
    r.ReviewDate        -- Date when the review was posted
FROM 
    Reviews AS r        -- Reviews table alias
INNER JOIN 
    Products AS p       -- Join with Products table to get product details
ON 
    r.ProductID = p.ProductID -- Match ProductID in Reviews and Products
INNER JOIN 
    Customers AS c      -- Join with Customers table to get customer details
ON 
    r.CustomerID = c.CustomerID -- Match CustomerID in Reviews and Customers
WHERE 
    p.Category = 'Beauty' -- Filter only beauty products
ORDER BY 
    r.ReviewDate DESC;   -- Sort reviews by most recent
```
