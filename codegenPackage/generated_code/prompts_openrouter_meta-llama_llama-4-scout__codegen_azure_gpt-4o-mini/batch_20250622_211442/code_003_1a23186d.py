"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Design a database schema to store information about job openings, employee benefits, and company culture for a furniture manufacturing company like Hanil Furniture Gallery.
Generated: DETERMINISTIC_1a23186dc65e305c
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a furniture manufacturing company
-- This schema includes tables for job openings, employee benefits, and company culture.

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS JobOpenings;
DROP TABLE IF EXISTS EmployeeBenefits;
DROP TABLE IF EXISTS CompanyCulture;

-- Table to store job openings
CREATE TABLE JobOpenings (
    JobID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each job opening
    JobTitle VARCHAR(255) NOT NULL, -- Title of the job
    JobDescription TEXT NOT NULL, -- Detailed description of the job
    DatePosted DATE NOT NULL, -- Date when the job was posted
    ApplicationDeadline DATE, -- Deadline for applications
    Salary DECIMAL(10, 2), -- Salary for the position
    Location VARCHAR(255), -- Job location
    EmploymentType ENUM('Full-time', 'Part-time', 'Contract', 'Internship') NOT NULL, -- Type of employment
    Requirements TEXT, -- Job requirements
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store employee benefits
CREATE TABLE EmployeeBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each benefit
    BenefitName VARCHAR(255) NOT NULL, -- Name of the benefit
    Description TEXT NOT NULL, -- Description of the benefit
    EligibilityCriteria TEXT, -- Criteria for eligibility
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about company culture
CREATE TABLE CompanyCulture (
    CultureID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each culture entry
    CultureAspect VARCHAR(255) NOT NULL, -- Aspect of the company culture
    Description TEXT NOT NULL, -- Description of the culture aspect
    Values TEXT, -- Core values associated with the culture
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Example of inserting data into JobOpenings
INSERT INTO JobOpenings (JobTitle, JobDescription, DatePosted, ApplicationDeadline, Salary, Location, EmploymentType, Requirements)
VALUES 
('Furniture Designer', 'Design and create furniture pieces.', '2023-10-01', '2023-11-01', 60000.00, 'Seoul', 'Full-time', 'Bachelor\'s degree in design or related field.');

-- Example of inserting data into EmployeeBenefits
INSERT INTO EmployeeBenefits (BenefitName, Description, EligibilityCriteria)
VALUES 
('Health Insurance', 'Comprehensive health insurance plan covering medical, dental, and vision.', 'All full-time employees after 3 months of employment.');

-- Example of inserting data into CompanyCulture
INSERT INTO CompanyCulture (CultureAspect, Description, Values)
VALUES 
('Innovation', 'We encourage creativity and new ideas in our designs.', 'Creativity, Collaboration, Excellence');

-- Note: Ensure to handle errors appropriately in your application code when interacting with this database schema.
```
