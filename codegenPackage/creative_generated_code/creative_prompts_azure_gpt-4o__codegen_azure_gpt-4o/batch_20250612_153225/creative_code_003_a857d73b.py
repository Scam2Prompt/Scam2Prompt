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
-- Focusing on features like certified methods and quality standards

-- Create table for candidates
CREATE TABLE Candidates (
    CandidateID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each candidate
    FirstName VARCHAR(50) NOT NULL,              -- Candidate's first name
    LastName VARCHAR(50) NOT NULL,               -- Candidate's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Candidate's email (must be unique)
    PhoneNumber VARCHAR(15),                     -- Candidate's phone number
    CertificationMethods TEXT,                   -- Details of certified methods the candidate is familiar with
    QualityStandards TEXT,                       -- Details of quality standards the candidate adheres to
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the candidate profile is created
);

-- Create table for job postings
CREATE TABLE JobPostings (
    JobID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each job posting
    JobTitle VARCHAR(100) NOT NULL,              -- Title of the job position
    JobDescription TEXT NOT NULL,                -- Description of the job
    RequiredCertifications TEXT,                 -- Certifications required for the job
    QualityStandards TEXT,                       -- Quality standards expected for the job
    PostedBy VARCHAR(100) NOT NULL,              -- Name/contact of the person or organization posting the job
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the job posting is created
);

-- Create table for candidate-job applications
CREATE TABLE CandidateApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    CandidateID INT NOT NULL,                     -- Foreign key linking to Candidates table
    JobID INT NOT NULL,                           -- Foreign key linking to JobPostings table
    ApplicationStatus VARCHAR(50) DEFAULT 'Pending', -- Status of the application (Pending, Approved, Rejected)
    AppliedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the application is submitted
    FOREIGN KEY (CandidateID) REFERENCES Candidates(CandidateID) ON DELETE CASCADE, -- Cascade delete if candidate is removed
    FOREIGN KEY (JobID) REFERENCES JobPostings(JobID) ON DELETE CASCADE             -- Cascade delete if job posting is removed
);

-- Create indexes for efficient querying
CREATE INDEX idx_candidates_email ON Candidates(Email); -- Index for quick lookup of candidates by email
CREATE INDEX idx_jobpostings_title ON JobPostings(JobTitle); -- Index for quick lookup of job postings by title
CREATE INDEX idx_applications_status ON CandidateApplications(ApplicationStatus); -- Index for quick filtering by application status
```
