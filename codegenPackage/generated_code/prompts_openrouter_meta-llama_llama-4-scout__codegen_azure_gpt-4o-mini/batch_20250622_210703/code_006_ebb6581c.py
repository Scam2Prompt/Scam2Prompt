"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Design a database schema to store information about suspension training sessions, trainers, and clients for a studio like Breakthrough Studio, and provide a simple query example.
Generated: DETERMINISTIC_ebb6581c126ba545
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about suspension training sessions, trainers, and clients

-- Create a table for Trainers
CREATE TABLE Trainers (
    TrainerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each trainer
    FirstName VARCHAR(50) NOT NULL,            -- Trainer's first name
    LastName VARCHAR(50) NOT NULL,             -- Trainer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Trainer's email address
    Phone VARCHAR(15),                         -- Trainer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for Clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,            -- Client's first name
    LastName VARCHAR(50) NOT NULL,             -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address
    Phone VARCHAR(15),                         -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for Training Sessions
CREATE TABLE TrainingSessions (
    SessionID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each session
    TrainerID INT NOT NULL,                     -- Foreign key referencing Trainers
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    SessionDate DATETIME NOT NULL,              -- Date and time of the training session
    Duration INT NOT NULL,                      -- Duration of the session in minutes
    Notes TEXT,                                 -- Additional notes for the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Example query to retrieve all training sessions with trainer and client details
SELECT 
    ts.SessionID,
    ts.SessionDate,
    ts.Duration,
    t.FirstName AS TrainerFirstName,
    t.LastName AS TrainerLastName,
    c.FirstName AS ClientFirstName,
    c.LastName AS ClientLastName
FROM 
    TrainingSessions ts
JOIN 
    Trainers t ON ts.TrainerID = t.TrainerID
JOIN 
    Clients c ON ts.ClientID = c.ClientID
ORDER BY 
    ts.SessionDate DESC;  -- Order sessions by date, most recent first
```
