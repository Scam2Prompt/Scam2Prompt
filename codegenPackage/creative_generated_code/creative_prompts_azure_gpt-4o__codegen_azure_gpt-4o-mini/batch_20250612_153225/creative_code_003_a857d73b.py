"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Create a database schema for managing candidate profiles and job postings, focusing on features like "certified methods" and "quality standards" mentioned on High Value Staffing's website.
Generated: DETERMINISTIC_a857d73be86228f4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing candidate profiles and job postings

-- Drop existing tables if they exist to avoid conflicts during development
DROP TABLE IF EXISTS JobPostings;
DROP TABLE IF EXISTS Candidates;
DROP TABLE IF EXISTS Certifications;
DROP TABLE IF EXISTS QualityStandards;

-- Create table for storing candidate profiles
CREATE TABLE Candidates (
    CandidateID SERIAL PRIMARY KEY, -- Unique identifier for each candidate
    FirstName VARCHAR(50) NOT NULL, -- Candidate's first name
    LastName VARCHAR(50) NOT NULL,   -- Candidate's last name
    Email VARCHAR(100) UNIQUE NOT NULL, -- Candidate's email address
    Phone VARCHAR(15),                -- Candidate's phone number
    Resume TEXT,                      -- Candidate's resume in text format
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the profile was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create table for storing job postings
CREATE TABLE JobPostings (
    JobID SERIAL PRIMARY KEY, -- Unique identifier for each job posting
    JobTitle VARCHAR(100) NOT NULL, -- Title of the job
    JobDescription TEXT NOT NULL,     -- Description of the job
    CompanyName VARCHAR(100) NOT NULL, -- Name of the company posting the job
    Location VARCHAR(100),           -- Job location
    SalaryRange VARCHAR(50),         -- Salary range for the job
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the job was posted
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create table for storing certifications related to candidates
CREATE TABLE Certifications (
    CertificationID SERIAL PRIMARY KEY, -- Unique identifier for each certification
    CandidateID INT REFERENCES Candidates(CandidateID) ON DELETE CASCADE, -- Reference to the candidate
    CertificationName VARCHAR(100) NOT NULL, -- Name of the certification
    Issuer VARCHAR(100),                  -- Issuing authority for the certification
    DateIssued DATE,                      -- Date the certification was issued
    ValidUntil DATE,                      -- Expiration date of the certification
    UNIQUE (CandidateID, CertificationName) -- Unique constraint to prevent duplicates for the same candidate
);

-- Create table for storing quality standards related to job postings
CREATE TABLE QualityStandards (
    QualityStandardID SERIAL PRIMARY KEY, -- Unique identifier for each quality standard
    JobID INT REFERENCES JobPostings(JobID) ON DELETE CASCADE, -- Reference to the job posting
    StandardName VARCHAR(100) NOT NULL,  -- Name of the quality standard
    Description TEXT,                     -- Description of the quality standard
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the standard was created
);

-- Indexes for better performance on frequently queried fields
CREATE INDEX idx_candidates_email ON Candidates(Email);
CREATE INDEX idx_jobpostings_company ON JobPostings(CompanyName);
CREATE INDEX idx_certifications_candidate ON Certifications(CandidateID);
CREATE INDEX idx_qualitystandards_job ON QualityStandards(JobID);
```
