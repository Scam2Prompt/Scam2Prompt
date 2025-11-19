"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Design a basic database schema to store information about clients, cases, and appointments for a law firm like Majeli Avocat, and suggest a suitable programming language for implementation.
Generated: DETERMINISTIC_458e3c885158b79d
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Law Firm

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store case information
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each case
    ClientID INT NOT NULL,                   -- Foreign key referencing Clients table
    CaseTitle VARCHAR(100) NOT NULL,         -- Title or name of the case
    CaseDescription TEXT,                    -- Detailed description of the case
    Status ENUM('Open', 'Closed', 'Pending') DEFAULT 'Open', -- Status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    CaseID INT NOT NULL,                          -- Foreign key referencing Cases table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Location VARCHAR(100),                        -- Location of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE
);

-- Suggested Programming Language: Python
-- Python is suitable for implementing this schema due to its robust libraries for database interaction (e.g., SQLAlchemy, psycopg2).
```
