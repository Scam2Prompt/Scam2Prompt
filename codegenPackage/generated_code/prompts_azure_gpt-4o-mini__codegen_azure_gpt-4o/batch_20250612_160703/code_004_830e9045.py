"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: Create a sample database schema for managing therapy sessions and outcomes based on the ICON Foundation's outcome-based mindset in clinical practice.
Generated: DETERMINISTIC_830e9045a059c4c2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing therapy sessions and outcomes
-- This schema is designed to support outcome-based clinical practices.

-- Table to store information about therapists
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,             -- Therapist's first name
    LastName VARCHAR(50) NOT NULL,              -- Therapist's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Therapist's email address
    PhoneNumber VARCHAR(15),                    -- Therapist's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,             -- Client's first name
    LastName VARCHAR(50) NOT NULL,              -- Client's last name
    DateOfBirth DATE,                           -- Client's date of birth
    Email VARCHAR(100) UNIQUE,                  -- Client's email address
    PhoneNumber VARCHAR(15),                    -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store therapy sessions
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each session
    TherapistID INT NOT NULL,                   -- Foreign key referencing Therapists table
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    SessionDate DATETIME NOT NULL,              -- Date and time of the therapy session
    DurationMinutes INT NOT NULL,               -- Duration of the session in minutes
    Notes TEXT,                                 -- Notes about the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store therapy outcomes
CREATE TABLE TherapyOutcomes (
    OutcomeID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each outcome
    SessionID INT NOT NULL,                     -- Foreign key referencing TherapySessions table
    OutcomeDescription TEXT NOT NULL,           -- Description of the therapy outcome
    OutcomeScore INT CHECK (OutcomeScore BETWEEN 1 AND 10), -- Outcome score (1-10 scale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (SessionID) REFERENCES TherapySessions(SessionID) ON DELETE CASCADE
);

-- Table to store predefined outcome metrics (e.g., for standardization)
CREATE TABLE OutcomeMetrics (
    MetricID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each metric
    MetricName VARCHAR(100) NOT NULL,           -- Name of the metric
    Description TEXT,                           -- Description of the metric
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to associate outcome metrics with therapy outcomes
CREATE TABLE OutcomeMetricAssociations (
    AssociationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    OutcomeID INT NOT NULL,                        -- Foreign key referencing TherapyOutcomes table
    MetricID INT NOT NULL,                         -- Foreign key referencing OutcomeMetrics table
    MetricValue VARCHAR(50),                       -- Value of the metric for the outcome
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (OutcomeID) REFERENCES TherapyOutcomes(OutcomeID) ON DELETE CASCADE,
    FOREIGN KEY (MetricID) REFERENCES OutcomeMetrics(MetricID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_therapist_email ON Therapists(Email);
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_session_date ON TherapySessions(SessionDate);
CREATE INDEX idx_outcome_score ON TherapyOutcomes(OutcomeScore);
```
