"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Create a database schema for a retail store management system that includes modules for inventory control, sales tracking, and electronic invoicing, as outlined by TICOM Software.
Generated: DETERMINISTIC_678eae0c1d6971ee
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Retail Store Management System Database Schema

-- Create schema for inventory control
CREATE TABLE Inventory (
    ItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each item
    ItemName VARCHAR(255) NOT NULL, -- Name of the item
    Description TEXT, -- Description of the item
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Number of items in stock (must be non-negative)
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price per unit
    Category VARCHAR(100), -- Category of the item
    SupplierID INT, -- Foreign key referring to the supplier providing the item
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create schema for sales tracking
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sale
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the sale
    CustomerID INT, -- Foreign key referring to the customer (nullable for guest customers)
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount of the sale
    PaymentMethod VARCHAR(50) NOT NULL, -- Payment method used (e.g., cash, credit card)
    Status ENUM('Completed', 'Pending', 'Cancelled') DEFAULT 'Completed', -- Status of the sale
    InvoiceID INT, -- Foreign key referring to the electronic invoice for the sale
    Notes TEXT -- Optional notes associated with the sale
);

-- Create schema for electronic invoices
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each invoice
    SaleID INT NOT NULL, -- Foreign key referring to the sale associated with the invoice
    InvoiceDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the invoice was issued
    CustomerDetails TEXT NOT NULL, -- Customer information (name, address, etc.)
    PaymentDetails TEXT NOT NULL, -- Payment information (card details, etc.)
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount for the invoice
    Status ENUM('Paid', 'Unpaid', 'Cancelled') DEFAULT 'Unpaid', -- Status of the invoice
    FOREIGN KEY (SaleID) REFERENCES Sales(SaleID) ON DELETE CASCADE -- Cascade delete when sale is deleted
);

-- Create schema for suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL, -- Name of the supplier
    ContactPerson VARCHAR(255), -- Contact person at the supplier
    PhoneNumber VARCHAR(50), -- Contact phone number
    Email VARCHAR(255), -- Contact email
    Address TEXT -- Address of the supplier
);

-- Create schema for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    CustomerName VARCHAR(255) NOT NULL, -- Name of the customer
    PhoneNumber VARCHAR(50), -- Contact phone number
    Email VARCHAR(255), -- Contact email
    Address TEXT -- Address of the customer
);

-- Create schema for inventory sales relationship
CREATE TABLE InventorySales (
    InventorySaleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the inventory-sale relationship
    SaleID INT NOT NULL, -- Foreign key referring to the sale
    ItemID INT NOT NULL, -- Foreign key referring to the inventory item
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of items sold
    LineTotal DECIMAL(10, 2) NOT NULL CHECK (LineTotal >= 0), -- Total price for the line item
    FOREIGN KEY (SaleID) REFERENCES Sales(SaleID) ON DELETE CASCADE, -- Cascade delete when sale is deleted
    FOREIGN KEY (ItemID) REFERENCES Inventory(ItemID) ON DELETE CASCADE -- Cascade delete when item is deleted
);

-- Add indexes for optimization
CREATE INDEX idx_inventory_category ON Inventory(Category); -- Index on category for faster queries
CREATE INDEX idx_sales_date ON Sales(SaleDate); -- Index on sale date for faster queries
CREATE INDEX idx_invoices_date ON Invoices(InvoiceDate); -- Index on invoice date for faster queries

-- Ensure referential integrity
ALTER TABLE Inventory
ADD FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL; -- Set supplier to NULL if deleted

ALTER TABLE Sales
ADD FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE SET NULL; -- Set customer to NULL if deleted
```
