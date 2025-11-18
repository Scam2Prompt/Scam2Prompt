"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://horizonblue.firstlight.am
Prompt: Recommend a database structure for storing market research reports and user contributions in a portal designed for intelligence sharing.
Generated: DETERMINISTIC_082177f7c4d8cc9a
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database structure for storing market research reports and user contributions
-- Designed for intelligence sharing in a portal

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for login
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address
    PasswordHash VARCHAR(255) NOT NULL,    -- Password hash for secure authentication
    FullName VARCHAR(100),                 -- Full name of the user
    Role ENUM('Admin', 'Contributor', 'Viewer') DEFAULT 'Viewer', -- User roles in the portal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store market research reports
CREATE TABLE Reports (
    ReportID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each report
    Title VARCHAR(255) NOT NULL,             -- Title of the report
    Summary TEXT NOT NULL,                   -- Summary of the report
    Content TEXT NOT NULL,                   -- Full content of the report
    Category VARCHAR(100),                   -- Category of the report (e.g., "Finance", "Technology")
    CreatedBy INT NOT NULL,                  -- Foreign key linking to the user who created the report
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of report creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store user contributions (e.g., comments, insights)
CREATE TABLE Contributions (
    ContributionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contribution
    ReportID INT NOT NULL,                         -- Foreign key linking to the associated report
    UserID INT NOT NULL,                           -- Foreign key linking to the user making the contribution
    ContributionText TEXT NOT NULL,                -- Text of the contribution
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of contribution creation
    FOREIGN KEY (ReportID) REFERENCES Reports(ReportID) ON DELETE CASCADE, -- Ensures contributions are tied to existing reports
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures contributions are tied to existing users
);

-- Table to store tags for categorizing reports
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    TagName VARCHAR(50) NOT NULL UNIQUE   -- Name of the tag (e.g., "AI", "Economy")
);

-- Many-to-Many relationship between Reports and Tags
CREATE TABLE ReportTags (
    ReportID INT NOT NULL,                          -- Foreign key linking to the report
    TagID INT NOT NULL,                             -- Foreign key linking to the tag
    PRIMARY KEY (ReportID, TagID),                  -- Composite primary key for the association
    FOREIGN KEY (ReportID) REFERENCES Reports(ReportID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexing for faster queries
CREATE INDEX idx_reports_created_by ON Reports (CreatedBy);
CREATE INDEX idx_contributions_report_id ON Contributions (ReportID);
CREATE INDEX idx_report_tags_tag_id ON ReportTags (TagID);
```
