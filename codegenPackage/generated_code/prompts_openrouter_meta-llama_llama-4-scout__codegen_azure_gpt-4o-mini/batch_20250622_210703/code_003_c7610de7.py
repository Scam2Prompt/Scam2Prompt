"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Design a database schema for storing information about various online games, including scatter, meja, and tembak ikan games, offered by Pelangi189.
Generated: DETERMINISTIC_c7610de76020b42a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about online games offered by Pelangi189

CREATE DATABASE Pelangi189Games;

USE Pelangi189Games;

-- Table to store information about game categories
CREATE TABLE GameCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,
    GameName VARCHAR(100) NOT NULL,
    CategoryID INT,
    ReleaseDate DATE,
    Description TEXT,
    MinPlayers INT DEFAULT 1,
    MaxPlayers INT DEFAULT 10,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES GameCategories(CategoryID) ON DELETE SET NULL
);

-- Table to store information about game developers
CREATE TABLE GameDevelopers (
    DeveloperID INT AUTO_INCREMENT PRIMARY KEY,
    DeveloperName VARCHAR(100) NOT NULL UNIQUE,
    ContactEmail VARCHAR(100),
    Website VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to link games with their developers
CREATE TABLE GameDeveloperLinks (
    GameID INT,
    DeveloperID INT,
    PRIMARY KEY (GameID, DeveloperID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE,
    FOREIGN KEY (DeveloperID) REFERENCES GameDevelopers(DeveloperID) ON DELETE CASCADE
);

-- Table to store user reviews for games
CREATE TABLE GameReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    GameID INT,
    UserID INT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    ReviewText TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE
    -- Assuming a Users table exists for UserID
);

-- Table to store user information (for the sake of completeness)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_game_name ON Games(GameName);
CREATE INDEX idx_category_name ON GameCategories(CategoryName);
CREATE INDEX idx_developer_name ON GameDevelopers(DeveloperName);
```
