"""
Generated Code Metadata:
========================
Original URL: https://jlelectricista.com
Prompt: Generate a sample database schema for storing information about electrical services, including client details, service types (residential/commercial), and job status.
Generated: DETERMINISTIC_20979e0920225bc5
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about electrical services

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    TypeName VARCHAR(50) NOT NULL,                -- Name of the service type (e.g., Residential, Commercial)
    Description TEXT,                             -- Description of the service type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service type record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store job details
CREATE TABLE Jobs (
    JobID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each job
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients table
    ServiceTypeID INT NOT NULL,                  -- Foreign key referencing ServiceTypes table
    JobStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Status of the job
    ScheduledDate DATE NOT NULL,                 -- Date when the job is scheduled
    CompletionDate DATE,                         -- Date when the job was completed (nullable)
    Notes TEXT,                                  -- Additional notes about the job
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the job record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE SET NULL -- Set NULL if service type is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_job_status ON Jobs(JobStatus);  -- Index for quick lookup by job status
CREATE INDEX idx_scheduled_date ON Jobs(ScheduledDate); -- Index for quick lookup by scheduled date
```
