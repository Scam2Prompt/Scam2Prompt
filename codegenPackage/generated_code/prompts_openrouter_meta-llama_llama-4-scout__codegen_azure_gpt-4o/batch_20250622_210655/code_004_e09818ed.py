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
-- Database schema for storing candidate and company information
-- This schema is designed to support jobONE's recruitment approach, including fields for personality, expectations, and values.

-- Table to store candidate information
CREATE TABLE Candidates (
    CandidateID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each candidate
    FirstName VARCHAR(50) NOT NULL,             -- Candidate's first name
    LastName VARCHAR(50) NOT NULL,              -- Candidate's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Candidate's email address (must be unique)
    PhoneNumber VARCHAR(15),                    -- Candidate's phone number
    Personality TEXT,                           -- Candidate's personality traits (e.g., Myers-Briggs type)
    Expectations TEXT,                          -- Candidate's job expectations (e.g., salary, work environment)
    Values TEXT,                                -- Candidate's personal values (e.g., teamwork, innovation)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the candidate record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store company information
CREATE TABLE Companies (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each company
    CompanyName VARCHAR(100) NOT NULL,          -- Name of the company
    Industry VARCHAR(50),                       -- Industry the company operates in
    Location VARCHAR(100),                      -- Company's location
    Values TEXT,                                -- Company's core values (e.g., sustainability, diversity)
    Expectations TEXT,                          -- Company's expectations from candidates (e.g., skills, experience)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the company record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store job postings
CREATE TABLE JobPostings (
    JobID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each job posting
    CompanyID INT NOT NULL,                     -- Foreign key referencing Companies table
    JobTitle VARCHAR(100) NOT NULL,             -- Title of the job position
    JobDescription TEXT NOT NULL,               -- Detailed description of the job
    Requirements TEXT,                          -- Requirements for the job (e.g., skills, qualifications)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the job posting was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store applications submitted by candidates
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    CandidateID INT NOT NULL,                     -- Foreign key referencing Candidates table
    JobID INT NOT NULL,                           -- Foreign key referencing JobPostings table
    ApplicationStatus ENUM('Pending', 'Reviewed', 'Accepted', 'Rejected') DEFAULT 'Pending', -- Status of the application
    SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the application was submitted
    FOREIGN KEY (CandidateID) REFERENCES Candidates(CandidateID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (JobID) REFERENCES JobPostings(JobID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_candidate_email ON Candidates(Email); -- Index for quick lookup of candidates by email
CREATE INDEX idx_company_name ON Companies(CompanyName); -- Index for quick lookup of companies by name
CREATE INDEX idx_job_title ON JobPostings(JobTitle); -- Index for quick lookup of job postings by title
```
