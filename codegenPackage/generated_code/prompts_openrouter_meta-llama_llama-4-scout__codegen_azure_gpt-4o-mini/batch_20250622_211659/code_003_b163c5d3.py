"""
Generated Code Metadata:
========================
Original URL: https://portal-crypto-io.com
Prompt: Create a SQL database schema to store information about Gould Barbers' shops, barbers, and clients.
Generated: DETERMINISTIC_b163c5d39c6ff16b
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Gould Barbers' Shops

-- Create a database for Gould Barbers
CREATE DATABASE GouldBarbers;

-- Use the newly created database
USE GouldBarbers;

-- Table to store information about barbershops
CREATE TABLE Barbershops (
    ShopID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each barbershop
    Name VARCHAR(100) NOT NULL,              -- Name of the barbershop
    Address VARCHAR(255) NOT NULL,           -- Address of the barbershop
    Phone VARCHAR(15),                        -- Contact phone number
    Email VARCHAR(100),                       -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about barbers
CREATE TABLE Barbers (
    BarberID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each barber
    ShopID INT NOT NULL,                       -- Foreign key referencing Barbershops
    Name VARCHAR(100) NOT NULL,                -- Name of the barber
    Specialty VARCHAR(100),                    -- Specialty of the barber (e.g., haircuts, shaves)
    Phone VARCHAR(15),                         -- Contact phone number
    Email VARCHAR(100),                        -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ShopID) REFERENCES Barbershops(ShopID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,                -- Name of the client
    Phone VARCHAR(15),                         -- Contact phone number
    Email VARCHAR(100),                        -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    BarberID INT NOT NULL,                         -- Foreign key referencing Barbers
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (BarberID) REFERENCES Barbers(BarberID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_barber_shop ON Barbers(ShopID);
CREATE INDEX idx_appointment_client ON Appointments(ClientID);
CREATE INDEX idx_appointment_barber ON Appointments(BarberID);
```
