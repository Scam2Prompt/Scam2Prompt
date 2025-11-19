"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Design a database schema to store information about car repair services, including services offered (e.g., engine repair, transmission repair), customer details, and appointment schedules.
Generated: DETERMINISTIC_ccad561e447a8666
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for car repair services

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    PhoneNumber VARCHAR(15) NOT NULL,           -- Customer's phone number
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service (e.g., engine repair)
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL                -- Price of the service
);

-- Table to store appointment schedules
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

-- Indexes for faster querying
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
