"""
Generated Code Metadata:
========================
Original URL: https://petroleumegate.com
Prompt: "Create a SQL database schema to store information about P.G.C.'s oil products, customers, and supply chain logistics."
Generated: DETERMINISTIC_08f71dae6aae7e4e
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for P.G.C.'s Oil Products, Customers, and Supply Chain Logistics

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS SupplyChainLogistics;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS OilProducts;

-- Table to store information about oil products
CREATE TABLE OilProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the oil product
    ProductType VARCHAR(100) NOT NULL,         -- Type of oil (e.g., crude, refined)
    QuantityInStock DECIMAL(10, 2) NOT NULL,   -- Quantity available in stock
    PricePerUnit DECIMAL(10, 2) NOT NULL,      -- Price per unit of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    CustomerName VARCHAR(255) NOT NULL,         -- Name of the customer
    ContactEmail VARCHAR(255) NOT NULL UNIQUE,  -- Email address of the customer
    PhoneNumber VARCHAR(20),                     -- Phone number of the customer
    Address VARCHAR(255),                        -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store supply chain logistics information
CREATE TABLE SupplyChainLogistics (
    LogisticsID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each logistics entry
    ProductID INT NOT NULL,                       -- Foreign key referencing OilProducts
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    Quantity DECIMAL(10, 2) NOT NULL,            -- Quantity of product being supplied
    SupplyDate DATE NOT NULL,                     -- Date of supply
    DeliveryStatus ENUM('Pending', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of delivery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of logistics entry creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ProductID) REFERENCES OilProducts(ProductID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON OilProducts(ProductName);
CREATE INDEX idx_customer_name ON Customers(CustomerName);
CREATE INDEX idx_supply_date ON SupplyChainLogistics(SupplyDate);
```
