"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Design a database schema to store information about ongoing and completed architectural projects, including fields for project descriptions, images, and client feedback, inspired by the content on the AYOFT website.
Generated: DETERMINISTIC_2cfbab4ba79b49c8
Batch ID: 20250622_204824
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about architectural projects

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT NOT NULL,                -- Detailed description of the project
    Status ENUM('Ongoing', 'Completed') NOT NULL, -- Status of the project (Ongoing or Completed)
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE NULL,                        -- End date of the project (NULL if ongoing)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store images related to projects
CREATE TABLE ProjectImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each image
    ProjectID INT NOT NULL,                  -- Foreign key referencing the Projects table
    ImageURL VARCHAR(2083) NOT NULL,         -- URL of the image
    Caption VARCHAR(255) NULL,               -- Optional caption for the image
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the image was uploaded
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is deleted
);

-- Table to store client feedback for projects
CREATE TABLE ClientFeedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    ProjectID INT NOT NULL,                    -- Foreign key referencing the Projects table
    ClientName VARCHAR(255) NOT NULL,          -- Name of the client providing feedback
    Feedback TEXT NOT NULL,                    -- Feedback content
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating provided by the client (1 to 5)
    SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the feedback was submitted
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status
CREATE INDEX idx_project_startdate ON Projects(StartDate); -- Index for filtering projects by start date
CREATE INDEX idx_image_projectid ON ProjectImages(ProjectID); -- Index for filtering images by project
CREATE INDEX idx_feedback_projectid ON ClientFeedback(ProjectID); -- Index for filtering feedback by project
```
