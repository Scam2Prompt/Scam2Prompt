"""
Generated Code Metadata:
========================
Original URL: https://guapaaltejer.com
Prompt: Design a database schema to store information about knitting and crochet patterns, including attributes such as yarn type, needle size, and skill level.
Generated: DETERMINISTIC_0acedf57cd6d01e6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing knitting and crochet patterns

-- Table to store information about patterns
CREATE TABLE Patterns (
    PatternID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pattern
    Name VARCHAR(255) NOT NULL,               -- Name of the pattern
    Description TEXT,                         -- Detailed description of the pattern
    SkillLevel ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Skill level required
    YarnType VARCHAR(255) NOT NULL,           -- Type of yarn recommended
    NeedleSize VARCHAR(50),                   -- Recommended needle or hook size
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the pattern was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store tags for patterns (e.g., "hat", "scarf", "blanket")
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    Name VARCHAR(100) NOT NULL UNIQUE     -- Name of the tag
);

-- Many-to-Many relationship between Patterns and Tags
CREATE TABLE PatternTags (
    PatternID INT NOT NULL,               -- Foreign key referencing Patterns
    TagID INT NOT NULL,                   -- Foreign key referencing Tags
    PRIMARY KEY (PatternID, TagID),       -- Composite primary key
    FOREIGN KEY (PatternID) REFERENCES Patterns(PatternID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE              -- Cascade delete
);

-- Table to store images associated with patterns
CREATE TABLE PatternImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each image
    PatternID INT NOT NULL,                 -- Foreign key referencing Patterns
    ImageURL VARCHAR(2083) NOT NULL,        -- URL of the image
    Caption VARCHAR(255),                   -- Optional caption for the image
    FOREIGN KEY (PatternID) REFERENCES Patterns(PatternID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store user reviews for patterns
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    PatternID INT NOT NULL,                  -- Foreign key referencing Patterns
    UserName VARCHAR(255) NOT NULL,          -- Name of the user leaving the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                            -- Optional comment from the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (PatternID) REFERENCES Patterns(PatternID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store additional attributes for patterns (e.g., "difficulty notes", "special techniques")
CREATE TABLE PatternAttributes (
    AttributeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attribute
    PatternID INT NOT NULL,                     -- Foreign key referencing Patterns
    AttributeName VARCHAR(255) NOT NULL,        -- Name of the attribute
    AttributeValue TEXT,                        -- Value of the attribute
    FOREIGN KEY (PatternID) REFERENCES Patterns(PatternID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for faster searching
CREATE INDEX idx_pattern_name ON Patterns(Name); -- Index for pattern name
CREATE INDEX idx_tag_name ON Tags(Name);         -- Index for tag name
CREATE INDEX idx_review_rating ON Reviews(Rating); -- Index for review ratings
```
