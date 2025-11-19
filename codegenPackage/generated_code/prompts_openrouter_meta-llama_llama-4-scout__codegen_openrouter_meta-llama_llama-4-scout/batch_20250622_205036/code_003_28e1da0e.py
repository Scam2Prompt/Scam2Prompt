"""
Generated Code Metadata:
========================
Original URL: https://theoportal.com
Prompt: "Design a database schema for an e-commerce platform specializing in pre-owned luxury fashion items, including tables for products, brands, and customer reviews."
Generated: DETERMINISTIC_28e1da0e8c841d13
Batch ID: 20250622_205036
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create a database for the e-commerce platform
CREATE DATABASE LuxuryFashion;

-- Use the database
USE LuxuryFashion;

-- Create a table for brands
CREATE TABLE Brands (
    BrandID INT AUTO_INCREMENT,
    BrandName VARCHAR(255) NOT NULL,
    BrandDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BrandID)
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    BrandID INT NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    Condition VARCHAR(50) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE
);

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create a table for product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    CustomerID INT NOT NULL,
    Rating TINYINT NOT NULL,
    Review TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    CHECK (Rating BETWEEN 1 AND 5)
);

-- Create a table for product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    ImageURL VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ImageID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Create a table for order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Insert some sample data
INSERT INTO Brands (BrandName, BrandDescription)
VALUES 
('Gucci', 'Italian luxury fashion brand'),
('Chanel', 'French luxury fashion brand'),
('Louis Vuitton', 'French luxury fashion brand');

INSERT INTO Products (BrandID, ProductName, ProductDescription, Price, Condition, Category)
VALUES 
(1, 'Gucci Handbag', 'Luxury handbag from Gucci', 1000.00, 'Excellent', 'Handbags'),
(2, 'Chanel Suit', 'Luxury suit from Chanel', 5000.00, 'Good', 'Apparel'),
(3, 'Louis Vuitton Shoes', 'Luxury shoes from Louis Vuitton', 800.00, 'Fair', 'Footwear');

INSERT INTO Customers (FirstName, LastName, Email, PasswordHash)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'password_hash'),
('Jane', 'Doe', 'jane.doe@example.com', 'password_hash');

INSERT INTO ProductReviews (ProductID, CustomerID, Rating, Review)
VALUES 
(1, 1, 5, 'Excellent product!'),
(2, 2, 4, 'Good product, but not perfect');

INSERT INTO ProductImages (ProductID, ImageURL)
VALUES 
(1, 'https://example.com/image1.jpg'),
(2, 'https://example.com/image2.jpg');

INSERT INTO Orders (CustomerID, TotalCost, Status)
VALUES 
(1, 1000.00, 'Shipped'),
(2, 5000.00, 'Pending');

INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice)
VALUES 
(1, 1, 1, 1000.00),
(2, 2, 1, 5000.00);
```
