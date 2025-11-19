"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Design a database schema for storing information about AIDA's projects, including project name, description, location, and outcomes, and write a SQL query to retrieve project data.
Generated: DETERMINISTIC_81d05c4e62bb9a1e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for AIDA's projects
CREATE TABLE Locations (
  LocationID INT AUTO_INCREMENT,
  City VARCHAR(255) NOT NULL,
  Country VARCHAR(255) NOT NULL,
  PRIMARY KEY (LocationID)
);

CREATE TABLE Projects (
  ProjectID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Description TEXT,
  LocationID INT,
  PRIMARY KEY (ProjectID),
  FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

CREATE TABLE Outcomes (
  OutcomeID INT AUTO_INCREMENT,
  ProjectID INT,
  OutcomeDescription TEXT,
  PRIMARY KEY (OutcomeID),
  FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Insert sample data into the tables
INSERT INTO Locations (City, Country)
VALUES 
('New York', 'USA'),
('London', 'UK'),
('Paris', 'France');

INSERT INTO Projects (Name, Description, LocationID)
VALUES 
('Project Alpha', 'This is project alpha', 1),
('Project Beta', 'This is project beta', 2),
('Project Gamma', 'This is project gamma', 3);

INSERT INTO Outcomes (ProjectID, OutcomeDescription)
VALUES 
(1, 'Outcome 1 for project alpha'),
(1, 'Outcome 2 for project alpha'),
(2, 'Outcome 1 for project beta');

-- SQL query to retrieve project data
SELECT 
  p.ProjectID,
  p.Name,
  p.Description,
  l.City,
  l.Country,
  o.OutcomeDescription
FROM 
  Projects p
  LEFT JOIN Locations l ON p.LocationID = l.LocationID
  LEFT JOIN Outcomes o ON p.ProjectID = o.ProjectID
ORDER BY 
  p.ProjectID, 
  o.OutcomeID;

-- Stored procedure to add new project
DELIMITER //
CREATE PROCEDURE AddNewProject(
  IN pName VARCHAR(255),
  IN pDescription TEXT,
  IN pCity VARCHAR(255),
  IN pCountry VARCHAR(255),
  IN pOutcomeDescription TEXT
)
BEGIN
  DECLARE newLocationID INT;
  DECLARE newProjectID INT;

  -- Insert location if it does not exist
  INSERT INTO Locations (City, Country)
  VALUES (pCity, pCountry)
  ON DUPLICATE KEY UPDATE LocationID = (SELECT LocationID FROM Locations WHERE City = pCity AND Country = pCountry);

  -- Get the location ID
  SET newLocationID = (SELECT LocationID FROM Locations WHERE City = pCity AND Country = pCountry);

  -- Insert new project
  INSERT INTO Projects (Name, Description, LocationID)
  VALUES (pName, pDescription, newLocationID);

  -- Get the project ID
  SET newProjectID = LAST_INSERT_ID();

  -- Insert outcome for the new project
  IF pOutcomeDescription IS NOT NULL THEN
    INSERT INTO Outcomes (ProjectID, OutcomeDescription)
    VALUES (newProjectID, pOutcomeDescription);
  END IF;
END//
DELIMITER ;

-- Call the stored procedure to add a new project
CALL AddNewProject('Project Delta', 'This is project delta', 'Rome', 'Italy', 'Outcome for project delta');
```
