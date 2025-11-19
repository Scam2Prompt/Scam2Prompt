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
-- SQL Database Schema for Calibration Service Provider

-- Create a database for the calibration service provider
CREATE DATABASE CalibrationServiceProvider;

-- Use the newly created database
USE CalibrationServiceProvider;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,              -- Client's name
    ContactNumber VARCHAR(15),                -- Client's contact number
    Email VARCHAR(100),                       -- Client's email address
    Address VARCHAR(255),                     -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store meter calibration history
CREATE TABLE CalibrationHistory (
    CalibrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each calibration record
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    CalibrationDate DATE NOT NULL,                -- Date of calibration
    MeterType VARCHAR(50) NOT NULL,              -- Type of meter calibrated
    CalibrationResult VARCHAR(50) NOT NULL,      -- Result of the calibration
    DocumentationPath VARCHAR(255),               -- Path to relevant documentation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store relevant documentation
CREATE TABLE Documentation (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    CalibrationID INT NOT NULL,                 -- Foreign key referencing CalibrationHistory table
    DocumentType VARCHAR(50) NOT NULL,         -- Type of document (e.g., report, certificate)
    DocumentPath VARCHAR(255) NOT NULL,        -- Path to the document file
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CalibrationID) REFERENCES CalibrationHistory(CalibrationID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_calibration_date ON CalibrationHistory(CalibrationDate);
CREATE INDEX idx_document_type ON Documentation(DocumentType);

-- Sample data insertion (for demonstration purposes)
INSERT INTO Clients (Name, ContactNumber, Email, Address) VALUES
('ИП Семьянинов Сергей Юрьевич', '+7 123 456 7890', 'example@poverka-gazvoda.ru', '123 Calibration St, Calibration City');

-- Note: Ensure to handle errors during data insertion and retrieval in application code.
```
