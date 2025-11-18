"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Create a database schema to manage appointments, messages, and follow-up calls for a virtual receptionist service like ProSync.
Generated: DETERMINISTIC_e73821c228515435
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Virtual Receptionist Service

-- Table to store receptionist user information
CREATE TABLE Receptionists (
    ReceptionistID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for receptionists
    FirstName VARCHAR(50) NOT NULL,                -- Receptionist's first name
    LastName VARCHAR(50) NOT NULL,                 -- Receptionist's last name
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Receptionist's email for login communication
    PhoneNumber VARCHAR(15),                       -- Receptionist's contact number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for clients
    FirstName VARCHAR(50) NOT NULL,                -- Client's first name
    LastName VARCHAR(50) NOT NULL,                 -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Client's email for communication
    PhoneNumber VARCHAR(15),                       -- Client's contact number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to manage appointments
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for appointments
    ClientID INT NOT NULL,                         -- Foreign key referring to Clients
    ReceptionistID INT NOT NULL,                   -- Foreign key referring to Receptionists
    AppointmentDateTime DATETIME NOT NULL,         -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    Notes TEXT,                                    -- Additional notes about the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ReceptionistID) REFERENCES Receptionists(ReceptionistID) ON DELETE SET NULL
);

-- Table to store messages
CREATE TABLE Messages (
    MessageID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for messages
    ClientID INT NOT NULL,                         -- Foreign key referring to Clients
    ReceptionistID INT NOT NULL,                   -- Foreign key referring to Receptionists
    MessageText TEXT NOT NULL,                     -- Content of the message
    SentDateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the message was sent
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ReceptionistID) REFERENCES Receptionists(ReceptionistID) ON DELETE SET NULL
);

-- Table to manage follow-up calls
CREATE TABLE FollowUpCalls (
    FollowUpCallID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for follow-up calls
    AppointmentID INT,                             -- Foreign key referring to Appointments
    ClientID INT NOT NULL,                         -- Foreign key referring to Clients
    ReceptionistID INT NOT NULL,                   -- Foreign key referring to Receptionists
    CallDateTime DATETIME NOT NULL,                -- Date and time of the follow-up call
    Status ENUM('Pending', 'Completed', 'Missed') DEFAULT 'Pending', -- Status of the follow-up call
    Notes TEXT,                                    -- Additional notes about the call
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ReceptionistID) REFERENCES Receptionists(ReceptionistID) ON DELETE SET NULL
);

-- Indexing for performance optimization and faster lookups
CREATE INDEX idx_ClientID_Appointments ON Appointments (ClientID);
CREATE INDEX idx_ReceptionistID_Appointments ON Appointments (ReceptionistID);
CREATE INDEX idx_ClientID_Messages ON Messages (ClientID);
CREATE INDEX idx_ClientID_FollowUpCalls ON FollowUpCalls (ClientID);
CREATE INDEX idx_AppointmentID_FollowUpCalls ON FollowUpCalls (AppointmentID);
```
