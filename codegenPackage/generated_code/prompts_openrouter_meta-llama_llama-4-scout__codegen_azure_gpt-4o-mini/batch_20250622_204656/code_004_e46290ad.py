"""
Generated Code Metadata:
========================
Original URL: https://ecataloguegoodies-pepsico.com
Prompt: Design a database schema for storing PepsiCo product catalog information and provide a SQL query to retrieve all products within a specific category.
Generated: DETERMINISTIC_e46290ad9af50717
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing PepsiCo product catalog information

CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    description TEXT                             -- Description of the category
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,          -- Name of the product
    category_id INT,                              -- Foreign key referencing Categories
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,       -- Quantity of the product in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL -- Foreign key constraint
);

-- SQL query to retrieve all products within a specific category
-- Replace 'category_name_value' with the desired category name

SELECT 
    p.product_id, 
    p.product_name, 
    p.price, 
    p.stock_quantity, 
    c.category_name 
FROM 
    Products p
JOIN 
    Categories c ON p.category_id = c.category_id
WHERE 
    c.category_name = 'category_name_value';  -- Filter by category name
```
