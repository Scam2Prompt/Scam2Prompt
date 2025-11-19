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
-- SQL Database Schema for Wedding Vendors, Clients, and Appointments

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Vendors;

-- Table to store information about wedding vendors
CREATE TABLE Vendors (
    VendorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each vendor
    Name VARCHAR(255) NOT NULL,               -- Name of the vendor
    Type VARCHAR(100) NOT NULL,                -- Type of service (e.g., florist, photographer)
    Phone VARCHAR(15),                         -- Contact phone number
    Email VARCHAR(255),                        -- Contact email address
    Website VARCHAR(255),                      -- Vendor's website URL
    Address VARCHAR(255),                      -- Physical address of the vendor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,          -- Client's first name
    LastName VARCHAR(100) NOT NULL,           -- Client's last name
    Email VARCHAR(255) NOT NULL UNIQUE,       -- Client's email address (must be unique)
    Phone VARCHAR(15),                        -- Client's contact phone number
    WeddingDate DATE NOT NULL,                -- Date of the wedding
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store appointments between clients and vendors
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    VendorID INT NOT NULL,                         -- Foreign key referencing Vendors
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_vendor_name ON Vendors(Name);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
