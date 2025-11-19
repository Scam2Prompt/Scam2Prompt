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

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductTypes;
DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS WoodProducts;

-- Create a table for product types
CREATE TABLE ProductTypes (
    ProductTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product type
    ProductTypeName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the product type (e.g., compensados resinados, portas)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the record was last updated
);

-- Create a table for materials
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the material (e.g., Sucupira, Itauba)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the record was last updated
);

-- Create a table for wood products
CREATE TABLE WoodProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each wood product
    ProductName VARCHAR(100) NOT NULL,  -- Name of the wood product
    ProductTypeID INT NOT NULL,  -- Foreign key referencing the ProductTypes table
    MaterialID INT NOT NULL,  -- Foreign key referencing the Materials table
    ProductionDate DATE NOT NULL,  -- Date when the product was produced
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the record was last updated
    FOREIGN KEY (ProductTypeID) REFERENCES ProductTypes(ProductTypeID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Insert sample data into ProductTypes
INSERT INTO ProductTypes (ProductTypeName) VALUES
('Compensados Resinados'),
('Portas');

-- Insert sample data into Materials
INSERT INTO Materials (MaterialName) VALUES
('Sucupira'),
('Itauba');
```
