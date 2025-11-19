"""
Generated Code Metadata:
========================
Original URL: https://job4chat.crediblejobs.in
Prompt: Design a database schema to store job applicant information, including contact details, education, and work experience, for a BPO company like TTEC.
Generated: DETERMINISTIC_7855f99bfc3e6c38
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing job applicant information for a BPO company

-- Table to store applicant's basic information
CREATE TABLE Applicants (
    ApplicantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each applicant
    FirstName VARCHAR(50) NOT NULL,             -- Applicant's first name
    LastName VARCHAR(50) NOT NULL,              -- Applicant's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Applicant's email address (must be unique)
    PhoneNumber VARCHAR(15) NOT NULL,           -- Applicant's phone number
    DateOfBirth DATE NOT NULL,                  -- Applicant's date of birth
    Address TEXT,                               -- Applicant's address
    City VARCHAR(50),                           -- City of residence
    State VARCHAR(50),                          -- State of residence
    Country VARCHAR(50),                        -- Country of residence
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store applicant's education details
CREATE TABLE Education (
    EducationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each education record
    ApplicantID INT NOT NULL,                   -- Foreign key referencing Applicants table
    InstitutionName VARCHAR(100) NOT NULL,      -- Name of the educational institution
    Degree VARCHAR(50) NOT NULL,                -- Degree obtained (e.g., Bachelor's, Master's)
    FieldOfStudy VARCHAR(50),                   -- Field of study (e.g., Computer Science, Business)
    StartDate DATE NOT NULL,                    -- Start date of the education
    EndDate DATE,                               -- End date of the education (NULL if ongoing)
    Grade VARCHAR(10),                          -- Grade or GPA
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store applicant's work experience
CREATE TABLE WorkExperience (
    ExperienceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each work experience record
    ApplicantID INT NOT NULL,                    -- Foreign key referencing Applicants table
    CompanyName VARCHAR(100) NOT NULL,           -- Name of the company
    JobTitle VARCHAR(50) NOT NULL,               -- Job title held by the applicant
    StartDate DATE NOT NULL,                     -- Start date of the job
    EndDate DATE,                                -- End date of the job (NULL if ongoing)
    Responsibilities TEXT,                       -- Description of job responsibilities
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for faster lookups
CREATE INDEX idx_applicant_email ON Applicants (Email);
CREATE INDEX idx_education_applicant ON Education (ApplicantID);
CREATE INDEX idx_work_experience_applicant ON WorkExperience (ApplicantID);
```
