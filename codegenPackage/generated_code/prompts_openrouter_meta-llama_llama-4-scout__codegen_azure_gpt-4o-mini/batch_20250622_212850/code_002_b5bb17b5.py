"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Generate a sample database schema for storing client information, counseling sessions, and therapist details for a counseling service like Dr. Rahileh Sadeghi's.
Generated: DETERMINISTIC_b5bb17b57354c0bd
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for a counseling service

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address
    PhoneNumber VARCHAR(15),                    -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store therapist details
CREATE TABLE Therapists (
    TherapistID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,            -- Therapist's first name
    LastName VARCHAR(50) NOT NULL,             -- Therapist's last name
    Specialty VARCHAR(100),                     -- Therapist's area of specialty
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Therapist's email address
    PhoneNumber VARCHAR(15),                    -- Therapist's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store counseling sessions
CREATE TABLE CounselingSessions (
    SessionID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each session
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    TherapistID INT NOT NULL,                   -- Foreign key referencing Therapists
    SessionDate DATETIME NOT NULL,              -- Date and time of the session
    Notes TEXT,                                 -- Notes taken during the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_therapist_email ON Therapists(Email);
CREATE INDEX idx_session_date ON CounselingSessions(SessionDate);
```
