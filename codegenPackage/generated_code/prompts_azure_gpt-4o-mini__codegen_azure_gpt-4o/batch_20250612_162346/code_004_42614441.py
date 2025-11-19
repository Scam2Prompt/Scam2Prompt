"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: Design a database schema for an online platform that categorizes home decoration products and services, reflecting the organization seen on origines-decoration.com.
Generated: DETERMINISTIC_426144416a4b1854
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online platform categorizing home decoration products and services

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username for login
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store categories of products and services
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL UNIQUE,         -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of category creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CategoryID INT NOT NULL,                  -- Foreign key to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Cascade delete if category is removed
);

-- Table to store services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(100) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Optional description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CategoryID INT NOT NULL,                  -- Foreign key to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of service creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Cascade delete if category is removed
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    UserID INT NOT NULL,                    -- Foreign key to Users table
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount of the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store order items (products and services)
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key to Orders table
    ProductID INT,                              -- Foreign key to Products table (nullable for services)
    ServiceID INT,                              -- Foreign key to Services table (nullable for products)
    Quantity INT NOT NULL,                      -- Quantity of the product/service ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product/service at the time of order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order item creation
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE SET NULL, -- Set NULL if product is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL -- Set NULL if service is removed
);

-- Table to store reviews for products and services
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    UserID INT NOT NULL,                     -- Foreign key to Users table
    ProductID INT,                           -- Foreign key to Products table (nullable for services)
    ServiceID INT,                           -- Foreign key to Services table (nullable for products)
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                            -- Optional comment for the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of review creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE SET NULL, -- Set NULL if product is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL -- Set NULL if service is removed
);

-- Table to store images for products and services
CREATE TABLE Images (
    ImageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each image
    ProductID INT,                          -- Foreign key to Products table (nullable for services)
    ServiceID INT,                          -- Foreign key to Services table (nullable for products)
    ImageURL VARCHAR(255) NOT NULL,         -- URL of the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of image creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete if product is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);
```
