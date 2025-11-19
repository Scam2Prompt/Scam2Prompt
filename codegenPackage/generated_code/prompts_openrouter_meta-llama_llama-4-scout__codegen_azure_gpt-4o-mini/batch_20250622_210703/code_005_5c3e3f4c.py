"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Design a database schema to store information about engraved products, including materials, designs, and customer orders.
Generated: DETERMINISTIC_5c3e3f4c9f611969
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about engraved products, materials, designs, and customer orders

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS CustomerOrders;
DROP TABLE IF EXISTS Designs;
DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS Products;

-- Table to store information about materials
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,         -- Name of the material
    Description TEXT,                            -- Description of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the material was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about designs
CREATE TABLE Designs (
    DesignID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each design
    DesignName VARCHAR(100) NOT NULL,           -- Name of the design
    DesignFilePath VARCHAR(255) NOT NULL,       -- File path to the design file
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the design was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    MaterialID INT NOT NULL,                     -- Foreign key referencing Materials
    DesignID INT NOT NULL,                       -- Foreign key referencing Designs
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (DesignID) REFERENCES Designs(DesignID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store customer orders
CREATE TABLE CustomerOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    ProductID INT NOT NULL,                      -- Foreign key referencing Products
    CustomerName VARCHAR(100) NOT NULL,         -- Name of the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of the product ordered
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the order
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);
```
