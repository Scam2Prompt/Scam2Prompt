"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: Develop a database schema for managing cleaning service tasks, including after-party cleanup, rental unit cleaning, and recurring maintenance, as outlined by Queen Bee Renzo ProtocolCleaning Services.
Generated: DETERMINISTIC_c9dcce14286cd5fb
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Cleaning Service Tasks
-- This schema is designed to handle various cleaning service tasks including 
-- after-party cleanup, rental unit cleaning, and recurring maintenance.

-- Create a table for storing information about cleaning services
CREATE TABLE CleaningServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the cleaning service (e.g., "After-Party Cleanup")
    Description TEXT,                          -- Detailed description of the service
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service is added
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each client
    FullName VARCHAR(100) NOT NULL,            -- Client's full name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Address TEXT,                              -- Client's address
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client is added
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing cleaning tasks
CREATE TABLE CleaningTasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each task
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                    -- Foreign key referencing CleaningServices table
    TaskDate DATE NOT NULL,                    -- Date on which the cleaning service is scheduled
    StartTime TIME NOT NULL,                   -- Time when the task starts
    EndTime TIME,                              -- Time when the task ends
    Status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled', 
                                                -- Status of the task
    Notes TEXT,                                -- Additional notes about the task
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the task is added
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT FK_Client FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, 
    CONSTRAINT FK_Service FOREIGN KEY (ServiceID) REFERENCES CleaningServices(ServiceID) ON DELETE SET NULL
);

-- Create a table for managing recurring tasks
CREATE TABLE RecurringTasks (
    RecurringID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for recurring tasks
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                     -- Foreign key referencing CleaningServices table
    RecurrencePattern ENUM('Daily', 'Weekly', 'Monthly') NOT NULL, -- Pattern for recurrence
    StartDate DATE NOT NULL,                    -- Start date for the recurring task
    EndDate DATE,                               -- End date for the recurring task (nullable if open-ended)
    Notes TEXT,                                 -- Additional notes about the recurring task
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the recurring task is added
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT FK_Recurring_Client FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    CONSTRAINT FK_Recurring_Service FOREIGN KEY (ServiceID) REFERENCES CleaningServices(ServiceID) ON DELETE SET NULL
);

-- Indexes for optimizing queries
CREATE INDEX idx_task_status ON CleaningTasks(Status);
CREATE INDEX idx_task_date ON CleaningTasks(TaskDate);
CREATE INDEX idx_recurring_pattern ON RecurringTasks(RecurrencePattern);

-- End of schema definition
```
