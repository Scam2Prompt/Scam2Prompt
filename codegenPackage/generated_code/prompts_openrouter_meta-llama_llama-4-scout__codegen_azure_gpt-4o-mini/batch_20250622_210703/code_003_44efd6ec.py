"""
Generated Code Metadata:
========================
Original URL: https://accuratehire.co.in
Prompt: "Design a database schema to store information about job seekers, job openings, and recruitment services, inspired by Accurate Hire's approach to connecting people with opportunities."
Generated: DETERMINISTIC_44efd6ecd7c667f1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about job seekers, job openings, and recruitment services

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS JobSeekers;
DROP TABLE IF EXISTS JobOpenings;
DROP TABLE IF EXISTS RecruitmentServices;
DROP TABLE IF EXISTS Applications;

-- Table to store information about job seekers
CREATE TABLE JobSeekers (
    JobSeekerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each job seeker
    FirstName VARCHAR(50) NOT NULL,            -- First name of the job seeker
    LastName VARCHAR(50) NOT NULL,             -- Last name of the job seeker
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address of the job seeker (must be unique)
    PhoneNumber VARCHAR(15),                    -- Phone number of the job seeker
    Resume TEXT,                                -- Resume content of the job seeker
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about job openings
CREATE TABLE JobOpenings (
    JobOpeningID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each job opening
    Title VARCHAR(100) NOT NULL,                 -- Title of the job opening
    Description TEXT NOT NULL,                    -- Description of the job opening
    CompanyName VARCHAR(100) NOT NULL,           -- Name of the company offering the job
    Location VARCHAR(100),                        -- Location of the job
    SalaryRange VARCHAR(50),                      -- Salary range for the job
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about recruitment services
CREATE TABLE RecruitmentServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each recruitment service
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the recruitment service
    ContactEmail VARCHAR(100) UNIQUE NOT NULL,    -- Contact email for the recruitment service
    PhoneNumber VARCHAR(15),                       -- Phone number for the recruitment service
    Website VARCHAR(100),                          -- Website URL for the recruitment service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store applications made by job seekers to job openings
CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each application
    JobSeekerID INT NOT NULL,                     -- Foreign key referencing JobSeekers
    JobOpeningID INT NOT NULL,                    -- Foreign key referencing JobOpenings
    ApplicationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of application
    Status ENUM('Applied', 'Interview', 'Offer', 'Rejected') DEFAULT 'Applied', -- Status of the application
    FOREIGN KEY (JobSeekerID) REFERENCES JobSeekers(JobSeekerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (JobOpeningID) REFERENCES JobOpenings(JobOpeningID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_jobseeker_email ON JobSeekers(Email);
CREATE INDEX idx_jobopening_title ON JobOpenings(Title);
CREATE INDEX idx_application_status ON Applications(Status);
```
