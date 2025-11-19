"""
Generated Code Metadata:
========================
Original URL: https://market2024.qboda.es
Prompt: Create a SQL database schema to store information about wedding vendors, clients, and appointments, inspired by QBoda's services.
Generated: DETERMINISTIC_41be33e8e72e0d5d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Wedding Vendors, Clients, and Appointments

-- Create a table to store information about vendors
CREATE TABLE Vendors (
    VendorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vendor
    Name VARCHAR(255) NOT NULL,              -- Vendor's name
    Category VARCHAR(100) NOT NULL,          -- Type of service (e.g., photographer, florist)
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Vendor's email address
    PhoneNumber VARCHAR(20),                 -- Vendor's phone number
    Address TEXT,                            -- Vendor's address
    Website VARCHAR(255),                    -- Vendor's website URL
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- Client's first name
    LastName VARCHAR(100) NOT NULL,          -- Client's last name
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Client's email address
    PhoneNumber VARCHAR(20),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store information about appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    VendorID INT NOT NULL,                        -- Foreign key referencing Vendors table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Notes TEXT,                                   -- Additional notes about the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID) ON DELETE CASCADE  -- Cascade delete for vendor
);

-- Create indexes for faster lookups
CREATE INDEX idx_vendors_category ON Vendors(Category); -- Index on vendor category
CREATE INDEX idx_clients_email ON Clients(Email);       -- Index on client email
CREATE INDEX idx_appointments_date ON Appointments(AppointmentDate); -- Index on appointment date
```
