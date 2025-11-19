"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Design a simple database schema to store information about customers, furniture, and moving services offered by آل البيت.
Generated: DETERMINISTIC_d37c5d965319423e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for آل البيت moving services
CREATE DATABASE al_bayt_moving_services;

-- Use the created database
USE al_bayt_moving_services;

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create a table to store furniture information
CREATE TABLE Furniture (
    FurnitureID INT AUTO_INCREMENT,
    FurnitureName VARCHAR(255) NOT NULL,
    Description TEXT,
    Dimensions VARCHAR(100),
    Weight DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (FurnitureID)
);

-- Create a table to store moving services offered
CREATE TABLE MovingServices (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create a table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ServiceID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ServiceID) REFERENCES MovingServices(ServiceID)
);

-- Create a table to store order items (furniture moved)
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    FurnitureID INT NOT NULL,
    Quantity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (FurnitureID) REFERENCES Furniture(FurnitureID)
);

-- Create a stored procedure to insert a new customer
DELIMITER //
CREATE PROCEDURE InsertCustomer(
    IN pFirstName VARCHAR(255),
    IN pLastName VARCHAR(255),
    IN pEmail VARCHAR(255),
    IN pPhone VARCHAR(20),
    IN pAddress VARCHAR(255),
    IN pCity VARCHAR(100),
    IN pState VARCHAR(100),
    IN pPostalCode VARCHAR(20),
    IN pCountry VARCHAR(100)
)
BEGIN
    INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, PostalCode, Country)
    VALUES (pFirstName, pLastName, pEmail, pPhone, pAddress, pCity, pState, pPostalCode, pCountry);
END//
DELIMITER ;

-- Create a stored procedure to insert a new order
DELIMITER //
CREATE PROCEDURE InsertOrder(
    IN pCustomerID INT,
    IN pServiceID INT,
    IN pOrderDate DATE,
    IN pTotalCost DECIMAL(10, 2)
)
BEGIN
    INSERT INTO Orders (CustomerID, ServiceID, OrderDate, TotalCost)
    VALUES (pCustomerID, pServiceID, pOrderDate, pTotalCost);
END//
DELIMITER ;

-- Example usage:
CALL InsertCustomer('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345', 'USA');
CALL InsertCustomer('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890', 'USA');

CALL InsertOrder(1, 1, '2022-01-01', 100.00);
CALL InsertOrder(2, 2, '2022-01-15', 200.00);
```
