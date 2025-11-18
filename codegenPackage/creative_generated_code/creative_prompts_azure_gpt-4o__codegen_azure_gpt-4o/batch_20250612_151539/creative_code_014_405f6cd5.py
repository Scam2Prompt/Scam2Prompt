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
-- Create database schema for storing casino information
-- This schema includes tables for casinos, bonuses, free spins, wagering requirements, and user ratings

-- Create table to store casino information
CREATE TABLE Casinos (
    CasinoID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each casino
    CasinoName VARCHAR(255) NOT NULL,                    -- Name of the casino
    WebsiteURL VARCHAR(255) NOT NULL,                    -- Website URL of the casino
    EstablishedYear INT NOT NULL,                        -- Year the casino was established
    ContactEmail VARCHAR(255),                           -- Optional contact email
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create table to store bonus information associated with casinos
CREATE TABLE Bonuses (
    BonusID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each bonus
    CasinoID INT NOT NULL,                               -- Foreign key to Casinos table
    BonusDescription VARCHAR(255) NOT NULL,             -- Description of the bonus
    BonusAmount DECIMAL(10, 2),                          -- Amount of the bonus (e.g., monetary value)
    BonusType ENUM('Deposit', 'No Deposit', 'Welcome'), -- Type of the bonus
    ExpirationDate DATE,                                 -- Expiration date of the bonus
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade deletion
);

-- Create table to store free spin information associated with casinos
CREATE TABLE FreeSpins (
    FreeSpinID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for free spins
    CasinoID INT NOT NULL,                               -- Foreign key to Casinos table
    FreeSpinCount INT NOT NULL,                          -- Number of free spins offered
    GameEligible VARCHAR(255),                           -- Eligible game for the free spins
    ExpirationDate DATE,                                 -- Expiration date of the free spins
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade deletion
);

-- Create table to store wagering requirements
CREATE TABLE WageringRequirements (
    WageringID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for wagering requirements
    CasinoID INT NOT NULL,                               -- Foreign key to Casinos table
    RequirementDescription VARCHAR(255) NOT NULL,       -- Description of the wagering requirements
    Multiplier INT NOT NULL,                             -- Multiplier for wager (e.g., 10x or 20x)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade deletion
);

-- Create table to store user ratings for casinos
CREATE TABLE UserRatings (
    RatingID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each rating
    CasinoID INT NOT NULL,                               -- Foreign key to Casinos table
    UserName VARCHAR(255) NOT NULL,                     -- Name of the user providing the rating
    UserEmail VARCHAR(255),                              -- Optional user email
    RatingValue TINYINT NOT NULL CHECK (RatingValue BETWEEN 1 AND 5), -- Rating value (1 to 5 scale)
    Review TEXT,                                         -- Optional textual review of the casino
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the record was created
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade deletion
);

-- Add indexes to improve query performance
CREATE INDEX idx_casino_name ON Casinos(CasinoName);
CREATE INDEX idx_bonus_casino_id ON Bonuses(CasinoID);
CREATE INDEX idx_free_spins_casino_id ON FreeSpins(CasinoID);
CREATE INDEX idx_wagering_casino_id ON WageringRequirements(CasinoID);
CREATE INDEX idx_ratings_casino_id ON UserRatings(CasinoID);
```
