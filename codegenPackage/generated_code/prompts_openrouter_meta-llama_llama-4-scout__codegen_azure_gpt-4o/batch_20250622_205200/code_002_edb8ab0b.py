"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Generate a SQL query to design a database schema for storing information about wood products, including product types (e.g., compensados resinados, portas), materials (e.g., Sucupira, Itauba), and production dates.
Generated: DETERMINISTIC_edb8ab0ba37d142c
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing information about wood products

-- Create a table to store product types
CREATE TABLE ProductTypes (
    ProductTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product type
    ProductTypeName VARCHAR(255) NOT NULL,        -- Name of the product type (e.g., compensados resinados, portas)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the product type was added
);

-- Create a table to store materials
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each material
    MaterialName VARCHAR(255) NOT NULL,           -- Name of the material (e.g., Sucupira, Itauba)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the material was added
);

-- Create a table to store wood products
CREATE TABLE WoodProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each wood product
    ProductTypeID INT NOT NULL,                   -- Foreign key referencing ProductTypes table
    MaterialID INT NOT NULL,                      -- Foreign key referencing Materials table
    ProductionDate DATE NOT NULL,                 -- Date when the product was produced
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    FOREIGN KEY (ProductTypeID) REFERENCES ProductTypes(ProductTypeID) ON DELETE CASCADE, -- Cascade delete for product type
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE          -- Cascade delete for material
);

-- Ensure the database schema is properly normalized and relationships are established
-- ProductTypes table stores types of products
-- Materials table stores types of materials
-- WoodProducts table links product types and materials with production dates
```
