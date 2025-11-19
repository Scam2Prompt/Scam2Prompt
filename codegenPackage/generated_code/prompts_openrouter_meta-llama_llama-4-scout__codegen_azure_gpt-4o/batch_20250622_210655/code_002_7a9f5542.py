"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Generate a sample database schema for storing information about cleaning services, customers, and appointments for a company like Maria HouseKeepers.
Generated: DETERMINISTIC_7a9f55422b927d6a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Maria HouseKeepers

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about cleaning services
CREATE TABLE CleaningServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the cleaning service
    Description TEXT,                         -- Description of the cleaning service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the cleaning service
    DurationInMinutes INT NOT NULL,           -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                       -- Foreign key referencing CleaningServices table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the appointment record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is deleted
    FOREIGN KEY (ServiceID) REFERENCES CleaningServices(ServiceID) ON DELETE CASCADE -- Cascade delete if service is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers (Email); -- Index for quick lookup by email
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate); -- Index for quick lookup by appointment date
```
