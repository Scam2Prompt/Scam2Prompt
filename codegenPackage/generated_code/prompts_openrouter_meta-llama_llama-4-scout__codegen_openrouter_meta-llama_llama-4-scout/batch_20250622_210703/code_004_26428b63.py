"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Develop a simple database schema to store information about clients, employees, and services provided by a youth mental healthcare company, considering the need for superior client-focused care.
Generated: DETERMINISTIC_26428b63e4d0423d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the youth mental healthcare company
CREATE DATABASE youth_mental_healthcare;

-- Use the created database
USE youth_mental_healthcare;

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create a table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Role ENUM('Counselor', 'Therapist', 'Psychiatrist', 'Admin') NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (EmployeeID)
);

-- Create a table to store service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create a table to store client-employee relationships (many-to-many)
CREATE TABLE ClientSessions (
    SessionID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    EmployeeID INT NOT NULL,
    ServiceID INT NOT NULL,
    SessionDate DATE NOT NULL,
    SessionTime TIME NOT NULL,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SessionID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create a table to store client service history
CREATE TABLE ClientServiceHistory (
    HistoryID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceID INT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (HistoryID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_ClientSessions_ClientID ON ClientSessions (ClientID);
CREATE INDEX idx_ClientSessions_EmployeeID ON ClientSessions (EmployeeID);
CREATE INDEX idx_ClientSessions_ServiceID ON ClientSessions (ServiceID);
CREATE INDEX idx_ClientServiceHistory_ClientID ON ClientServiceHistory (ClientID);
CREATE INDEX idx_ClientServiceHistory_ServiceID ON ClientServiceHistory (ServiceID);
```

```sql
-- Example usage:
INSERT INTO Clients (FirstName, LastName, DateOfBirth, Email, Phone, Address)
VALUES ('John', 'Doe', '2000-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO Employees (FirstName, LastName, Email, Role, Phone)
VALUES ('Jane', 'Smith', 'jane.smith@example.com', 'Counselor', '987-654-3210');

INSERT INTO Services (ServiceName, Description)
VALUES ('Individual Therapy', 'One-on-one therapy sessions');

INSERT INTO ClientSessions (ClientID, EmployeeID, ServiceID, SessionDate, SessionTime, Notes)
VALUES (1, 1, 1, '2022-01-01', '10:00:00', 'Initial assessment');

INSERT INTO ClientServiceHistory (ClientID, ServiceID, StartDate, EndDate)
VALUES (1, 1, '2022-01-01', NULL);
```
