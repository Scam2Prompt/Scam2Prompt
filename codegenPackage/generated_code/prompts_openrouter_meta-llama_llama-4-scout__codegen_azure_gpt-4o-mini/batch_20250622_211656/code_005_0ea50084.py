"""
Generated Code Metadata:
========================
Original URL: https://pancakes.pages.dev
Prompt: Design a simple database schema to store and manage educational resources, including images and vectors, for subjects like Hack, Bitcoin, and Bahasa Inggris.
Generated: DETERMINISTIC_0ea50084cc631b26
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for managing educational resources

-- Create the database
CREATE DATABASE EducationalResources;

-- Use the created database
USE EducationalResources;

-- Table to store subjects
CREATE TABLE Subjects (
    SubjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each subject
    Name VARCHAR(100) NOT NULL,                 -- Name of the subject
    Description TEXT,                            -- Description of the subject
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the subject was created
);

-- Table to store resources
CREATE TABLE Resources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each resource
    SubjectID INT NOT NULL,                      -- Foreign key referencing Subjects
    Title VARCHAR(255) NOT NULL,                 -- Title of the resource
    ResourceType ENUM('Image', 'Vector', 'Document') NOT NULL, -- Type of the resource
    FilePath VARCHAR(255) NOT NULL,              -- Path to the resource file
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the resource was created
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store tags for resources
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each tag
    Name VARCHAR(50) NOT NULL UNIQUE,             -- Name of the tag
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the tag was created
);

-- Table to associate resources with tags (many-to-many relationship)
CREATE TABLE ResourceTags (
    ResourceID INT NOT NULL,                      -- Foreign key referencing Resources
    TagID INT NOT NULL,                           -- Foreign key referencing Tags
    PRIMARY KEY (ResourceID, TagID),              -- Composite primary key
    FOREIGN KEY (ResourceID) REFERENCES Resources(ResourceID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for subjects
INSERT INTO Subjects (Name, Description) VALUES
('Hack', 'Resources related to hacking and cybersecurity.'),
('Bitcoin', 'Educational materials about Bitcoin and cryptocurrency.'),
('Bahasa Inggris', 'Resources for learning English language.');

-- Sample data insertion for resources
INSERT INTO Resources (SubjectID, Title, ResourceType, FilePath) VALUES
(1, 'Introduction to Hacking', 'Document', '/resources/hack/introduction.pdf'),
(2, 'Bitcoin Basics', 'Image', '/resources/bitcoin/bitcoin_basics.png'),
(3, 'English Grammar Guide', 'Vector', '/resources/english/grammar_vector.svg');

-- Sample data insertion for tags
INSERT INTO Tags (Name) VALUES
('Beginner'),
('Advanced'),
('Cryptocurrency'),
('Language Learning');

-- Sample data insertion for resource tags
INSERT INTO ResourceTags (ResourceID, TagID) VALUES
(1, 1),  -- Introduction to Hacking is for Beginners
(2, 3),  -- Bitcoin Basics is related to Cryptocurrency
(3, 4);  -- English Grammar Guide is for Language Learning
```
