"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://934ummfm.com
Prompt: Design a database schema for storing information about educational programs and podcasts, reflecting the structure used by UMM FM for their content management.
Generated: DETERMINISTIC_6d511a5a22dbd880
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Educational Programs and Podcasts
-- This schema is designed to reflect the structure used by UMM FM for content management.

-- Table: EducationalPrograms
CREATE TABLE EducationalPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY,   -- Primary key for the program
    Title VARCHAR(255) NOT NULL,                -- Title of the educational program
    Description TEXT,                           -- Detailed description of the program
    Category VARCHAR(100),                      -- Category or genre of the program
    Language VARCHAR(50),                       -- Language the program is in
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Podcasts
CREATE TABLE Podcasts (
    PodcastID INT AUTO_INCREMENT PRIMARY KEY,   -- Primary key for the podcast
    Title VARCHAR(255) NOT NULL,                -- Title of the podcast
    Description TEXT,                           -- Detailed description of the podcast
    Host VARCHAR(255),                          -- Host of the podcast
    Duration INT,                               -- Duration of the podcast in minutes
    Language VARCHAR(50),                       -- Language the podcast is in
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the podcast was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: ProgramEpisodes
CREATE TABLE ProgramEpisodes (
    EpisodeID INT AUTO_INCREMENT PRIMARY KEY,   -- Primary key for the episode
    ProgramID INT NOT NULL,                     -- Foreign key linking to the EducationalPrograms table
    Title VARCHAR(255) NOT NULL,                -- Title of the episode
    Description TEXT,                           -- Detailed description of the episode
    Duration INT,                               -- Duration of the episode in minutes
    ReleaseDate DATE,                           -- Release date of the episode
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the episode was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: PodcastEpisodes
CREATE TABLE PodcastEpisodes (
    EpisodeID INT AUTO_INCREMENT PRIMARY KEY,   -- Primary key for the episode
    PodcastID INT NOT NULL,                     -- Foreign key linking to the Podcasts table
    Title VARCHAR(255) NOT NULL,                -- Title of the episode
    Description TEXT,                           -- Detailed description of the episode
    Duration INT,                               -- Duration of the episode in minutes
    ReleaseDate DATE,                           -- Release date of the episode
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the episode was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PodcastID) REFERENCES Podcasts(PodcastID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: Contributors
CREATE TABLE Contributors (
    ContributorID INT AUTO_INCREMENT PRIMARY KEY, -- Primary key for the contributor
    Name VARCHAR(255) NOT NULL,                   -- Name of the contributor
    Bio TEXT,                                     -- Short biography of the contributor
    Email VARCHAR(255),                           -- Email address for communication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the contributor record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: ProgramContributors (Many-to-Many relationship between EducationalPrograms and Contributors)
CREATE TABLE ProgramContributors (
    ProgramID INT NOT NULL,                     -- Foreign key linking to the EducationalPrograms table
    ContributorID INT NOT NULL,                 -- Foreign key linking to the Contributors table
    Role VARCHAR(100),                          -- The role of the contributor in the program (e.g., "Speaker", "Editor")
    PRIMARY KEY (ProgramID, ContributorID),     -- Composite primary key
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ContributorID) REFERENCES Contributors(ContributorID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: PodcastContributors (Many-to-Many relationship between Podcasts and Contributors)
CREATE TABLE PodcastContributors (
    PodcastID INT NOT NULL,                     -- Foreign key linking to the Podcasts table
    ContributorID INT NOT NULL,                 -- Foreign key linking to the Contributors table
    Role VARCHAR(100),                          -- The role of the contributor in the podcast (e.g., "Guest", "Producer")
    PRIMARY KEY (PodcastID, ContributorID),     -- Composite primary key
    FOREIGN KEY (PodcastID) REFERENCES Podcasts(PodcastID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ContributorID) REFERENCES Contributors(ContributorID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Indexes for quick lookups and efficient queries
CREATE INDEX idx_program_category ON EducationalPrograms (Category);
CREATE INDEX idx_podcast_host ON Podcasts (Host);
CREATE INDEX idx_contributor_name ON Contributors (Name);
CREATE INDEX idx_program_title ON EducationalPrograms (Title);
CREATE INDEX idx_podcast_title ON Podcasts (Title);
```
