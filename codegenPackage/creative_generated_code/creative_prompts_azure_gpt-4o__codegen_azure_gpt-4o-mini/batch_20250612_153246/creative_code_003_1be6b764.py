"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthcareventure.nl
Prompt: Create a database schema in SQL to manage client-focused care data for youth mental healthcare companies, incorporating fields for psychiatry, psychology, begeleiding, and opvang+ services.
Generated: DETERMINISTIC_1be6b7644facfe55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for managing client-focused care data in youth mental healthcare

CREATE DATABASE YouthMentalHealthcare;
USE YouthMentalHealthcare;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,                -- Client's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Client's gender
    ContactInfo VARCHAR(255),                  -- Client's contact information
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store service types offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the service (e.g., psychiatry, psychology, begeleiding, opvang+)
    Description TEXT,                           -- Description of the service offered
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store appointments for clients
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key reference to Clients table
    ServiceID INT NOT NULL,                       -- Foreign key reference to Services table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Duration INT NOT NULL,                        -- Duration of the appointment in minutes
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure client deletion cascades to appointments
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure service deletion cascades to appointments
);

-- Table to store treatment plans for clients
CREATE TABLE TreatmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each treatment plan
    ClientID INT NOT NULL,                        -- Foreign key reference to Clients table
    PlanDetails TEXT NOT NULL,                    -- Details of the treatment plan
    StartDate DATE NOT NULL,                      -- Start date of the treatment plan
    EndDate DATE,                                 -- Optional end date of the treatment plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure client deletion cascades to treatment plans
);

-- Table to store feedback from clients
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each feedback record
    ClientID INT NOT NULL,                        -- Foreign key reference to Clients table
    ServiceID INT NOT NULL,                       -- Foreign key reference to Services table
    FeedbackDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of feedback submission
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the client (1 to 5 scale)
    Comments TEXT,                                -- Additional comments from the client
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure client deletion cascades to feedback
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure service deletion cascades to feedback
);

-- Indexes can be added to improve query performance if necessary
-- Example: CREATE INDEX idx_client_service ON Appointments(ClientID, ServiceID);
```
