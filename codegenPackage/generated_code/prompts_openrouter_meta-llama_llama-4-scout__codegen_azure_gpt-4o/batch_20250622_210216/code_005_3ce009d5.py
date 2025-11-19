"""
Generated Code Metadata:
========================
Original URL: https://origineth.net
Prompt: "Design a simple database schema to store Steam game information, including game details, sales data, and user ratings."
Generated: DETERMINISTIC_3ce009d54483d863
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing Steam game information

-- Table to store game details
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    Name VARCHAR(255) NOT NULL,            -- Name of the game
    Developer VARCHAR(255),                -- Developer of the game
    Publisher VARCHAR(255),                -- Publisher of the game
    ReleaseDate DATE,                      -- Release date of the game
    Genre VARCHAR(100),                    -- Genre of the game
    Description TEXT,                      -- Description of the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store sales data
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sale record
    GameID INT NOT NULL,                   -- Foreign key referencing Games table
    Price DECIMAL(10, 2) NOT NULL,         -- Current price of the game
    DiscountPercentage INT DEFAULT 0,      -- Discount percentage (if any)
    UnitsSold INT DEFAULT 0,               -- Number of units sold
    Revenue DECIMAL(15, 2) DEFAULT 0,      -- Total revenue generated
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to store user ratings
CREATE TABLE Ratings (
    RatingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rating
    GameID INT NOT NULL,                     -- Foreign key referencing Games table
    UserID INT NOT NULL,                     -- Identifier for the user (can reference a Users table if needed)
    Rating INT CHECK (Rating BETWEEN 1 AND 10), -- Rating value (1 to 10 scale)
    Review TEXT,                             -- Optional user review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Ensure data integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_game_name ON Games(Name); -- Index for searching games by name
CREATE INDEX idx_game_genre ON Games(Genre); -- Index for searching games by genre
CREATE INDEX idx_sales_gameid ON Sales(GameID); -- Index for sales data lookup by game
CREATE INDEX idx_ratings_gameid ON Ratings(GameID); -- Index for ratings lookup by game
```
