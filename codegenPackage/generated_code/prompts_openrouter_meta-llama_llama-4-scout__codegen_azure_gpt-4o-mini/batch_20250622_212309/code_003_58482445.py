"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Create a simple database schema to store information about pipe cleaning and maintenance services, inspired by the offerings of Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_58482445d27a219d
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about pipe cleaning and maintenance services

-- Create a database for the pipe cleaning services
CREATE DATABASE PipeCleaningServices;

-- Use the created database
USE PipeCleaningServices;

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    Duration INT NOT NULL,                      -- Estimated duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store service appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the appointment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Table to store feedback from customers
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feedback entry
    AppointmentID INT NOT NULL,                  -- Foreign key referencing Appointments
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the customer (1 to 5)
    Comments TEXT,                               -- Additional comments from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the feedback was submitted
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
