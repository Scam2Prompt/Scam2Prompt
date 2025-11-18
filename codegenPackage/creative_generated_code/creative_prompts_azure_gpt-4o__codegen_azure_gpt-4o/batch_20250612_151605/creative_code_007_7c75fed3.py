"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Write a SQL query to store and retrieve product categories (e.g., "Kerti gépek" or "Fotelek") and their associated details from a database modeled after "Poly-Market.hu."
Generated: DETERMINISTIC_7c75fed39118b1ad
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category (e.g., "Kerti gépek", "Fotelek")
    Description TEXT,                           -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Insert sample product categories into the table
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
    ('Kerti gépek', 'Garden machinery and tools for outdoor use'),
    ('Fotelek', 'Comfortable armchairs for indoor seating');

-- Retrieve all product categories and their details
SELECT 
    CategoryID, 
    CategoryName, 
    Description, 
    CreatedAt, 
    UpdatedAt
FROM 
    ProductCategories;

-- Retrieve a specific product category by name (e.g., "Kerti gépek")
SELECT 
    CategoryID, 
    CategoryName, 
    Description, 
    CreatedAt, 
    UpdatedAt
FROM 
    ProductCategories
WHERE 
    CategoryName = 'Kerti gépek';

-- Error handling: Ensure table exists before querying
-- This step should be incorporated into application code or procedures managing this SQL logic.
```
