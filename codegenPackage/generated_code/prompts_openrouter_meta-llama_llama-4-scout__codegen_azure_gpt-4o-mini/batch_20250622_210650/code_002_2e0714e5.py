"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Generate a sample database schema for a cleaning services company, including tables for customers, services, and appointments.
Generated: DETERMINISTIC_2e0714e590fac4c3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample Database Schema for a Cleaning Services Company

-- Drop existing tables if they exist (for re-creation purposes)
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address (unique)
    Phone VARCHAR(15),                           -- Customer's phone number
    Address VARCHAR(255),                        -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store available cleaning services
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the cleaning service
    Description TEXT,                             -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the service
    Duration INT NOT NULL,                        -- Estimated duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was added
);

-- Table to store appointments for cleaning services
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the appointment was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St, Springfield'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St, Springfield');

INSERT INTO Services (ServiceName, Description, Price, Duration) VALUES
('Basic Cleaning', 'Standard cleaning service for homes.', 100.00, 120),
('Deep Cleaning', 'Thorough cleaning service for homes.', 200.00, 240);

INSERT INTO Appointments (CustomerID, ServiceID, AppointmentDate, Status) VALUES
(1, 1, '2023-10-15 10:00:00', 'Scheduled'),
(2, 2, '2023-10-16 14:00:00', 'Scheduled');
```
