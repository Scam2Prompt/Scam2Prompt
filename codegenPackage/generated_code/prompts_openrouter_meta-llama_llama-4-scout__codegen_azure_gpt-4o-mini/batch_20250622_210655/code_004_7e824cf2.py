"""
Generated Code Metadata:
========================
Original URL: https://saldiana.com.br
Prompt: "Design a database schema to store information about Sal Diana's products, including product lines (e.g., Linha Diana, Linha Apolo), product descriptions, and pricing information."
Generated: DETERMINISTIC_7e824cf291f4a081
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Sal Diana's products

-- Create a table for product lines
CREATE TABLE ProductLines (
    id SERIAL PRIMARY KEY, -- Unique identifier for each product line
    name VARCHAR(255) NOT NULL, -- Name of the product line (e.g., Linha Diana, Linha Apolo)
    description TEXT, -- Description of the product line
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product line was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product line was last updated
);

-- Create a table for products
CREATE TABLE Products (
    id SERIAL PRIMARY KEY, -- Unique identifier for each product
    product_line_id INT NOT NULL, -- Foreign key referencing the product line
    name VARCHAR(255) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (product_line_id) REFERENCES ProductLines(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on product line name for faster searches
CREATE INDEX idx_product_line_name ON ProductLines(name);

-- Create an index on product name for faster searches
CREATE INDEX idx_product_name ON Products(name);
```
