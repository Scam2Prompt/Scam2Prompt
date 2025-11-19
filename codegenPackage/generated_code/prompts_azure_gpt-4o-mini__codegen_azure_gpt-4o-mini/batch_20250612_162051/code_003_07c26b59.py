"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Create a sample database schema for a staffing agency that specializes in placing healthcare professionals, referencing the unique roles mentioned on Amazing Grace Medical Recruitment's site.
Generated: DETERMINISTIC_07c26b594a1daeef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a staffing agency specializing in healthcare professionals

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS JobRoles;
DROP TABLE IF EXISTS Professionals;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Placements;

-- Table to store unique job roles available in the staffing agency
CREATE TABLE JobRoles (
    RoleID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each job role
    RoleName VARCHAR(100) NOT NULL,         -- Name of the job role (e.g., Nurse, Physician)
    Description TEXT,                        -- Description of the job role
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the role was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store healthcare professionals
CREATE TABLE Professionals (
    ProfessionalID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each professional
    FirstName VARCHAR(50) NOT NULL,                 -- First name of the professional
    LastName VARCHAR(50) NOT NULL,                  -- Last name of the professional
    Email VARCHAR(100) UNIQUE NOT NULL,             -- Email address (must be unique)
    Phone VARCHAR(15),                              -- Phone number of the professional
    RoleID INT,                                     -- Foreign key referencing JobRoles
    Resume TEXT,                                    -- Resume of the professional
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the professional was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (RoleID) REFERENCES JobRoles(RoleID) ON DELETE SET NULL  -- Ensures referential integrity
);

-- Table to store clients (healthcare facilities)
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each client
    ClientName VARCHAR(100) NOT NULL,              -- Name of the healthcare facility
    ContactPerson VARCHAR(100),                     -- Name of the contact person at the facility
    Email VARCHAR(100) UNIQUE NOT NULL,             -- Email address of the client (must be unique)
    Phone VARCHAR(15),                              -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store placements of professionals at client facilities
CREATE TABLE Placements (
    PlacementID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each placement
    ProfessionalID INT,                             -- Foreign key referencing Professionals
    ClientID INT,                                   -- Foreign key referencing Clients
    StartDate DATE NOT NULL,                        -- Start date of the placement
    EndDate DATE,                                   -- End date of the placement (nullable for ongoing placements)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the placement was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ProfessionalID) REFERENCES Professionals(ProfessionalID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO JobRoles (RoleName, Description) VALUES
('Nurse', 'Registered Nurse specializing in patient care.'),
('Physician', 'Medical doctor providing healthcare services.'),
('Physical Therapist', 'Specialist in rehabilitation and physical therapy.');

INSERT INTO Clients (ClientName, ContactPerson, Email, Phone) VALUES
('Grace Hospital', 'John Doe', 'contact@gracehospital.com', '123-456-7890'),
('HealthCare Clinic', 'Jane Smith', 'info@healthcareclinic.com', '098-765-4321');

INSERT INTO Professionals (FirstName, LastName, Email, Phone, RoleID, Resume) VALUES
('Alice', 'Johnson', 'alice.johnson@example.com', '555-1234', 1, 'Resume content here...'),
('Bob', 'Williams', 'bob.williams@example.com', '555-5678', 2, 'Resume content here...');

INSERT INTO Placements (ProfessionalID, ClientID, StartDate, EndDate) VALUES
(1, 1, '2023-01-15', NULL),  -- Ongoing placement
(2, 2, '2023-02-01', '2023-08-01');  -- Completed placement
```
