"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Design a database schema to store information about hair services, products, and client appointments for a beauty salon management system.
Generated: DETERMINISTIC_b090c6143f9b728d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Beauty Salon Management System

-- Create a table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,  -- Client's phone number (unique)
    Email VARCHAR(100) UNIQUE,                 -- Client's email address (optional, unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Create a table to store information about hair services
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    Duration INT NOT NULL                       -- Duration of the service in minutes
);

-- Create a table to store information about products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0         -- Quantity of the product in stock
);

-- Create a table to store client appointments
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the appointment was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store product usage in appointments
CREATE TABLE AppointmentProducts (
    AppointmentProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each record
    AppointmentID INT NOT NULL,                          -- Foreign key referencing Appointments
    ProductID INT NOT NULL,                              -- Foreign key referencing Products
    Quantity INT NOT NULL,                               -- Quantity of the product used in the appointment
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);
```
