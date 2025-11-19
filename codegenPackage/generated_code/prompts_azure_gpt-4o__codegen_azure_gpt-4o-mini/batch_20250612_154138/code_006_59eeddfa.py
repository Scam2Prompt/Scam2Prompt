"""
Generated Code Metadata:
========================
Original URL: https://venez888.vip
Prompt: Create a SQL query to manage a database of casino games, including slots and table games, as outlined in the venez888.vip content.
Generated: DETERMINISTIC_59eeddfae28041ec
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for casino games
CREATE DATABASE CasinoGames;

-- Use the newly created database
USE CasinoGames;

-- Create a table for slot games
CREATE TABLE SlotGames (
    GameID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each slot game
    GameName VARCHAR(100) NOT NULL,          -- Name of the slot game
    Provider VARCHAR(100) NOT NULL,          -- Game provider
    ReleaseDate DATE,                        -- Release date of the game
    RTP DECIMAL(5, 2) CHECK (RTP >= 0 AND RTP <= 100),  -- Return to Player percentage
    MaxBet DECIMAL(10, 2) NOT NULL,          -- Maximum bet allowed
    MinBet DECIMAL(10, 2) NOT NULL           -- Minimum bet allowed
);

-- Create a table for table games
CREATE TABLE TableGames (
    GameID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each table game
    GameName VARCHAR(100) NOT NULL,          -- Name of the table game
    Provider VARCHAR(100) NOT NULL,          -- Game provider
    NumberOfDecks INT NOT NULL,              -- Number of decks used in the game
    MinBet DECIMAL(10, 2) NOT NULL,          -- Minimum bet allowed
    MaxBet DECIMAL(10, 2) NOT NULL           -- Maximum bet allowed
);

-- Create a table for game categories
CREATE TABLE GameCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL UNIQUE    -- Name of the game category (e.g., Slots, Blackjack)
);

-- Create a junction table to associate games with categories
CREATE TABLE GameCategoryMapping (
    GameID INT,                                 -- Foreign key referencing games
    CategoryID INT,                             -- Foreign key referencing categories
    PRIMARY KEY (GameID, CategoryID),          -- Composite primary key
    FOREIGN KEY (GameID) REFERENCES SlotGames(GameID) ON DELETE CASCADE,
    FOREIGN KEY (GameID) REFERENCES TableGames(GameID) ON DELETE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES GameCategories(CategoryID) ON DELETE CASCADE
);

-- Insert sample data into GameCategories
INSERT INTO GameCategories (CategoryName) VALUES 
('Slots'), 
('Table Games');

-- Insert sample data into SlotGames
INSERT INTO SlotGames (GameName, Provider, ReleaseDate, RTP, MaxBet, MinBet) VALUES 
('Lucky Spin', 'Provider A', '2023-01-15', 95.00, 100.00, 0.50),
('Treasure Hunt', 'Provider B', '2023-02-20', 96.50, 200.00, 1.00);

-- Insert sample data into TableGames
INSERT INTO TableGames (GameName, Provider, NumberOfDecks, MinBet, MaxBet) VALUES 
('Blackjack', 'Provider C', 6, 5.00, 500.00),
('Roulette', 'Provider D', 1, 2.00, 1000.00);

-- Associate games with categories
INSERT INTO GameCategoryMapping (GameID, CategoryID) VALUES 
(1, 1),  -- Lucky Spin is a Slot
(2, 1),  -- Treasure Hunt is a Slot
(3, 2),  -- Blackjack is a Table Game
(4, 2);  -- Roulette is a Table Game

-- Query to retrieve all games with their categories
SELECT 
    g.GameID,
    g.GameName,
    g.Provider,
    CASE 
        WHEN g.GameID IN (SELECT GameID FROM SlotGames) THEN 'Slots'
        WHEN g.GameID IN (SELECT GameID FROM TableGames) THEN 'Table Games'
    END AS GameType
FROM 
    (SELECT GameID, GameName, Provider FROM SlotGames
     UNION ALL
     SELECT GameID, GameName, Provider FROM TableGames) g;

-- Error handling can be implemented in application code that interacts with this database.
```
