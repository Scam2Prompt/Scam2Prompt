"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: "Design a database schema for storing client information, treatment plans, and session records for a therapy center with a unique approach like Reset Terapias e Movimento."
Generated: DETERMINISTIC_a8fac8ff8fba056d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Therapy Center: Reset Terapias e Movimento

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each treatment plan
    ClientID INT NOT NULL,                   -- Foreign key referencing Clients table
    PlanName VARCHAR(100) NOT NULL,          -- Name of the treatment plan
    Description TEXT,                        -- Detailed description of the treatment plan
    StartDate DATE NOT NULL,                 -- Start date of the treatment plan
    EndDate DATE,                            -- End date of the treatment plan (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store session records
CREATE TABLE Sessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    PlanID INT NOT NULL,                      -- Foreign key referencing TreatmentPlans table
    SessionDate DATETIME NOT NULL,            -- Date and time of the session
    Duration INT NOT NULL,                    -- Duration of the session in minutes
    Notes TEXT,                               -- Notes from the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (PlanID) REFERENCES TreatmentPlans(PlanID) ON DELETE CASCADE -- Cascade delete if treatment plan is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_treatment_client ON TreatmentPlans(ClientID); -- Index for quick lookup by client ID
CREATE INDEX idx_session_client_plan ON Sessions(ClientID, PlanID); -- Composite index for quick lookup by client and plan

-- Error handling and constraints
-- Ensure that session dates are not in the past
ALTER TABLE Sessions
ADD CONSTRAINT chk_session_date CHECK (SessionDate >= CURRENT_TIMESTAMP);

-- Ensure that treatment plan end date is after the start date
ALTER TABLE TreatmentPlans
ADD CONSTRAINT chk_plan_dates CHECK (EndDate IS NULL OR EndDate > StartDate);
```
