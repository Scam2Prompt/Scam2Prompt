"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: "Design a database schema to store information about various Himalayan salt products, including their types, prices, and quantities."
Generated: DETERMINISTIC_6396fbb87d309e2e
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Himalayan salt products

-- Create a table to store product types
CREATE TABLE ProductTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each product type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the product type (e.g., "Himalayan Pink Salt")
    description TEXT -- Description of the product type
);

-- Create a table to store salt products
CREATE TABLE SaltProducts (
    id SERIAL PRIMARY KEY, -- Unique identifier for each salt product
    name VARCHAR(100) NOT NULL, -- Name of the salt product
    type_id INT NOT NULL, -- Foreign key referencing the product type
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product, must be non-negative
    quantity INT NOT NULL CHECK (quantity >= 0), -- Quantity of the product in stock, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (type_id) REFERENCES ProductTypes(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the name column of SaltProducts for faster searches
CREATE INDEX idx_salt_product_name ON SaltProducts(name);

-- Create an index on the price column of SaltProducts for faster price-based queries
CREATE INDEX idx_salt_product_price ON SaltProducts(price);
```
