"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Design a basic database schema for storing candidate and company information, including fields for personality, expectations, and values, based on jobONE's recruitment approach.
Generated: DETERMINISTIC_e09818edd39acfb4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a basic database schema for storing candidate and company information

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Candidates;
DROP TABLE IF EXISTS Companies;

-- Create a table to store candidate information
CREATE TABLE Candidates (
    CandidateID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each candidate
    FirstName VARCHAR(50) NOT NULL,              -- Candidate's first name
    LastName VARCHAR(50) NOT NULL,                -- Candidate's last name
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Candidate's email address (must be unique)
    Phone VARCHAR(15),                            -- Candidate's phone number
    Personality VARCHAR(255),                     -- Candidate's personality traits
    Expectations TEXT,                            -- Candidate's job expectations
    Values TEXT,                                  -- Candidate's personal values
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to store company information
CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each company
    CompanyName VARCHAR(100) NOT NULL,           -- Name of the company
    Industry VARCHAR(50),                         -- Industry in which the company operates
    Location VARCHAR(100),                        -- Location of the company
    CompanyValues TEXT,                           -- Core values of the company
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to link candidates to companies (many-to-many relationship)
CREATE TABLE CandidateCompany (
    CandidateID INT,                              -- Foreign key referencing Candidates
    CompanyID INT,                                -- Foreign key referencing Companies
    PRIMARY KEY (CandidateID, CompanyID),        -- Composite primary key
    FOREIGN KEY (CandidateID) REFERENCES Candidates(CandidateID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Insert sample data into Candidates table
INSERT INTO Candidates (FirstName, LastName, Email, Phone, Personality, Expectations, Values)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 'Outgoing, Team Player', 'Looking for growth opportunities', 'Integrity, Innovation'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321', 'Analytical, Detail-oriented', 'Work-life balance', 'Sustainability, Collaboration');

-- Insert sample data into Companies table
INSERT INTO Companies (CompanyName, Industry, Location, CompanyValues)
VALUES 
('Tech Innovations', 'Technology', 'San Francisco, CA', 'Innovation, Excellence'),
('Green Solutions', 'Environmental', 'Austin, TX', 'Sustainability, Community');

-- Insert sample data into CandidateCompany table to establish relationships
INSERT INTO CandidateCompany (CandidateID, CompanyID)
VALUES 
(1, 1),  -- John Doe is linked to Tech Innovations
(2, 2);  -- Jane Smith is linked to Green Solutions
```
