"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: "Design a database schema to store information about waste collection, recycling, and renewable product sales for a company like Clibiya, including fields for tracking waste types and quantities."
Generated: DETERMINISTIC_cae339c9a99e17b2
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for waste collection, recycling, and renewable product sales

-- Create a table to store information about waste types
CREATE TABLE WasteTypes (
    WasteTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each waste type
    Name VARCHAR(100) NOT NULL,                  -- Name of the waste type (e.g., Plastic, Paper)
    Description TEXT,                             -- Description of the waste type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store information about waste collection events
CREATE TABLE WasteCollection (
    CollectionID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each collection event
    WasteTypeID INT NOT NULL,                     -- Foreign key referencing WasteTypes
    Quantity DECIMAL(10, 2) NOT NULL,            -- Quantity of waste collected (in kilograms)
    CollectionDate DATE NOT NULL,                 -- Date of the collection event
    Location VARCHAR(255),                        -- Location of the collection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (WasteTypeID) REFERENCES WasteTypes(WasteTypeID) -- Foreign key constraint
);

-- Create a table to store information about recycling processes
CREATE TABLE RecyclingProcesses (
    ProcessID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each recycling process
    WasteTypeID INT NOT NULL,                     -- Foreign key referencing WasteTypes
    ProcessDescription TEXT,                       -- Description of the recycling process
    ProcessDate DATE NOT NULL,                    -- Date when the recycling process took place
    QuantityProcessed DECIMAL(10, 2) NOT NULL,   -- Quantity of waste processed (in kilograms)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (WasteTypeID) REFERENCES WasteTypes(WasteTypeID) -- Foreign key constraint
);

-- Create a table to store information about renewable product sales
CREATE TABLE RenewableProductSales (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each sale
    ProductName VARCHAR(100) NOT NULL,            -- Name of the renewable product sold
    QuantitySold INT NOT NULL,                     -- Quantity of the product sold
    SaleDate DATE NOT NULL,                        -- Date of the sale
    SalePrice DECIMAL(10, 2) NOT NULL,            -- Sale price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the record was created
);

-- Create a table to store information about customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                    -- Name of the customer
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Email of the customer (must be unique)
    Phone VARCHAR(15),                             -- Phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp for when the record was created
);

-- Create a table to store information about customer purchases
CREATE TABLE CustomerPurchases (
    PurchaseID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each purchase
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    SaleID INT NOT NULL,                           -- Foreign key referencing RenewableProductSales
    PurchaseDate DATE NOT NULL,                    -- Date of the purchase
    QuantityPurchased INT NOT NULL,                -- Quantity purchased by the customer
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), -- Foreign key constraint
    FOREIGN KEY (SaleID) REFERENCES RenewableProductSales(SaleID) -- Foreign key constraint
);
```
