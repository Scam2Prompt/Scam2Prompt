"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Develop a SQL database schema to store information about customers, services offered by a company like شركة الاحترافية, and appointments scheduled, considering factors like service pricing and customer satisfaction.
Generated: DETERMINISTIC_802e79478cc910d5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for شركة الاحترافية

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS CustomerSatisfaction;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Customer's email address (unique)
    Phone VARCHAR(15),                        -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store services offered by the company
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    Description TEXT,                          -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was added
);

-- Table to store appointments scheduled by customers
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the appointment was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store customer satisfaction ratings for services
CREATE TABLE CustomerSatisfaction (
    SatisfactionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each satisfaction record
    AppointmentID INT NOT NULL,                    -- Foreign key referencing Appointments
    Rating INT CHECK (Rating BETWEEN 1 AND 5),     -- Rating from 1 to 5
    Feedback TEXT,                                 -- Optional feedback from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the feedback was recorded
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
