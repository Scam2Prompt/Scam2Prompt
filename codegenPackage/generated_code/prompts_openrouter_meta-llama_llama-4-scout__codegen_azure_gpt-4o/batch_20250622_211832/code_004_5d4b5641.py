"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a SQL database schema to store client information, meter calibration history, and relevant documentation for a calibration service provider like ИП Семьянинов Сергей Юрьевич on https://poverka-gazvoda.ru.
Generated: DETERMINISTIC_5d4b5641c08f88b2
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for a calibration service provider

-- Create a database
CREATE DATABASE CalibrationService;

-- Use the created database
USE CalibrationService;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FullName VARCHAR(255) NOT NULL,          -- Full name of the client
    PhoneNumber VARCHAR(15) NOT NULL,        -- Contact phone number
    Email VARCHAR(255),                      -- Email address (optional)
    Address TEXT NOT NULL,                   -- Physical address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store meter information
CREATE TABLE Meters (
    MeterID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each meter
    ClientID INT NOT NULL,                   -- Foreign key to associate meter with a client
    MeterType VARCHAR(100) NOT NULL,         -- Type of the meter (e.g., gas, water)
    SerialNumber VARCHAR(100) NOT NULL,      -- Serial number of the meter
    InstallationDate DATE,                   -- Date the meter was installed
    LastCalibrationDate DATE,                -- Date of the last calibration
    NextCalibrationDue DATE,                 -- Date when the next calibration is due
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store calibration history
CREATE TABLE CalibrationHistory (
    CalibrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each calibration record
    MeterID INT NOT NULL,                         -- Foreign key to associate calibration with a meter
    CalibrationDate DATE NOT NULL,                -- Date of calibration
    TechnicianName VARCHAR(255) NOT NULL,         -- Name of the technician who performed the calibration
    CalibrationResult VARCHAR(255) NOT NULL,      -- Result of the calibration (e.g., Passed, Failed)
    Notes TEXT,                                   -- Additional notes about the calibration
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (MeterID) REFERENCES Meters(MeterID) ON DELETE CASCADE -- Cascade delete if meter is removed
);

-- Table to store documentation related to calibration
CREATE TABLE CalibrationDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each document
    MeterID INT NOT NULL,                        -- Foreign key to associate document with a meter
    DocumentName VARCHAR(255) NOT NULL,          -- Name of the document
    DocumentPath VARCHAR(255) NOT NULL,          -- Path to the document file
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the document was uploaded
    FOREIGN KEY (MeterID) REFERENCES Meters(MeterID) ON DELETE CASCADE -- Cascade delete if meter is removed
);

-- Indexes for faster lookups
CREATE INDEX idx_client_phone ON Clients (PhoneNumber);
CREATE INDEX idx_meter_serial ON Meters (SerialNumber);
CREATE INDEX idx_calibration_date ON CalibrationHistory (CalibrationDate);
CREATE INDEX idx_document_path ON CalibrationDocuments (DocumentPath);

-- End of schema creation
```
