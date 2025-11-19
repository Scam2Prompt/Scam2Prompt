"""
Generated Code Metadata:
========================
Original URL: https://carehelpers.pt
Prompt: Design a database schema in SQL for managing client information and service requests for a home care provider like CARE HELPERS, focusing on activities of daily living and technical aids.
Generated: DETERMINISTIC_3c4bff9a0b0ea223
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for CARE HELPERS

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Email VARCHAR(100),                      -- Client's email address
    Address TEXT NOT NULL,                   -- Client's residential address
    EmergencyContactName VARCHAR(100),       -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),       -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service request
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ServiceType ENUM('Daily Living', 'Technical Aid') NOT NULL, -- Type of service requested
    Description TEXT NOT NULL,                -- Detailed description of the service request
    RequestDate DATE NOT NULL,                -- Date the service was requested
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    AssignedCaregiver VARCHAR(100),           -- Name of the assigned caregiver (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store caregivers information
CREATE TABLE Caregivers (
    CaregiverID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each caregiver
    FirstName VARCHAR(50) NOT NULL,             -- Caregiver's first name
    LastName VARCHAR(50) NOT NULL,              -- Caregiver's last name
    PhoneNumber VARCHAR(15),                    -- Caregiver's phone number
    Email VARCHAR(100),                         -- Caregiver's email address
    Specialization ENUM('Daily Living', 'Technical Aid', 'Both') NOT NULL, -- Caregiver's area of expertise
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to log service activities
CREATE TABLE ServiceLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each log entry
    RequestID INT NOT NULL,                     -- Foreign key referencing ServiceRequests table
    CaregiverID INT NOT NULL,                   -- Foreign key referencing Caregivers table
    ActivityDescription TEXT NOT NULL,          -- Description of the activity performed
    ActivityDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the activity
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID) ON DELETE SET NULL -- Ensures data integrity
);

-- Table to store feedback from clients
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feedback entry
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    RequestID INT NOT NULL,                     -- Foreign key referencing ServiceRequests table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating provided by the client (1 to 5)
    Comments TEXT,                              -- Additional comments from the client
    FeedbackDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the feedback
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_name ON Clients (FirstName, LastName); -- Index for client name
CREATE INDEX idx_service_status ON ServiceRequests (Status);   -- Index for service request status
CREATE INDEX idx_caregiver_specialization ON Caregivers (Specialization); -- Index for caregiver specialization
```
