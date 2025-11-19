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
-- Database schema for a car repair service system

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT                               -- Customer's address
);

-- Table to store services offered by the repair shop
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service (e.g., Engine Repair)
    Description TEXT,                          -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL              -- Price of the service
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table to store repair shop staff details (optional, if needed)
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,              -- Staff member's first name
    LastName VARCHAR(50) NOT NULL,               -- Staff member's last name
    Role VARCHAR(50) NOT NULL,                   -- Role of the staff member (e.g., Mechanic, Manager)
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Staff member's email address
    PhoneNumber VARCHAR(15)                      -- Staff member's phone number
);

-- Table to assign staff to appointments (optional, if needed)
CREATE TABLE AppointmentStaff (
    AppointmentStaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    AppointmentID INT NOT NULL,                        -- Foreign key referencing Appointments table
    StaffID INT NOT NULL,                              -- Foreign key referencing Staff table
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for quick lookup of services by name
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index for quick lookup of appointments by date
```
