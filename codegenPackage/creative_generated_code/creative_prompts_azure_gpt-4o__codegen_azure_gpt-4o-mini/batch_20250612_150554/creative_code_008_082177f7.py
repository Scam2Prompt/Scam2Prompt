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

-- Create a database for the portal
CREATE DATABASE MarketResearchPortal;

-- Use the created database
USE MarketResearchPortal;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,           -- Unique username for each user
    Email VARCHAR(100) NOT NULL UNIQUE,              -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,              -- Hashed password for authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the user registered
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Table to store market research reports
CREATE TABLE ResearchReports (
    ReportID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each report
    Title VARCHAR(255) NOT NULL,                      -- Title of the research report
    Content TEXT NOT NULL,                            -- Main content of the research report
    AuthorID INT NOT NULL,                            -- Foreign key referencing the author
    PublishedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the report was published
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID)  -- Establishing relationship with Users table
);

-- Table to store user contributions (comments, feedback)
CREATE TABLE Contributions (
    ContributionID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each contribution
    ReportID INT NOT NULL,                             -- Foreign key referencing the research report
    UserID INT NOT NULL,                              -- Foreign key referencing the user
    ContributionText TEXT NOT NULL,                   -- Text of the contribution
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the contribution was made
    FOREIGN KEY (ReportID) REFERENCES ResearchReports(ReportID),  -- Establishing relationship with ResearchReports table
    FOREIGN KEY (UserID) REFERENCES Users(UserID)     -- Establishing relationship with Users table
);

-- Table to store categories for research reports
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE         -- Name of the category
);

-- Table to link reports with categories (many-to-many relationship)
CREATE TABLE ReportCategories (
    ReportID INT NOT NULL,                             -- Foreign key referencing the research report
    CategoryID INT NOT NULL,                           -- Foreign key referencing the category
    PRIMARY KEY (ReportID, CategoryID),               -- Composite primary key
    FOREIGN KEY (ReportID) REFERENCES ResearchReports(ReportID),  -- Establishing relationship with ResearchReports table
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)  -- Establishing relationship with Categories table
);

-- Optional: Table to store ratings for reports
CREATE TABLE ReportRatings (
    RatingID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each rating
    ReportID INT NOT NULL,                             -- Foreign key referencing the research report
    UserID INT NOT NULL,                              -- Foreign key referencing the user
    Rating INT CHECK (Rating >= 1 AND Rating <= 5),  -- Rating value between 1 and 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the rating was submitted
    FOREIGN KEY (ReportID) REFERENCES ResearchReports(ReportID),  -- Establishing relationship with ResearchReports table
    FOREIGN KEY (UserID) REFERENCES Users(UserID)     -- Establishing relationship with Users table
);
```
