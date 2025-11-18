"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Develop a database schema for managing vocational education certifications, including fields for program type, completion status, and issuing authority, based on the AVEA certificate system.
Generated: DETERMINISTIC_2eb8e53732903eb5
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Vocational Education Certifications
-- This schema is designed to store information about certifications
-- based on the AVEA certificate system.

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address (unique)
    PhoneNumber VARCHAR(15)                   -- Contact phone number
);

-- Table to store information about certification programs
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the certification program
    ProgramType ENUM('Technical', 'Business', 'Healthcare', 'Education', 'Other') NOT NULL, -- Type of program
    DurationMonths INT NOT NULL,              -- Duration of the program in months
    Description TEXT                          -- Detailed description of the program
);

-- Table to store information about issuing authorities
CREATE TABLE IssuingAuthorities (
    AuthorityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each issuing authority
    AuthorityName VARCHAR(100) NOT NULL,        -- Name of the issuing authority
    ContactEmail VARCHAR(100) UNIQUE NOT NULL,  -- Contact email
    ContactPhone VARCHAR(15),                   -- Contact phone number
    Address TEXT                                -- Physical address
);

-- Table to record certifications issued to students
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    StudentID INT NOT NULL,                         -- Foreign key referencing Students table
    ProgramID INT NOT NULL,                         -- Foreign key referencing Programs table
    AuthorityID INT NOT NULL,                       -- Foreign key referencing IssuingAuthorities table
    CompletionStatus ENUM('Completed', 'In Progress', 'Not Started', 'Failed') NOT NULL, -- Status of completion
    IssueDate DATE,                                 -- Date certification was issued
    ExpiryDate DATE,                                -- Expiry date for the certification, if applicable
    CertificateNumber VARCHAR(50) UNIQUE NOT NULL, -- Unique certificate number
    CONSTRAINT FK_Student FOREIGN KEY (StudentID)
        REFERENCES Students(StudentID)
        ON DELETE CASCADE,                         -- Delete certification if student is removed
    CONSTRAINT FK_Program FOREIGN KEY (ProgramID)
        REFERENCES Programs(ProgramID)
        ON DELETE CASCADE,                         -- Delete certification if program is removed
    CONSTRAINT FK_Authority FOREIGN KEY (AuthorityID)
        REFERENCES IssuingAuthorities(AuthorityID)
        ON DELETE CASCADE                          -- Delete certification if authority is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_students_email ON Students (Email); -- Index on email for faster lookups
CREATE INDEX idx_certifications_certificate_number ON Certifications (CertificateNumber); -- Index on certificate number
```
