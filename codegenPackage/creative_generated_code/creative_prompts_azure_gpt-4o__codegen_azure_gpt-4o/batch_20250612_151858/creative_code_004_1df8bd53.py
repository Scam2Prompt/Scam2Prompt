"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Create a SQL database schema for an e-commerce site that categorizes products into "Men," "Women," "Kids," and "Home & Living," with subcategories like "Shoes," "Accessories," and "Perfumes," as structured on brandsoutlet.qa.
Generated: DETERMINISTIC_1df8bd53c34d3f81
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create database schema for the e-commerce site

-- Create a table for storing main categories (e.g., Men, Women, Kids, Home & Living)
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for storing subcategories (e.g., Shoes, Accessories, Perfumes)
CREATE TABLE Subcategories (
    SubcategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subcategory
    Name VARCHAR(255) NOT NULL,                   -- Name of the subcategory
    CategoryID INT NOT NULL,                      -- Foreign key to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensure relational integrity
);

-- Create a table for storing products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Number of items in stock
    SubcategoryID INT NOT NULL,               -- Foreign key to Subcategories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (SubcategoryID) REFERENCES Subcategories(SubcategoryID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensure relational integrity
);

-- Create a table for storing product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each image
    ProductID INT NOT NULL,                 -- Foreign key to Products table
    ImageURL VARCHAR(2083) NOT NULL,        -- URL of the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensure relational integrity
);

-- Create a table for storing orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerID INT NOT NULL,                -- Foreign key to Customers table (assuming a Customers table exists)
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount for the order
    Status VARCHAR(255) DEFAULT 'Pending', -- Current status of the order (e.g., Pending, Completed, Cancelled)
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for storing order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key to Orders table
    ProductID INT NOT NULL,                       -- Foreign key to Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE ON UPDATE CASCADE, -- Ensure relational integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE ON UPDATE CASCADE -- Ensure relational integrity
);
```
