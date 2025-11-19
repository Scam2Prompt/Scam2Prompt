"""
Generated Code Metadata:
========================
Original URL: https://cbienetre.com
Prompt: "Create a SQL database schema to store information about massage therapy clients, including their medical history and treatment plans."
Generated: DETERMINISTIC_a51bbe8af5745195
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL schema to store information about massage therapy clients, their medical history, and treatment plans.

-- Create a database named 'MassageTherapy'
CREATE DATABASE MassageTherapy;

-- Use the newly created database
USE MassageTherapy;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Email VARCHAR(100),                      -- Client's email address
    Address TEXT,                            -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store medical history of clients
CREATE TABLE MedicalHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each medical history record
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    Condition VARCHAR(255) NOT NULL,          -- Medical condition or issue
    Notes TEXT,                               -- Additional notes about the condition
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store treatment plans for clients
CREATE TABLE TreatmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each treatment plan
    ClientID INT NOT NULL,                   -- Foreign key referencing Clients table
    TreatmentDescription TEXT NOT NULL,      -- Description of the treatment plan
    StartDate DATE NOT NULL,                 -- Start date of the treatment plan
    EndDate DATE,                            -- End date of the treatment plan (optional)
    Notes TEXT,                              -- Additional notes about the treatment plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store session details for treatments
CREATE TABLE TreatmentSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    PlanID INT NOT NULL,                      -- Foreign key referencing TreatmentPlans table
    SessionDate DATETIME NOT NULL,            -- Date and time of the session
    DurationMinutes INT NOT NULL,             -- Duration of the session in minutes
    Notes TEXT,                               -- Additional notes about the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PlanID) REFERENCES TreatmentPlans(PlanID) ON DELETE CASCADE -- Cascade delete if treatment plan is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_name ON Clients (FirstName, LastName); -- Index for client name search
CREATE INDEX idx_medical_history_client ON MedicalHistory (ClientID); -- Index for medical history lookup
CREATE INDEX idx_treatment_plan_client ON TreatmentPlans (ClientID); -- Index for treatment plan lookup
CREATE INDEX idx_session_plan ON TreatmentSessions (PlanID); -- Index for session lookup
```
