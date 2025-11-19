"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconfoundation.online
Prompt: Create a sample database schema for managing therapy sessions and outcomes based on the ICON Foundation's outcome-based mindset in clinical practice.
Generated: DETERMINISTIC_830e9045a059c4c2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing therapy sessions and outcomes
-- Based on the ICON Foundation's outcome-based mindset in clinical practice

-- Create a table for therapists
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,               -- Therapist's first name
    LastName VARCHAR(50) NOT NULL,                -- Therapist's last name
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Therapist's email address
    PhoneNumber VARCHAR(15),                      -- Therapist's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for clients/patients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,               -- Client's first name
    LastName VARCHAR(50) NOT NULL,                -- Client's last name
    DateOfBirth DATE NOT NULL,                    -- Client's date of birth
    Email VARCHAR(100) UNIQUE,                    -- Client's email address
    PhoneNumber VARCHAR(15),                      -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for therapy sessions
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each session
    ClientID INT NOT NULL,                        -- Foreign key linking to the Clients table
    TherapistID INT NOT NULL,                     -- Foreign key linking to the Therapists table
    SessionDate DATETIME NOT NULL,                -- Date and time of the therapy session
    SessionType VARCHAR(100) NOT NULL,            -- Type of therapy session (e.g., CBT, DBT, etc.)
    Notes TEXT,                                   -- Additional notes about the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE
);

-- Create a table for tracking outcomes of therapy sessions
CREATE TABLE SessionOutcomes (
    OutcomeID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each outcome record
    SessionID INT NOT NULL,                       -- Foreign key linking to the TherapySessions table
    OutcomeScore DECIMAL(4,2) NOT NULL,           -- Numeric score representing the outcome
    OutcomeDescription VARCHAR(255),             -- Description of the outcome (e.g., improvement observed)
    FollowUpRequired BOOLEAN DEFAULT FALSE,       -- Indicates if follow-up is necessary
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Record creation timestamp
    FOREIGN KEY (SessionID) REFERENCES TherapySessions(SessionID) ON DELETE CASCADE
);

-- Create a table for outcome categories (optional, for categorizing outcomes)
CREATE TABLE OutcomeCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL UNIQUE,     -- Name of the outcome category
    Description TEXT                              -- Description of the category
);

-- Example linking table for categorizing session outcomes (optional)
CREATE TABLE OutcomeCategoryMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each mapping record
    OutcomeID INT NOT NULL,                       -- Foreign key linking to the SessionOutcomes table
    CategoryID INT NOT NULL,                      -- Foreign key linking to the OutcomeCategories table
    FOREIGN KEY (OutcomeID) REFERENCES SessionOutcomes(OutcomeID) ON DELETE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES OutcomeCategories(CategoryID) ON DELETE CASCADE
);

-- Indexes for faster querying (if necessary)
CREATE INDEX idx_clients_email ON Clients(Email);
CREATE INDEX idx_therapists_email ON Therapists(Email);
CREATE INDEX idx_sessions_date ON TherapySessions(SessionDate);
CREATE INDEX idx_outcomes_score ON SessionOutcomes(OutcomeScore);
```
