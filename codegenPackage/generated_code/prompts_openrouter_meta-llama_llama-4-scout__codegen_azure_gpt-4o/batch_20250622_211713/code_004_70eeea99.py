"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Design a database schema to store information about professor positions, applicants, and selection results at IGEOG, and provide recommendations for suitable database management systems (DBMS).
Generated: DETERMINISTIC_70eeea9969328d3e
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for IGEOG Professor Positions, Applicants, and Selection Results

-- Table to store information about professor positions
CREATE TABLE ProfessorPositions (
    PositionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each position
    Title VARCHAR(255) NOT NULL,               -- Title of the position (e.g., "Assistant Professor")
    Department VARCHAR(255) NOT NULL,          -- Department offering the position
    Description TEXT,                          -- Detailed description of the position
    Requirements TEXT,                         -- Requirements for the position
    PostedDate DATE NOT NULL,                  -- Date the position was posted
    ClosingDate DATE NOT NULL                  -- Deadline for applications
);

-- Table to store information about applicants
CREATE TABLE Applicants (
    ApplicantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each applicant
    FirstName VARCHAR(255) NOT NULL,            -- Applicant's first name
    LastName VARCHAR(255) NOT NULL,             -- Applicant's last name
    Email VARCHAR(255) NOT NULL UNIQUE,         -- Applicant's email address
    PhoneNumber VARCHAR(20),                    -- Applicant's phone number
    Resume TEXT NOT NULL,                       -- Link or text of the applicant's resume
    CoverLetter TEXT,                           -- Link or text of the applicant's cover letter
    ApplicationDate DATE NOT NULL               -- Date the application was submitted
);

-- Table to store applications for professor positions
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    PositionID INT NOT NULL,                      -- Foreign key referencing ProfessorPositions
    ApplicantID INT NOT NULL,                     -- Foreign key referencing Applicants
    Status ENUM('Pending', 'Reviewed', 'Accepted', 'Rejected') DEFAULT 'Pending', -- Application status
    ReviewDate DATE,                              -- Date the application was reviewed
    FOREIGN KEY (PositionID) REFERENCES ProfessorPositions(PositionID) ON DELETE CASCADE,
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID) ON DELETE CASCADE
);

-- Table to store selection results
CREATE TABLE SelectionResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each result
    ApplicationID INT NOT NULL,              -- Foreign key referencing Applications
    Selected BOOLEAN NOT NULL,               -- Whether the applicant was selected (true/false)
    Notes TEXT,                              -- Additional notes about the selection decision
    DecisionDate DATE NOT NULL,              -- Date the decision was made
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID) ON DELETE CASCADE
);

-- Recommendations for DBMS:
-- 1. MySQL: Suitable for web applications, widely supported, and offers excellent performance for structured data.
-- 2. PostgreSQL: Ideal for complex queries, advanced features, and scalability.
-- 3. SQLite: Lightweight and easy to set up for smaller projects or prototyping.
-- 4. Microsoft SQL Server: Good for enterprise-level applications with integration into Microsoft ecosystems.
-- 5. Oracle Database: Suitable for large-scale, high-performance applications with advanced security features.
```
