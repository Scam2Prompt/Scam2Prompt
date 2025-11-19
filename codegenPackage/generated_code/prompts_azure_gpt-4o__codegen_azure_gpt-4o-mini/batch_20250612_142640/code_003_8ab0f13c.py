"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Create a database schema for managing award nominations and winners based on the structure described in MN SWAP's award nomination information.
Generated: DETERMINISTIC_8ab0f13c8c464f78
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing award nominations and winners

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS AwardNominations;
DROP TABLE IF EXISTS Awards;
DROP TABLE IF EXISTS Nominees;
DROP TABLE IF EXISTS Winners;

-- Table to store information about awards
CREATE TABLE Awards (
    AwardID SERIAL PRIMARY KEY, -- Unique identifier for each award
    AwardName VARCHAR(255) NOT NULL, -- Name of the award
    Description TEXT, -- Description of the award
    Year INT NOT NULL CHECK (Year > 0) -- Year the award is given
);

-- Table to store information about nominees
CREATE TABLE Nominees (
    NomineeID SERIAL PRIMARY KEY, -- Unique identifier for each nominee
    NomineeName VARCHAR(255) NOT NULL, -- Name of the nominee
    NomineeEmail VARCHAR(255) UNIQUE NOT NULL, -- Email of the nominee
    NomineeBio TEXT -- Short biography of the nominee
);

-- Table to store nominations for awards
CREATE TABLE AwardNominations (
    NominationID SERIAL PRIMARY KEY, -- Unique identifier for each nomination
    AwardID INT NOT NULL, -- Foreign key referencing the Awards table
    NomineeID INT NOT NULL, -- Foreign key referencing the Nominees table
    NominationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of nomination
    Status VARCHAR(50) DEFAULT 'Pending', -- Status of the nomination (e.g., Pending, Approved, Rejected)
    FOREIGN KEY (AwardID) REFERENCES Awards(AwardID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (NomineeID) REFERENCES Nominees(NomineeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store winners of awards
CREATE TABLE Winners (
    WinnerID SERIAL PRIMARY KEY, -- Unique identifier for each winner
    AwardID INT NOT NULL, -- Foreign key referencing the Awards table
    NomineeID INT NOT NULL, -- Foreign key referencing the Nominees table
    WinningDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the winner is announced
    FOREIGN KEY (AwardID) REFERENCES Awards(AwardID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (NomineeID) REFERENCES Nominees(NomineeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_award_name ON Awards(AwardName);
CREATE INDEX idx_nominee_name ON Nominees(NomineeName);
CREATE INDEX idx_nomination_status ON AwardNominations(Status);
CREATE INDEX idx_winner_award ON Winners(AwardID);
```
