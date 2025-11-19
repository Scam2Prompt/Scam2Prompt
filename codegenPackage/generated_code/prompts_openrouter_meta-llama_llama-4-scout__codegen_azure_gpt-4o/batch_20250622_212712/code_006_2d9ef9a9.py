"""
Generated Code Metadata:
========================
Original URL: https://nassauccw.com
Prompt: Design a database schema to store information about CCW permit applicants and their application status, inspired by the services offered by Trigon Tactics for managing the application process.
Generated: DETERMINISTIC_2d9ef9a9f8466020
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about CCW permit applicants and their application status

-- Table to store applicant information
CREATE TABLE Applicants (
    ApplicantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each applicant
    FirstName VARCHAR(50) NOT NULL,            -- Applicant's first name
    LastName VARCHAR(50) NOT NULL,             -- Applicant's last name
    DateOfBirth DATE NOT NULL,                 -- Applicant's date of birth
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Applicant's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Applicant's phone number
    Address TEXT NOT NULL,                     -- Applicant's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store application details
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    ApplicantID INT NOT NULL,                     -- Foreign key linking to the Applicants table
    ApplicationDate DATE NOT NULL,                -- Date the application was submitted
    Status ENUM('Pending', 'Approved', 'Rejected', 'Under Review') NOT NULL DEFAULT 'Pending', -- Application status
    Notes TEXT,                                   -- Additional notes or comments about the application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID) ON DELETE CASCADE -- Cascade delete if applicant is removed
);

-- Table to store application status history
CREATE TABLE ApplicationStatusHistory (
    StatusHistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each status change record
    ApplicationID INT NOT NULL,                     -- Foreign key linking to the Applications table
    Status ENUM('Pending', 'Approved', 'Rejected', 'Under Review') NOT NULL, -- Status at the time of the record
    ChangeDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the status change
    ChangedBy VARCHAR(100),                         -- Name or identifier of the person who changed the status
    Notes TEXT,                                     -- Additional notes about the status change
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID) ON DELETE CASCADE -- Cascade delete if application is removed
);

-- Table to store system users (e.g., administrators or reviewers)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for secure storage
    Role ENUM('Admin', 'Reviewer') NOT NULL, -- Role of the user in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Indexes for optimizing queries
CREATE INDEX idx_applicant_email ON Applicants(Email); -- Index for quick lookup by email
CREATE INDEX idx_application_status ON Applications(Status); -- Index for quick lookup by status
CREATE INDEX idx_status_history_date ON ApplicationStatusHistory(ChangeDate); -- Index for quick lookup by change date
```
