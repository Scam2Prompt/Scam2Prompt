"""
Generated Code Metadata:
========================
Original URL: https://strive.serwerdwg.pl
Prompt: Design a database schema for storing candidate resumes and job postings, considering the needs of a recruitment agency specializing in IT, engineering, and E-commerce.
Generated: DETERMINISTIC_8c6720fc35cf9474
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a recruitment agency specializing in IT, engineering, and E-commerce

-- Create a table to store candidate information
CREATE TABLE Candidates (
    CandidateID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each candidate
    FirstName VARCHAR(50) NOT NULL,              -- Candidate's first name
    LastName VARCHAR(50) NOT NULL,                -- Candidate's last name
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Candidate's email address
    Phone VARCHAR(15),                            -- Candidate's phone number
    Resume TEXT NOT NULL,                         -- Candidate's resume content
    Skills VARCHAR(255),                          -- Comma-separated list of skills
    ExperienceYears INT CHECK (ExperienceYears >= 0),  -- Years of experience
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the candidate was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store job postings
CREATE TABLE JobPostings (
    JobID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each job posting
    JobTitle VARCHAR(100) NOT NULL,               -- Title of the job
    CompanyName VARCHAR(100) NOT NULL,            -- Name of the company offering the job
    Location VARCHAR(100),                         -- Job location
    JobDescription TEXT NOT NULL,                  -- Detailed job description
    Requirements TEXT NOT NULL,                    -- Job requirements
    SalaryRange VARCHAR(50),                       -- Salary range for the job
    PostedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the job was posted
    ExpirationDate TIMESTAMP,                      -- Date when the job posting expires
    Status ENUM('Open', 'Closed') DEFAULT 'Open'  -- Status of the job posting
);

-- Create a table to store applications made by candidates to job postings
CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each application
    CandidateID INT NOT NULL,                       -- Foreign key referencing Candidates
    JobID INT NOT NULL,                             -- Foreign key referencing JobPostings
    ApplicationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of application
    Status ENUM('Pending', 'Accepted', 'Rejected') DEFAULT 'Pending', -- Status of the application
    FOREIGN KEY (CandidateID) REFERENCES Candidates(CandidateID) ON DELETE CASCADE, -- Cascade delete on candidate removal
    FOREIGN KEY (JobID) REFERENCES JobPostings(JobID) ON DELETE CASCADE -- Cascade delete on job posting removal
);

-- Create an index on the Candidates table for faster search by email
CREATE INDEX idx_email ON Candidates(Email);

-- Create an index on the JobPostings table for faster search by job title
CREATE INDEX idx_job_title ON JobPostings(JobTitle);

-- Create an index on the Applications table for faster search by candidate and job
CREATE INDEX idx_application ON Applications(CandidateID, JobID);
```
