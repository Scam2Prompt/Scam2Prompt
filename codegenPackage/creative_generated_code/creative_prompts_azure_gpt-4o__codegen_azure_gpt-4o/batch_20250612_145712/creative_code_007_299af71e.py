"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Recommend a database schema for storing genealogical records, including fields for family names, historical collections, and media attachments, as described on the Meyer/Seim family website.
Generated: DETERMINISTIC_299af71e51a94064
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing genealogical records

-- Table to store individual person records
CREATE TABLE Persons (
    PersonID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each person
    FirstName VARCHAR(50) NOT NULL,           -- First name of the person
    LastName VARCHAR(50) NOT NULL,            -- Last name of the person
    BirthDate DATE,                           -- Date of birth
    DeathDate DATE,                           -- Date of death (NULL if still alive)
    Gender ENUM('Male', 'Female', 'Other'),   -- Gender of the person
    Notes TEXT,                               -- Additional notes or biographical information
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store family relationships
CREATE TABLE FamilyRelations (
    RelationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each relationship
    ParentID INT NOT NULL,                      -- PersonID of the parent
    ChildID INT NOT NULL,                       -- PersonID of the child
    RelationType ENUM('Biological', 'Adoptive', 'Step'), -- Type of relationship
    FOREIGN KEY (ParentID) REFERENCES Persons(PersonID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ChildID) REFERENCES Persons(PersonID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store historical collections (e.g., family events, locations)
CREATE TABLE HistoricalCollections (
    CollectionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the collection
    Title VARCHAR(100) NOT NULL,                 -- Title of the collection
    Description TEXT,                            -- Description of the collection
    EventDate DATE,                              -- Date of the historical event (if applicable)
    Location VARCHAR(255),                       -- Location of the event (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate persons with historical collections
CREATE TABLE PersonCollections (
    PersonCollectionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier
    PersonID INT NOT NULL,                             -- Person involved in the collection
    CollectionID INT NOT NULL,                         -- Associated collection ID
    Role VARCHAR(100),                                 -- Role of the person in the collection
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CollectionID) REFERENCES HistoricalCollections(CollectionID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store media attachments (e.g., photos, documents)
CREATE TABLE MediaAttachments (
    MediaID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the media
    FilePath VARCHAR(255) NOT NULL,                 -- Path to the media file
    FileType VARCHAR(50),                           -- Type of media (e.g., image/jpeg, application/pdf)
    Description TEXT,                               -- Description of the media
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the media was uploaded
    UploadedBy VARCHAR(100),                        -- Name of the uploader
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate media with persons
CREATE TABLE PersonMedia (
    PersonMediaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier
    PersonID INT NOT NULL,                        -- Associated person ID
    MediaID INT NOT NULL,                         -- Associated media ID
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (MediaID) REFERENCES MediaAttachments(MediaID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to associate media with collections
CREATE TABLE CollectionMedia (
    CollectionMediaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier
    CollectionID INT NOT NULL,                        -- Associated collection ID
    MediaID INT NOT NULL,                             -- Associated media ID
    FOREIGN KEY (CollectionID) REFERENCES HistoricalCollections(CollectionID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (MediaID) REFERENCES MediaAttachments(MediaID) ON DELETE CASCADE -- Ensures referential integrity
);
```
