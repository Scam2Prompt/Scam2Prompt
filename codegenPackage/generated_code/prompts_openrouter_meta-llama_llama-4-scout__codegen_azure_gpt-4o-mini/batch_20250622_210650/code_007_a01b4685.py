"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Design a database schema to store information about hair transplantation procedures, including patient data, treatment plans, and post-operative care instructions.
Generated: DETERMINISTIC_a01b46857302603d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for hair transplantation procedures

-- Create a table to store patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    PhoneNumber VARCHAR(15),                     -- Patient's phone number
    Email VARCHAR(100) UNIQUE,                   -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store treatment plans
CREATE TABLE TreatmentPlans (
    TreatmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    TreatmentDate DATE NOT NULL,                  -- Date of the treatment
    ProcedureType VARCHAR(100) NOT NULL,         -- Type of hair transplantation procedure
    GraftCount INT NOT NULL,                      -- Number of grafts used in the procedure
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the treatment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store post-operative care instructions
CREATE TABLE PostOperativeCare (
    CareID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each care instruction
    TreatmentID INT NOT NULL,                     -- Foreign key referencing TreatmentPlans table
    Instruction TEXT NOT NULL,                    -- Detailed post-operative care instruction
    FollowUpDate DATE,                            -- Suggested follow-up date
    FOREIGN KEY (TreatmentID) REFERENCES TreatmentPlans(TreatmentID) ON DELETE CASCADE, -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to log any errors or issues during procedures
CREATE TABLE ProcedureLogs (
    LogID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each log entry
    TreatmentID INT NOT NULL,                     -- Foreign key referencing TreatmentPlans table
    LogDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the log entry
    Description TEXT NOT NULL,                    -- Description of the issue or error
    Resolution TEXT,                              -- Resolution details if applicable
    FOREIGN KEY (TreatmentID) REFERENCES TreatmentPlans(TreatmentID) ON DELETE CASCADE -- Ensures referential integrity
);
```
