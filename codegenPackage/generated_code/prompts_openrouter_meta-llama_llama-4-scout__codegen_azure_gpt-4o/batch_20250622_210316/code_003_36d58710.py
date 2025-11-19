"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: "Design a database schema for an e-commerce platform focused on sports equipment, inspired by the product offerings on activesport.cz."
Generated: DETERMINISTIC_36d58710c20ca270
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform focused on sports equipment

-- Table: Users
-- Stores information about users of the platform
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for security
    PhoneNumber VARCHAR(15),              -- Optional phone number
    Address TEXT,                         -- Optional address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Categories
-- Stores product categories (e.g., "Running", "Cycling", "Swimming")
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL UNIQUE,         -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of category creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Products
-- Stores information about sports equipment products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CategoryID INT NOT NULL,                  -- Foreign key to Categories table
    ImageURL VARCHAR(255),                    -- URL to the product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Cascade delete if category is removed
);

-- Table: Orders
-- Stores information about customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    UserID INT NOT NULL,                    -- Foreign key to Users table
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount of the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Order status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table: OrderItems
-- Stores details of products in each order
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key to Orders table
    ProductID INT NOT NULL,                     -- Foreign key to Products table
    Quantity INT NOT NULL,                      -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Table: Reviews
-- Stores customer reviews for products
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    ProductID INT NOT NULL,                  -- Foreign key to Products table
    UserID INT NOT NULL,                     -- Foreign key to Users table
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                            -- Optional review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of review creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete if product is removed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table: Cart
-- Stores items in a user's shopping cart
CREATE TABLE Cart (
    CartID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cart item
    UserID INT NOT NULL,                   -- Foreign key to Users table
    ProductID INT NOT NULL,                -- Foreign key to Products table
    Quantity INT NOT NULL,                 -- Quantity of the product in the cart
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Table: PaymentMethods
-- Stores payment methods for users
CREATE TABLE PaymentMethods (
    PaymentMethodID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment method
    UserID INT NOT NULL,                            -- Foreign key to Users table
    CardNumber VARCHAR(16) NOT NULL,               -- Card number (encrypted in production)
    ExpiryDate DATE NOT NULL,                      -- Expiry date of the card
    CardHolderName VARCHAR(100) NOT NULL,          -- Name of the cardholder
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of payment method creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table: Wishlists
-- Stores products added to a user's wishlist
CREATE TABLE Wishlists (
    WishlistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each wishlist item
    UserID INT NOT NULL,                       -- Foreign key to Users table
    ProductID INT NOT NULL,                    -- Foreign key to Products table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of wishlist item creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);
```
