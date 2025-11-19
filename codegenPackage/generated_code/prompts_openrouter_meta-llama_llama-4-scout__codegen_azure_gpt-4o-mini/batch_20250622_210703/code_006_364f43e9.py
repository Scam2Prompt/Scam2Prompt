"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Create a SQL query to manage and retrieve data about housekeeping services, including client information, service types, and employee assignments, for a facility management company.
Generated: DETERMINISTIC_364f43e92b5bb8a4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the facility management company
CREATE DATABASE FacilityManagement;

-- Use the created database
USE FacilityManagement;

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,
    ClientName VARCHAR(100) NOT NULL,
    ContactNumber VARCHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(255)
);

-- Create a table for service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT PRIMARY KEY AUTO_INCREMENT,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL
);

-- Create a table for employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    EmployeeName VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100),
    HireDate DATE NOT NULL
);

-- Create a table for housekeeping services
CREATE TABLE HousekeepingServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,
    ClientID INT,
    ServiceTypeID INT,
    EmployeeID INT,
    ServiceDate DATE NOT NULL,
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE SET NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE SET NULL
);

-- Insert sample data into Clients table
INSERT INTO Clients (ClientName, ContactNumber, Email, Address) VALUES
('John Doe', '123-456-7890', 'john.doe@example.com', '123 Elm St, Springfield'),
('Jane Smith', '987-654-3210', 'jane.smith@example.com', '456 Oak St, Springfield');

-- Insert sample data into ServiceTypes table
INSERT INTO ServiceTypes (ServiceName, Description, Price) VALUES
('Basic Cleaning', 'Standard cleaning service for homes.', 100.00),
('Deep Cleaning', 'Thorough cleaning service for homes.', 200.00);

-- Insert sample data into Employees table
INSERT INTO Employees (EmployeeName, PhoneNumber, Email, HireDate) VALUES
('Alice Johnson', '555-123-4567', 'alice.johnson@example.com', '2022-01-15'),
('Bob Brown', '555-765-4321', 'bob.brown@example.com', '2022-02-20');

-- Query to retrieve all housekeeping services with client, service type, and employee information
SELECT 
    hs.ServiceID,
    c.ClientName,
    st.ServiceName,
    e.EmployeeName,
    hs.ServiceDate,
    hs.Status
FROM 
    HousekeepingServices hs
JOIN 
    Clients c ON hs.ClientID = c.ClientID
JOIN 
    ServiceTypes st ON hs.ServiceTypeID = st.ServiceTypeID
JOIN 
    Employees e ON hs.EmployeeID = e.EmployeeID
ORDER BY 
    hs.ServiceDate DESC;

-- Error handling is managed by the database engine; ensure to check for foreign key constraints and data integrity.
```
