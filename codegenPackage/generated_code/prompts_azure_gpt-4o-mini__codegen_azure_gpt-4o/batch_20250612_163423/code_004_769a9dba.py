"""
Generated Code Metadata:
========================
Original URL: https://johnbarrybaker.com
Prompt: Design a database schema for storing client information and accident details for a personal injury law firm, ensuring it includes fields for various accident types and client contact methods.
Generated: DETERMINISTIC_769a9dba55fc72dc
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client information and accident details
-- Designed for a personal injury law firm

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100),                      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's physical address
    PreferredContactMethod ENUM('Email', 'Phone', 'Mail') NOT NULL, -- Preferred contact method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store accident details
CREATE TABLE Accidents (
    AccidentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accident
    ClientID INT NOT NULL,                     -- Foreign key linking to the Clients table
    AccidentType ENUM('Car', 'SlipAndFall', 'Workplace', 'MedicalMalpractice', 'Other') NOT NULL, -- Type of accident
    AccidentDate DATE NOT NULL,                -- Date of the accident
    Description TEXT,                          -- Detailed description of the accident
    Location TEXT,                             -- Location where the accident occurred
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_accident_type ON Accidents(AccidentType); -- Index for filtering by accident type
```
