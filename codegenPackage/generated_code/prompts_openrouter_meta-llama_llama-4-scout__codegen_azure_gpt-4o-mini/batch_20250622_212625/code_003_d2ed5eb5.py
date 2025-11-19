"""
Generated Code Metadata:
========================
Original URL: https://newhomepoocoin.blogspot.com
Prompt: "Design a simple database schema for a shoe inventory management system that includes tables for different shoe types (sapatos, sandalias, tenis) and their attributes."
Generated: DETERMINISTIC_d2ed5eb5de6b0893
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Shoe Inventory Management System

-- Create a table for shoe types
CREATE TABLE ShoeTypes (
    ShoeTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each shoe type
    TypeName VARCHAR(50) NOT NULL               -- Name of the shoe type (e.g., sapatos, sandalias, tenis)
);

-- Create a table for shoes
CREATE TABLE Shoes (
    ShoeID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each shoe
    ShoeTypeID INT NOT NULL,                     -- Foreign key referencing ShoeTypes
    Brand VARCHAR(50) NOT NULL,                  -- Brand of the shoe
    Size DECIMAL(4,2) NOT NULL,                  -- Size of the shoe (e.g., 42.5)
    Color VARCHAR(30) NOT NULL,                  -- Color of the shoe
    Quantity INT NOT NULL DEFAULT 0,             -- Quantity available in stock
    Price DECIMAL(10,2) NOT NULL,                -- Price of the shoe
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the shoe entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ShoeTypeID) REFERENCES ShoeTypes(ShoeTypeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for shoe attributes (e.g., material, style)
CREATE TABLE ShoeAttributes (
    AttributeID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each attribute
    ShoeID INT NOT NULL,                          -- Foreign key referencing Shoes
    AttributeName VARCHAR(50) NOT NULL,          -- Name of the attribute (e.g., material, style)
    AttributeValue VARCHAR(100) NOT NULL,        -- Value of the attribute (e.g., leather, casual)
    FOREIGN KEY (ShoeID) REFERENCES Shoes(ShoeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for ShoeTypes
INSERT INTO ShoeTypes (TypeName) VALUES 
('sapatos'), 
('sandalias'), 
('tenis');

-- Sample data insertion for Shoes
INSERT INTO Shoes (ShoeTypeID, Brand, Size, Color, Quantity, Price) VALUES 
(1, 'BrandA', 42.5, 'Black', 10, 99.99), 
(2, 'BrandB', 40.0, 'Brown', 5, 49.99), 
(3, 'BrandC', 41.0, 'White', 20, 79.99);

-- Sample data insertion for ShoeAttributes
INSERT INTO ShoeAttributes (ShoeID, AttributeName, AttributeValue) VALUES 
(1, 'Material', 'Leather'), 
(1, 'Style', 'Formal'), 
(2, 'Material', 'Synthetic'), 
(2, 'Style', 'Casual'), 
(3, 'Material', 'Mesh'), 
(3, 'Style', 'Sport');
```
