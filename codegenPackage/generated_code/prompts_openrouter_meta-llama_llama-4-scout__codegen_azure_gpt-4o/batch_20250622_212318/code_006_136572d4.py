"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Generate a sample database schema for storing customer information, appointments, and services offered by a plumbing company like ERA ElbeRohr & Abwassertechnik GmbH & Co. KG.
Generated: DETERMINISTIC_136572d4dda1ec3f
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a plumbing company to store customer information, appointments, and services

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address VARCHAR(255),                      -- Customer's address
    City VARCHAR(50),                          -- City of residence
    PostalCode VARCHAR(10),                    -- Postal code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store services offered by the company
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    DurationInMinutes INT NOT NULL,           -- Estimated duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete for customer
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE     -- Cascade delete for service
);

-- Create indexes for faster lookups
CREATE INDEX idx_customer_email ON Customers(Email); -- Index on email for quick customer lookup
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index on appointment date for scheduling
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index on service name for quick service lookup
```
