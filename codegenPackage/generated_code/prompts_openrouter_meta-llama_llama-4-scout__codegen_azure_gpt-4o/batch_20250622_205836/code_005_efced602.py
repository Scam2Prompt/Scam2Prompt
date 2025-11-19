"""
Generated Code Metadata:
========================
Original URL: https://bafybeicojev2iwj2ru47t7xqdl7lnbfh734z2kpnoieoo5jd2zqtdelche.ipfs.dweb.link
Prompt: "Design a database schema for storing NFT metadata and tournament results for a platform like Mojo Melee."
Generated: DETERMINISTIC_efced602b4fd6e16
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing NFT metadata and tournament results for a platform like Mojo Melee

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for account creation
);

-- Table to store NFT metadata
CREATE TABLE NFTs (
    NFTID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each NFT
    UserID INT NOT NULL,                   -- Foreign key referencing the owner of the NFT
    Name VARCHAR(100) NOT NULL,            -- Name of the NFT
    Description TEXT,                      -- Description of the NFT
    ImageURL VARCHAR(255),                 -- URL to the NFT image
    Metadata JSON,                         -- Additional metadata stored as JSON
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for NFT creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store tournament information
CREATE TABLE Tournaments (
    TournamentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tournament
    Name VARCHAR(100) NOT NULL,                  -- Name of the tournament
    StartDate TIMESTAMP NOT NULL,                -- Start date and time of the tournament
    EndDate TIMESTAMP NOT NULL,                  -- End date and time of the tournament
    PrizePool DECIMAL(10, 2) NOT NULL,           -- Prize pool amount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for tournament creation
);

-- Table to store tournament results
CREATE TABLE TournamentResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each result entry
    TournamentID INT NOT NULL,                  -- Foreign key referencing the tournament
    UserID INT NOT NULL,                        -- Foreign key referencing the user
    Rank INT NOT NULL,                          -- Rank achieved by the user
    Prize DECIMAL(10, 2),                       -- Prize amount won by the user
    RecordedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for result recording
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE, -- Cascade delete if tournament is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_UserID ON NFTs(UserID);
CREATE INDEX idx_TournamentID ON TournamentResults(TournamentID);
CREATE INDEX idx_UserTournament ON TournamentResults(UserID, TournamentID);

-- Error handling and constraints
-- Ensure that tournament end date is after the start date
ALTER TABLE Tournaments
ADD CONSTRAINT chk_EndDateAfterStartDate CHECK (EndDate > StartDate);

-- Ensure that rank is a positive integer
ALTER TABLE TournamentResults
ADD CONSTRAINT chk_PositiveRank CHECK (Rank > 0);

-- Ensure that prize pool and prize amounts are non-negative
ALTER TABLE Tournaments
ADD CONSTRAINT chk_NonNegativePrizePool CHECK (PrizePool >= 0);

ALTER TABLE TournamentResults
ADD CONSTRAINT chk_NonNegativePrize CHECK (Prize >= 0);
```
