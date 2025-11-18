"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Create a database schema for storing information about plumbing service calls, including fields for service type (e.g., asbestos removal, pipe rehabilitation), customer details, and technician assignments, inspired by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_c6fee5a1d532c625
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Plumbing Service Calls Management

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's phone number
    Address TEXT NOT NULL,                     -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer record was created
);

-- Table to store technician details
CREATE TABLE Technicians (
    TechnicianID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each technician
    FirstName VARCHAR(50) NOT NULL,              -- Technician's first name
    LastName VARCHAR(50) NOT NULL,               -- Technician's last name
    Email VARCHAR(100) UNIQUE,                   -- Technician's email address
    PhoneNumber VARCHAR(15),                     -- Technician's phone number
    Specialty VARCHAR(100),                      -- Technician's specialty area
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the technician record was created
);

-- Table to store service types offered
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service type (e.g., asbestos removal)
    Description TEXT,                             -- Description of the service type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service type record was created
);

-- Table to store plumbing service call details
CREATE TABLE ServiceCalls (
    ServiceCallID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service call
    CustomerID INT NOT NULL,                      -- Foreign key referring to the Customers table
    TechnicianID INT,                             -- Foreign key referring to the Technicians table
    ServiceTypeID INT NOT NULL,                   -- Foreign key referring to the ServiceTypes table
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the service call
    Notes TEXT,                                   -- Additional notes about the service call
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service call record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if Customer is deleted
    FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID) ON DELETE SET NULL, -- Set NULL if Technician is deleted
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE RESTRICT -- Restrict delete if ServiceType is referenced
);

-- Indexes for optimizing queries
CREATE INDEX IDX_Customers_Email ON Customers (Email); -- Index on Customer email for fast lookup
CREATE INDEX IDX_Technicians_Email ON Technicians (Email); -- Index on Technician email for fast lookup
CREATE INDEX IDX_ServiceCalls_DateTime ON ServiceCalls (AppointmentDate, AppointmentTime); -- Composite index for appointment date and time
```
