"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: "Design a database schema for storing information about textile courses, including diploma and degree programs, and their affiliations with boards of technical education."
Generated: DETERMINISTIC_8dff4a7b63801d9f
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about textile courses, including diploma and degree programs,
-- and their affiliations with boards of technical education.

-- Create a table to store information about boards of technical education
CREATE TABLE Boards (
    BoardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each board
    BoardName VARCHAR(255) NOT NULL,        -- Name of the board
    Country VARCHAR(100),                   -- Country where the board is located
    EstablishedYear INT,                    -- Year the board was established
    WebsiteURL VARCHAR(255),                -- Official website of the board
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store information about textile courses
CREATE TABLE TextileCourses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    ProgramType ENUM('Diploma', 'Degree') NOT NULL, -- Type of program (Diploma or Degree)
    DurationYears INT NOT NULL,              -- Duration of the course in years
    Description TEXT,                        -- Detailed description of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store affiliations between courses and boards
CREATE TABLE CourseAffiliations (
    AffiliationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each affiliation
    CourseID INT NOT NULL,                        -- Foreign key referencing TextileCourses
    BoardID INT NOT NULL,                         -- Foreign key referencing Boards
    AffiliationDate DATE,                         -- Date when the affiliation was established
    Status ENUM('Active', 'Inactive') DEFAULT 'Active', -- Status of the affiliation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (CourseID) REFERENCES TextileCourses(CourseID) ON DELETE CASCADE, -- Cascade delete for course
    FOREIGN KEY (BoardID) REFERENCES Boards(BoardID) ON DELETE CASCADE -- Cascade delete for board
);

-- Indexes for optimizing queries
CREATE INDEX idx_course_name ON TextileCourses(CourseName);
CREATE INDEX idx_board_name ON Boards(BoardName);
CREATE INDEX idx_affiliation_status ON CourseAffiliations(Status);

-- Example of error handling: Ensure proper constraints
-- Prevent duplicate affiliations for the same course and board
ALTER TABLE CourseAffiliations
ADD CONSTRAINT unique_course_board_affiliation UNIQUE (CourseID, BoardID);
```
