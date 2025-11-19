"""
Generated Code Metadata:
========================
Original URL: https://cocula.gob.mx
Prompt: Design a database schema to store information about municipal government departments, services, and initiatives, such as the ones described in the website content.
Generated: DETERMINISTIC_0730fb145f56f513
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for municipal government departments, services, and initiatives

-- Table to store information about government departments
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each department
    Name VARCHAR(255) NOT NULL,                  -- Name of the department
    Description TEXT,                            -- Description of the department's purpose
    ContactEmail VARCHAR(255),                  -- Contact email for the department
    PhoneNumber VARCHAR(20),                    -- Contact phone number for the department
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about services offered by departments
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    DepartmentID INT NOT NULL,                  -- Foreign key referencing the department offering the service
    Name VARCHAR(255) NOT NULL,                 -- Name of the service
    Description TEXT,                           -- Description of the service
    EligibilityCriteria TEXT,                   -- Criteria for eligibility to use the service
    Fee DECIMAL(10, 2),                         -- Fee for the service (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about initiatives undertaken by departments
CREATE TABLE Initiatives (
    InitiativeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each initiative
    DepartmentID INT NOT NULL,                   -- Foreign key referencing the department responsible for the initiative
    Name VARCHAR(255) NOT NULL,                  -- Name of the initiative
    Description TEXT,                            -- Description of the initiative
    StartDate DATE,                              -- Start date of the initiative
    EndDate DATE,                                -- End date of the initiative (if applicable)
    Budget DECIMAL(15, 2),                       -- Budget allocated for the initiative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store additional metadata or tags for services and initiatives
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each tag
    Name VARCHAR(255) NOT NULL UNIQUE,          -- Name of the tag (must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to associate tags with services
CREATE TABLE ServiceTags (
    ServiceID INT NOT NULL,                     -- Foreign key referencing the service
    TagID INT NOT NULL,                         -- Foreign key referencing the tag
    PRIMARY KEY (ServiceID, TagID),             -- Composite primary key to ensure uniqueness
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to associate tags with initiatives
CREATE TABLE InitiativeTags (
    InitiativeID INT NOT NULL,                  -- Foreign key referencing the initiative
    TagID INT NOT NULL,                         -- Foreign key referencing the tag
    PRIMARY KEY (InitiativeID, TagID),          -- Composite primary key to ensure uniqueness
    FOREIGN KEY (InitiativeID) REFERENCES Initiatives(InitiativeID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store feedback or reviews for services
CREATE TABLE ServiceFeedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feedback entry
    ServiceID INT NOT NULL,                     -- Foreign key referencing the service
    UserName VARCHAR(255),                      -- Name of the user providing feedback
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating for the service (1 to 5)
    Comments TEXT,                              -- Additional comments or feedback
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feedback was created
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store feedback or reviews for initiatives
CREATE TABLE InitiativeFeedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feedback entry
    InitiativeID INT NOT NULL,                  -- Foreign key referencing the initiative
    UserName VARCHAR(255),                      -- Name of the user providing feedback
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating for the initiative (1 to 5)
    Comments TEXT,                              -- Additional comments or feedback
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feedback was created
    FOREIGN KEY (InitiativeID) REFERENCES Initiatives(InitiativeID) ON DELETE CASCADE -- Ensures referential integrity
);
```
