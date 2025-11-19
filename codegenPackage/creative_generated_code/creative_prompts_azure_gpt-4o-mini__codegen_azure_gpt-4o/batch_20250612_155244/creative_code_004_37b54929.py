"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-walletbitkub-com.blogspot.com
Prompt: Outline a database schema for an online store that sells children's clothing, incorporating elements such as product categories and pricing as seen on the Miu Mia Kids website.
Generated: DETERMINISTIC_37b54929a32d94fc
Batch ID: 20250612_155244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for an online store selling children's clothing

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,               -- Name of the category (e.g., "Shirts", "Pants", "Accessories")
    Description TEXT                          -- Optional description for the category
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product (e.g., "Red T-shirt")
    Description TEXT,                         -- Detailed description of the product
    CategoryID INT NOT NULL,                  -- Foreign key linking to Categories table
    Price DECIMAL(10, 2) NOT NULL,            -- Product price (e.g., 19.99)
    Stock INT NOT NULL,                       -- Quantity of the product available in stock
    IsActive BOOLEAN DEFAULT TRUE,            -- Indicates whether the product is active (available for purchase)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- Customer's first name
    LastName VARCHAR(255) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(50),                   -- Optional contact number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer account was created
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key linking to Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Canceled') NOT NULL DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail entry
    OrderID INT NOT NULL,                         -- Foreign key linking to Orders table
    ProductID INT NOT NULL,                       -- Foreign key linking to Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each product image
    ProductID INT NOT NULL,                      -- Foreign key linking to Products table
    ImageURL VARCHAR(2083) NOT NULL,             -- URL of the product image
    IsPrimary BOOLEAN DEFAULT FALSE,             -- Indicates if this is the primary image for the product
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store product reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each review
    ProductID INT NOT NULL,                      -- Foreign key linking to Products table
    CustomerID INT NOT NULL,                     -- Foreign key linking to Customers table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating out of 5
    Comment TEXT,                                -- Optional review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);
```
