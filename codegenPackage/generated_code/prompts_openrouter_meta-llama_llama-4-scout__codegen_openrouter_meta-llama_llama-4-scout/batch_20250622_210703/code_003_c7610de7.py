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
-- Create a database for Pelangi189 games
CREATE DATABASE Pelangi189Games;

-- Use the Pelangi189Games database
USE Pelangi189Games;

-- Create a table for game categories
CREATE TABLE GameCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a table for games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT,
    GameCategoryID INT,
    GameName VARCHAR(255) NOT NULL,
    GameDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (GameID),
    FOREIGN KEY (GameCategoryID) REFERENCES GameCategories(CategoryID)
);

-- Create a table for game types (e.g., scatter, meja, tembak ikan)
CREATE TABLE GameTypes (
    GameTypeID INT AUTO_INCREMENT,
    GameID INT,
    TypeName VARCHAR(255) NOT NULL,
    TypeDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (GameTypeID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID)
);

-- Create a table for game providers
CREATE TABLE GameProviders (
    ProviderID INT AUTO_INCREMENT,
    ProviderName VARCHAR(255) NOT NULL,
    ProviderDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProviderID)
);

-- Create a table for game versions
CREATE TABLE GameVersions (
    GameVersionID INT AUTO_INCREMENT,
    GameID INT,
    ProviderID INT,
    VersionName VARCHAR(255) NOT NULL,
    VersionDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (GameVersionID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID),
    FOREIGN KEY (ProviderID) REFERENCES GameProviders(ProviderID)
);

-- Create a table for game settings
CREATE TABLE GameSettings (
    GameSettingID INT AUTO_INCREMENT,
    GameVersionID INT,
    SettingName VARCHAR(255) NOT NULL,
    SettingValue VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (GameSettingID),
    FOREIGN KEY (GameVersionID) REFERENCES GameVersions(GameVersionID)
);

-- Create a table for game statistics
CREATE TABLE GameStatistics (
    GameStatisticID INT AUTO_INCREMENT,
    GameVersionID INT,
    StatisticName VARCHAR(255) NOT NULL,
    StatisticValue INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (GameStatisticID),
    FOREIGN KEY (GameVersionID) REFERENCES GameVersions(GameVersionID)
);

-- Insert sample data into GameCategories table
INSERT INTO GameCategories (CategoryName, Description)
VALUES 
('Scatter Games', 'Games with scatter symbols'),
('Meja Games', 'Table games'),
('Tembak Ikan Games', 'Shooting games');

-- Insert sample data into Games table
INSERT INTO Games (GameCategoryID, GameName, GameDescription)
VALUES 
(1, 'Scatter Game 1', 'This is a scatter game'),
(2, 'Meja Game 1', 'This is a meja game'),
(3, 'Tembak Ikan Game 1', 'This is a tembak ikan game');

-- Insert sample data into GameTypes table
INSERT INTO GameTypes (GameID, TypeName, TypeDescription)
VALUES 
(1, 'Scatter Type 1', 'This is a scatter type'),
(2, 'Meja Type 1', 'This is a meja type'),
(3, 'Tembak Ikan Type 1', 'This is a tembak ikan type');

-- Insert sample data into GameProviders table
INSERT INTO GameProviders (ProviderName, ProviderDescription)
VALUES 
('Provider 1', 'This is a game provider'),
('Provider 2', 'This is another game provider');

-- Insert sample data into GameVersions table
INSERT INTO GameVersions (GameID, ProviderID, VersionName, VersionDescription)
VALUES 
(1, 1, 'Version 1.0', 'This is a game version'),
(2, 2, 'Version 2.0', 'This is another game version');

-- Insert sample data into GameSettings table
INSERT INTO GameSettings (GameVersionID, SettingName, SettingValue)
VALUES 
(1, 'Setting 1', 'Value 1'),
(2, 'Setting 2', 'Value 2');

-- Insert sample data into GameStatistics table
INSERT INTO GameStatistics (GameVersionID, StatisticName, StatisticValue)
VALUES 
(1, 'Statistic 1', 100),
(2, 'Statistic 2', 200);
```
