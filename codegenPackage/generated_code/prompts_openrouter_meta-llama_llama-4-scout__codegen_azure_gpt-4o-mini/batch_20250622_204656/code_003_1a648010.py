"""
Generated Code Metadata:
========================
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: "Design a database schema to store information about glass products, including product types, materials, and dimensions, inspired by the product offerings on the Maryart website."
Generated: DETERMINISTIC_1a6480100eae495d
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about glass products

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductTypes;
DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS Dimensions;
DROP TABLE IF EXISTS GlassProducts;

-- Table to store different types of glass products
CREATE TABLE ProductTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each product type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the product type
    description TEXT -- Description of the product type
);

-- Table to store different materials used in glass products
CREATE TABLE Materials (
    id SERIAL PRIMARY KEY, -- Unique identifier for each material
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the material
    description TEXT -- Description of the material
);

-- Table to store dimensions of glass products
CREATE TABLE Dimensions (
    id SERIAL PRIMARY KEY, -- Unique identifier for each dimension
    height DECIMAL(10, 2) NOT NULL, -- Height of the product in cm
    width DECIMAL(10, 2) NOT NULL, -- Width of the product in cm
    depth DECIMAL(10, 2) NOT NULL -- Depth of the product in cm
);

-- Table to store information about glass products
CREATE TABLE GlassProducts (
    id SERIAL PRIMARY KEY, -- Unique identifier for each glass product
    name VARCHAR(100) NOT NULL, -- Name of the glass product
    product_type_id INT NOT NULL, -- Foreign key referencing ProductTypes
    material_id INT NOT NULL, -- Foreign key referencing Materials
    dimension_id INT NOT NULL, -- Foreign key referencing Dimensions
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (product_type_id) REFERENCES ProductTypes(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (material_id) REFERENCES Materials(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (dimension_id) REFERENCES Dimensions(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO ProductTypes (name, description) VALUES
('Vase', 'A decorative container for flowers.'),
('Glassware', 'Drinking vessels made of glass.'),
('Window Pane', 'A flat piece of glass used in windows.');

INSERT INTO Materials (name, description) VALUES
('Borosilicate Glass', 'A type of glass with low thermal expansion.'),
('Tempered Glass', 'Safety glass processed by controlled thermal treatments.'),
('Fused Glass', 'Glass that has been melted and fused together.');

INSERT INTO Dimensions (height, width, depth) VALUES
(30.00, 15.00, 15.00),
(10.00, 10.00, 10.00),
(100.00, 50.00, 0.50);

INSERT INTO GlassProducts (name, product_type_id, material_id, dimension_id, price) VALUES
('Elegant Vase', 1, 1, 1, 29.99),
('Classic Glass', 2, 2, 2, 9.99),
('Large Window Pane', 3, 3, 3, 199.99);
```
