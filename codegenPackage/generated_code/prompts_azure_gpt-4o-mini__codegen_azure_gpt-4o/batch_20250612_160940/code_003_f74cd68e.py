"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Develop a sample database schema for managing client information, appointment scheduling, and service offerings in a legal and accounting firm, based on the practice areas of Carthew Chau & Co.
Generated: DETERMINISTIC_f74cd68ea025f227
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client information, appointment scheduling, and service offerings
-- for a legal and accounting firm.

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store practice areas offered by the firm
CREATE TABLE PracticeAreas (
    PracticeAreaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each practice area
    Name VARCHAR(100) NOT NULL UNIQUE,             -- Name of the practice area (e.g., "Tax Accounting", "Corporate Law")
    Description TEXT,                              -- Description of the practice area
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store services offered within each practice area
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    PracticeAreaID INT NOT NULL,              -- Foreign key referencing PracticeAreas table
    Name VARCHAR(100) NOT NULL,               -- Name of the service (e.g., "Tax Filing", "Contract Drafting")
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PracticeAreaID) REFERENCES PracticeAreas(PracticeAreaID) ON DELETE CASCADE
);

-- Create a table to store appointment scheduling information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create a table to store staff information (optional, if needed for scheduling purposes)
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,         -- Staff member's first name
    LastName VARCHAR(50) NOT NULL,          -- Staff member's last name
    Email VARCHAR(100) NOT NULL UNIQUE,     -- Staff member's email address
    PhoneNumber VARCHAR(15),                -- Staff member's phone number
    Role ENUM('Lawyer', 'Accountant', 'Admin') NOT NULL, -- Role of the staff member
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to assign staff to appointments (optional, if needed for scheduling purposes)
CREATE TABLE AppointmentStaff (
    AppointmentStaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    AppointmentID INT NOT NULL,                        -- Foreign key referencing Appointments table
    StaffID INT NOT NULL,                              -- Foreign key referencing Staff table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the staff was assigned
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_service_practice_area ON Services(PracticeAreaID);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
CREATE INDEX idx_staff_role ON Staff(Role);
```
