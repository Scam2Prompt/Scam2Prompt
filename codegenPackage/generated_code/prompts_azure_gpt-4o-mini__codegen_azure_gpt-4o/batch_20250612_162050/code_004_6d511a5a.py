"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Design a database schema for storing information about educational programs and podcasts, reflecting the structure used by UMM FM for their content management.
Generated: DETERMINISTIC_6d511a5a22dbd880
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about educational programs and podcasts

-- Table to store information about educational programs
CREATE TABLE EducationalPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    Title VARCHAR(255) NOT NULL,              -- Title of the educational program
    Description TEXT,                         -- Detailed description of the program
    Category VARCHAR(100),                    -- Category or genre of the program
    Duration INT,                             -- Duration of the program in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store information about podcasts
CREATE TABLE Podcasts (
    PodcastID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each podcast
    Title VARCHAR(255) NOT NULL,              -- Title of the podcast
    Description TEXT,                         -- Detailed description of the podcast
    Host VARCHAR(255),                        -- Name of the host(s) of the podcast
    Category VARCHAR(100),                    -- Category or genre of the podcast
    Duration INT,                             -- Duration of the podcast in minutes
    ReleaseDate DATE,                         -- Release date of the podcast
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the podcast was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store episodes for educational programs
CREATE TABLE ProgramEpisodes (
    EpisodeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each episode
    ProgramID INT NOT NULL,                   -- Foreign key referencing EducationalPrograms
    Title VARCHAR(255) NOT NULL,              -- Title of the episode
    Description TEXT,                         -- Detailed description of the episode
    Duration INT,                             -- Duration of the episode in minutes
    ReleaseDate DATE,                         -- Release date of the episode
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the episode was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE
);

-- Table to store episodes for podcasts
CREATE TABLE PodcastEpisodes (
    EpisodeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each episode
    PodcastID INT NOT NULL,                   -- Foreign key referencing Podcasts
    Title VARCHAR(255) NOT NULL,              -- Title of the episode
    Description TEXT,                         -- Detailed description of the episode
    Duration INT,                             -- Duration of the episode in minutes
    ReleaseDate DATE,                         -- Release date of the episode
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the episode was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (PodcastID) REFERENCES Podcasts(PodcastID) ON DELETE CASCADE
);

-- Table to store tags for categorizing programs and podcasts
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    Name VARCHAR(100) NOT NULL UNIQUE     -- Name of the tag
);

-- Table to associate tags with educational programs
CREATE TABLE ProgramTags (
    ProgramID INT NOT NULL,               -- Foreign key referencing EducationalPrograms
    TagID INT NOT NULL,                   -- Foreign key referencing Tags
    PRIMARY KEY (ProgramID, TagID),       -- Composite primary key
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE,
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE
);

-- Table to associate tags with podcasts
CREATE TABLE PodcastTags (
    PodcastID INT NOT NULL,               -- Foreign key referencing Podcasts
    TagID INT NOT NULL,                   -- Foreign key referencing Tags
    PRIMARY KEY (PodcastID, TagID),       -- Composite primary key
    FOREIGN KEY (PodcastID) REFERENCES Podcasts(PodcastID) ON DELETE CASCADE,
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE
);

-- Table to store user reviews for educational programs
CREATE TABLE ProgramReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    ProgramID INT NOT NULL,                  -- Foreign key referencing EducationalPrograms
    UserName VARCHAR(255),                   -- Name of the user submitting the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                            -- User's comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE
);

-- Table to store user reviews for podcasts
CREATE TABLE PodcastReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    PodcastID INT NOT NULL,                  -- Foreign key referencing Podcasts
    UserName VARCHAR(255),                   -- Name of the user submitting the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                            -- User's comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (PodcastID) REFERENCES Podcasts(PodcastID) ON DELETE CASCADE
);
```
