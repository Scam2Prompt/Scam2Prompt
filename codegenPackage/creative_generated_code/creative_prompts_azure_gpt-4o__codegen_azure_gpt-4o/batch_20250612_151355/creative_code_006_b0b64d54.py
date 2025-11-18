"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaks.xyz
Prompt: Write a SQL query to store and retrieve architectural project data, including project names, descriptions, and multimedia links, for a database similar to the one used by Ayoft.
Generated: DETERMINISTIC_b0b64d5463247075
Batch ID: 20250612_151355
URLs Found: 8
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/video2.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/newimage1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/video1.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/video3.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/newvideo1.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```sql
-- Database: ArchitectureProjectsDB
-- Table: Projects
-- Purpose: Store and retrieve architectural project data including names, descriptions, and multimedia links.

-- Create the Projects table
CREATE TABLE IF NOT EXISTS Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the architectural project
    ProjectDescription TEXT NOT NULL,         -- Detailed description of the project
    MultimediaLinks TEXT NOT NULL,            -- JSON string or comma-separated links to multimedia resources
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record is created
    UpdatedAt DATETIME ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update of the record
);

-- Insert new project data into the Projects table
INSERT INTO Projects (ProjectName, ProjectDescription, MultimediaLinks)
VALUES 
    ('Modern Villa', 'A luxurious modern villa design with open spaces.', '["https://example.com/image1.jpg", "https://example.com/video1.mp4"]'),
    ('Urban Skyscraper', 'A state-of-the-art skyscraper built with sustainable materials.', '["https://example.com/image2.jpg", "https://example.com/video2.mp4"]'),
    ('Community Center', 'A community-focused design with multifunctional spaces.', '["https://example.com/image3.jpg", "https://example.com/video3.mp4"]');

-- Retrieve all project data
SELECT ProjectID, ProjectName, ProjectDescription, MultimediaLinks, CreatedAt, UpdatedAt
FROM Projects;

-- Retrieve a specific project based on the project name
SELECT ProjectID, ProjectName, ProjectDescription, MultimediaLinks, CreatedAt, UpdatedAt
FROM Projects
WHERE ProjectName = 'Modern Villa';

-- Update multimedia links for a specific project
UPDATE Projects
SET MultimediaLinks = '["https://example.com/newimage1.jpg", "https://example.com/newvideo1.mp4"]'
WHERE ProjectName = 'Modern Villa';

-- Delete a project by its ID
DELETE FROM Projects
WHERE ProjectID = 3;

-- Error handling example using a stored procedure
DELIMITER $$

CREATE PROCEDURE GetProjectByName(IN projectName VARCHAR(255))
BEGIN
    -- Check if project name exists
    DECLARE projectExists INT;

    SELECT COUNT(*) INTO projectExists
    FROM Projects
    WHERE ProjectName = projectName;

    IF projectExists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Project not found.';
    ELSE
        -- Retrieve the project details
        SELECT ProjectID, ProjectName, ProjectDescription, MultimediaLinks, CreatedAt, UpdatedAt
        FROM Projects
        WHERE ProjectName = projectName;
    END IF;
END $$

DELIMITER ;

-- Example usage of the stored procedure
CALL GetProjectByName('Modern Villa');

```
