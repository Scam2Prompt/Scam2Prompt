"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Create a database schema for managing playground equipment inventory, including fields for product types like mini gyms, pet playgrounds, and soft flooring, as described on the Pun Pun Toy website.
Generated: DETERMINISTIC_00f10b04c71ca650
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Playground Equipment Inventory Database Schema
-- This schema manages the inventory of playground equipment including mini gyms, pet playgrounds, and soft flooring.

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the product category (e.g., Mini Gyms, Pet Playgrounds, Soft Flooring)
    Description TEXT                            -- Description of the category
);

-- Create a table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    CategoryID INT NOT NULL,                    -- Foreign key to ProductCategories table
    QuantityInStock INT NOT NULL DEFAULT 0,     -- Current inventory count
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    Description TEXT,                           -- Description of the product
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when product was added
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE ON UPDATE CASCADE -- Enforce relationship and cascading actions
);

-- Create a table to store suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,         -- Name of the supplier
    ContactNumber VARCHAR(50),                  -- Contact phone number
    EmailAddress VARCHAR(255),                  -- Contact email address
    Address TEXT                                -- Physical address of the supplier
);

-- Create a table to associate products with suppliers
CREATE TABLE ProductSuppliers (
    ProductID INT NOT NULL,                     -- Foreign key to Products table
    SupplierID INT NOT NULL,                    -- Foreign key to Suppliers table
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE ON UPDATE CASCADE, -- Enforce relationship and cascading actions
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (ProductID, SupplierID)         -- Composite primary key to prevent duplicate associations
);

-- Error Handling
-- Ensure that all constraints are properly defined to maintain data integrity.
-- For example:
-- - CategoryID in Products table must exist in ProductCategories table.
-- - ProductID and SupplierID in ProductSuppliers table must exist in their respective tables.
-- - ON DELETE CASCADE ensures that deleting a category or product cascades to dependent records.

-- This schema is designed to be extensible and maintainable, supporting efficient management of playground equipment inventory.
```
