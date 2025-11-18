"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Create a database schema to store information about casinos, including bonuses, free spins, wagering requirements, and user ratings, as structured on Santa Claus Casino.
Generated: DETERMINISTIC_405f6cd5305aa7d4
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create database schema for storing information about casinos
-- including bonuses, free spins, wagering requirements, and user ratings.

-- Drop existing tables if they exist (for a clean slate in development)
DROP TABLE IF EXISTS UserRatings;
DROP TABLE IF EXISTS WageringRequirements;
DROP TABLE IF EXISTS Bonuses;
DROP TABLE IF EXISTS Casinos;

-- Table to store information about casinos
CREATE TABLE Casinos (
    CasinoID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each casino
    Name VARCHAR(255) NOT NULL,               -- Name of the casino
    Location VARCHAR(255),                     -- Location of the casino
    EstablishedYear INT,                       -- Year the casino was established
    Website VARCHAR(255)                       -- Official website of the casino
);

-- Table to store information about bonuses offered by casinos
CREATE TABLE Bonuses (
    BonusID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each bonus
    CasinoID INT,                              -- Foreign key referencing Casinos
    BonusType VARCHAR(100) NOT NULL,          -- Type of bonus (e.g., Welcome, No Deposit)
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount of the bonus
    IsActive BOOLEAN DEFAULT TRUE,             -- Status of the bonus (active/inactive)
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE
);

-- Table to store information about free spins offered by casinos
CREATE TABLE FreeSpins (
    FreeSpinID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each free spin offer
    CasinoID INT,                              -- Foreign key referencing Casinos
    NumberOfSpins INT NOT NULL,                -- Number of free spins offered
    ExpiryDate DATE,                           -- Expiry date of the free spins offer
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE
);

-- Table to store wagering requirements for bonuses
CREATE TABLE WageringRequirements (
    RequirementID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each requirement
    BonusID INT,                                   -- Foreign key referencing Bonuses
    WageringMultiplier DECIMAL(5, 2) NOT NULL,    -- Multiplier for the wagering requirement
    FOREIGN KEY (BonusID) REFERENCES Bonuses(BonusID) ON DELETE CASCADE
);

-- Table to store user ratings for casinos
CREATE TABLE UserRatings (
    RatingID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each rating
    CasinoID INT,                                 -- Foreign key referencing Casinos
    UserID INT NOT NULL,                          -- Identifier for the user (could reference a Users table)
    Rating INT NOT NULL CHECK (Rating >= 1 AND Rating <= 5), -- Rating value (1 to 5 stars)
    ReviewText TEXT,                              -- Optional text review by the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the rating was created
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE
);

-- Optionally, you can create indexes on frequently queried columns for performance.
CREATE INDEX idx_casino_name ON Casinos(Name);
CREATE INDEX idx_bonus_casino ON Bonuses(CasinoID);
CREATE INDEX idx_freespins_casino ON FreeSpins(CasinoID);
CREATE INDEX idx_wagering_bonus ON WageringRequirements(BonusID);
CREATE INDEX idx_ratings_casino ON UserRatings(CasinoID);
CREATE INDEX idx_ratings_user ON UserRatings(UserID);
```
