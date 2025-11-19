"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Design a basic database schema for storing client information, credits, and educational programs for a cooperative like Cooprometa.
Generated: DETERMINISTIC_72a2c718827b14fb
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Cooprometa

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store credit information
CREATE TABLE Credits (
    CreditID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each credit record
    ClientID INT NOT NULL,                   -- Foreign key linking to the Clients table
    Amount DECIMAL(10, 2) NOT NULL,          -- Credit amount
    InterestRate DECIMAL(5, 2) NOT NULL,     -- Interest rate for the credit
    StartDate DATE NOT NULL,                 -- Start date of the credit
    EndDate DATE NOT NULL,                   -- End date of the credit
    Status ENUM('Active', 'Closed', 'Defaulted') DEFAULT 'Active', -- Status of the credit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the credit was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store educational programs
CREATE TABLE EducationalPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the educational program
    Description TEXT,                         -- Description of the program
    StartDate DATE NOT NULL,                  -- Start date of the program
    EndDate DATE NOT NULL,                    -- End date of the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store client enrollments in educational programs
CREATE TABLE ProgramEnrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    ClientID INT NOT NULL,                       -- Foreign key linking to the Clients table
    ProgramID INT NOT NULL,                      -- Foreign key linking to the EducationalPrograms table
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    CompletionStatus ENUM('Enrolled', 'Completed', 'Dropped') DEFAULT 'Enrolled', -- Status of enrollment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the enrollment was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_credit_client ON Credits(ClientID); -- Index for quick lookup of credits by client
CREATE INDEX idx_enrollment_client ON ProgramEnrollments(ClientID); -- Index for quick lookup of enrollments by client
CREATE INDEX idx_enrollment_program ON ProgramEnrollments(ProgramID); -- Index for quick lookup of enrollments by program
```
