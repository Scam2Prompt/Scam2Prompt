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
-- Database Schema for Recruitment Services

-- Table to store information about job seekers
CREATE TABLE JobSeekers (
    JobSeekerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each job seeker
    FirstName VARCHAR(50) NOT NULL,             -- First name of the job seeker
    LastName VARCHAR(50) NOT NULL,              -- Last name of the job seeker
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Email address of the job seeker
    PhoneNumber VARCHAR(15),                    -- Contact number of the job seeker
    Resume TEXT,                                -- Resume content or link to the resume
    Skills TEXT,                                -- Comma-separated list of skills
    ExperienceYears INT,                        -- Number of years of experience
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the record was created
);

-- Table to store information about job openings
CREATE TABLE JobOpenings (
    JobOpeningID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each job opening
    JobTitle VARCHAR(100) NOT NULL,              -- Title of the job
    CompanyName VARCHAR(100) NOT NULL,           -- Name of the company offering the job
    Location VARCHAR(100),                       -- Location of the job
    JobDescription TEXT NOT NULL,                -- Detailed description of the job
    RequiredSkills TEXT,                         -- Comma-separated list of required skills
    SalaryRange VARCHAR(50),                     -- Salary range for the job
    PostedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the job was posted
);

-- Table to store information about recruitment services
CREATE TABLE RecruitmentServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each recruitment service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the recruitment service
    Description TEXT,                            -- Description of the service
    ContactEmail VARCHAR(100) NOT NULL,          -- Contact email for the service
    ContactPhone VARCHAR(15),                    -- Contact phone number for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the record was created
);

-- Table to store applications made by job seekers to job openings
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    JobSeekerID INT NOT NULL,                      -- Foreign key referencing JobSeekers table
    JobOpeningID INT NOT NULL,                     -- Foreign key referencing JobOpenings table
    ApplicationStatus ENUM('Pending', 'Reviewed', 'Accepted', 'Rejected') DEFAULT 'Pending', -- Status of the application
    AppliedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the application was made
    FOREIGN KEY (JobSeekerID) REFERENCES JobSeekers(JobSeekerID) ON DELETE CASCADE,
    FOREIGN KEY (JobOpeningID) REFERENCES JobOpenings(JobOpeningID) ON DELETE CASCADE
);

-- Table to store relationships between recruitment services and job openings
CREATE TABLE ServiceJobOpeningLinks (
    LinkID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each link
    ServiceID INT NOT NULL,                       -- Foreign key referencing RecruitmentServices table
    JobOpeningID INT NOT NULL,                    -- Foreign key referencing JobOpenings table
    FOREIGN KEY (ServiceID) REFERENCES RecruitmentServices(ServiceID) ON DELETE CASCADE,
    FOREIGN KEY (JobOpeningID) REFERENCES JobOpenings(JobOpeningID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_jobseekers_email ON JobSeekers(Email); -- Index for quick lookup of job seekers by email
CREATE INDEX idx_jobopenings_title ON JobOpenings(JobTitle); -- Index for quick lookup of job openings by title
CREATE INDEX idx_applications_status ON Applications(ApplicationStatus); -- Index for filtering applications by status
```
