"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Create a database schema for managing client reviews and project details, including fields for mortar type, tuckpointing details, and remedial techniques, inspired by Premier Pointing's services.
Generated: DETERMINISTIC_7a1403ddafc763ba
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing client reviews and project details

-- Create a database named 'ClientReviewsDB'
CREATE DATABASE ClientReviewsDB;

-- Use the created database
USE ClientReviewsDB;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT,
    ProjectDescription TEXT NOT NULL,
    MortarType VARCHAR(50),
    TuckpointingDetails TEXT,
    RemedialTechniques TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store client reviews for projects
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT,
    ReviewText TEXT NOT NULL,
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Insert sample data into the Clients table
INSERT INTO Clients (Name, Email, Phone) VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890'),
('Jane Smith', 'jane.smith@example.com', '098-765-4321');

-- Insert sample data into the Projects table
INSERT INTO Projects (ClientID, ProjectDescription, MortarType, TuckpointingDetails, RemedialTechniques) VALUES 
(1, 'Repairing the facade of the building', 'Type S Mortar', 'Repointing of the entire facade', 'Sealant application'),
(2, 'Restoration of historic brickwork', 'Type N Mortar', 'Selective tuckpointing required', 'Waterproofing treatment');

-- Insert sample data into the Reviews table
INSERT INTO Reviews (ProjectID, ReviewText, Rating) VALUES 
(1, 'Excellent work on the facade!', 5),
(2, 'The restoration of the brickwork was satisfactory.', 4);

-- Query to retrieve all projects with client details
SELECT 
    p.ProjectID,
    c.Name AS ClientName,
    p.ProjectDescription,
    p.MortarType,
    p.TuckpointingDetails,
    p.RemedialTechniques,
    r.ReviewText,
    r.Rating
FROM 
    Projects p
JOIN 
    Clients c ON p.ClientID = c.ClientID
LEFT JOIN 
    Reviews r ON p.ProjectID = r.ProjectID
ORDER BY 
    p.CreatedAt DESC;
```
