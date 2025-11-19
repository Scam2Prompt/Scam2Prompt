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
-- Database schema for storing client information and accident details for a personal injury law firm

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (must be unique)
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store accident details
CREATE TABLE Accidents (
    AccidentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each accident
    ClientID INT NOT NULL,                       -- Foreign key referencing the Clients table
    AccidentType ENUM('Car', 'Motorcycle', 'Bicycle', 'Slip and Fall', 'Workplace', 'Other') NOT NULL,  -- Type of accident
    AccidentDate DATE NOT NULL,                  -- Date of the accident
    Description TEXT,                            -- Detailed description of the accident
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the accident was recorded
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store client contact methods
CREATE TABLE ContactMethods (
    ContactMethodID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each contact method
    ClientID INT NOT NULL,                            -- Foreign key referencing the Clients table
    Method ENUM('Email', 'Phone', 'Mail', 'In-Person') NOT NULL,  -- Type of contact method
    Preferred BOOLEAN DEFAULT FALSE,                  -- Indicates if this is the preferred contact method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the contact method was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_accident_client ON Accidents(ClientID);
CREATE INDEX idx_contact_client ON ContactMethods(ClientID);
```
