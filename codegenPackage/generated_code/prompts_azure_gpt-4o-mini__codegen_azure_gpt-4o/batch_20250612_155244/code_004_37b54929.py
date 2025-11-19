"""
Generated Code Metadata:
========================
Original URL: https://www-walletbitkub-com.blogspot.com
Prompt: Outline a database schema for an online store that sells children's clothing, incorporating elements such as product categories and pricing as seen on the Miu Mia Kids website.
Generated: DETERMINISTIC_37b54929a32d94fc
Batch ID: 20250612_155244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store selling children's clothing

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Tops", "Bottoms", "Accessories")
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategories
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity of the product available in stock
    Description TEXT,                          -- Optional description of the product
    ImageURL VARCHAR(2083),                    -- URL to the product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures category deletion cascades to products
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- Customer's first name
    LastName VARCHAR(255) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Optional phone number
    Address TEXT,                              -- Optional address for shipping
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key linking to Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures customer deletion cascades to orders
);

-- Table to store order details (products in each order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key linking to Orders
    ProductID INT NOT NULL,                       -- Foreign key linking to Products
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures order deletion cascades to order details
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures product deletion cascades to order details
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each review
    ProductID INT NOT NULL,                     -- Foreign key linking to Products
    CustomerID INT NOT NULL,                    -- Foreign key linking to Customers
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                            -- Optional review text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures product deletion cascades to reviews
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures customer deletion cascades to reviews
);

-- Table to store promotional discounts
CREATE TABLE Discounts (
    DiscountID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each discount
    DiscountCode VARCHAR(50) NOT NULL UNIQUE,   -- Unique discount code
    Description TEXT,                           -- Optional description of the discount
    DiscountPercentage DECIMAL(5, 2) NOT NULL, -- Percentage discount (e.g., 10.00 for 10%)
    StartDate DATE NOT NULL,                    -- Start date of the discount
    EndDate DATE NOT NULL,                      -- End date of the discount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the discount was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the discount was last updated
);
```
