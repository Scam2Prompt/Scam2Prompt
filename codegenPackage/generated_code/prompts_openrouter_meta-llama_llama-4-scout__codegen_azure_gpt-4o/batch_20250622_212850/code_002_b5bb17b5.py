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
-- Database schema for a counseling service

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    DateOfBirth DATE,                        -- Client's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store therapist information
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,             -- Therapist's first name
    LastName VARCHAR(50) NOT NULL,              -- Therapist's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Therapist's email address
    PhoneNumber VARCHAR(15),                    -- Therapist's phone number
    Specialization VARCHAR(100),                -- Therapist's area of specialization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store counseling session details
CREATE TABLE CounselingSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    TherapistID INT NOT NULL,                 -- Foreign key referencing Therapists table
    SessionDate DATETIME NOT NULL,            -- Date and time of the session
    DurationInMinutes INT NOT NULL,           -- Duration of the session in minutes
    Notes TEXT,                               -- Notes about the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE -- Cascade delete for therapist
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index on client email for faster lookups
CREATE INDEX idx_therapist_email ON Therapists(Email); -- Index on therapist email for faster lookups
CREATE INDEX idx_session_date ON CounselingSessions(SessionDate); -- Index on session date for faster scheduling queries
```
