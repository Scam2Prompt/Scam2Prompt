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
-- Database schema for managing a library of eBooks, audiobooks, and educational animations for children

-- Table to store information about different media types
CREATE TABLE MediaTypes (
    MediaTypeID INT PRIMARY KEY AUTO_INCREMENT,
    MediaTypeName VARCHAR(50) NOT NULL UNIQUE
);

-- Table to store information about the media items
CREATE TABLE MediaItems (
    MediaItemID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Description TEXT,
    MediaTypeID INT,
    ReleaseDate DATE,
    ISBN VARCHAR(20) UNIQUE,
    FilePath VARCHAR(255) NOT NULL,
    Duration INT, -- Duration in seconds for audiobooks and animations
    Rating DECIMAL(3, 2) DEFAULT 0.00, -- Average rating
    FOREIGN KEY (MediaTypeID) REFERENCES MediaTypes(MediaTypeID)
);

-- Table to store user information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store user reviews for media items
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,
    MediaItemID INT,
    UserID INT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating from 1 to 5
    ReviewText TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (MediaItemID) REFERENCES MediaItems(MediaItemID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Table to store tags for filtering and searching
CREATE TABLE Tags (
    TagID INT PRIMARY KEY AUTO_INCREMENT,
    TagName VARCHAR(50) NOT NULL UNIQUE
);

-- Table to associate media items with tags
CREATE TABLE MediaItemTags (
    MediaItemID INT,
    TagID INT,
    PRIMARY KEY (MediaItemID, TagID),
    FOREIGN KEY (MediaItemID) REFERENCES MediaItems(MediaItemID),
    FOREIGN KEY (TagID) REFERENCES Tags(TagID)
);

-- Indexes for improving search performance
CREATE INDEX idx_media_title ON MediaItems(Title);
CREATE INDEX idx_media_author ON MediaItems(Author);
CREATE INDEX idx_media_rating ON MediaItems(Rating);
CREATE INDEX idx_user_username ON Users(Username);
CREATE INDEX idx_review_media ON Reviews(MediaItemID);
CREATE INDEX idx_review_user ON Reviews(UserID);
```
