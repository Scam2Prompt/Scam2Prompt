"""
Generated Code Metadata:
========================
Original URL: https://my-store-f9e36a.creator-spring.com
Prompt: Design a database schema for an e-commerce platform selling various products such as EthXY apparel, accessories, and drinkware, including details like product colors and prices.
Generated: DETERMINISTIC_8137f053397316b1
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling EthXY products

-- Create a table for storing product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for storing products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    CategoryID INT,                              -- Foreign key referencing ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing product colors
CREATE TABLE ProductColors (
    ColorID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each color
    ColorName VARCHAR(50) NOT NULL,              -- Name of the color
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the color was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the color was last updated
);

-- Create a junction table for associating products with their available colors
CREATE TABLE ProductColorAssociations (
    ProductID INT,                               -- Foreign key referencing Products
    ColorID INT,                                 -- Foreign key referencing ProductColors
    PRIMARY KEY (ProductID, ColorID),           -- Composite primary key to ensure uniqueness
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ColorID) REFERENCES ProductColors(ColorID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    UserID INT NOT NULL,                         -- Identifier for the user placing the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status VARCHAR(50) NOT NULL,                 -- Status of the order (e.g., Pending, Shipped, Completed)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the order was last updated
);

-- Create a table for storing order items
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT,                                 -- Foreign key referencing Orders
    ProductID INT,                               -- Foreign key referencing Products
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```
