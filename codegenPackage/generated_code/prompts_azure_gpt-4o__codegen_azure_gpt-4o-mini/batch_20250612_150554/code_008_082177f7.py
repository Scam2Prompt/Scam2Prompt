"""
Generated Code Metadata:
========================
Original URL: https://horizonblue.firstlight.am
Prompt: Recommend a database structure for storing market research reports and user contributions in a portal designed for intelligence sharing.
Generated: DETERMINISTIC_082177f7c4d8cc9a
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database structure for storing market research reports and user contributions

-- Create a database for the intelligence sharing portal
CREATE DATABASE IntelligenceSharingPortal;

-- Use the created database
USE IntelligenceSharingPortal;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for login
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email for user communication
    PasswordHash VARCHAR(255) NOT NULL,       -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store market research reports
CREATE TABLE ResearchReports (
    ReportID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each report
    Title VARCHAR(255) NOT NULL,              -- Title of the research report
    Description TEXT,                          -- Brief description of the report
    AuthorID INT NOT NULL,                     -- Foreign key referencing the user who created the report
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of report creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID) ON DELETE CASCADE  -- Ensures reports are deleted if the user is deleted
);

-- Table to store user contributions to reports
CREATE TABLE Contributions (
    ContributionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each contribution
    ReportID INT NOT NULL,                           -- Foreign key referencing the report being contributed to
    ContributorID INT NOT NULL,                      -- Foreign key referencing the user who made the contribution
    ContributionText TEXT NOT NULL,                  -- Text of the contribution
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of contribution creation
    FOREIGN KEY (ReportID) REFERENCES ResearchReports(ReportID) ON DELETE CASCADE,  -- Ensures contributions are deleted if the report is deleted
    FOREIGN KEY (ContributorID) REFERENCES Users(UserID) ON DELETE CASCADE  -- Ensures contributions are deleted if the user is deleted
);

-- Table to store tags for categorizing reports
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each tag
    TagName VARCHAR(50) NOT NULL UNIQUE    -- Unique name for the tag
);

-- Table to associate reports with tags (many-to-many relationship)
CREATE TABLE ReportTags (
    ReportID INT NOT NULL,                   -- Foreign key referencing the report
    TagID INT NOT NULL,                      -- Foreign key referencing the tag
    PRIMARY KEY (ReportID, TagID),          -- Composite primary key
    FOREIGN KEY (ReportID) REFERENCES ResearchReports(ReportID) ON DELETE CASCADE,  -- Ensures associations are deleted if the report is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE  -- Ensures associations are deleted if the tag is deleted
);
```
