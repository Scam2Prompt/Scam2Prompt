"""
Generated Code Metadata:
========================
Original URL: https://www.adour-pompes-funebres.fr
Prompt: "Design a simple database schema to store information about funeral services, including client details, service types (e.g., transport, ceremony), and payment methods."
Generated: DETERMINISTIC_79e834198f23b179
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for funeral services
CREATE DATABASE FuneralServices;

-- Use the FuneralServices database
USE FuneralServices;

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    PRIMARY KEY (ClientID)
);

-- Create a table for service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT,
    ServiceTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ServiceTypeID)
);

-- Create a table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceTypeID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    ServiceTime TIME NOT NULL,
    Location VARCHAR(255) NOT NULL,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID)
);

-- Create a table for payment methods
CREATE TABLE PaymentMethods (
    PaymentMethodID INT AUTO_INCREMENT,
    PaymentMethodName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (PaymentMethodID)
);

-- Create a table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    ServiceID INT NOT NULL,
    PaymentMethodID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
    FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethods(PaymentMethodID)
);

-- Insert sample data into ServiceTypes table
INSERT INTO ServiceTypes (ServiceTypeName, Description)
VALUES 
('Transport', 'Funeral transport services'),
('Ceremony', 'Funeral ceremony services'),
('Cremation', 'Cremation services'),
('Burial', 'Burial services');

-- Insert sample data into PaymentMethods table
INSERT INTO PaymentMethods (PaymentMethodName, Description)
VALUES 
('Cash', 'Cash payment'),
('Credit Card', 'Credit card payment'),
('Bank Transfer', 'Bank transfer payment');

-- Create a stored procedure to add a new client
DELIMITER //
CREATE PROCEDURE AddClient(
    IN pFirstName VARCHAR(255),
    IN pLastName VARCHAR(255),
    IN pEmail VARCHAR(255),
    IN pPhone VARCHAR(20),
    IN pAddress VARCHAR(255)
)
BEGIN
    INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
    VALUES (pFirstName, pLastName, pEmail, pPhone, pAddress);
END//
DELIMITER ;

-- Create a stored procedure to add a new service
DELIMITER //
CREATE PROCEDURE AddService(
    IN pClientID INT,
    IN pServiceTypeID INT,
    IN pServiceDate DATE,
    IN pServiceTime TIME,
    IN pLocation VARCHAR(255)
)
BEGIN
    INSERT INTO Services (ClientID, ServiceTypeID, ServiceDate, ServiceTime, Location)
    VALUES (pClientID, pServiceTypeID, pServiceDate, pServiceTime, pLocation);
END//
DELIMITER ;

-- Create a stored procedure to add a new payment
DELIMITER //
CREATE PROCEDURE AddPayment(
    IN pServiceID INT,
    IN pPaymentMethodID INT,
    IN pPaymentDate DATE,
    IN pAmount DECIMAL(10, 2)
)
BEGIN
    INSERT INTO Payments (ServiceID, PaymentMethodID, PaymentDate, Amount)
    VALUES (pServiceID, pPaymentMethodID, pPaymentDate, pAmount);
END//
DELIMITER ;
```
