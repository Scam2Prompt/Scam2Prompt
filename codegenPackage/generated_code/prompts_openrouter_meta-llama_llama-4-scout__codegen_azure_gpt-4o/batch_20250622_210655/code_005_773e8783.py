"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Design a database schema to store customer information, repair services, and product inventory for a business like Geeks on Repair.
Generated: DETERMINISTIC_773e878341c99518
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Geeks on Repair Business

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store repair services
CREATE TABLE RepairServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the repair service
    Description TEXT,                          -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    EstimatedDuration VARCHAR(50),             -- Estimated duration for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store product inventory
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Quantity INT NOT NULL,                     -- Quantity available in inventory
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store repair orders
CREATE TABLE RepairOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each repair order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                    -- Foreign key referencing RepairServices table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    Status VARCHAR(50) DEFAULT 'Pending',      -- Status of the repair order (e.g., Pending, In Progress, Completed)
    TotalCost DECIMAL(10, 2),                  -- Total cost of the repair order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES RepairServices(ServiceID) ON DELETE CASCADE
);

-- Table to store product sales
CREATE TABLE ProductSales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product sale
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ProductID INT NOT NULL,                    -- Foreign key referencing Products table
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the sale
    Quantity INT NOT NULL,                     -- Quantity of the product sold
    TotalCost DECIMAL(10, 2),                  -- Total cost of the sale
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index on email for faster lookups
CREATE INDEX idx_service_name ON RepairServices(ServiceName); -- Index on service name for faster lookups
CREATE INDEX idx_product_name ON Products(ProductName); -- Index on product name for faster lookups
```
