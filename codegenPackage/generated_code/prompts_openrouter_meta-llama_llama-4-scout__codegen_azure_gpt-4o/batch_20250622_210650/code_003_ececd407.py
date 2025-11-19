"""
Generated Code Metadata:
========================
Original URL: https://ranchioffline.com
Prompt: Design a database schema for an e-commerce platform like RanchiOffline that offers multiple products and services, including government documentation support.
Generated: DETERMINISTIC_ececd407644e3a84
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform offering products, services, and government documentation support

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    PhoneNumber VARCHAR(15),               -- Contact number of the user
    Address TEXT,                          -- Address of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    Category VARCHAR(255),                    -- Category of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    Category VARCHAR(255),                    -- Category of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store government documentation support information
CREATE TABLE DocumentationSupport (
    DocID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each documentation support service
    Name VARCHAR(255) NOT NULL,              -- Name of the documentation support service
    Description TEXT,                        -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the service
    RequiredDocuments TEXT,                  -- List of required documents for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each order
    UserID INT NOT NULL,                     -- Reference to the user who placed the order
    TotalAmount DECIMAL(10, 2) NOT NULL,     -- Total amount of the order
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store order items (products and services)
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Reference to the order
    ProductID INT,                              -- Reference to the product (nullable for services)
    ServiceID INT,                              -- Reference to the service (nullable for products)
    Quantity INT NOT NULL,                      -- Quantity of the product/service
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product/service
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE SET NULL, -- Foreign key constraint
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL -- Foreign key constraint
);

-- Table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    OrderID INT NOT NULL,                      -- Reference to the order
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount paid
    PaymentMethod ENUM('CreditCard', 'DebitCard', 'NetBanking', 'UPI', 'CashOnDelivery') NOT NULL, -- Payment method
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment was created
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store reviews for products and services
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    UserID INT NOT NULL,                       -- Reference to the user who wrote the review
    ProductID INT,                             -- Reference to the product (nullable for services)
    ServiceID INT,                             -- Reference to the service (nullable for products)
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the user (1 to 5)
    Comment TEXT,                              -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE SET NULL, -- Foreign key constraint
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL -- Foreign key constraint
);
```
