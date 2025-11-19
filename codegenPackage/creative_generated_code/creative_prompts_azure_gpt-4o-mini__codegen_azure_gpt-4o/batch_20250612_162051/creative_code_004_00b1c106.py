"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cefor.org.br
Prompt: Design a database schema for managing records of children and adolescents served by CEFOR, including their situations and the services they receive.
Generated: DETERMINISTIC_00b1c106d2f1ac76
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing records of children and adolescents served by CEFOR

-- Table to store information about children and adolescents
CREATE TABLE Persons (
    PersonID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each individual
    FirstName VARCHAR(50) NOT NULL,          -- First name
    LastName VARCHAR(50) NOT NULL,           -- Last name
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender
    DateOfBirth DATE NOT NULL,               -- Date of birth
    ContactInfo TEXT,                        -- Contact information such as phone, email, etc.
    Address TEXT,                            -- Home address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update timestamp
);

-- Table to store information about the situations faced by children and adolescents
CREATE TABLE Situations (
    SituationID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each situation
    PersonID INT NOT NULL,                         -- Foreign key linking to Persons table
    Description TEXT NOT NULL,                     -- Detailed description of the situation
    ReportedDate DATE NOT NULL,                    -- Date the situation was reported
    ResolvedDate DATE,                             -- Date the situation was resolved (optional)
    Status ENUM('Active', 'Resolved') DEFAULT 'Active', -- Current status of the situation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update timestamp
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE -- Cascade delete if the person is removed
);

-- Table to store information about the services provided to children and adolescents
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,             -- Name of the service
    Description TEXT,                              -- Detailed description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
);

-- Table to store records of services provided to specific individuals for specific situations
CREATE TABLE PersonServices (
    PersonServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the record
    PersonID INT NOT NULL,                          -- Foreign key linking to Persons table
    SituationID INT NOT NULL,                       -- Foreign key linking to Situations table
    ServiceID INT NOT NULL,                         -- Foreign key linking to Services table
    ProvidedDate DATE NOT NULL,                     -- Date the service was provided
    Notes TEXT,                                     -- Additional notes or observations
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update timestamp
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, -- Cascade delete if the person is removed
    FOREIGN KEY (SituationID) REFERENCES Situations(SituationID) ON DELETE CASCADE, -- Cascade delete if the situation is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if the service is removed
);

-- Index for optimizing queries on frequently accessed columns
CREATE INDEX idx_PersonID ON Persons(PersonID);
CREATE INDEX idx_SituationID ON Situations(SituationID);
CREATE INDEX idx_ServiceID ON Services(ServiceID);
CREATE INDEX idx_PersonServiceID ON PersonServices(PersonServiceID);

-- Error handling is implicitly managed by constraints such as NOT NULL, ENUMs, and CASCADE.
-- Additional validation should be handled at the application level.
```
