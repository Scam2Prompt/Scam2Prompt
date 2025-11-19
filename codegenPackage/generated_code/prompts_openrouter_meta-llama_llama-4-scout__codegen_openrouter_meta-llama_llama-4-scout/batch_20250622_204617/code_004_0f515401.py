"""
Generated Code Metadata:
========================
Original URL: https://eferroeacobrza.blogspot.com
Prompt: "Write a SQL query to manage orders and customers for a company that distributes iron and steel products, including services like dobradeira de calhas and guilhotina."
Generated: DETERMINISTIC_0f515401711c6c8a
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for iron and steel products distribution company

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactName VARCHAR(255) NOT NULL,
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    Region VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    Phone VARCHAR(20),
    Fax VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    PRIMARY KEY (CustomerID)
);

-- Create table for orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate DATE NOT NULL,
    RequiredDate DATE,
    ShippedDate DATE,
    ShipVia INT,
    Freight DECIMAL(10, 2),
    ShipName VARCHAR(255),
    ShipAddress VARCHAR(255),
    ShipCity VARCHAR(100),
    ShipRegion VARCHAR(100),
    ShipPostalCode VARCHAR(20),
    ShipCountry VARCHAR(100),
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for products (iron and steel products)
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    SupplierID INT,
    CategoryID INT,
    QuantityPerUnit VARCHAR(100),
    UnitPrice DECIMAL(10, 2) NOT NULL,
    UnitsInStock INT,
    UnitsOnOrder INT,
    ReorderLevel INT,
    Discontinued BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (ProductID)
);

-- Create table for order details
CREATE TABLE OrderDetails (
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL,
    Discount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create table for services (dobradeira de calhas and guilhotina)
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ServiceID)
);

-- Create table for order services
CREATE TABLE OrderServices (
    OrderID INT NOT NULL,
    ServiceID INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (OrderID, ServiceID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Insert sample data into tables
INSERT INTO Customers (CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax, Email)
VALUES 
('Company A', 'John Doe', 'CEO', '123 Main St', 'Anytown', 'CA', '12345', 'USA', '555-555-5555', '555-555-5556', 'john.doe@example.com'),
('Company B', 'Jane Smith', 'Manager', '456 Elm St', 'Othertown', 'NY', '67890', 'USA', '555-555-5557', '555-555-5558', 'jane.smith@example.com');

INSERT INTO Orders (CustomerID, OrderDate, RequiredDate, ShippedDate, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry)
VALUES 
(1, '2022-01-01', '2022-01-15', '2022-01-10', 100.00, 'Company A', '123 Main St', 'Anytown', 'CA', '12345', 'USA'),
(2, '2022-01-05', '2022-01-20', '2022-01-15', 200.00, 'Company B', '456 Elm St', 'Othertown', 'NY', '67890', 'USA');

INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
VALUES 
('Iron Pipe', 1, 1, '10 ft', 50.00, 100, 50, 20, FALSE),
('Steel Beam', 2, 2, '20 ft', 100.00, 50, 20, 10, FALSE);

INSERT INTO OrderDetails (OrderID, ProductID, UnitPrice, Quantity, Discount)
VALUES 
(1, 1, 50.00, 2, 0.00),
(1, 2, 100.00, 1, 0.00),
(2, 1, 50.00, 1, 0.00);

INSERT INTO Services (ServiceName, Description, Price)
VALUES 
('Dobradeira de Calhas', 'Sheet metal folding service', 200.00),
('Guilhotina', 'Shearing service', 100.00);

INSERT INTO OrderServices (OrderID, ServiceID, Quantity)
VALUES 
(1, 1, 1),
(2, 2, 2);

-- Query to retrieve all orders with customer information and order details
SELECT 
    o.OrderID,
    c.CompanyName,
    c.ContactName,
    o.OrderDate,
    od.ProductID,
    p.ProductName,
    od.Quantity,
    s.ServiceID,
    srv.ServiceName
FROM 
    Orders o
INNER JOIN 
    Customers c ON o.CustomerID = c.CustomerID
LEFT JOIN 
    OrderDetails od ON o.OrderID = od.OrderID
LEFT JOIN 
    Products p ON od.ProductID = p.ProductID
LEFT JOIN 
    OrderServices os ON o.OrderID = os.OrderID
LEFT JOIN 
    Services srv ON os.ServiceID = srv.ServiceID
ORDER BY 
    o.OrderID;

-- Query to retrieve total sales by customer
SELECT 
    c.CompanyName,
    SUM(od.UnitPrice * od.Quantity) AS TotalSales
FROM 
    Customers c
INNER JOIN 
    Orders o ON c.CustomerID = o.CustomerID
INNER JOIN 
    OrderDetails od ON o.OrderID = od.OrderID
GROUP BY 
    c.CompanyName
ORDER BY 
    TotalSales DESC;

-- Query to retrieve total revenue by service
SELECT 
    srv.ServiceName,
    SUM(srv.Price * os.Quantity) AS TotalRevenue
FROM 
    Services srv
INNER JOIN 
    OrderServices os ON srv.ServiceID = os.ServiceID
GROUP BY 
    srv.ServiceName
ORDER BY 
    TotalRevenue DESC;
```
