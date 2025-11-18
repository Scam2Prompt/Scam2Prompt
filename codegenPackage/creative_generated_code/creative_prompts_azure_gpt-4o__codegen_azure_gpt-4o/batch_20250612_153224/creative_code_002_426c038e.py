"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techcherio.com
Prompt: Create a database schema for a B2B web application, incorporating features mentioned in TechCherio's software development services.
Generated: DETERMINISTIC_426c038ee96a669f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a B2B web application
-- This schema incorporates features typically required for B2B software.

-- Create a table for storing company information
CREATE TABLE Companies (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each company
    Name VARCHAR(255) NOT NULL,              -- Company name
    Address TEXT,                            -- Company address
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Contact email (must be unique)
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    Website VARCHAR(255),                    -- Company website URL
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each user
    CompanyID INT NOT NULL,                  -- Foreign key linking to Companies table
    FirstName VARCHAR(100) NOT NULL,         -- User's first name
    LastName VARCHAR(100) NOT NULL,          -- User's last name
    Email VARCHAR(255) UNIQUE NOT NULL,      -- User's email (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    Role ENUM('Admin', 'Manager', 'Employee') NOT NULL, -- User role within the company
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE -- Cascade delete if the company is removed
);

-- Create a table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Product name
    Description TEXT,                         -- Product description
    Price DECIMAL(10, 2) NOT NULL,            -- Product price
    StockQuantity INT NOT NULL,               -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for storing orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    CompanyID INT NOT NULL,                   -- Foreign key linking to Companies table
    UserID INT NOT NULL,                      -- Foreign key linking to Users table (who placed the order)
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total order amount
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') NOT NULL, -- Order status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE, -- Cascade delete if the company is removed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET NULL -- Set to NULL if the user is removed
);

-- Create a table for storing order details (products in an order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key linking to Orders table
    ProductID INT NOT NULL,                       -- Foreign key linking to Products table
    Quantity INT NOT NULL,                        -- Quantity of a specific product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if the order is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE SET NULL -- Set to NULL if the product is removed
);

-- Create a table for logging system activities
CREATE TABLE ActivityLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each log entry
    UserID INT,                              -- Foreign key linking to Users table 
    Action VARCHAR(255) NOT NULL,            -- Description of the action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time when the action occurred
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET NULL -- Set to NULL if the user is removed
);
```
