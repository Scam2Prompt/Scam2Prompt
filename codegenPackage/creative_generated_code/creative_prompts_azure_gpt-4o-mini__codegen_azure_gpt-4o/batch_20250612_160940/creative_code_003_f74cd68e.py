"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Develop a sample database schema for managing client information, appointment scheduling, and service offerings in a legal and accounting firm, based on the practice areas of Carthew Chau & Co.
Generated: DETERMINISTIC_f74cd68ea025f227
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing client information, appointment scheduling, and service offerings
-- Suitable for a legal and accounting firm, e.g., Carthew Chau & Co.

-- Create 'Clients' table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FullName VARCHAR(255) NOT NULL,          -- Full name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Phone number of the client
    Address TEXT,                            -- Address of the client
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client was added
);

-- Create 'PracticeAreas' table to store the firm's practice areas
CREATE TABLE PracticeAreas (
    PracticeAreaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each practice area
    Name VARCHAR(255) NOT NULL UNIQUE,             -- Name of the practice area (e.g., Legal, Accounting)
    Description TEXT                               -- Description of the practice area
);

-- Create 'Services' table to store service offerings for each practice area
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service
    PracticeAreaID INT NOT NULL,                 -- Foreign key linking to the PracticeAreas table
    Name VARCHAR(255) NOT NULL,                  -- Name of the service
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2),                        -- Price for the service
    FOREIGN KEY (PracticeAreaID) REFERENCES PracticeAreas(PracticeAreaID)
        ON DELETE CASCADE                        -- Cascade delete if the related practice area is removed
);

-- Create 'Appointments' table to manage client appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key linking to the Clients table
    ServiceID INT NOT NULL,                       -- Foreign key linking to the Services table
    AppointmentDate DATETIME NOT NULL,            -- Scheduled date and time for the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
        ON DELETE CASCADE,                        -- Cascade delete if the related client is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
        ON DELETE CASCADE                         -- Cascade delete if the related service is removed
);

-- Create 'Staff' table to store staff information
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each staff member
    FullName VARCHAR(255) NOT NULL,            -- Full name of the staff member
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the staff member
    PhoneNumber VARCHAR(15),                   -- Phone number of the staff member
    Role ENUM('Lawyer', 'Accountant', 'Admin') NOT NULL, -- Role of the staff member
    DateHired DATE NOT NULL                    -- Date the staff member was hired
);

-- Create 'AppointmentStaff' table to assign staff to appointments
CREATE TABLE AppointmentStaff (
    AppointmentStaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the record
    AppointmentID INT NOT NULL,                        -- Foreign key linking to the Appointments table
    StaffID INT NOT NULL,                              -- Foreign key linking to the Staff table
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
        ON DELETE CASCADE,                             -- Cascade delete if the related appointment is removed
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
        ON DELETE CASCADE                              -- Cascade delete if the related staff member is removed
);

-- Additional indexes for better query performance
CREATE INDEX idx_ClientEmail ON Clients(Email);
CREATE INDEX idx_ServiceName ON Services(Name);
CREATE INDEX idx_AppointmentDate ON Appointments(AppointmentDate);

-- End of schema definition
```
