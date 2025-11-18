"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Write SQL queries to manage a database for an online store, including tables for product categories, discounts, and user accounts, as seen on Multan Designs.
Generated: DETERMINISTIC_55a9eb2c96a31f2d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for discounts
CREATE TABLE Discounts (
    DiscountID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each discount
    DiscountName VARCHAR(255) NOT NULL,        -- Name of the discount
    DiscountPercent DECIMAL(5, 2) NOT NULL CHECK (DiscountPercent >= 0 AND DiscountPercent <= 100), 
    -- Discount percentage (0-100)
    StartDate DATE NOT NULL,                   -- Start date of the discount
    EndDate DATE NOT NULL,                     -- End date of the discount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the discount is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for user accounts
CREATE TABLE UserAccounts (
    UserID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique ID for each user
    UserName VARCHAR(255) NOT NULL,           -- Username of the user
    Email VARCHAR(255) NOT NULL UNIQUE,       -- Email (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,       -- Hashed password for security
    Role ENUM('Customer', 'Admin') DEFAULT 'Customer', -- Role of the user
    IsActive BOOLEAN DEFAULT TRUE,            -- Whether the account is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the account is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Add a foreign key relation between products and categories
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product
    CategoryID INT,                           -- Foreign key to the ProductCategories table
    DiscountID INT,                           -- Foreign key to the Discounts table
    Stock INT NOT NULL DEFAULT 0 CHECK (Stock >= 0), -- Number of items in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) 
    ON DELETE SET NULL ON UPDATE CASCADE, -- Handle category deletion/update
    FOREIGN KEY (DiscountID) REFERENCES Discounts(DiscountID) 
    ON DELETE SET NULL ON UPDATE CASCADE   -- Handle discount deletion/update
);

-- Insert sample data for testing (optional)
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Clothing', 'Apparel like shirts, pants, and dresses'),
('Accessories', 'Items such as watches, jewelry, and belts');

INSERT INTO Discounts (DiscountName, DiscountPercent, StartDate, EndDate) VALUES
('New Year Sale', 20.00, '2023-12-30', '2024-01-05'),
('Summer Sale', 15.00, '2024-06-01', '2024-06-15');

INSERT INTO UserAccounts (UserName, Email, PasswordHash, Role) VALUES
('JohnDoe', 'johndoe@example.com', SHA2('password123', 256), 'Customer'),
('AdminUser', 'admin@example.com', SHA2('adminpassword', 256), 'Admin');

INSERT INTO Products (ProductName, Price, CategoryID, DiscountID, Stock) VALUES
('Men T-Shirt', 500.00, 1, NULL, 50),
('Gold Bracelet', 1500.00, 2, 1, 25);
```
