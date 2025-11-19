"""
Generated Code Metadata:
========================
Original URL: https://delourier.com
Prompt: Design a database schema for an e-commerce platform that sells high-end chain mail fashion apparel, including tables for products, materials, and orders.
Generated: DETERMINISTIC_c90b82754786d67f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling high-end chain mail fashion apparel

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                           -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store material information
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each material
    MaterialName VARCHAR(255) NOT NULL,         -- Name of the material
    Description TEXT,                            -- Description of the material
    CostPerUnit DECIMAL(10, 2) NOT NULL         -- Cost per unit of the material
);

-- Table to store the relationship between products and materials
CREATE TABLE ProductMaterials (
    ProductMaterialID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the relationship
    ProductID INT NOT NULL,                          -- Foreign key referencing Products
    MaterialID INT NOT NULL,                         -- Foreign key referencing Materials
    QuantityUsed INT NOT NULL,                       -- Quantity of material used in the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each order
    UserID INT NOT NULL,                            -- Identifier for the user placing the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,           -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Assuming a Users table exists
);

-- Table to store order items (products included in each order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order item
    OrderID INT NOT NULL,                           -- Foreign key referencing Orders
    ProductID INT NOT NULL,                         -- Foreign key referencing Products
    Quantity INT NOT NULL,                          -- Quantity of the product ordered
    PriceAtPurchase DECIMAL(10, 2) NOT NULL,       -- Price of the product at the time of purchase
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store user information (assuming it is needed for the Orders table)
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each user
    Username VARCHAR(255) NOT NULL UNIQUE,         -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,            -- Hashed password for security
    Email VARCHAR(255) NOT NULL UNIQUE,            -- Unique email address for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp for when the user was created
);
```
