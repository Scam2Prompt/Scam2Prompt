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

-- Table to store candidate information
CREATE TABLE Candidates (
    CandidateID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each candidate
    FirstName VARCHAR(50) NOT NULL,             -- Candidate's first name
    LastName VARCHAR(50) NOT NULL,              -- Candidate's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Candidate's email address (must be unique)
    PhoneNumber VARCHAR(15),                    -- Candidate's phone number
    LinkedInProfile VARCHAR(255),               -- URL to candidate's LinkedIn profile
    PortfolioURL VARCHAR(255),                  -- URL to candidate's portfolio
    Resume TEXT NOT NULL,                       -- Candidate's resume (stored as plain text or JSON)
    Skills JSON NOT NULL,                       -- Candidate's skills (stored as JSON array)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the candidate record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store job postings
CREATE TABLE JobPostings (
    JobID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each job posting
    Title VARCHAR(100) NOT NULL,                -- Job title
    Description TEXT NOT NULL,                  -- Detailed job description
    Requirements JSON NOT NULL,                 -- Job requirements (stored as JSON array)
    Location VARCHAR(100),                      -- Job location
    EmploymentType ENUM('Full-Time', 'Part-Time', 'Contract', 'Internship') NOT NULL, -- Type of employment
    Industry ENUM('IT', 'Engineering', 'E-commerce') NOT NULL, -- Industry category
    SalaryRange VARCHAR(50),                    -- Salary range for the job
    PostedBy VARCHAR(100) NOT NULL,             -- Name of the recruiter or company posting the job
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the job posting was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store applications submitted by candidates for job postings
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    CandidateID INT NOT NULL,                     -- Foreign key referencing Candidates table
    JobID INT NOT NULL,                           -- Foreign key referencing JobPostings table
    CoverLetter TEXT,                             -- Cover letter submitted by the candidate
    ApplicationStatus ENUM('Pending', 'Reviewed', 'Accepted', 'Rejected') DEFAULT 'Pending', -- Status of the application
    AppliedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the application was submitted
    FOREIGN KEY (CandidateID) REFERENCES Candidates(CandidateID) ON DELETE CASCADE, -- Cascade delete if candidate is removed
    FOREIGN KEY (JobID) REFERENCES JobPostings(JobID) ON DELETE CASCADE -- Cascade delete if job posting is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_candidate_skills ON Candidates(Skills); -- Index for searching candidates by skills
CREATE INDEX idx_job_industry ON JobPostings(Industry);  -- Index for filtering job postings by industry
CREATE INDEX idx_application_status ON Applications(ApplicationStatus); -- Index for filtering applications by status
```
