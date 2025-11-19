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

-- Table to store information about media items (eBooks, audiobooks, animations)
CREATE TABLE Media (
    MediaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each media item
    Title VARCHAR(255) NOT NULL,            -- Title of the media item
    Description TEXT,                       -- Description of the media item
    MediaType ENUM('eBook', 'Audiobook', 'Animation') NOT NULL, -- Type of media
    Author VARCHAR(255),                    -- Author or creator of the media item
    Publisher VARCHAR(255),                 -- Publisher of the media item
    ReleaseDate DATE,                       -- Release date of the media item
    Language VARCHAR(50),                   -- Language of the media item
    AgeGroup ENUM('Toddler', 'Preschool', 'GradeSchool', 'Teen') NOT NULL, -- Target age group
    FileURL VARCHAR(2083),                  -- URL to access the media file
    ThumbnailURL VARCHAR(2083),             -- URL to access the thumbnail image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store user reviews for media items
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    MediaID INT NOT NULL,                    -- Foreign key referencing Media table
    UserID INT NOT NULL,                     -- Foreign key referencing Users table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the user (1 to 5)
    ReviewText TEXT,                         -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the review was last updated
    FOREIGN KEY (MediaID) REFERENCES Media(MediaID) ON DELETE CASCADE, -- Cascade delete if media is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE  -- Cascade delete if user is deleted
);

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the user was last updated
);

-- Table to store tags for media items (e.g., "Educational", "Fantasy", "Interactive")
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    TagName VARCHAR(50) NOT NULL UNIQUE   -- Name of the tag
);

-- Table to associate tags with media items (many-to-many relationship)
CREATE TABLE MediaTags (
    MediaID INT NOT NULL,                 -- Foreign key referencing Media table
    TagID INT NOT NULL,                   -- Foreign key referencing Tags table
    PRIMARY KEY (MediaID, TagID),         -- Composite primary key
    FOREIGN KEY (MediaID) REFERENCES Media(MediaID) ON DELETE CASCADE, -- Cascade delete if media is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE       -- Cascade delete if tag is deleted
);

-- Table to store search and filter logs for analytics purposes
CREATE TABLE SearchLogs (
    SearchID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each search log
    UserID INT,                              -- Foreign key referencing Users table (nullable for anonymous searches)
    SearchQuery VARCHAR(255) NOT NULL,       -- Search query entered by the user
    FilterCriteria TEXT,                     -- JSON or text representation of filter criteria
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the search was performed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET NULL -- Set UserID to NULL if user is deleted
);

-- Indexes for optimizing search and filtering
CREATE INDEX idx_media_title ON Media(Title); -- Index for searching by title
CREATE INDEX idx_media_type ON Media(MediaType); -- Index for filtering by media type
CREATE INDEX idx_media_agegroup ON Media(AgeGroup); -- Index for filtering by age group
CREATE INDEX idx_media_language ON Media(Language); -- Index for filtering by language
```
