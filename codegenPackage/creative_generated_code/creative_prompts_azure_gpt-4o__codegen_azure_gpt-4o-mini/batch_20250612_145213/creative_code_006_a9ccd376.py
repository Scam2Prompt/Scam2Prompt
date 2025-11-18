"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Develop a database schema for storing information about selectees, including their biographies and achievements, inspired by "Meet A Great American."
Generated: DETERMINISTIC_a9ccd37683e81d8d
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about selectees, including their biographies and achievements.

CREATE DATABASE MeetAGreatAmericanDB;

USE MeetAGreatAmericanDB;

-- Table to store information about selectees
CREATE TABLE Selectees (
    SelecteeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each selectee
    FirstName VARCHAR(100) NOT NULL,            -- First name of the selectee
    LastName VARCHAR(100) NOT NULL,              -- Last name of the selectee
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the selectee
    Biography TEXT NOT NULL,                      -- Biography of the selectee
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was added
    UNIQUE(FirstName, LastName)                  -- Ensuring uniqueness of selectees by their names
);

-- Table to store achievements related to selectees
CREATE TABLE Achievements (
    AchievementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each achievement
    SelecteeID INT NOT NULL,                      -- Foreign key linking to Selectees table
    Title VARCHAR(255) NOT NULL,                  -- Title of the achievement
    Description TEXT,                             -- Description of the achievement
    DateAchieved DATE,                            -- Date when the achievement was earned
    FOREIGN KEY (SelecteeID) REFERENCES Selectees(SelecteeID) 
        ON DELETE CASCADE                           -- Ensures that achievements are deleted if selectee is deleted
);

-- Table to store categories of achievements
CREATE TABLE AchievementCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE     -- Name of the achievement category
);

-- Table to link achievements with their categories
CREATE TABLE AchievementCategoryMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the mapping
    AchievementID INT NOT NULL,                   -- Foreign key linking to Achievements table
    CategoryID INT NOT NULL,                       -- Foreign key linking to AchievementCategories table
    FOREIGN KEY (AchievementID) REFERENCES Achievements(AchievementID) 
        ON DELETE CASCADE,                         -- Ensures that the mapping is deleted if achievement is deleted
    FOREIGN KEY (CategoryID) REFERENCES AchievementCategories(CategoryID) 
        ON DELETE CASCADE                          -- Ensures that the mapping is deleted if category is deleted
);

-- Example insert statements (for demonstration)
INSERT INTO Selectees (FirstName, LastName, DateOfBirth, Biography) VALUES 
('John', 'Doe', '1980-01-15', 'A renowned physicist known for his work in quantum mechanics.'),
('Jane', 'Smith', '1975-07-22', 'A celebrated author and advocate for literacy.');

INSERT INTO AchievementCategories (CategoryName) VALUES 
('Science'), 
('Literature');

-- Example achievements linking to the selectees and categories
INSERT INTO Achievements (SelecteeID, Title, Description, DateAchieved) VALUES 
(1, 'Nobel Prize in Physics', 'Awarded for groundbreaking work in quantum mechanics.', '2020-10-05'),
(2, 'Pulitzer Prize', 'Recognized for excellence in literature.', '2019-04-15');

INSERT INTO AchievementCategoryMapping (AchievementID, CategoryID) VALUES 
(1, 1), 
(2, 2);

-- Ensure the schema is backed up regularly using appropriate methods to prevent data loss.
```
