"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Create a SQL query to manage a database of casino games, including slots and table games, as outlined in the venez888.vip content.
Generated: DETERMINISTIC_59eeddfae28041ec
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema for the casino games database
CREATE SCHEMA IF NOT EXISTS CasinoGames;

-- Switch to the CasinoGames schema
USE CasinoGames;

-- Table to store game categories (e.g., slots, table games)
CREATE TABLE IF NOT EXISTS GameCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category (e.g., Slots, Table Games)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for updates
);

-- Table to store casino games
CREATE TABLE IF NOT EXISTS Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the game
    GameName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the game
    CategoryID INT NOT NULL,  -- Foreign key referencing GameCategories
    Provider VARCHAR(255) NOT NULL,  -- Name of the provider (e.g., NetEnt, Microgaming)
    RTP DECIMAL(5, 2) NOT NULL CHECK (RTP BETWEEN 0 AND 100),  -- Return-to-player percentage (0-100)
    MaxBet DECIMAL(10, 2) NOT NULL,  -- Maximum bet amount
    MinBet DECIMAL(10, 2) NOT NULL,  -- Minimum bet amount
    ReleasedDate DATE NOT NULL,  -- Release date of the game
    IsActive BOOLEAN DEFAULT TRUE,  -- Indicates whether the game is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the game was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for updates
    FOREIGN KEY (CategoryID) REFERENCES GameCategories(CategoryID)  -- Enforce valid categories
);

-- Error handling: Ensure the tables are created successfully
-- (Typically handled by the database system, but validation scripts can be added in production environments)

-- Insert default category data
INSERT INTO GameCategories (CategoryName)
VALUES ('Slots'), ('Table Games')
ON DUPLICATE KEY UPDATE CategoryName = VALUES(CategoryName);  -- Prevent duplicate entries

-- Example insertion of casino games
INSERT INTO Games (GameName, CategoryID, Provider, RTP, MaxBet, MinBet, ReleasedDate, IsActive)
VALUES 
    ('Starburst', 1, 'NetEnt', 96.1, 1000.00, 0.10, '2012-11-01', TRUE),
    ('Roulette Pro', 2, 'Microgaming', 97.3, 5000.00, 1.00, '2015-06-15', TRUE)
ON DUPLICATE KEY UPDATE 
    GameName = VALUES(GameName), 
    RTP = VALUES(RTP), 
    MaxBet = VALUES(MaxBet), 
    MinBet = VALUES(MinBet), 
    ReleasedDate = VALUES(ReleasedDate), 
    IsActive = VALUES(IsActive);  -- Prevent duplicate entries

-- Query to fetch all active games
SELECT 
    g.GameID, 
    g.GameName, 
    c.CategoryName, 
    g.Provider, 
    g.RTP, 
    g.MaxBet, 
    g.MinBet, 
    g.ReleasedDate, 
    g.IsActive
FROM 
    Games g
JOIN 
    GameCategories c ON g.CategoryID = c.CategoryID
WHERE 
    g.IsActive = TRUE
ORDER BY 
    g.ReleasedDate DESC;  -- Order by release date, latest first
```
