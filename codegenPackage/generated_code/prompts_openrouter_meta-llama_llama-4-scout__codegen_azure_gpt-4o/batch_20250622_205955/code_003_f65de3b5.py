"""
Generated Code Metadata:
========================
Original URL: https://coarco.org
Prompt: "Design a database schema for a platform that manages art exhibitions and projects, including fields for artist bios, project descriptions, and image galleries."
Generated: DETERMINISTIC_f65de3b5aacdf79f
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing art exhibitions and projects

-- Table to store information about artists
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Full name of the artist
    Bio TEXT,                                -- Biography of the artist
    WebsiteURL VARCHAR(255),                 -- Optional website link for the artist
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    Title VARCHAR(255) NOT NULL,              -- Title of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE,                           -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    ArtistID INT NOT NULL,                    -- Foreign key linking to the artist
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE -- Cascade delete if artist is removed
);

-- Table to store image galleries for projects
CREATE TABLE ProjectImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each image
    ProjectID INT NOT NULL,                  -- Foreign key linking to the project
    ImageURL VARCHAR(255) NOT NULL,          -- URL of the image
    Caption VARCHAR(255),                    -- Optional caption for the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Table to store information about exhibitions
CREATE TABLE Exhibitions (
    ExhibitionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each exhibition
    Name VARCHAR(255) NOT NULL,                  -- Name of the exhibition
    Description TEXT,                            -- Detailed description of the exhibition
    StartDate DATE NOT NULL,                     -- Start date of the exhibition
    EndDate DATE NOT NULL,                       -- End date of the exhibition
    Location VARCHAR(255),                       -- Location of the exhibition
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to associate projects with exhibitions
CREATE TABLE ExhibitionProjects (
    ExhibitionID INT NOT NULL,                  -- Foreign key linking to the exhibition
    ProjectID INT NOT NULL,                     -- Foreign key linking to the project
    PRIMARY KEY (ExhibitionID, ProjectID),      -- Composite primary key to ensure unique associations
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions(ExhibitionID) ON DELETE CASCADE, -- Cascade delete if exhibition is removed
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);
```
