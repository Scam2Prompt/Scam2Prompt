"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: "Design a database schema for storing information about window and door products, including their characteristics and installation services, inspired by the content on nellyservis.sk."
Generated: DETERMINISTIC_d04f6fb7d62ed642
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about window and door products,
-- including their characteristics and installation services.

-- Table to store product categories (e.g., windows, doors)
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., "Windows", "Doors")
    Description TEXT                           -- Optional description of the category
);

-- Table to store individual products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key to ProductCategories
    Material VARCHAR(255),                     -- Material of the product (e.g., "Wood", "PVC", "Aluminum")
    Dimensions VARCHAR(255),                   -- Dimensions of the product (e.g., "120x150 cm")
    Color VARCHAR(255),                        -- Color of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity available in stock
    Description TEXT,                          -- Optional description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store installation services
CREATE TABLE InstallationServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the service
    Name VARCHAR(255) NOT NULL,                -- Name of the installation service
    Description TEXT,                          -- Optional description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the installation service
    DurationHours INT NOT NULL,                -- Estimated duration of the service in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to associate products with installation services
CREATE TABLE ProductInstallationServices (
    ProductID INT NOT NULL,                    -- Foreign key to Products
    ServiceID INT NOT NULL,                    -- Foreign key to InstallationServices
    PRIMARY KEY (ProductID, ServiceID),        -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES InstallationServices(ServiceID) ON DELETE CASCADE
);

-- Table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the order
    CustomerName VARCHAR(255) NOT NULL,        -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,       -- Email of the customer
    CustomerPhone VARCHAR(20),                 -- Phone number of the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., "Pending", "Completed")
    Notes TEXT                                 -- Optional notes for the order
);

-- Table to store order details (products in the order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the order detail
    OrderID INT NOT NULL,                         -- Foreign key to Orders
    ProductID INT NOT NULL,                       -- Foreign key to Products
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store order installation services
CREATE TABLE OrderInstallationServices (
    OrderInstallationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the order installation service
    OrderID INT NOT NULL,                               -- Foreign key to Orders
    ServiceID INT NOT NULL,                             -- Foreign key to InstallationServices
    Price DECIMAL(10, 2) NOT NULL,                      -- Price of the service at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES InstallationServices(ServiceID) ON DELETE CASCADE
);
```
