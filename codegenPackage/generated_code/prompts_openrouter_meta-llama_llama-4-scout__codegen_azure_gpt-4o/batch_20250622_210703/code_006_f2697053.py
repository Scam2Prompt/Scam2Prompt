"""
Generated Code Metadata:
========================
Original URL: https://marinekiosk.gr
Prompt: "Design a database schema for storing information about cannabis products, including their types (CBD, CBG, CB9), quantities, and suppliers, as seen on Marine Kiosk's website."
Generated: DETERMINISTIC_f2697053695c676b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about cannabis products, their types, quantities, and suppliers.

-- Create a table to store supplier information
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactInfo VARCHAR(255),                  -- Contact information for the supplier
    Address TEXT,                              -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store cannabis product types
CREATE TABLE ProductTypes (
    TypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product type
    Name VARCHAR(50) NOT NULL UNIQUE,      -- Name of the product type (e.g., CBD, CBG, CB9)
    Description TEXT,                      -- Optional description of the product type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store cannabis product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    TypeID INT NOT NULL,                      -- Foreign key referencing ProductTypes table
    Quantity INT NOT NULL,                    -- Quantity of the product available
    SupplierID INT NOT NULL,                  -- Foreign key referencing Suppliers table
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (TypeID) REFERENCES ProductTypes(TypeID) ON DELETE CASCADE, -- Cascade delete for product type
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Cascade delete for supplier
);

-- Create indexes for faster querying
CREATE INDEX idx_product_type ON Products(TypeID);
CREATE INDEX idx_supplier ON Products(SupplierID);
```
