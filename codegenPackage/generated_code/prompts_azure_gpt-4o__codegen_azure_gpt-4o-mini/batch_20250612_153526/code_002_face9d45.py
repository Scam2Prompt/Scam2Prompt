"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Generate code for a database schema to manage business and investment clubs, including entrepreneurship training sessions and funding opportunities, as described in the "Inua Pato" sustainable livelihood program.
Generated: DETERMINISTIC_face9d45b73ffb9f
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing business and investment clubs
-- including entrepreneurship training sessions and funding opportunities
-- as part of the "Inua Pato" sustainable livelihood program.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS FundingOpportunities;
DROP TABLE IF EXISTS TrainingSessions;
DROP TABLE IF EXISTS Clubs;
DROP TABLE IF EXISTS Members;

-- Table to store information about business and investment clubs
CREATE TABLE Clubs (
    ClubID SERIAL PRIMARY KEY, -- Unique identifier for each club
    ClubName VARCHAR(100) NOT NULL, -- Name of the club
    Description TEXT, -- Description of the club's purpose and activities
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of club creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about members of the clubs
CREATE TABLE Members (
    MemberID SERIAL PRIMARY KEY, -- Unique identifier for each member
    ClubID INT NOT NULL, -- Foreign key referencing the club
    MemberName VARCHAR(100) NOT NULL, -- Name of the member
    Email VARCHAR(100) UNIQUE NOT NULL, -- Unique email for each member
    JoinedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the member joined
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about entrepreneurship training sessions
CREATE TABLE TrainingSessions (
    SessionID SERIAL PRIMARY KEY, -- Unique identifier for each training session
    ClubID INT NOT NULL, -- Foreign key referencing the club
    SessionTitle VARCHAR(100) NOT NULL, -- Title of the training session
    SessionDate DATE NOT NULL, -- Date of the training session
    Duration INT NOT NULL, -- Duration of the session in hours
    Description TEXT, -- Description of the training session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of session creation
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about funding opportunities
CREATE TABLE FundingOpportunities (
    FundingID SERIAL PRIMARY KEY, -- Unique identifier for each funding opportunity
    ClubID INT NOT NULL, -- Foreign key referencing the club
    FundingSource VARCHAR(100) NOT NULL, -- Source of the funding
    Amount DECIMAL(10, 2) NOT NULL, -- Amount of funding available
    ApplicationDeadline DATE NOT NULL, -- Deadline for application
    Description TEXT, -- Description of the funding opportunity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of funding opportunity creation
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_club_name ON Clubs(ClubName);
CREATE INDEX idx_member_email ON Members(Email);
CREATE INDEX idx_session_date ON TrainingSessions(SessionDate);
CREATE INDEX idx_funding_source ON FundingOpportunities(FundingSource);
```
