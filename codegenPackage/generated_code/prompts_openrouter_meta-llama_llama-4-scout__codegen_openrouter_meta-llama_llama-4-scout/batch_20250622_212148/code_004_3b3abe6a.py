"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a SQL database schema to store information about carpet types, repair services, customer testimonials, and contact details, similar to Perfect Melbourne Carpet's database.
Generated: DETERMINISTIC_3b3abe6a4de95858
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for carpet repair services
CREATE DATABASE CarpetRepairServices;

-- Use the database
USE CarpetRepairServices;

-- Create table for carpet types
CREATE TABLE CarpetTypes (
    CarpetTypeID INT AUTO_INCREMENT,
    CarpetTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CarpetTypeID)
);

-- Create table for repair services
CREATE TABLE RepairServices (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for customer testimonials
CREATE TABLE Testimonials (
    TestimonialID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    Testimonial TEXT NOT NULL,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TestimonialID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for contact details
CREATE TABLE ContactDetails (
    ContactDetailID INT AUTO_INCREMENT,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ContactDetailID)
);

-- Create table for carpet repair service orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ServiceID INT NOT NULL,
    CarpetTypeID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ServiceID) REFERENCES RepairServices(ServiceID),
    FOREIGN KEY (CarpetTypeID) REFERENCES CarpetTypes(CarpetTypeID)
);

-- Create indexes for foreign keys
CREATE INDEX idx_orders_customer_id ON Orders(CustomerID);
CREATE INDEX idx_orders_service_id ON Orders(ServiceID);
CREATE INDEX idx_orders_carpet_type_id ON Orders(CarpetTypeID);
CREATE INDEX idx_testimonials_customer_id ON Testimonials(CustomerID);
```

```sql
-- Insert sample data into tables
INSERT INTO CarpetTypes (CarpetTypeName, Description)
VALUES 
('Wool Carpet', 'High-quality wool carpet'),
('Synthetic Carpet', 'Durable synthetic carpet'),
('Natural Fiber Carpet', 'Eco-friendly natural fiber carpet');

INSERT INTO RepairServices (ServiceName, Description, Price)
VALUES 
('Carpet Cleaning', 'Deep cleaning of carpets', 100.00),
('Carpet Repair', 'Repair of damaged carpets', 200.00),
('Carpet Replacement', 'Replacement of old carpets', 500.00);

INSERT INTO Customers (FirstName, LastName, Email, Phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210');

INSERT INTO Testimonials (CustomerID, Testimonial, Rating)
VALUES 
(1, 'Excellent service!', 5),
(2, 'Good job!', 4);

INSERT INTO ContactDetails (Address, City, State, PostalCode, Phone, Email)
VALUES 
('123 Main St', 'Melbourne', 'VIC', '3000', '123-456-7890', 'info@example.com');

INSERT INTO Orders (CustomerID, ServiceID, CarpetTypeID, OrderDate, TotalCost)
VALUES 
(1, 1, 1, '2022-01-01', 100.00),
(2, 2, 2, '2022-01-15', 200.00);
```
