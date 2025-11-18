"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7054company.github.io
Prompt: Develop a database schema in SQL to track consulting, development, and support services for a company similar to 7054Company.
Generated: DETERMINISTIC_6a963d16bb53debe
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema to track consulting, development, and support services

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    Phone VARCHAR(15),                       -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Name of the service (e.g., Consulting, Development, Support)
    Description TEXT,                         -- Detailed description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each project
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    Name VARCHAR(255) NOT NULL,                 -- Name of the project
    Description TEXT,                           -- Detailed description of the project
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project (nullable if ongoing)
    Status ENUM('Active', 'Completed', 'On Hold') DEFAULT 'Active', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Handle client deletion
);

-- Create a table to link services to projects
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects table
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services table
    Hours INT NOT NULL,                              -- Number of hours dedicated to this service for the project
    Rate DECIMAL(10, 2) NOT NULL,                    -- Hourly rate for the service
    TotalCost AS (Hours * Rate) PERSISTENT,          -- Total cost calculated from hours and rate
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Handle project deletion
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Handle service deletion
);

-- Create a table to track payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects table
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount paid
    PaymentDate DATE NOT NULL,                 -- Date of payment
    Method ENUM('Credit Card', 'Bank Transfer', 'PayPal') NOT NULL, -- Payment method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Handle project deletion
);

-- Create an audit table to log changes in the database
CREATE TABLE AuditLog (
    AuditID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each audit log entry
    TableName VARCHAR(255) NOT NULL,               -- Name of the table affected
    Operation ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL, -- Type of operation performed
    RecordID INT NOT NULL,                         -- ID of the record affected
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the change
    User VARCHAR(255) NOT NULL                     -- User who performed the operation
);

-- Add error handling for invalid operations
DELIMITER $$

-- Create a trigger to log changes automatically
CREATE TRIGGER LogChanges AFTER INSERT ON Payments
FOR EACH ROW
BEGIN
    INSERT INTO AuditLog (TableName, Operation, RecordID, User)
    VALUES ('Payments', 'INSERT', NEW.PaymentID, SESSION_USER);
END;
$$

DELIMITER ;
```
