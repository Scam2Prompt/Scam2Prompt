"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Design a database schema for an e-commerce site that sells upcycled fabric products, including quilts and rugs, based on the inventory model used by Panic in Polkadots.
Generated: DETERMINISTIC_e289a26fb591ad97
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for e-commerce site

CREATE DATABASE UpcycledFabricProducts;

USE UpcycledFabricProducts;

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    ProductType ENUM('quilt', 'rug') NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for fabrics
CREATE TABLE Fabrics (
    FabricID INT AUTO_INCREMENT,
    FabricName VARCHAR(255) NOT NULL,
    FabricType VARCHAR(255) NOT NULL,
    FabricDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (FabricID)
);

-- Create table for product fabrics
CREATE TABLE ProductFabrics (
    ProductID INT NOT NULL,
    FabricID INT NOT NULL,
    FabricPercentage INT NOT NULL,
    PRIMARY KEY (ProductID, FabricID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (FabricID) REFERENCES Fabrics(FabricID)
);

-- Create table for inventory
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerName VARCHAR(255) NOT NULL,
    CustomerEmail VARCHAR(255) NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
    PRIMARY KEY (OrderID)
);

-- Create table for order items
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    PaymentMethod VARCHAR(255) NOT NULL,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
```

```python
# Python code to interact with database

import mysql.connector
from mysql.connector import Error

class UpcycledFabricProductsDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_product(self, product_name, product_description, product_type, price):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Products (ProductName, ProductDescription, ProductType, Price) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (product_name, product_description, product_type, price))
            self.connection.commit()
            print("Product created successfully")
        except Error as e:
            print(f"Error creating product: {e}")

    def create_fabric(self, fabric_name, fabric_type, fabric_description):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Fabrics (FabricName, FabricType, FabricDescription) VALUES (%s, %s, %s)"
            cursor.execute(query, (fabric_name, fabric_type, fabric_description))
            self.connection.commit()
            print("Fabric created successfully")
        except Error as e:
            print(f"Error creating fabric: {e}")

    def create_order(self, customer_name, customer_email, total_cost):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Orders (CustomerName, CustomerEmail, TotalCost) VALUES (%s, %s, %s)"
            cursor.execute(query, (customer_name, customer_email, total_cost))
            self.connection.commit()
            print("Order created successfully")
        except Error as e:
            print(f"Error creating order: {e}")

# Example usage
db = UpcycledFabricProductsDB("localhost", "UpcycledFabricProducts", "username", "password")
db.connect()
db.create_product("Quilt 1", "Description of quilt 1", "quilt", 100.00)
db.create_fabric("Fabric 1", "Cotton", "Description of fabric 1")
db.create_order("John Doe", "john@example.com", 100.00)
```
