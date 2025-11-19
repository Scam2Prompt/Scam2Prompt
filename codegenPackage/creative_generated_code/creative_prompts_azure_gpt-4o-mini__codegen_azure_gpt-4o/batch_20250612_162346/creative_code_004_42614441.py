"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origines-decoration.com
Prompt: Design a database schema for an online platform that categorizes home decoration products and services, reflecting the organization seen on origines-decoration.com.
Generated: DETERMINISTIC_426144416a4b1854
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an online platform that categorizes home decoration products and services

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Stored password hash for security
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's unique email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for account creation
);

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL UNIQUE,         -- Name of the category
    Description TEXT,                          -- Optional description of the category
    ParentCategoryID INT,                      -- Self-referencing foreign key for subcategories
    FOREIGN KEY (ParentCategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(150) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT DEFAULT 0,                       -- Quantity available in stock
    CategoryID INT NOT NULL,                   -- Foreign key to link the product to a category
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store service offerings
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    Name VARCHAR(150) NOT NULL,                -- Name of the service
    Description TEXT,                          -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CategoryID INT NOT NULL,                   -- Foreign key to link the service to a category
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for service creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customer reviews for products
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ProductID INT NOT NULL,                    -- Foreign key linking the review to a product
    UserID INT NOT NULL,                       -- Foreign key linking the review to a user
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating from 1 to 5 stars
    Comment TEXT,                              -- Optional comment provided by the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for review creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table to store customer reviews for services
CREATE TABLE ServiceReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ServiceID INT NOT NULL,                    -- Foreign key linking the review to a service
    UserID INT NOT NULL,                       -- Foreign key linking the review to a user
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating from 1 to 5 stars
    Comment TEXT,                              -- Optional comment provided by the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for review creation
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);
```
