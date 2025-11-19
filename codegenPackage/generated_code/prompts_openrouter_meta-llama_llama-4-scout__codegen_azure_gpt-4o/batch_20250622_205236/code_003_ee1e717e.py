"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Design a database schema to store sweepstakes entries and their corresponding prize information, inspired by the structure implied on thedaybrightener.com.
Generated: DETERMINISTIC_ee1e717e3fd39db6
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing sweepstakes entries and prize information

-- Table to store users who enter the sweepstakes
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- First name of the user
    LastName VARCHAR(50) NOT NULL,         -- Last name of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user (must be unique)
    PhoneNumber VARCHAR(15),               -- Optional phone number of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was created
);

-- Table to store sweepstakes information
CREATE TABLE Sweepstakes (
    SweepstakesID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sweepstakes
    Name VARCHAR(100) NOT NULL,                   -- Name of the sweepstakes
    Description TEXT,                              -- Description of the sweepstakes
    StartDate DATE NOT NULL,                      -- Start date of the sweepstakes
    EndDate DATE NOT NULL,                        -- End date of the sweepstakes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the sweepstakes was created
);

-- Table to store prizes associated with sweepstakes
CREATE TABLE Prizes (
    PrizeID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each prize
    SweepstakesID INT NOT NULL,                   -- Foreign key referencing Sweepstakes table
    Name VARCHAR(100) NOT NULL,                   -- Name of the prize
    Description TEXT,                              -- Description of the prize
    Quantity INT NOT NULL DEFAULT 1,              -- Number of prizes available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the prize was created
    FOREIGN KEY (SweepstakesID) REFERENCES Sweepstakes(SweepstakesID) ON DELETE CASCADE
);

-- Table to store entries for sweepstakes
CREATE TABLE Entries (
    EntryID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each entry
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    SweepstakesID INT NOT NULL,                   -- Foreign key referencing Sweepstakes table
    EntryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entry was made
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (SweepstakesID) REFERENCES Sweepstakes(SweepstakesID) ON DELETE CASCADE
);

-- Table to store winners and their prize information
CREATE TABLE Winners (
    WinnerID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each winner record
    EntryID INT NOT NULL,                         -- Foreign key referencing Entries table
    PrizeID INT NOT NULL,                         -- Foreign key referencing Prizes table
    AwardedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the prize was awarded
    FOREIGN KEY (EntryID) REFERENCES Entries(EntryID) ON DELETE CASCADE,
    FOREIGN KEY (PrizeID) REFERENCES Prizes(PrizeID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_sweepstakes_dates ON Sweepstakes (StartDate, EndDate);
CREATE INDEX idx_entries_user_sweepstakes ON Entries (UserID, SweepstakesID);
CREATE INDEX idx_winners_entry_prize ON Winners (EntryID, PrizeID);
```
