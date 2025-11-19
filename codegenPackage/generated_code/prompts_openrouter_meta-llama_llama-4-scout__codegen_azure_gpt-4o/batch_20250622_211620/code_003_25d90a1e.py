"""
Generated Code Metadata:
========================
Original URL: https://redclayware.com
Prompt: Design a basic database schema for an online store, such as Red Clay Ware, that needs to manage products, inventory, and customer subscriptions.
Generated: DETERMINISTIC_25d90a1e648bbfd4
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to manage inventory
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for inventory record
    ProductID INT NOT NULL,                     -- Foreign key referencing Products table
    Quantity INT NOT NULL,                      -- Quantity of the product in stock
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last inventory update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure inventory is deleted if product is deleted
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- Customer's first name
    LastName VARCHAR(255) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer was added
);

-- Table to manage customer subscriptions
CREATE TABLE Subscriptions (
    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subscription
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers table
    ProductID INT NOT NULL,                        -- Foreign key referencing Products table
    StartDate DATE NOT NULL,                       -- Start date of the subscription
    EndDate DATE,                                  -- End date of the subscription (nullable for ongoing subscriptions)
    Status ENUM('Active', 'Inactive', 'Cancelled') DEFAULT 'Active', -- Status of the subscription
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the subscription was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure subscription is deleted if customer is deleted
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure subscription is deleted if product is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(Name); -- Index for quick product name searches
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick customer email lookups
CREATE INDEX idx_subscription_status ON Subscriptions(Status); -- Index for filtering subscriptions by status
```
