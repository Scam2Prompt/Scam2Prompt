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

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service (e.g., "Pipe Cleaning", "Maintenance")
    Description TEXT,                             -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,                -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store service appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    ServiceTypeID INT NOT NULL,                   -- Foreign key referencing ServiceTypes table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Notes TEXT,                                   -- Additional notes about the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Cascade delete if service type is removed
);

-- Create a table to store maintenance logs
CREATE TABLE MaintenanceLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each maintenance log
    AppointmentID INT NOT NULL,                   -- Foreign key referencing Appointments table
    TechnicianName VARCHAR(100) NOT NULL,         -- Name of the technician who performed the service
    WorkPerformed TEXT NOT NULL,                  -- Detailed description of the work performed
    MaterialsUsed TEXT,                           -- Materials used during the service
    Duration INT NOT NULL,                        -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Cascade delete if appointment is removed
);

-- Create a table to store feedback from customers
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each feedback entry
    AppointmentID INT NOT NULL,                   -- Foreign key referencing Appointments table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Customer rating (1 to 5 stars)
    Comments TEXT,                                -- Customer comments about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Cascade delete if appointment is removed
);

-- Ensure the database is optimized for production use
-- Add indexes for faster queries
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
CREATE INDEX idx_feedback_rating ON Feedback(Rating);
```
