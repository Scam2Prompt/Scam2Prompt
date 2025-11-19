"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Design a database schema for storing and managing a library of eBooks, audiobooks, and educational animations for children, incorporating features like search, filtering, and user reviews.
Generated: DETERMINISTIC_055d5bd679aacdfc
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for library management system

CREATE DATABASE LibraryManagement;

USE LibraryManagement;

-- Create table for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    Role ENUM('admin', 'moderator', 'user') DEFAULT 'user',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (UserID)
);

-- Create table for eBooks
CREATE TABLE eBooks (
    eBookID INT AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Description TEXT,
    FilePath VARCHAR(255) NOT NULL,
    FileType VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (eBookID)
);

-- Create table for audiobooks
CREATE TABLE Audiobooks (
    AudiobookID INT AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Description TEXT,
    FilePath VARCHAR(255) NOT NULL,
    FileType VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AudiobookID)
);

-- Create table for educational animations
CREATE TABLE Animations (
    AnimationID INT AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    FilePath VARCHAR(255) NOT NULL,
    FileType VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AnimationID)
);

-- Create table for reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    UserID INT NOT NULL,
    eBookID INT,
    AudiobookID INT,
    AnimationID INT,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Comment TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (eBookID) REFERENCES eBooks(eBookID),
    FOREIGN KEY (AudiobookID) REFERENCES Audiobooks(AudiobookID),
    FOREIGN KEY (AnimationID) REFERENCES Animations(AnimationID),
    CHECK ((eBookID IS NOT NULL AND AudiobookID IS NULL AND AnimationID IS NULL) OR 
           (eBookID IS NULL AND AudiobookID IS NOT NULL AND AnimationID IS NULL) OR 
           (eBookID IS NULL AND AudiobookID IS NULL AND AnimationID IS NOT NULL))
);

-- Create table for search index
CREATE FULLTEXT INDEX idx_search ON eBooks (Title, Author, Description);
CREATE FULLTEXT INDEX idx_search_audio ON Audiobooks (Title, Author, Description);
CREATE FULLTEXT INDEX idx_search_animation ON Animations (Title, Description);

-- Stored procedure for searching eBooks, audiobooks, and animations
DELIMITER //
CREATE PROCEDURE SearchLibrary(IN searchTerm VARCHAR(255))
BEGIN
    SELECT 
        'eBook' AS Type, 
        eBookID AS ID, 
        Title, 
        Author, 
        Description 
    FROM 
        eBooks 
    WHERE 
        MATCH (Title, Author, Description) AGAINST (searchTerm IN NATURAL LANGUAGE MODE)
    UNION ALL
    SELECT 
        'Audiobook' AS Type, 
        AudiobookID AS ID, 
        Title, 
        Author, 
        Description 
    FROM 
        Audiobooks 
    WHERE 
        MATCH (Title, Author, Description) AGAINST (searchTerm IN NATURAL LANGUAGE MODE)
    UNION ALL
    SELECT 
        'Animation' AS Type, 
        AnimationID AS ID, 
        Title, 
        NULL AS Author, 
        Description 
    FROM 
        Animations 
    WHERE 
        MATCH (Title, Description) AGAINST (searchTerm IN NATURAL LANGUAGE MODE);
END//
DELIMITER ;

-- Example usage:
-- CALL SearchLibrary('example search term');

-- Create view for user reviews
CREATE VIEW UserReviews AS
SELECT 
    U.UserID, 
    U.Name, 
    COALESCE(e.Title, a.Title, an.Title) AS Title, 
    R.Rating, 
    R.Comment, 
    R.CreatedAt
FROM 
    Reviews R
JOIN 
    Users U ON R.UserID = U.UserID
LEFT JOIN 
    eBooks e ON R.eBookID = e.eBookID
LEFT JOIN 
    Audiobooks a ON R.AudiobookID = a.AudiobookID
LEFT JOIN 
    Animations an ON R.AnimationID = an.AnimationID;
```
